import socket, threading
from database import *

def create_user(client_socket):
    client_socket.sendall("Enter username for the account\n> ".encode())
    name = client_socket.recv(1024).decode().strip().replace(":",'')
    client_socket.sendall("Enter password for the account\n> ".encode())
    pwd = client_socket.recv(1024).decode().strip()
    client_socket.sendall("Enter your uni\n> ".encode())
    uni = client_socket.recv(1024).decode().strip()
    if check_user(name):
        client_socket.sendall("User already registered.\n".encode())
        return
    add_account(name,pwd,uni)

    client_socket.sendall(f"Account created\nUsername: {name}\nPassword: {pwd}\n\n".encode())

def login(client_socket):

    client_socket.sendall("Enter your Username: ".encode())
    name = client_socket.recv(1024).decode().strip()

    valid = login_check(name)
    print(valid)
    if type(valid) == tuple:
        client_socket.sendall(f"they go to {str(valid[1]).strip()}\n".encode())
    elif type(valid) == sqlite3.OperationalError:
        client_socket.sendall(f"ERROR: {valid}\n".encode())
    else:
        client_socket.sendall("No user found\n".encode())
def handle_client(client_socket):
    try:
        MENU = "Commands are as follows:\n1. Create account\n2. Check uni\n> "
        hello_message = "Hello Welcome to my Database fundamentals SQL project!!\nI used a Sqlite3 backend and got ChatGPT to write the SQL queries\nIt should be secure right? :)\n\n"
        client_socket.sendall(hello_message.encode())
        client_socket.sendall(MENU.encode())
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break  # No more data, break the loop
            data = data.strip()
            if data.lower() in ["exit",'q','quit']:
                client_socket.close()
                break
            
            if data=='1':
                create_user(client_socket)
            elif data=='2':
                login(client_socket)
            
            client_socket.sendall("Press Enter to continue: ".encode())
            client_socket.recv(1024).decode().strip()
            client_socket.sendall(MENU.encode())

    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()
        print(f"Connection closed.")

def main():
    # Create a socket object
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to a specific address and port
    server_socket.bind(('0.0.0.0', 54129))
    
    # Listen for incoming connections
    server_socket.listen(1)
    print("Server is listening on port 2222...")
    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
            


    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
