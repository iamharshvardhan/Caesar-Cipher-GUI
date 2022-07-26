from ast import alias
from ctypes import alignment
from tkinter import *

# ---------------------------- Encoding and Decoding ------------------------------- #

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encoder():
    simple_word = input_message_text.get("1.0", "end-1c")
    shift_key = key.get()
    encoded_word = ""
    for char in simple_word:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_key
            encoded_word += alphabet[new_position]
        else:
            encoded_word += char
    output_message_text.insert(END, encoded_word)


def decoder():
    simple_word = input_message_text.get("1.0", "end-1c")
    shift_key = key.get() * -1
    decoded_word = ""
    for char in simple_word:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_key
            decoded_word += alphabet[new_position]
        else:
            decoded_word += char
    output_message_text.insert(END, decoded_word)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Caeser Cipher")
window.config(height=500, width=500, padx=50, pady=50)

input_message = Label(text="Pre-Operation:", font=("Arial", 10))
input_message.grid(column=1, row=0, padx=5, pady=5)

input_message_text = Text(width=30, height=1)
input_message_text.grid(column=2, row=0)

encode = Button(text="Encode", font=("Times New Roman", 10), width=10, command=encoder)
encode.grid(column=1, row=2)

key = Scale(from_=1, to=25, width=15, orient=HORIZONTAL)
key.grid(column=2, row=2)

decode = Button(text="Decode", font=("Times New Roman", 10), width=10, command=decoder)
decode.grid(column=3, row=2)

output_message = Label(text="Post-Operation:", font=("Arial", 10))
output_message.grid(column=1, row=3, padx=5, pady=5)

output_message_text = Text(width=30, height=1)
output_message_text.grid(column=2, row=3)


window.mainloop()
