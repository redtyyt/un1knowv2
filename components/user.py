import os, base64, random, json
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
    return os.path.join(os.path.abspath(os.sep), "Users", os.getlogin(), "AppData", "Local", "Un1", "awards.json")

def _load_awards() -> list:
    """Returns the current medal list. (Empty if the file doesn't exist)"""
    path = get_awards_file_path()
    if not os.path.exists(path):
        return []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("medals", [])
    except (json.JSONDecodeError, IOError):
        return []

def _save_awards(medals:list):
    """Writes medal list on the disk."""
    path = get_awards_file_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump({"medals": medals}, f, indent=2, ensure_ascii=False)


def award_user(user_name: str, medal: str):
    medals = _load_awards()
    if medal in medals:
        helpOut(f"{user_name}, hai già questa medaglia <{medal}>")
        return False

    medals.append(medal)
    _save_awards(medals)
    helpOut(f"Complimenti {user_name}! Hai ottenuto una nuova medaglia: {medal}.")
    return True

def delete_user_progress(user_name: str) -> bool:
    errorOut(f"Sicuro di voler eliminare TUTTI I TUOI PROGRESSI IN-APP, {user_name}?")
    while True:
        choice = input("(si/no) >> ").strip().lower()
        if choice in {"si", "s"}:
            _save_awards([])
            helpOut("Progressi eliminati correttamente.")
            return True
        elif choice in {"no", "n"}:
            helpOut("Ok, non lo cancello più adesso.")
            return False
        else:
            errorOut("Risposta non valida, digita 'si' o 'no'.")

def get_user_awards(user_name: str):
    medals = _load_awards()
    if not medals:
        helpOut(f"{user_name}, non hai ancora ottenuto alcuna medaglia. Completa delle sfide e le otterrai.")
        return False, [], []
    f = medals[0] if len(medals) > 0 else None
    s = medals[1] if len(medals) > 1 else None
    return True, f, s