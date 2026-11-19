import socket

def burrows_wheeler(stringa):
    if not stringa:
        return""

rotazioni =[]

for i in range(len(stringa)):
    rotazione=stringa[i:]+stringa[:i]
    rotazioni.append(rotazione)

    rotazione.sort()

     risultato=""
for rotazione in rotazioni:
        risultato +=rotazione[-1]

        return risultato

HOST="127.0.0.1"
PORT=5000

stinga=input("inserisci una stringa:")

client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(HOST,PORT)
server. listen(1)

print("Server in ascolto sulla porta"PORT)

while True:
    connessione,indirizzo=server.accept()
    print("Connessione ricevuta da:",indirizzo)

    whit connessione:
    dati=connessione.recv(4096)

    if not dati:

        stringa=dati.decode("utf-8")
        print("string ricevuta:",stringa)
         risultato = burrows_wheeler(stringa)
         print("Trasformata bwt:"risultato)
         connessione.sendall(risultato.encode("utf-8"))

         print("Risultato inviato al client")

