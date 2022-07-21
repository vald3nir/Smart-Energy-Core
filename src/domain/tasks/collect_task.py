import threading
import time


def _task(listener):
    while True:
        time.sleep(1)
        print('This is coming from another thread')
        listener()


class DataCollectTask:

    def __init__(self, listener):
        super().__init__()
        self.task_runner = threading.Thread(target=_task(listener), args=[])

    def start(self):
        self.task_runner.start()

    def exit(self):
        self.task_runner.join()


if __name__ == '__main__':
    def callback():
        print("callback")
        t1.exit()


    t1 = DataCollectTask(listener=callback)
    t1.start()
