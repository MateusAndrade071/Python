from pytube import YouTube
import customtkinter as ctk
import tkinter 
from tkinter import *

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

# --------------- funcoes

def download():
    try:
        ytlink = link.get()
        ytobject = YouTube(ytlink,on_progress_callback=carregando)
        video = ytobject.streams.get_highest_resolution()
        video.download()
        resultado.configure(Text='Download Completo!')
    except:
        resultado.configure(text='Erro no Download - link Inválido')

def carregando(stream,x,bytes_restantes):
    tamanho_total = stream.filesize
    byte_baixado = tamanho_total - bytes_restantes
    porcentagem = (byte_baixado/tamanho_total)*100
    por = str(int(porcentagem))
    progresso.update()
    progresso.configure(text=f'{por}%')
    #Barra de progresso
    barra.update()
    barra.set(float(porcentagem)/100)
# ----------------------

janela = ctk.CTk()
janela.geometry('800x400')
janela.title('Youtube Downloader V1.1')

ctk.CTkLabel(janela,text='youtube Downloader V1.1',font=('arial',30,'bold')).pack(pady=5)
url = tkinter.StringVar()
link = ctk.CTkEntry(janela,placeholder_text='Digite a URL',width=600,height=40,textvariable=url)
link.pack(pady=5)

btn = ctk.CTkButton(janela, text='Baixar',font=('arial',15,'bold'),command=download)
btn.pack(pady=5)

titulo = ctk.CTkLabel(janela,text='')
titulo.pack(pady=5)

progresso = ctk.CTkLabel(janela,text='0%',font=('arial',25,'bold'))
progresso.pack(pady=3)

barra = ctk.CTkProgressBar(janela,width=500,fg_color='grey',progress_color='white')
barra.set(0)
barra.pack(pady=5)

resultado = ctk.CTkLabel(janela,text='',font=('arial',18,'bold'))
resultado.pack(pady=5)

janela.mainloop()