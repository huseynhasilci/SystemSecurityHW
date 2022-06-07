import threading
import socket
username = input('Type Username: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 55000))


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
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()
