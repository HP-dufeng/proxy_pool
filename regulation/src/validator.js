const request = require('request');

module.exports = function(proxy){
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}

    const p = new Promise((resolve, reject) => {
        request.get({ url:'http://cn.bing.com', proxy: proxy, headers:headers }, function (error, response) {
            if (!error) {
                resolve(response);
            } else {
                reject(error);
            }      
        });
        //TODO: do more test...
    })
    
    return p;

}
