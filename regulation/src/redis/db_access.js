/**
 * Keys description:
 * 
 * proxies: a sorted set of all the proxy created so far

 */


const client = require('./index').redisClient;
const models = require('./models');

exports.getProxies = async () => {
  const data = await client.zrevrangebyscoreAsync('proxies', '+inf', '-inf');
  return data ;
};

exports.addProxy = async (proxy, score) => {
    const totalCount = await client.zcard('proxies');
    if(totalCount < 1000){
        client.zadd('proxies', score, proxy);
    } else {

    }
};



