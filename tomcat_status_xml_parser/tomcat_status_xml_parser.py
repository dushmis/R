# http://user:password@localhost:port/manager_if_it_is_available/status?XML=true

import sys
rootElement = 0
data = {}
filename = ""
# import smtplib # Import smtplib for the actual sending function
# from email.mime.text import MIMEText # Import the email module

# print "jvm_memory_free:$status->{jvm}->{memory}->{free} ";
# print "jvm_memory_max:$status->{jvm}->{memory}->{max} ";
# print "jvm_memory_total:$status->{jvm}->{memory}->{total} ";
# print "connector_max_time:$status->{connector}->{$connector}->{requestInfo}->{maxTime} ";
# print "connector_error_count:$status->{connector}->{$connector}->{requestInfo}->{errorCount} ";
# print "connector_bytes_sent:$status->{connector}->{$connector}->{requestInfo}->{bytesSent} ";
# print "connector_processing_time:$status->{connector}->{$connector}->{requestInfo}->{processingTime} ";
# print "connector_request_count:$status->{connector}->{$connector}->{requestInfo}->{requestCount} ";
# print "connector_bytes_received:$status->{connector}->{$connector}->{requestInfo}->{bytesReceived} ";

# print "connector_current_thread_count:$status->{connector}->{$connector}->{threadInfo}->{currentThreadCount} ";
# print "connector_min_spare_threads:$status->{connector}->{$connector}->{threadInfo}->{minSpareThreads} ";
# print "connector_max_threads:$status->{connector}->{$connector}->{threadInfo}->{maxThreads} ";
# print "connector_max_spare_threads:$status->{connector}->{$connector}->{threadInfo}->{maxSpareThreads} ";
# print "connector_current_threads_busy:$status->{connector}->{$connector}->{threadInfo}->{currentThreadsBusy} ";


# def send_email(subject,content,fro,to):
#     msg = MIMEText(content)
#     msg['Subject'] = subject
#     msg['From'] = fro
#     msg['To'] = ', '.join(to);
#     s = smtplib.SMTP('localhost')
#     s.sendmail(fro,to, msg.as_string())
#     s.quit()

def dothework():
    if sys.argv.__len__() < 2:
        print("invalid arguments")
        return
    import xml.etree.ElementTree as ET
    import time
    global rootElement, data, filename
    filename = sys.argv[1]
    rootElement = ET.parse(filename).getroot()
    data.update(free=findvalueint("jvm/memory", "free"))
    data.update(max=findvalueint("jvm/memory", "max"))
    data.update(total=findvalueint("jvm/memory", "total"))
    import datetime, os
    filedatetime = format(datetime.datetime.fromtimestamp(os.path.getmtime(filename)),"%Y-%m-%d %H:%M:%S")
    data.update(datetime=filedatetime)

    for connector in getallconnectors():
        name = "connector_" + connector.get("name")[1:-1]
        maxTime = str(connector.find("requestInfo").get("maxTime"))
        errorCount = str(connector.find("requestInfo").get("errorCount"))
        bytesSent = str(connector.find("requestInfo").get("bytesSent"))
        processingTime = str(connector.find( "requestInfo").get("processingTime"))
        requestCount = str(connector.find("requestInfo").get("requestCount"))
        bytesReceived = str(connector.find("requestInfo").get("bytesReceived"))
        currentThreadCount = str(connector.find( "threadInfo").get("currentThreadCount"))
        minSpareThreads = str(connector.find( "threadInfo").get("minSpareThreads"))
        maxThreads = str(connector.find("threadInfo").get("maxThreads"))
        maxSpareThreads = str(connector.find( "threadInfo").get("maxSpareThreads"))
        currentThreadsBusy = str(connector.find( "threadInfo").get("currentThreadsBusy"))
        data['maxTime' + name] = maxTime
        data['errorCount' + name] = errorCount
        data['bytesSent' + name] = bytesSent
        data['processingTime' + name] = processingTime
        data['requestCount' + name] = requestCount
        data['bytesReceived' + name] = bytesReceived

        data['currentThreadCount' + name] = currentThreadCount
        data['minSpareThreads' + name] = minSpareThreads
        data['maxThreads' + name] = maxThreads
        data['maxSpareThreads' + name] = maxSpareThreads
        data['currentThreadsBusy' + name] = currentThreadsBusy
        data['workers' + name] = connector.findall("workers/worker").__len__()
        # if(int(currentThreadCount) >= (int(maxThreads) * 0.9)):
        #     mail_content = "currentThreadCount is %s and max is %s for %s" % (currentThreadCount,maxThreads,name)
        #     mail_subject = "%s reached limit" % (name)
    print(data)
    import csv
    with open('data.csv', 'a') as f:
        w = csv.DictWriter(f, data.keys())
        w.writerow(data)


def getallconnectors():
    return [connector for connector in rootElement.findall("connector")]


def findvalueint(element, tag):
    global rootElement
    return int(rootElement.find(element).get(tag))


def findvalue(element, tag):
    return element.get(tag)


if __name__ == "__main__":
    dothework()
