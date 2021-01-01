""" 内存监控
"""
def memory_stat():
    mem = {}
    f = open('/proc/meminfo', 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        if len(line) < 2:
            continue
        name = line.split(':')[0]
        var = line.split(':')[1].split()[0]
        mem[name] = float(var)
    mem['MemUsed'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']
    #记录内存使用率 已使用 总内存和缓存大小
    res = {}
    res['percent'] = int(round(mem['MemUsed'] / mem['MemTotal'] * 100))
    res['used'] = round(mem['MemUsed'] / (1024 * 1024), 2)
    res['MemTotal'] = round(mem['MemTotal'] / (1024 * 1024), 2)
    res['Buffers'] = round(mem['Buffers'] / (1024 * 1024), 2)
    return res
""" CPU负载监控
"""
def load_stat():
    loadavg = {}
    f = open("/proc/loadavg")
    con = f.read().split()
    f.close()
    loadavg['lavg_1']=con[0]
    loadavg['lavg_5']=con[1]
    loadavg['lavg_15']=con[2]
    loadavg['nr']=con[3]


    prosess_list = loadavg['nr'].split('/')
    loadavg['running_prosess']=prosess_list[0]
    loadavg['total_prosess']=prosess_list[1]

    loadavg['last_pid']=con[4]

    return loadavg
""" 磁盘空间监控
"""
def disk_stat():
    import os
    hd={}
    disk = os.statvfs('/')
    hd['available'] = float(disk.f_bsize * disk.f_bavail)
    hd['capacity'] = float(disk.f_bsize * disk.f_blocks)
    hd['used'] = float((disk.f_blocks - disk.f_bfree) * disk.f_frsize)
    res = {}
    res['used'] = round(hd['used'] / (1024 * 1024 * 1024), 2)
    res['capacity'] = round(hd['capacity'] / (1024 * 1024 * 1024), 2)
    res['available'] = res['capacity'] - res['used']
    res['percent'] = int(round(float(res['used']) / res['capacity'] * 100))
    return res
""" 获取当前服务器ip
"""
def get_ip(ifname):
    import socket
    import fcntl
    import struct
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])
#!/usr/bin/env python
# from __future__ import print_function

def net_stat():
    net = {}
    f = open("/proc/net/dev")
    lines = f.readlines()
    f.close
    for line in lines[2:]:
        line = line.split(":")
        eth_name = line[0].strip()
        if eth_name != 'lo':
            net_io = {}
            net_io['receive'] = round(float(line[1].split()[0]) / (1024.0 * 1024.0),2)
            net_io['transmit'] = round(float(line[1].split()[8]) / (1024.0 * 1024.0),2)
            net[eth_name] = net_io
    return net

if __name__ == '__main__':
    netdevs = net_stat()
    print(netdevs)