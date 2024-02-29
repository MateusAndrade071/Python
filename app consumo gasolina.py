import customtkinter as ctkn

ctkn.set_appearance_mode('dark')
ctkn.set_default_color_theme('green')
janela = ctkn.CTk()
janela.geometry('550x400')
janela.iconbitmap('49_85223.ico')
janela.title('Combustivel app 2024')

def calcular():
    d = int(distancia.get())
    c = int(consumo.get())
    p = float(preco.get())
    
    valor = (d/c)*p
    
    resultado.configure(text=f'O gasto total da viagem foi R$ {valor:.2f}')

texto = ctkn.CTkLabel(janela,text='Pit Stop',font=('verdana',20,'bold'))
texto.pack(padx=10,pady=10)

distancia = ctkn.CTkEntry(janela,placeholder_text="digite a distancia da viagem: ",width=300,height=30,fg_color='gray',
text_color='black',placeholder_text_color='white')
distancia.pack(padx=10,pady=10)

consumo = ctkn.CTkEntry(janela,placeholder_text="digite o consumo da viagem: ",width=300,height=30,fg_color='gray',
text_color='black',placeholder_text_color='white')
consumo.pack(padx=10,pady=10)

preco = ctkn.CTkEntry(janela,placeholder_text="digite o preço da viagem: ",width=300,height=30,fg_color='gray',
text_color='black',placeholder_text_color='white')
preco.pack(padx=10,pady=10)

botao = ctkn.CTkButton(janela,text='calcular viagem',font=('verdana',20,'bold'),fg_color='darkgreen',hover_color='darkred',height=50,command=calcular)
botao.pack(padx=10,pady=10)

resultado = ctkn.CTkLabel(janela,text='',text_color='yellow',font=('verdana',18,'bold'))
resultado.pack(padx=10,pady=10)

janela.mainloop()