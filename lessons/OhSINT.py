import subprocess
from prompt_toolkit import prompt
from prompt_toolkit.patch_stdout import patch_stdout
from components.un1print import helpOut

def des(username:str):
    print(f"Ciao {username}, questa è una lezione tradotta in italiano da tryhackme.com.")
    print(f"In questa sfida dovrai capire a partire DA UNA SOLA IMMAGINE la sua provenienza fino ad arrivare a rispondere a tutte le domande.")
    ready = input("Pronto? Clicca enter per iniziare.")
    if ready:
        return True
    
def ohsint():
    print("Ora verrà scaricata un'immagine proprio nella cartella Un1hackers.")
    print("Aspetta che si scarichi e ti dirò cosa fare.")
    subprocess.Popen('curl -O "https://tryhackme-vm-upload.s3.eu-west-1.amazonaws.com/WindowsXP_1551719014755.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA2YR2KKQMWLXEMXW4%2F20250724%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20250724T074952Z&X-Amz-Expires=120&X-Amz-Signature=d0d9f8dd51889a0e1be91330bd317e85ba876f95d8dab952ec187b3b192d803f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject"')

def gestore(user_name:str):
    ss = des(user_name)
    if ss == True:
        ohsint()