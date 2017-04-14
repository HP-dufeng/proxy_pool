const amqp = require('amqp');

const test = require('./validator');

const subscriber = (callback) => {
    const rabbit = amqp.createConnection();

    rabbit.on('ready', function(){
        rabbit.exchange('proxy_pool_exchange', {type: 'direct',autoDelete: false}, function(ex){
            rabbit.queue('validate_queue', {autoDelete: false}, function(q){
                q.bind('proxy_pool_exchange', 'validate_queue');
                q.subscribe(function(message, headers, deliveryInfo, messageObject){
                    const [host, port, proxy_type]  = JSON.parse(message.data.toString('utf8'));

                    callback(`${proxy_type.toLowerCase()}://${host}:${port}`);
                });
            });
        });
    });
}


module.exports = subscriber;

