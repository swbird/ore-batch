import random
import subprocess
import time
import psutil

# 要启动的进程数量
process_count = 50
# 存放进程信息的列表
processes = []
rpc = '' # rpc 地址
keypair = '' # 私钥
priority_fee = '1000000'
threads = '30'
orepath = './target/release/ore'


def start_process():
    
    cmd = [orepath, '--rpc', rpc, '--keypair', keypair, '--priority-fee', priority_fee, 'mine', '--threads', threads]
    proc = subprocess.Popen(cmd)
    return {'process': proc, 'cmd': cmd}

def check_processes():
    
    for proc_info in processes:
        if proc_info['process'].poll() is not None:  # 进程已退出
            print(f"进程 {proc_info['process'].pid} 已退出，正在重启...")
            proc_info['process'] = subprocess.Popen(proc_info['cmd'])  # 重启进程

# 
for _ in range(process_count):
    processes.append(start_process())
    time.sleep(random.random()*10) # 随机延迟 防止cpu瞬时占用过高

# 每隔一段时间检查进程状态
while True:
    check_processes()
    time.sleep(10)  # 每10秒检查一次
