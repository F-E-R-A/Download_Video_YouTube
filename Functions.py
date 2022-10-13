import tkinter as tk
import tkinter.messagebox
from tkinter import *
from tkinter import ttk, BOTH, LEFT, X, Y, VERTICAL, HORIZONTAL, RIGHT, TOP, N, S, W, SE, NW, NONE, BOTTOM, YES, NO, \
    filedialog
import Image
from PIL import ImageTk
from tkinter.font import Font
import youtube_dl


class Functions():
    def __init__(self, **kwargs):
        print("Iniciando o construtor...")
        pass

    def Connect_1(self, **kwargs):
        Link_ = [self.Imp1.get()]
        GET_Select = self.Select1.get()
        try:
            self.LB3['text'] = ""
            self.LB4['text'] = ""
            if GET_Select == "MP4":
                #print(Link_)
                self.Baixar_MP4(Link_)
            if GET_Select == "MP3":
                self.Baixar_MP3(Link_)
        except youtube_dl.utils.DownloadError:
            self.LB3['text'] = "*"
            self.LB4['text'] = "O campo está VAZIO ou a URL é inválida."

    def Baixar_MP4(self, Link):
        link = Link
        ydl_options = {
                       'format': 'best',
                       'outtmpl': 'C:/Users/%USERNAME%/Downloads/%(title)s.mp4'
                       }
        with youtube_dl.YoutubeDL(ydl_options) as ydl:
            ydl.download(link)

    def Baixar_MP3(self, Link):
        link = Link
        ydl_opetions = {
                        'format': 'bestaudio/best',
                        'outtmpl': 'C:/Users/%USERNAME%/Downloads/%(title)s.mp3',
                        'postprogressor': [{'key': 'FFmpegExtractAudio',
                                            'preferredcodec': 'mp3',
                                            'preferredquality': '192',
                                           }]
                       }
        with youtube_dl.YoutubeDL(ydl_opetions) as ydl:
            ydl.download(link)


    def Close(self):
        MSG = tkinter.messagebox.askquestion(title="Sair do programa", message="Você realmente deseja sair?")
        if MSG == "yes":
            self.root.destroy()

    def Clean_Imput(self):
        self.Imp1.delete(0, END)

    def Janela_1(self, **kwargs):
        self.root = tk.Tk()
        self.root.geometry("650x350+360+180")
        self.root.title("Download_Your_Video")
        self.root.resizable(True, True)

        Icon_0 = tk.PhotoImage(file="Images/youtube.png")
        LB1 = tk.Label(master=self.root, text="  Baixe vídeos do YouTube gratuitamente.", image=Icon_0, bg="blue", fg="white", compound=LEFT)
        LB1.pack(fill=BOTH, ipady=5)

        #Primeiro Frame:
        Frame_1 = tk.Frame(master=self.root)
        Frame_1.pack()

        LB2 = tk.Label(master=Frame_1, text="Cole o link do vídeo abaixo:", anchor="w")
        LB2.pack(fill=BOTH, side=TOP, expand=NO, padx=48, pady=(50, 0))

        #Mensagem de alerta de Erro "Campo vazio":
        Font_0 = tk.font.Font(family='Arial', size=15)
        self.LB3 = tk.Label(master=Frame_1, text="", font=Font_0, fg="red")
        self.LB3.pack(fill=X, side=tk.LEFT, padx=(39,0))

        self.Imp1 = tk.Entry(master=Frame_1, width=80)
        self.Imp1.pack(fill=X, side=tk.LEFT, padx=(2, 5), ipady=3, anchor="n")

        self.Select1 = ttk.Combobox(master=Frame_1, width=10)
        self.Select1["values"] = ("MP4",
                             "MP3",
                             "WAV",
                             "MOV",
                             "AVI")
        self.Select1.current(0)
        self.Select1.pack(side=tk.TOP, padx=(2, 50), ipady=3, anchor="w")

        #Terceiro Frame:
        Frame_3 = tk.Frame(master=self.root)
        Frame_3.pack(ipadx=92)

        #Mensagem de alerta de erro "Campo vazio":
        Font_1 = tk.font.Font(family='Arial', size=8)
        self.LB4 = tk.Label(master=Frame_3, text="", font=Font_1, fg="red", anchor="w")
        self.LB4.pack(fill=BOTH, padx=(50, 0))

        Icon_1 = tk.PhotoImage(file="Images/sair.png")
        BT1 = tk.Button(master=Frame_3, text="  Sair", image=Icon_1, bg="#FFA6A6", fg="black", border=1, command=self.Close, compound=LEFT)
        BT1.pack(side=LEFT, padx=(50, 0), pady=(30, 0), ipadx=10, ipady=2)

        Icon_2 = tk.PhotoImage(file="Images/campo-de-texto.png")
        BT2 = tk.Button(master=Frame_3, text="  Limpar campo", image=Icon_2, bg="#00B5EC", fg="black", border=1, command=self.Clean_Imput, compound=LEFT)
        BT2.pack(side=LEFT, padx=10, pady=(30, 0), ipadx=10, ipady=2)

        Icon_3 = tk.PhotoImage(file="Images/baixar.png")
        BT3 = tk.Button(master=Frame_3, text="  Baixar", image=Icon_3, bg="#8EFF92", fg="black", border=1, command=self.Connect_1, compound=LEFT)
        BT3.pack(side=RIGHT, padx=50, pady=(30, 0), ipadx=20, ipady=2)

        #Quarto Frame:
        Frame_4 = tk.Frame(master=self.root)
        Frame_4.pack()

        self.LB5 = tk.Label(master=Frame_4, text="Após clicar em BAIXAR, espere até que o Download seja concluído.\n "
                                                 "O programa pode travar durante o processo de Download.", fg="#097C9F")
        self.LB5.pack(pady=(20,0))

        #Quinto Frame:
        Frame_5 = tk.Frame(master=self.root)
        Frame_5.pack(pady=(10,0))

        self.IMG_1 = ImageTk.PhotoImage(Image.open("Images/checked.png"))
        self.Image_Label_1 = tk.Label(master=Frame_5, image=self.IMG_1)
        self.Image_Label_1.pack(side=tk.LEFT)

        Font_2 = tk.font.Font(family='Verdana', size=12)
        self.LB6 = tk.Label(master=Frame_5, text="Download Concluído!", font=Font_2, fg="green")
        self.LB6.pack(fill=BOTH, side=tk.TOP, padx=(5,0))

        Font_3 = tk.font.Font(family="Verdana", size=7)
        self.LB7 = tk.Label(master=Frame_5, text="Seu arquivo está na pasta de Downloads.", font=Font_3, fg="green")
        self.LB7.pack(side=TOP)



        self.root.mainloop()





