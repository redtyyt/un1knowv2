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
    
def get_awards_file_path() -> str:
    return os.path.join(os.path.abspath(os.sep), "Users", os.getlogin(), "AppData", "Local", "Un1", "awards.un1")

def award_user(user_name: str, medal: str):
    file_path = get_awards_file_path()
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Evita duplicati
    current_awards = set()
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            current_awards = set([line.strip() for line in f.readlines()])

    if medal in current_awards:
        helpOut(f"{user_name}, hai già questa medaglia: {medal}.")
        return False

    with open(file_path, 'a') as f:
        f.write(medal + '\n')

    helpOut(f"BRAVO {user_name}! Hai ottenuto una nuova medaglia: {medal}!")
    return True

def delete_user_progress(user_name: str):
    file_path = get_awards_file_path()
    errorOut(f"Sei sicuro di voler eliminare il tuo progresso, {user_name}?")
    
    while True:
        io = input("(si o no o s/n) >> ").strip().lower()
        if io in ["si", "s"]:
            with open(file_path, 'w') as f:
                f.write("")
            helpOut("Progresso eliminato correttamente.")
            return True
        elif io in ["no", "n"]:
            helpOut("Ok, nessuna modifica fatta.")
            return False
        else:
            errorOut("Risposta non valida. Scrivi 'si' o 'no'.")

def get_user_awards(user_name: str):
    file_path = get_awards_file_path()

    if not os.path.exists(file_path):
        return False, [], []

    try:
        with open(file_path, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
            return lines[:1], lines[1:2]
    except Exception as e:
        errorOut(f"Errore durante la lettura dei premi: {e}")
        return False
