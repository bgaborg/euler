import threading
import time


class ParserThread (threading.Thread):
    exitFlag = 0

    def __init__(self, threadID, name, q, qLock):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
        self.qLock = qLock

    def run(self):
        print "Starting " + self.name
        process_data(self.name, self.q, self.qLock)
        print "Exiting " + self.name


def process_data(threadName, q, qLock):
    while not ParserThread.exitFlag:
        qLock.acquire()
        if not q.empty():
            data = q.get()
            qLock.release()
            print "%s processing %s" % (threadName, data)
        else:
            qLock.release()
        time.sleep(1)
