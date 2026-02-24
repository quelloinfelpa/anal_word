import tkinter as tk
from tkinter import filedialog

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    label.config(text=file_path)

def analyze_file():
    path = label.cget("text")
    with open(path, "r") as f:
        righe = f.readlines()
        f.close()

    count = 0
    punt = 0
    spazi = 0

    for r in righe:
        for c in r:
            if c in [".", ",", ";", ":", "!", "?"]:
                punt+=1
            elif c == " ":
                spazi+=1
            count+=1
    
    text_box.config(state=tk.NORMAL)
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, "Numero totale di caratteri: " + str(count) + "\n")
    text_box.insert(tk.END, "Numero totale di segni di punteggiatura (. , ; : ! ?): " + str(punt) + "\n")
    text_box.insert(tk.END, "Numero totale di spazi: " + str(spazi) + "\n")

#layout: label che salva il percorso al file
#bottone a destra del label per selezionare il percorso
#bottone sotto per avviare l'analisi del file
#textbox che mostra i risultati della precedente analisi

root = tk.Tk()
root.title("Analisi file txt")
root.geometry("500x400")

label = tk.Label(root, text="Percorso del file: ")
label.pack()

button_select_file = tk.Button(root, text="Seleziona file", command=select_file)
button_select_file.pack()

button_analyze = tk.Button(root, text="Analizza file", command=analyze_file)
button_analyze.pack()

text_box = tk.Text(root)
text_box.insert(tk.END, "Risultati dell'analisi del file")
text_box.config(state=tk.DISABLED)
text_box.pack()



root.mainloop()