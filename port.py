# coding=gbk
import queue
import requests
import json
import time
requests.packages.urllib3.disable_warnings()

api_url = "https://10.12.153.99:443/api"
keep_alive = True
CONTEST_ID = 725
session_cookie = "MTczMzQ2NzUzNHxOd3dBTkVsRVYxZFZTMXBXU1ZST05VWldNMVpaVVVSU1REVlVXRmRTUVU1TFZWUlpNa1pJVlVreVVVcEVNazVTV1VKSFZFUTNTMEU9fENpxgQZDyGd10ry6gl3ZjmVxRPZDBDfnE67ZcgOmTlz"

def get_ssh_hosts(queue):
    while (keep_alive):
        response = requests.get(url=f"{api_url}/awd/rank?id={CONTEST_ID}", verify=False)
        print('[', end='')
        for group in json.loads(response.text)["scores"]:
            try:
                group_id = group["groupID"]
                section_id = group["sectionStates"][0]["sectionID"]
                
                response = requests.get(url=f"{api_url}/awd/machine?groupID={group_id}&sectionID={section_id}", verify=False, cookies={"SESSIONID":session_cookie})
                machine = json.loads(response.text)["machineInfo"][0]
                ip = machine["ip"]
                ports = machine["portInfos"]
                for port in ports:
                    if (port["targetPort"] == 80):
                        ssh_port = ports[1]["publishedPort"]
                        print(str(ssh_port) + ", ", end='')
            except:
                pass
        print(']')
        time.sleep(300)

if __name__ == "__main__":
    quere = []
    get_ssh_hosts(queue)