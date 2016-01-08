import Queue
import threading

from ParserThreadImpl import ParserThread


class ThreadRunner:
    def __init__(self):
        pass

    threadList = ["Thread-1", "Thread-2", "Thread-3"]
    nameList = ["One", "Two", "Three", "Four", "Five"]
    queueLock = threading.Lock()
    workQueue = Queue.Queue(10)
    threads = []
    threadID = 1

    def run(self):
        for tName in self.threadList:
            thread = ParserThread(self.threadID, tName, self.workQueue, self.queueLock)
            thread.start()
            self.threads.append(thread)
            self.threadID += 1

        # Fill the queue
        self.queueLock.acquire()
        for word in self.nameList:
            self.workQueue.put(word)
        self.queueLock.release()

        # Wait for queue to empty
        while not self.workQueue.empty():
            pass

        # Notify threads it's time to exit
        ParserThread.exitFlag = 1

        # Wait for all threads to complete
        for t in self.threads:
            t.join()
        print "Exiting Main Thread"


if __name__ == '__main__':
    ThreadRunner().run()
