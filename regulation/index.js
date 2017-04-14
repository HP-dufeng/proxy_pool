const subscriber = require('./src/subscriber');
const validate = require('./src/validator');
const redis = require('./src/redis/db_access');


function test(proxy) {
    const start = Date.now();
    validate(proxy)
        .then(response => {
            const end = Date.now();

            const { statusCode } = response;
            if(statusCode >= 200 && statusCode <400){
                const score = end - start;
                redis.addProxy(proxy, score);
            }

            console.log(`${proxy}, statusCode: ${statusCode}`);
        })
        .catch(error => {
            console.log(error.code);
        })
}

subscriber(test);