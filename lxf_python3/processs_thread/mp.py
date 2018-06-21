# multiprocessing 模块为python提供了跨平台的多进程支持

import os
from multiprocessing import Process


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s), ppid is %s' % (name, os.getpid(), os.getppid()))


if __name__ == '__main__':
    print("Parent process %s" % os.getpid())
    p = Process(target=run_proc, args=('test',))  # 创建子进程
    print('Child process will start...')
    p.start()  # 开始执行子进程
    p.join()  # 父进程等待子进程执行完成再开始往下执行
    print('Child process end.')
