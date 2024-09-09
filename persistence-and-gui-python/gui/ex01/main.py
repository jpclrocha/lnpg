from tkinter import *

window = Tk()
window.title("Agenda")
window.geometry('450x300')

def salvar_usuario():
    nome_input = nome.get()
    endereco_input = endereco.get()
    idade_input = idade.get()
    cpf_input = cpf.get()
    
    with open("ex.txt","a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome_input} - {endereco_input} - {idade_input} - {cpf_input}\n")

def deletar_usuario():
    print("DDDD")

nomeLabel = Label(window, text="Digite seu nome")
nomeVar = StringVar()
nome = Entry(window, textvariable=nomeVar)

enderecoLabel = Label(window, text="Digite seu endereco")
enderecoVar = StringVar()
endereco = Entry(window, textvariable=enderecoVar)

cpfLabel = Label(window, text="Digite seu cpf")
cpfVar = StringVar()
cpf = Entry(window, textvariable=cpfVar)

idadeLabel = Label(window, text="Digite sua idade")
idadeVar = IntVar()
idade = Entry(window, textvariable=idadeVar)

salvar = Button(window,text="Salvar", command=salvar_usuario)
deletar = Button(window, text="Deletar", command=deletar_usuario)

listbox = Listbox(window, height=10)

# populando listbox
listboxComponents = []
with open("ex.txt", "r", encoding="utf-8") as arquivo:
    arquivoList = arquivo.read().split("\n")
    arquivoList.pop()
    listboxComponentsVar = StringVar(value=arquivoList)
    for msg in arquivoList:
        listbox.insert(-1,msg)

# configuracao do layout com grid
nomeLabel.grid(row=0)
nome.grid(row=0,column=1)

enderecoLabel.grid(row=1)
endereco.grid(row=1,column=1)

cpfLabel.grid(row=2)
cpf.grid(row=2,column=1)

idadeLabel.grid(row=3)
idade.grid(row=3,column=1)

salvar.grid(row=4, column=0)
deletar.grid(row=4, column=1)

listbox.grid(row=5 ,column=0,columnspan=2)


window.mainloop()


