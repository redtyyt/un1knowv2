import os
import time
import threading
from colorama import Fore
from components.un1print import restart
from components.user import award_user

# Lista per salvare le domande già risposte
domande_risposte = []

def des(username: str):
    print(f"Ciao {username}, questa è una lezione tradotta in italiano da tryhackme.com.")
    print("In questa sfida dovrai capire a partire DA UNA SOLA IMMAGINE la sua provenienza, fino ad arrivare a rispondere a tutte le domande.")

def ohsint():
    print("Ora verrà scaricata un'immagine proprio nella cartella Un1hackers.")
    print("Aspetta che si scarichi e ti dirò cosa fare.")
    os.system('curl -O "https://raw.githubusercontent.com/redtyyt/un1knowv2/resources/WindowsXP_1551719014755.jpg"')
    print("Ho appena finito di scaricare sul tuo PC l'immagine da cui devi partire.")
    print("Ora te la apro...")
    os.system("WindowsXP_1551719014755.jpg")
    time.sleep(2.5)
    print(Fore.GREEN + "Adesso prova a prendere tutti i dati possibili da quell'immagine!" + Fore.RESET)
    print("""Le domande sono:
 1. Cosa raffigura l'avatar di questo utente?
 2. In che città si trova questa persona?
 3. Qual è il suo indirizzo di posta personale?
 4. Dove hai trovato il suo indirizzo email (nome sito web)?
 5. Dove è andato in vacanza?""")
    print("Per rispondere a una domanda, digita il numero di questa.\n")

def rispondi():
    while True:
        dom = input("Num domanda >> ").strip()
        
        if dom not in ["1", "2", "3", "4", "5", "exit"]:
            print("Non c'è alcuna domanda col numero che hai scritto.")
            continue
        
        if dom == "exit":
            restart()
            break

        if dom in domande_risposte:
            print("Hai già risposto a questa domanda!")
            continue

        risposta = input("Scrivi la risposta >> ").strip().lower()

        risposte_corrette = {
            "1": "gatto",
            "2": ["london", "londra"],
            "3": "owoodflint@gmail.com",
            "4": "github",
            "5": "new york"
        }

        corretta = False

        if dom in ["1", "3", "4", "5"]:
            corretta = risposta == risposte_corrette[dom]
        elif dom == "2":
            corretta = risposta in risposte_corrette["2"]

        if corretta:
            print(Fore.GREEN + "Bravo! Risposta corretta." + Fore.RESET)
            domande_risposte.append(dom)
        else:
            print(Fore.RED + "Risposta sbagliata, prova a investigare meglio!" + Fore.RESET)

def get_are_all_asked(user_name: str):
    while True:
        if all(q in domande_risposte for q in ["1", "2", "3", "4", "5"]):
            print(Fore.GREEN + "\nHai risposto a tutte le domande! Ottimo lavoro!" + Fore.RESET)
            award_user(user_name, "ohsint\n")
            time.sleep(4)
            restart()
            break
        time.sleep(1)

def gestore(user_name: str):
    des(user_name)
    input("Pronto? Premi Enter per iniziare.")
    ohsint()
    threading.Thread(target=get_are_all_asked, daemon=True, args=(user_name,)).start()
    rispondi()
