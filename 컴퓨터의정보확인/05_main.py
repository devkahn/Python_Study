# 컴퓨터의 정보 확인
## pip install psutil

import psutil


print('>>>컴퓨터의 정보 확인')
print()
cpu = psutil.cpu_freq()
print(cpu)

cpu_core = psutil.cpu_count(logical=False)
print(cpu_core)

memory = psutil.virtual_memory()
print(memory)

disk = psutil.disk_partitions()
print(disk)

net = psutil.net_io_counters()
print(net)




print('>>>필요한 정보만 출력하는 코드 만들기')
print()

cpu_current_ghz = round(cpu.current/1000, 2)
print(f"cpu 속도 : {cpu_current_ghz}GHz")

print(f"코어 : {cpu_core} 개")

memory_total = round(memory.total/ 1024**3)
print(f"메모리 : {memory_total}GB")

for p in disk:
    print(p.mountpoint, p.fstype, end='  ')
    du = psutil.disk_usage(p.mountpoint)
    disk_total = round(du.total / 1024**3)
    print(f'디스스크기 : { disk_total}GB')

net = psutil.net_io_counters()
sent = round(net.bytes_sent/1024**2, 1)
recv = round(net.bytes_recv/1024**2, 1)
print(f'보내기 : {sent}MB 받기:{recv}MB')



print('>>>1초당 반복해서 정보를 출력하는 코드 만들기')
print()

curr_sent = 0
curr_recv = 0

prev_sent = 0
prev_recv = 0

while True:
    cpu_p = psutil.cpu_percent(interval=1)
    print(f'cpu사용량: {cpu_p}%')
    
    memory_curr = psutil.virtual_memory()
    memory_avail = round(memory_curr.available/1024**3, 1)
    print(f'사용 가능한 메모리 : {memory_avail}GB')
    
    net_curr = psutil.net_io_counters()
    curr_sent = net_curr.bytes_sent/1024**2
    curr_recv = net_curr.bytes_recv/1024**2
    
    sent_curr = round(curr_sent-prev_sent, 1)
    recv_curr = round(curr_recv-prev_recv, 1)
    print(f'보내기 : {sent_curr}MB 받기 : {recv_curr}MB')
    
    prev_sent = curr_sent
    prev_recv = curr_recv