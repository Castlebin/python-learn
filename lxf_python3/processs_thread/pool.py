# multiprocessing中的Pool为多进程任务提供了进程池

import os
import random
import time
from multiprocessing import Pool


def long_time_task(name):
    print('Run task %s (%s), ppid %s' % (name, os.getpid(), os.getppid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s (%s) runs %0.2f seconds.' % (name, os.getpid(), (end - start)))


if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Pool(4)  # 创建一个进程池
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))

    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
