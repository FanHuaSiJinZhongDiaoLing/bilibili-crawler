import threading
from single_fetch import single_fetch
from queue import Queue
import csv

def multi_thread_crawl(task_list, worker_num=5):
    """
    task_list: 任务列表（如 bvid 列表）
    worker_num: 线程数量
    """

    q = Queue()

    # 把任务放进队列
    for item in task_list:
        q.put(item)

    # 线程负责执行的函数
    def worker():
        while not q.empty():
            task = q.get()
            try:
                single_fetch(task)  # <-- 单任务执行，无返回值
            except Exception as e:
                print(f"任务 {task} 出错：{e}")
            finally:
                q.task_done()

    # 创建并启动线程
    threads = []
    for _ in range(worker_num):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    # 等待所有线程结束
    for t in threads:
        t.join()

burl_list = []

with open('test.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # 跳过标题行
    for row in reader:
        burl_list.append("https://www.bilibili.com/video/"+row[2])  # 第三列
print("====================")
multi_thread_crawl(burl_list,3)