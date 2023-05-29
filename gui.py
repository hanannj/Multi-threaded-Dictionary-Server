import tkinter as tk
import socket

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Dictionary Client")
        self.master.geometry("400x600")
        self.master.resizable(True, True)  # allow window resizing
        self.create_widgets()

    def create_widgets(self):
        # Label for the word entry field
        word_label = tk.Label(self.master, text="Enter a word:", font=("Arial", 14))
        word_label.pack(pady=10)

        # Entry field for the word
        self.word_entry = tk.Entry(self.master, font=("Arial", 14))
        self.word_entry.pack()
        self.word_entry.bind("<Return>", lambda event: self.send_word())  # bind Return key

        # Submit button
        submit_button = tk.Button(self.master, text="Submit", font=("Arial", 14), command=self.send_word)
        submit_button.pack(pady=10)

        # Frame for the definition label and scrollbar
        definition_frame = tk.Frame(self.master)
        definition_frame.pack(pady=10)

        # Scrollbar for the definition text
        scrollbar = tk.Scrollbar(definition_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Label for the definition text
        self.definition_label = tk.Text(definition_frame, font=("Arial", 14), wrap=tk.WORD, yscrollcommand=scrollbar.set)
        self.definition_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Connect the scrollbar to the definition text
        scrollbar.config(command=self.definition_label.yview)

    def send_word(self):
        word = self.word_entry.get()

        # Create the client socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect(("localhost", 12345))

        # Send a word to the server
        client_socket.send(word.encode())

        # Receive the definition from the server
        definition = client_socket.recv(1024).decode()

        # Update the definition label
        self.definition_label.delete(1.0, tk.END)
        self.definition_label.insert(tk.END, definition)

        # Close the socket
        client_socket.close()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
