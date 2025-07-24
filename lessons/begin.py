import time
from prompt_toolkit import prompt
from prompt_toolkit.patch_stdout import patch_stdout
from components.un1print import helpOut
from components.user import award_user


def desc(username:str=""):
    print(f"In questa lezione, {username} dovrai riuscire ad arrivare ad un file nel desktop di questo computer tramite questo terminale e poi capirne il contenuto.")

def cmd():
    with patch_stdout():
        command = prompt("PS C:\\Users\\Computer> ")
        if command == "cd Desktop":
            print("Corretto! Adesso ti trovi nel desktop. Ora trova il file 'hello.txt' e poi capiscine il contenuto.")
            command = prompt("PS C:\\Users\\Computer\\Desktop> ")
            if command == "ls":
                print("Anche questa opzione è corretta. Serve per capire dov'è il file in questo caso.")
                print("""Mode         LastWriteTime     Length  Name
                      ____         _____________     ______  ____
                      a----     32/06/2025   10:00      2    hello.txt""")
            command = prompt("PS C:\\Users\\Computer\\Desktop> ")    
            if command == "cat hello.txt":
                print("\nciao!\n")
                print("Esatto! Proprio così. Sei riuscito a trovare il contenuto del file tramite il comando 'cat'. Ricordatelo per le prossime sfide!")
                print("Possiamo anche dire che hai catturato la bandiera! Complimenti!")
                return True
        else:
            print("\nComando non corretto o non registrato... Prova a usare un altro comando\n")
            cmd()

def gestore(usr_name:str):
    desc(usr_name)
    time.sleep(5)
    res = cmd()
    if res == True:
        award_user(usr_name, "inizio\n")