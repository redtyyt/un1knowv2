import socket, threading, time
from components.un1print import helpOut, errorOut, normalOut, restart
from prompt_toolkit import prompt
from prompt_toolkit.patch_stdout import patch_stdout

def _get_loc_ip_():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()
    except Exception as e:
        if e == "[WinError 10051] Tentativo di operazione del socket verso una rete non raggiungibile":
            ip = "Not connected"
        ip = f"Unknown. {e}"
    finally:
        s.close()
    return ip

def uni_connect(user_name:str, to_ip:str="", type:str="client", to_port:int=12345):
    if not user_name:
        errorOut("You can't enter here! You have no permission (code 403).")
        time.sleep(1)
        restart()
    if type == "client":
        if to_ip and to_port:
            try:
                cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                cli_sock.connect((to_ip, to_port))
                helpOut(f"[{user_name}] Now connected to {to_ip}:{to_port}\n\n")

                def recieve():
                    while True:
                        try:
                            data = cli_sock.recv(1024).decode()
                            if data:
                                print("\r" + " " * 80 + "\r", end="")
                                normalOut(f"{data}\n", anim=False)
                        except Exception as e:
                            errorOut(f"[{user_name}] Connection interrupted : {e}\n")
                            break
                
                threading.Thread(target=recieve, daemon=True).start()
                with patch_stdout():
                    while True:
                        message = prompt("You >> ")
                        if message.lower == f"[{user_name}] /exit\n":
                            break
                        elif message.lower == f"[{user_name}] /refresh\n":
                            restart()
                        encoded = f"[{user_name}] {message}\n".encode()
                        cli_sock.sendall(encoded)
                
                cli_sock.close()
                errorOut(f"[{user_name}] Disconnected from the host")
            except KeyboardInterrupt:
                errorOut("Loading main menu...")
                restart()
    elif type == "server":
        if to_port:
            try:
                HOST = '0.0.0.0'
                PORT = to_port

                lp = _get_loc_ip_()
                helpOut(f"[{user_name}] Your LAN IP is: {lp}", anim=False)
                helpOut(f"[{user_name}] Tell the clients this IP and PORT: {lp}:{PORT}", anim=False)

                svr_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                svr_sock.bind((HOST, PORT))
                helpOut(f"[{user_name}] Connected to {HOST}:{PORT}", anim=False)

                svr_sock.listen()
                helpOut(f"[{user_name}] Listening...")

                cli_socket, cli_addr = svr_sock.accept()
                errorOut(f"[{user_name}] New connection from {cli_socket} (his name will be revealed when he sends a message).\n\n", anim=False)

                def svr_rec():
                    while True:
                        try:
                            data = cli_socket.recv(1024).decode()
                            if data:
                                print("\r" + " " * 80 + "\r", end="")
                                normalOut(f"{data}\n", anim=False)
                        except Exception as e:
                            errorOut(f"[{user_name}] Connection interrupted : {e}")
                            break
                threading.Thread(target=svr_rec, daemon=True).start()
                with patch_stdout():
                    while True:
                        message = prompt("You (server) >> ")
                        if message.lower == f"[{user_name}] /exit\n":
                            message = "THE SERVER IS EXITING!"
                            break
                        encoded = f"[{user_name}] {message}\n".encode()
                        cli_socket.sendall(encoded)
                
                cli_socket.close()
                svr_sock.close()
                errorOut(f"[{user_name}] Connection closed!")
            except KeyboardInterrupt:
                errorOut("Closing connections...")
                cli_socket.close()
                svr_sock.close()
                restart()