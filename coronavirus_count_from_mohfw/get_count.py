import requests
import matplotlib.pyplot as plt

def getcount(city,text):
  return (city,int(text.split(city)[1].split('>')[2].split('<')[0]))

d=requests.get("https://www.mohfw.gov.in/")
x=d.content
k=str(x)
#print(k.split('Gujarat')[1].split('>')[2].split('<')[0])
#print(k.split('Haryana')[1].split('>')[2].split('<')[0])
cities=['Andhra Pradesh', 'Bihar', 'Chhattisgarh', 'Delhi', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Tamil Nadu', 'Telengana', 'Chandigarh', 'Jammu and Kashmir', 'Ladakh', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
allc=list()
for city in cities:
  allc.append(getcount(city,k))

print(allc)
#ddplt.plot(allc)
#plt.show()