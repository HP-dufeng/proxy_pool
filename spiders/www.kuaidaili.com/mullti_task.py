import threading
import time
from queue import Queue

class MultiCrawl:
    def __init__(self, action, number_of_threads = 8):
        self.action = action
        self.number_of_threads = number_of_threads
        self.queue = Queue()
        self.create_workers()
        

    # Create worker threads (will die when main exits)
    def create_workers(self):
        for _ in range(self.number_of_threads):
            t = threading.Thread(target=self.work)
            t.daemon = True
            t.start()
    
    # Do the next job in the queue
    def work(self):
        while True:
            params = self.queue.get()
            self.action(params)
            self.queue.task_done()

    # Each queued link is a new job
    def do_jobs(self, links):
        for link in links:
            time.sleep(1)
            self.queue.put((link))
        self.queue.join()

