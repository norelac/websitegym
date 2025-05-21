import nltk
from nltk.chat.util import Chat, reflections

# Definisi pola dan respons
pola = [
    (r"Halo|Hi|Hai", ["Halo!", "Hi!", "Hai!"]),
    (r"Apa kabar?", ["Saya baik, terima kasih!", "Baik sekali!"]),
    (r"Siapa namamu?", ["Saya adalah chatbot sederhana."]),
    (r"Bye|Selamat tinggal", ["Selamat tinggal!", "Sampai jumpa!"]),
]

# Buat chatbot
chatbot = Chat(pola, reflections)

# Mulai percakapan
print("Halo! Saya adalah chatbot sederhana. Ketik 'Bye' untuk mengakhiri.")
while True:
    user_input = input("Anda: ")
    if user_input.lower() == "bye":
        print("Chatbot: Selamat tinggal!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)