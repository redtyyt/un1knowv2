from colorama import Fore
import time
import sys, os

def normalOut(text:str,anim:bool=True):
    if not anim:
        sys.stdout.write("\n[-] " + text)
        sys.stdout.flush()
    else:
        animation = "\n[-] " + text
        for i in range(len(animation)):
            time.sleep(0.06)
            sys.stdout.write(animation[i % len(animation)])
            sys.stdout.flush()

def errorOut(text:str,anim:bool=True):
    if not anim:
        sys.stderr.write(f"\n{Fore.RED}[!]{Fore.RESET}" + text)
        sys.stdout.flush()
    else:
        animation = f"\n{Fore.RED}[!]{Fore.RESET} " + text
        for i in range(len(animation)):
            time.sleep(0.02)
            sys.stdout.write(animation[i % len(animation)])
            sys.stdout.flush()

def helpOut(text:str,anim:bool=True,animtime:float=0.06):
    if not anim:
        sys.stdout.write(f"\n{Fore.CYAN}[:]" + text + Fore.RESET)
    else:
        animation = "\n[:] " + text
        for i in range(len(animation)):
            time.sleep(animtime)
            sys.stdout.write(Fore.GREEN + animation[i % len(animation)] + Fore.RESET)
            sys.stdout.flush()

def loading_anim(repeatimes:int=1):
    animation = "|/-\\"
    for i in range(10):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    os.system("cls")

def initial_logo():
    animation = Fore.RED + r"""                                                                               
                      ,--.               ,--.        ,--.   ,----..                                                  
                    ,--.'|    ,---,  ,--/  /|      ,--.'|  /   /   \            .---.                       ,----,   
         ,--,   ,--,:  : | ,`--.' ,---,': / '  ,--,:  : | /   .     :          /. ./|                     .'   .' \  
       ,'_ /|,`--.'`|  ' :/    /  :   : '/ /,`--.'`|  ' :.   /   ;.  \     .--'.  ' ;                   ,----,'    | 
  .--. |  | :|   :  :  | :    |.' |   '   , |   :  :  | .   ;   /  ` ;    /__./ \ : |             .---. |    :  .  ; 
,'_ /| :  . |:   |   \ | `----':  '   |  /  :   |   \ | ;   |  ; \ ; |.--'.  '   \' .           /.  ./| ;    |.'  /  
|  ' | |  . .|   : '  '; |  '   ' |   ;  ;  |   : '  '; |   :  | ; | /___/ \ |    ' '         .-' . ' | `----'/  ;   
|  | ' |  | |'   ' ;.    ;  |   | :   '   \ '   ' ;.    .   |  ' ' ' ;   \  \;      :        /___/ \: |   /  ;  /    
:  | | :  ' ;|   | | \   |  '   : |   |    '|   | | \   '   ;  \; /  |\   ;  `      |        .   \  ' .  ;  /  /-,   
|  ; ' |  | ''   : |  ; .'  |   | '   : |.  '   : |  ; .'\   \  ',  /  .   \    .\  ;         \   \   ' /  /  /.`|   
:  | : ;  ; ||   | '`--'    '   : |   | '_\.|   | '`--'   ;   :    /    \   \   ' \ |          \   \  ./__;      :   
'  :  `--'   '   : |        ;   |.'   : |   '   : |        \   \ .'      :   '  |--"            \   \ |   :    .'    
:  ,      .-.;   |.'        '---' ;   |,'   ;   |.'         `---`         \   \ ;                '---";   | .'       
 `--`----'   '---'                '---'     '---'                          '---"                      `---'          
                                                    
    """ + Fore.RESET
    for i in range(len(animation)):
        time.sleep(0.0006)
        sys.stdout.write(animation[i % len(animation)])
        sys.stdout.flush()

def input_anim(text:str=""):
    animation = "\n[>] " + text
    for i in range(len(animation)):
        time.sleep(0.06)
        sys.stdout.write(animation[i % len(animation)])
        sys.stdout.flush()

def restart(code:int=-1, arg1="", arg2=""):
    try:
        sys.stdout.write("Restarting terminal...\n")
        sys.stdout.flush()
        cmd = ""
        if arg1 and not arg2:
            cmd = f'python main.py -t "{arg1}"'
        elif arg2 and not arg1:
            cmd = f'python main.py -ip "{arg2}"'
        elif arg1 and arg2:
            cmd = f'python main.py -ip "{arg2}" -t "{arg1}"'
        else:
            cmd = "python main.py"
        with open("__cache__/happened.log", "w") as f:
            f.write("restarted")
            f.close()
            
        os.system(cmd)
        sys.exit(code)
    except FileNotFoundError:
        sys.stdout.write("Can't restart terminal. Please rerun the command manually.")