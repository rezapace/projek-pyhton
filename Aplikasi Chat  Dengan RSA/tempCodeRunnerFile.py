from socket import *
from threading import Thread
import tkinter, sys, time
import RSA

def receive():
    """Handles receiving of messages."""
    msg_list.insert(tkinter.END, " Welcome! %s" % NAME)
    msg_list.insert(tkinter.END, " You are online!")
    while True:
        try:
            msg = CLIENT.recv(BUFFER_SIZE).decode("utf8")
            msg = RSA.decrypt_string(msg, private_key_1)
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break

def send(event = None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()    
    my_msg.set("")  # Clears input field.
    msg = NAME + ": " + msg
    msg_list.insert(tkinter.END, msg)
    msg = RSA.encrypt_string(msg, public_key_2)
    CLIENT.send(bytes(msg, "utf8"))
    

def on_closing(event = None):
    """This function is to be called when the window is closed."""
    msg_list.insert(tkinter.END, "going offline...")
    time.sleep(2)
    CLIENT.close()
    top.quit()
    sys.exit()


#----tkinter GUI----
top = tkinter.Tk()
top.title("Aplikasi Chat Menggunakan Algoritma RSA")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=25, width=100, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

input_frame = tkinter.Frame(top)
input_text = tkinter.Entry(input_frame, textvariable=my_msg, width=50)
input_text.grid(row=0, column=0, padx=5, pady=5)

send_button = tkinter.Button(input_frame, text="Send", command=send, width=10)
send_button.grid(row=0, column=1, padx=5, pady=5)

input_frame.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)
