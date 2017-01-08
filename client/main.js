var MIN_FLUSH_RATE = 0.5;
var MAX_FLUSH_RATE = 0.1;
var MIN_QUEUE_LENGTH = 2;

var queue = [];
var last_flush = new Date();

function notify(message) {
    queue.push(message);
    console.log(message.url);
}

function flush() {
    now = new Date();
    if(
        queue.length >= MIN_QUEUE_LENGTH ||
        ((now - last_flush) >= MIN_FLUSH_RATE * 60 * 1000 && queue.length > 0)
    ){
        console.log("Flushing a queue with " + queue.length + " elements.");
        last_flush = new Date();

        var payload = queue.slice();
        queue.length = 0;

        var handle_error = function(){
            console.error("Send failed. Pushing back the queue.");
            Array.prototype.push.apply(queue, payload);
        }

        var xhr = new XMLHttpRequest();
        xhr.open("POST", "http://localhost:4200/append", true);
        xhr.onload = function (e) {
            if (xhr.readyState === 4) {
                if (xhr.status === 200) {
                    console.log("Queue sent.");
                } else {
                    handle_error();
                }
            }
        };
        xhr.onerror = handle_error;
        xhr.timeout = 500;
        xhr.ontimeout = handle_error;
        xhr.send(JSON.stringify(payload));
    } else {
        console.log("Queue has only " + queue.length + " elements. Waiting before flushing...");
    }
}

browser.runtime.onMessage.addListener(notify);
window.setInterval(flush, MAX_FLUSH_RATE * 60 * 1000);
