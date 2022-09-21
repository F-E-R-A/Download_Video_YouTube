import tkinter as tk
from tkinter import END

import youtube_dl


def Connect():
    link = Imp1.get()
    if link == "":
        LB3["text"] = "Campo acima não pode estar vazio."
    else:
        try:
            LB3["text"] = "Link válido."
            LB5["text"] = "Aguarde o download ser concluído..."
            Link_Format = [link]
            Download(Link_Format)
        except(youtube_dl.utils.DownloadError):
            LB3["text"] = "Error. Link inválido."

def Download(Link):
    link = Link
    with youtube_dl.YoutubeDL() as ydl:
        try:
            ydl.download(link)
            LB5["fg"] = "green"
            LB5["text"] = "Download concluído com sucesso."
        except:
            LB5["text"] = "Error..."


def Close():
    root.destroy()

def Clean():
    Imp1.delete(0, END)


root = tk.Tk()
root.geometry("430x300")
root.title("You_Download")

LB1 = tk.Label(root, text="Baixe vídeos do YouTube Gratuitamente. Basta colar o link do vídeo abaixo.")
LB1.place(x=20, y=20)

LB2 = tk.Label(root, text="Cole a url do vídeo aqui.", fg="blue")
LB2.place(x=140, y=120)

LB3 = tk.Label(root, text="", fg="red")
LB3.place(x=53, y=174)

LB5 = tk.Label(root, text="", fg="blue")
LB5.place(x=50, y=240)

Imp1 = tk.Entry(root)
Imp1.place(x=50, y=150, width=320, height=25)

BT1 = tk.Button(root, text="Fechar", command=Close)
BT1.place(x=50, y=195, width=70)

BT2 = tk.Button(root, text="Limpar campo", command=Clean)
BT2.place(x=130, y=195)

BT3 = tk.Button(root, text="Baixar", command=Connect)
BT3.place(x=300, y=195, width=70)

root.mainloop()