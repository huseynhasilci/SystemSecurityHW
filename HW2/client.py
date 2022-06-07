import threading
import socket
username = input('Type Username: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 55000))


def show_users(user_list):
    print(f'\nUser List:\n-----------')
    for i in range(len(user_list)):
        print(f'{i+1}- {user_list[i]}')
    user_choice = input("--------------------\nChoice >> ")
    client.send(user_choice.encode('utf-8'))
    response = client.recv(4096).decode('utf-8')
    if response:
        print(f'Verification Result: Verified!\n-------------\n{response}\n-------------\n')
    else:
        print(f'Verification Result: Not Verified!')


def client_receive():
    global username
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "username":
                client.send(username.encode('utf-8'))
            elif message == "invalid-username":
                print("Username is taken. Please try another one.")
                username = input('Type Username: ')
                client.send(username.encode('utf-8'))
            elif message == "select-option":
                print("""\nSelect an option:\n1- Verify User Certificates\n2- Message integration""")
                choice = input("Choice >> ")
                client.send(choice.encode('utf-8'))
                users_string = client.recv(1024).decode('utf-8')
                user_list = users_string.strip().split(" ")
                show_users(user_list)
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()
