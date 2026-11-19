import socket

HOST="127.0.0.1"
PORT=5000

stinga=input("inserisci una stringa:")

client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    client.connect((HOST,PORT))
    print("connessione al server stabilita")

    client.sendall(stringa.encode("utf-8"))
    dati=client.recv(4096)

    risultato=dati.decode("utf-8")

    print("trasformata di Burrows-Wheeler:"risultato)

    exception ConnectionRefusedError:
        print("Errore impossibile connettersi")

    finally:
        client.close()
