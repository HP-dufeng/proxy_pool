const request = require('request');

const start = Date.now();
request.get({ url:'http://cn.bing.com'}, function (error, response) {
    const end  = Date.now();
    const timespan = end - start;
    console.log(response);    
});