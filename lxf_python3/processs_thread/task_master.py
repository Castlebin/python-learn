import queue
import random
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()


def ret_task_queue():
    global task_queue
    return task_queue


def ret_result_queue():
    global result_queue
    return result_queue


class QueueManager(BaseManager):
    pass


if __name__ == '__main__':
    QueueManager.register('get_task_queue', callable=ret_task_queue)
    QueueManager.register('get_result_queue', callable=ret_result_queue)

    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0, 1000)
        print('Put task %d' % n)
        task.put(n)

    print('Try to get results...')

    for i in range(0, 10):
        n = result.get(timeout=10)
        print('Result is %s' % n)

    manager.shutdown()
    print('master exit')
