var request = require('request');

var j = request.jar()
var request = request.defaults({jar:j})

var logindata={};

var options = {
    url: 'https://setup.icloud.com/setup/ws/1/login?clientBuildNumber=14H40&clientId=<CLIENT>',
    method: 'POST',
    gzip: true,
    encoding: null,
    headers: {
        'Accept-Encoding': 'gzip, deflate',
        'Origin': 'https://www.icloud.com',
        'Accept-Language': 'en-US,en;q=0.8,hi;q=0.6',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'Content-Type': 'text/plain',
        'Accept': '*/*',
        'Referer': 'https://www.icloud.com/',
        'Connection': 'keep-alive',
        'DNT': 1
    },
    form:'{"apple_id":"user@me.com","password":"<PASSWORD>","extended_login":false}'
};

function callback(error, response, body) {
    data=JSON.parse(body);
    logindata=data;
    getList(j);
}

request(options, callback);

function callback_(error, response, body) {
    console.log(error);
    console.log(response.status);
    // console.log(body);
}


function getList(j){
    var request = require('request');
    var cookie = "X-APPLE-WEB-ID=<COOKIE>;domain=icloud.com;secure=true;host=icloud.com";
    j.setCookie(cookie,"p08-fmipweb.icloud.com");
    console.log(j);
    var request = request.defaults({jar:j})

    var options_ = {
        url: 'https://p08-fmipweb.icloud.com/fmipservice/client/web/initClient?clientBuildNumber=14H40&clientId=<CLIENT>&dsid=1051801372',
        method: 'POST',
        gzip: true,
        encoding: null,
        headers: {
            'Accept-Encoding': 'gzip, deflate',
            'Origin': 'https://www.icloud.com',
            'Accept-Language': 'en-US,en;q=0.8,hi;q=0.6',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
            'Content-Type': 'text/plain',
            'Accept': '*/*',
            'Referer': 'https://www.icloud.com/applications/find/current/en-us/index.html?',
            'Connection': 'keep-alive',
            'DNT': 1
        },
        form:'{"clientContext":{"appName":"iCloud Find (Web)","appVersion":"2.0","timezone":"US/Pacific","inactiveTime":2313,"apiVersion":"3.0","fmly":true}}'
    };
    console.log(options_);
    request(options_, callback_);
}


