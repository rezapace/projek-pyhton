from socket import *
from threading import Thread
import tkinter, sys, time
import RSA

def receive():
    """Mengelola penerimaan pesan."""
    msg_list.insert(tkinter.END, " selamat datang! %s" % NAME)
    msg_list.insert(tkinter.END, " kamu sudah online!")
    while True:
        try:
            # Menerima pesan dari client dengan buffer size yang telah ditentukan 
            msg = CLIENT.recv(BUFFER_SIZE).decode("utf8")
            # Dekripsi pesan menggunakan private key 1
            msg = RSA.decrypt_string(msg, private_key_1)
            # Menambahkan pesan ke list pesan
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Kemungkinan client telah meninggalkan chat.
            break

def send(event = None):  # event dikirim oleh binders.
    """Mengelola pengiriman pesan."""
    # Mengambil pesan dari input field
    msg = my_msg.get()    
    my_msg.set("")  # Membersihkan input field.
    # Menambahkan nama pengguna di depan pesan
    msg = NAME + ": " + msg
    # Menambahkan pesan ke list pesan
    msg_list.insert(tkinter.END, msg)
    # Enkripsi pesan menggunakan public key 2
    msg = RSA.encrypt_string(msg, public_key_2)
    # Mengirim pesan ke client
    CLIENT.send(bytes(msg, "utf8"))
    

def on_closing(event = None):
    """Fungsi ini akan dipanggil ketika jendela ditutup."""
    msg_list.insert(tkinter.END, "going offline...")
    time.sleep(2)
    # Menutup koneksi dengan client
    CLIENT.close()
    top.quit()
    sys.exit()


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


# Membuat koneksi socket antara client dan server
HOST = input('Masukkan host: ')
PORT = int(input('Masukkan port: '))
NAME = input('Masukkan nama Anda: ')
BUFFER_SIZE = 1024
ADDRESS = (HOST, PORT)

CLIENT = socket(AF_INET, SOCK_STREAM)    # objek socket client
CLIENT.connect(ADDRESS)	# untuk terhubung ke alamat socket server

# Membuat kunci RSA
public_key_1, private_key_1 = RSA.key_generator()
msg = str(public_key_1[0]) + '*' + str(public_key_1[1])
CLIENT.send(bytes(msg, "utf8"))
m = CLIENT.recv(BUFFER_SIZE).decode('utf8')
public_key_2 = [int(x) for x in m.split('*')]

# Membuat thread untuk fungsi receive
receive_thread = Thread(target = receive)   
receive_thread.start()
tkinter.mainloop()  # Menjalankan GUI.