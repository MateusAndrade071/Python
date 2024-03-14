import customtkinter as ctk
from deep_translator import GoogleTranslator

#Funções ---------------------

def traduzir():
    texto_para_traduzir = user_text.get()
    linguagem = lang_to_var.get()
    resultado = GoogleTranslator(source='auto',target=linguagem).translate(texto_para_traduzir)
    translated_text.configure(state='normal')
    translated_text.delete(0,'end')
    translated_text.insert(0,resultado)
#---------------------------------

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

janela = ctk.CTk()
janela.minsize(500,500)
janela.maxsize(600,500)
janela.title('tradutor universal v1.0')

ctk.CTkLabel(janela,text='Tradutor Universal V1.0',font=('Arial',25,'bold'),text_color='DarkGray').pack(anchor=ctk.CENTER,pady=5)

app_frame = ctk.CTkFrame(janela,width=500,height=500,fg_color='transparent')
app_frame.pack(fill=ctk.X, padx=20,pady=10)

ctk.CTkLabel(app_frame,text='Texto para traduzir',font=('Arial',18,'bold')).pack(fill=ctk.X,pady=10)

user_text = ctk.CTkEntry(app_frame,placeholder_text='Digite o texto para traduzir',height=50)
user_text.pack(fill=ctk.X)

ctk.CTkLabel(app_frame,text='Escolha o idioma',font=('Arial',15,'bold')).pack(fill=ctk.X,pady=10)

lang_to_var = ctk.StringVar(value='english')
lang_list = GoogleTranslator().get_supported_languages()

lang_to = ctk.CTkOptionMenu(app_frame,values=lang_list,variable=lang_to_var,dropdown_hover_color='blue')
lang_to.set('english')
lang_to.pack(pady=5)

ctk.CTkLabel(app_frame,text='Texto traduzido',font=('Arial',15,'bold')).pack(fill=ctk.X,pady=10)

translated_text = ctk.CTkEntry(app_frame,placeholder_text='O texto traduzido será mostrado aqui',height=100,placeholder_text_color='gray')
translated_text.pack(fill=ctk.X)

translated_btn = ctk.CTkButton(app_frame,text='Traduzir',font=('Arial',14,'bold'),height=40,command=traduzir)
translated_btn.pack(fill=ctk.X,pady=20)

janela.mainloop()