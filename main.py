import os, subprocess
from components.un1print import errorOut, helpOut, normalOut, restart, loading_anim, initial_logo, input_anim
from components.user import check_usr, _log_usr_, _get_cached_usr_, _decode_usr_, get_user_awards, delete_user_progress
from components.network import _get_loc_ip_, uni_connect
from lessons import begin, OhSINT

try:
    os.system("cls")
    loading_anim(2)
    initial_logo()

    isUser = check_usr()

    cachedusr = _get_cached_usr_()

    if cachedusr != None:
        lines = cachedusr.readlines()
        first_line = lines[0].strip()
        username = first_line
    else:
        username = _decode_usr_()
    
    def decode_commands():
        try:
            with open("__cache__/happened.log", "r") as f:
                lines = f.read()
                if lines == "restarted":
                    helpOut("Successfully restarted terminal!")
                    f.close()
            os.remove("__cache__/happened.log")
        except FileNotFoundError:
            pass

        if isUser:
            if username:
                usr = username.lower()
                input_anim(f"[{usr}] Insert command")
            else:
                input_anim(f"[User] Insert command")
        else:
            input_anim("Insert command")

        cmd = input(" >> ")

        if cmd == "exit":
            os.system("cls")
            return 0
        elif cmd == "uni user":
            if isUser == None:
                errorOut("You do not have any user registered")
                decode_commands()
            else:
                use = _decode_usr_()
                print(str(use))
                decode_commands()
        elif cmd == "uni login":
            usrname = input("User name >> ")
            password = input("User password >> ")
            ip = _get_loc_ip_()
            _log_usr_(usrname, password=password, default_ip=ip)
            helpOut("Successfully logged in statically. The next time you launch a network collaboration, you will have this username: " + usrname + ", and this IP address (for now): " + str(ip), animtime=0.004)
            decode_commands()
        elif cmd == "refresh":
            restart()
        elif cmd == "uni connect client" and username != None:
            to_ip = input("SERVER IP >> ")
            to_port = input("SERVER PORT >> ")
            if to_port.isalnum():
                uni_connect(str(username),to_ip,"client",int(to_port))
            else:
                errorOut("You wrote a NON-INT number for the port bro. If you didn't understand, please ask to redty.")
        elif cmd == "uni connect server" and username != None:
            port = input("On what port do you want to host? >> ")
            if port.isalnum():
                uni_connect(str(username), to_port=int(port), type="server")
            else:
                errorOut("You wrote a NON-INT number for the port bro. If you didn't understand, please ask to redty.")
        elif cmd == "uni connect" and username != None:
            to_ip = input("SERVER IP >> ")
            to_port = input("SERVER PORT >> ")
            if to_port.isalnum():
                uni_connect(str(username),to_ip,"client",int(to_port))
            else:
                errorOut("You wrote a NON-INT number for the port bro. If you didn't understand, please ask to redty.")
        elif cmd == "uni update":
            subprocess.Popen("git fetch")
            subprocess.Popen("git pull main")
            helpOut("Updated source code.")
        elif cmd == "uni lesson 1" and username != None:
            begin.gestore(username)
            decode_commands()
        elif cmd == "uni lesson 2" and username != None:
            OhSINT.gestore(username)
        elif cmd == "uni awards" and username != None:
            helpOut(f"Caricamento degli avanzamenti per l'utente {username}...")
            get_user_awards(username)
            decode_commands()
        elif cmd == "uni awards remove" and username:
            delete_user_progress(username)
            decode_commands()
        else:
            if username == None:
                errorOut("Non hai il permesso!! (error 403)")
            else:
                errorOut("Puoi scrivere qualcosa di serio???")
            decode_commands()
            
    decode_commands()
except KeyboardInterrupt:
    os.system("cls")
    errorOut("Exiting... (You could have type exit!)")
    exit(0)