# Server Script untuk aplikasi chat multithreaded untuk dua klien
from socket import *
from threading import Thread

client_sock = []    # menyimpan socket klien kedua
client_addresses = {}   # menyimpan {kunci: socket klien, nilai: alamat klien}
public_key = []     # menyimpan kunci publik dari kedua klien

def accept_incoming_connections():
    """Menyiapkan pengelolaan untuk klien yang masuk"""
    client, client_address = SERVER.accept() #Menerima koneksi dari klien
    client_sock.append(client) #Menambahkan klien ke list client_sock
    print("%s:%s telah terhubung." % client_address) #Mencetak alamat klien yang terhubung
    public_key.append(client.recv(BUFFER_SIZE)) #Menerima public key dari klien
    client_addresses[client] = client_address #Menyimpan alamat klien ke dictionary client_addresses


# Fungsi untuk menangani koneksi dari klien pertama
def handle_client1(client_sock, client_addresses):
    """Menangani koneksi klien pertama"""
    # Mengirimkan public key ke klien pertama
    client_sock[0].send(public_key[1])
    
    # Perulangan untuk menerima dan mengirim pesan
    while True:
        # Menerima pesan dari klien pertama
        msg0 = client_sock[0].recv(BUFFER_SIZE)
        # Mengirim pesan ke klien kedua
        client_sock[1].send(msg0)
        # Menampilkan pesan yang diterima dari klien pertama
        print(" Client 1: %s" % msg0.decode('utf8'))


# Fungsi ini digunakan untuk menangani koneksi kedua dari client
def handle_client2(client_sock, client_addresses): 
    """Menangani koneksi kedua dari client"""
    # Mengirimkan public key kepada client
    client_sock[1].send(public_key[0])
    
    # Perulangan untuk menerima dan mengirim pesan
    while True:
        # Menerima pesan dari client
        msg1 = client_sock[1].recv(BUFFER_SIZE)
        # Mengirim pesan ke client lain
        client_sock[0].send(msg1)
        # Menampilkan pesan yang diterima
        print(" Client 2: %s" % msg1.decode('utf8'))


#----SOCKET Part----
# Port dapat diubah sesuai keinginan
HOST = gethostbyname(gethostname())     # Mendapatkan IP host
PORT = 42000
BUFFER_SIZE = 1024   # Ukuran buffer penerima
ADDRESS = (HOST, PORT)  # Alamat socket server

SERVER = socket(AF_INET, SOCK_STREAM)   # Membuat objek socket
SERVER.bind(ADDRESS)    # Menghubungkan IP dan nomor port socket

SERVER.listen(2)
print('Server IP: ', HOST)
print("Menunggu koneksi...")
accept_incoming_connections()
accept_incoming_connections()

Thread(target = handle_client1, args = (client_sock, client_addresses)).start()
Thread(target = handle_client2, args = (client_sock, client_addresses)).start()
print('Percakapan terenkripsi: ')
SERVER.close()