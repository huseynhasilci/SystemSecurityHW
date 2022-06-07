import threading
import socket
import time

from User import User
from CA import CA

host = 'localhost'
port = 55000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = {}  # key: username, value: client
users = {}  # key: username, value: User Class


def handle_option(option, client):
    if option == '1':
        string = ' '.join([str(usr) for usr in clients.keys()])
        client.send(string.encode('utf-8'))
        user_choice = client.recv(20).decode('utf-8')
        nicknames = string.strip().split(" ")
        selected_user = users[nicknames[int(user_choice) - 1]]
        # verify public key.
        response = CA.verify_public_key(selected_user.get_certificated_public_key(), selected_user.get_public_key())
        client.send(response)


# Function to handle clients'connections


def handle_client(client):
    try:
        client.send('username'.encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        # check username
        while True:
            is_valid = check_username(username)
            if not is_valid:
                client.send('invalid-username'.encode('utf-8'))
                username = client.recv(1024).decode('utf-8')
                continue
            break
        # create user with certificated public key.
        # ---------- PART - 1 --------------------------
        user = User(username)
        user.create_key_pair()
        certificated_public_key = CA.certificate_public_key(username, user.get_public_key())
        user.set_certificated_public_key(certificated_public_key)
        # -----------------------------------------------
        # add to system.
        users[username] = user
        clients[username] = client
        client.send('SERVER MESSAGE: you are now connected!'.encode('utf-8'))
        time.sleep(1)
        # redirect user wrt option
        while True:
            client.send("select-option".encode('utf-8'))
            option = client.recv(20).decode('utf-8')
            handle_option(option, client)
    except:
        username = ""
        _user = ""
        for user in clients:
            if clients[user] == client:
                username = user
                _user = user
                break
        del clients[_user]
        client.close()
        del users[username]


def check_username(username):
    if username in clients.keys():
        return False
    return True
# Main function to receive the clients connection


def receive():
    print('Server is running and listening ...')
    while True:
        client, address = server.accept()
        print(f'connection is established with {str(address)}')
        # thread
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


if __name__ == "__main__":
    CA = CA()
    receive()