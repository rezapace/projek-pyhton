from socket import *
from threading import Thread
import tkinter, sys, time
import RSA

def receive():
    """Mengelola penerimaan pesan."""
    msg_list.insert(tkinter.END, " Selamat datang! %s" % NAME)
    msg_list.insert(tkinter.END, " Anda sudah online!")
    while True:
        try:
            # Menerima pesan dari client dengan buffer size yang telah ditentukan 
            msg = CLIENT.recv(BUFFER_SIZE).decode("utf8")
            # Dekripsi pesan menggunakan private key 2 
            msg = RSA.decrypt_string(msg, private_key_2)
            # Menambahkan pesan ke list 
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Kemungkinan client telah meninggalkan chat.
            break

def send(event = None):  # event dikirimkan oleh pengikat.
    """Mengelola pengiriman pesan."""
    msg = my_msg.get()    
    my_msg.set("")  # Membersihkan kolom input.
    msg = NAME + ": " + msg
    msg_list.insert(tkinter.END, msg)
    msg = RSA.encrypt_string(msg, public_key_1)
    CLIENT.send(bytes(msg, "utf8"))

def on_closing(event = None):
    """Fungsi ini akan dipanggil ketika jendela ditutup."""
    msg_list.insert(tkinter.END, "going offline...") # Menambahkan pesan 'going offline...' ke daftar pesan
    time.sleep(2) # Menunggu selama 2 detik
    CLIENT.close() # Menutup koneksi dengan client
    top.quit() # Keluar dari window
    sys.exit() # Keluar dari program


# Membuat GUI menggunakan tkinter
top = tkinter.Tk()
top.title("Aplikasi Chat Menggunakan Algoritma RSA")

# Membuat frame untuk pesan
messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # Untuk pesan yang akan dikirim.
scrollbar = tkinter.Scrollbar(messages_frame)  # Untuk navigasi melalui pesan lama.
# Berikut akan berisi pesan.
msg_list = tkinter.Listbox(messages_frame, height=25, width=100, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

# Membuat frame untuk input
input_frame = tkinter.Frame(top)
input_text = tkinter.Entry(input_frame, textvariable=my_msg, width=50)
input_text.grid(row=0, column=0, padx=5, pady=5)

# Membuat tombol kirim
send_button = tkinter.Button(input_frame, text="Send", command=send, width=10)
send_button.grid(row=0, column=1, padx=5, pady=5)

input_frame.pack()

# Membuat fungsi saat window ditutup
top.protocol("WM_DELETE_WINDOW", on_closing)


# Mendefinisikan variabel HOST, PORT, NAME, BUFFER_SIZE, dan ADDRESS
HOST = input('Masukkan host: ')
PORT = int(input('Masukkan port: '))
NAME = input('Masukkan nama Anda: ')
BUFFER_SIZE = 1024
ADDRESS = (HOST, PORT)

# Membuat objek socket client
CLIENT = socket(AF_INET, SOCK_STREAM)

# Menghubungkan ke alamat socket server
CLIENT.connect(ADDRESS)

# Membuat kunci RSA
public_key_2, private_key_2 = RSA.key_generator()

# Mengirimkan public key ke server
msg = str(public_key_2[0]) + '*' + str(public_key_2[1])
CLIENT.send(bytes(msg, "utf8"))

# Menerima public key dari server
m = CLIENT.recv(BUFFER_SIZE).decode('utf8')
public_key_1 = [int(x) for x in m.split('*')]

# Membuat thread untuk method receive
receive_thread = Thread(target = receive)
receive_thread.start()

# Memulai eksekusi GUI
tkinter.mainloop()
