# Client TCP multithread che invia NUM_WORKERS richieste contemporanee al server
# Ogni richiesta contiene un'operazione aritmetica da eseguire

import socket         # Per la comunicazione di rete
import json           # Per la codifica/decodifica JSON
import random         # Per generare numeri casuali
import time           # Per misurare i tempi di esecuzione
import threading      # Per gestire l'esecuzione parallela (multithreading)

# --- Configurazione ---
HOST = "127.0.0.1"           # IP del server
PORT = 5005                # Porta del server (assicurarsi che il server stia ascoltando su questa)
NUM_WORKERS = 15            # Numero di richieste (thread) da inviare in parallelo
OPERAZIONI = ["+", "-", "*", "/", "%"]  # Lista delle operazioni consentite

#1 Funzione che genera le richieste simulate per il server
def genera_richieste(address, port):
    #2 apertura socket client
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
        sock_service.connect((address, port))  # Connessione al server

        #3 generazione dei di operatori randomini
        primo_numero = random.randint(0, 100)
        operazione = OPERAZIONI[random.randint(0, 3)]  # Scegli operazione a caso (tra le prime 4)
        secondo_numero = random.randint(0, 100)

        print(f"{threading.current_thread().name}: {primo_numero}{operazione}{secondo_numero}")

        #4 Salviamo i dati in un dizionario che verrà convertito in un json
        messaggio = {
            "primo_numero": primo_numero,
            "operazione": operazione,
            "secondo_numero": secondo_numero
        }
        messaggio = json.dumps(messaggio)

        ##5 Invia il pacchetto al server
        sock_service.sendall(messaggio.encode("UTF-8"))

        #6 Inizia il tempo che ci metterà il server a rispondere
        start_time_thread = time.time()

        #7 Aspetta la risposta del server
        data = sock_service.recv(1024)

    data.decode()

    #8 Dopo aver ricevuto mette in pause il tempo, lo calcola e mostra in console il tempo e i dati ricevuti
    end_time_thread = time.time()
    print("Received: ", )
    print(f"{threading.current_thread().name} exec time = ", end_time_thread - start_time_thread)

# --- Punto di ingresso del programma ---
if __name__ == "__main__":
    start_time = time.time()  # Tempo di inizio totale

    #9 Lista di Threads per la generazione di richieste
    threads = [
        threading.Thread(target=genera_richieste, args=(HOST, PORT))
        for _ in range(NUM_WORKERS)
    ]

    #10 Fa partire i thread
    [thread.start() for thread in threads]

    #11 Aspetta che tutti i thread finiscano
    [thread.join() for thread in threads]

    end_time = time.time()  # Tempo di fine totale

    # Stampa il tempo complessivo impiegato per eseguire tutte le richieste
    print("Tempo totale impiegato = ", end_time - start_time)