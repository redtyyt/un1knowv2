import os, base64, random
from components.un1print import errorOut, helpOut

def _log_usr_(usr:str,default_ip:str="0.0.0.0",password:str="None"):
    login = os.getlogin()
    usr_b = usr.encode()
    base85_login = base64.b85encode(usr_b)
    print(base85_login)
    password_b = password.encode()
    base64_pass = base64.b64encode(password_b)
    abs_path = os.path.abspath(os.sep)
    usr_ref = abs_path + "Users\\" + login + "\\AppData\\Local\\Un1\\"
    cache_usr = open("__cache__/usr.un1", 'w')
    try:
        os.mkdir(usr_ref)
    except FileExistsError:
        pass
    
    cache_usr.write(f"{usr}\n{default_ip}\n{str(password_b)}")
    tkn = random.randbytes(1)

    usr_f = open(usr_ref + "usr.un1", 'w')
    
    usr_f.writelines(f"{base85_login}\n{tkn}\n{base64_pass}")
    usr_f.close()
    return True

def check_usr():
    try:
        usr_ref = os.path.abspath(os.sep) + "Users\\" + os.getlogin() + "\\AppData\\Local\\Un1\\usr.un1"
        usr_file = open(usr_ref, 'r')
        return usr_file
    except FileNotFoundError:
        return None
    
def _get_cached_usr_():
    try:
        f = open("__cache__/usr.un1", 'r')
        return f
    except FileNotFoundError:
        errorOut("No cached user found.")
        return None

def _decode_usr_():
    try:
        usr_ref = os.path.join(os.path.abspath(os.sep), "Users", os.getlogin(), "AppData", "Local", "Un1", "usr.un1")
        
        with open(usr_ref, 'r') as usr_f:
            lines = usr_f.readlines()

        # Estrai la prima riga, togli il prefisso b' e l'apice finale
        first_line = lines[0].strip()
        if first_line.startswith("b'") and first_line.endswith("'"):
            base85_encoded = first_line[2:-1]
        else:
            return None  # Formato non valido

        # Decodifica base85
        decoded_username = base64.b85decode(base85_encoded)

        # Debug print (puoi rimuoverlo o sostituirlo con errorOut)
        print("Decoded username:", decoded_username.decode(errors="ignore"))

        return decoded_username.decode(errors="ignore")

    except FileNotFoundError:
        return None
    
def award_user(user_name:str, medal:str):
    helpOut(f"BRAVO {user_name}! Hai ottenuto una nuova medaglia: {medal}!")
    usr_ref = os.path.join(os.path.abspath(os.sep), "Users", os.getlogin(), "AppData", "Local", "Un1", "awards.un1")
    f = open(usr_ref, 'a')
    f.write(medal)
    f.close()
    return True

def delete_user_progress(user_name:str):
    errorOut(f"Sei sicuro di eliminare il tuo progresso {user_name}?")
    io = input("(si o no o s/n) >> ")
    if io == "si" or io == "s":
        usr_ref = os.path.join(os.path.abspath(os.sep), "Users", os.getlogin(), "AppData", "Local", "Un1", "awards.un1")
        f = open(usr_ref, 'w')
        f.write("")
        f.close()
        return True
    if io == "no" or io == "n":
        helpOut("Ok sei a posto.")
        return False
    else:
        errorOut("Cosa? Puoi rispondere")