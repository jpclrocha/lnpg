from tkinter import *
from tkinter import messagebox

FILENAME = "ex.txt"
def carregar_items():
    with open(FILENAME, "r", encoding="utf-8") as arquivo:
        lista = arquivo.readlines()
        return [line.replace("\n","") for line in lista]
    
def carregar_listbox():
    itemList = carregar_items()
    for item in itemList:
        listbox.insert(END, item)

def limpar_campos():
    nome.delete(0, END)
    endereco.delete(0, END)
    cpf.delete(0, END)
    idade.delete(0, END)

def onSelect(event):
    item = listbox.get(int(listbox.curselection()[0])).split(" - ")
    nomeVar.set(item[0])
    enderecoVar.set(item[1])
    cpfVar.set(item[2])
    idadeVar.set(item[3])

def atualizar_usuario():
    lista = carregar_items()

    nome_input = nome.get().strip()
    endereco_input = endereco.get().strip()
    idade_input = idade.get().strip()
    cpf_input = cpf.get().strip()

    item = f"{nome_input} - {endereco_input} - {cpf_input} - {idade_input}"
    item_listbox = listbox.get(listbox.curselection()[0])

    if(item != item_listbox):
        if(item in lista):
            # voltar aqui
            res = messagebox.showwarning("Valores duplicados não são aceitos!", f"'{item}' já existe na lista!")
            if(res):
                lista.index(item)
            return
        
        lista[lista.index(item_listbox)] = item

        with open(FILENAME, "r+", encoding="utf-8") as arquivo:
            # setando o mouse no inicio e apagando todo o conteudo do arquivo
            arquivo.seek(0)
            arquivo.truncate(0)

            # escrevendo a nova lista, ja tendo removido o item deletado
            for i in lista:
                arquivo.write(i + "\n")

            # pegando o index do item a ser deletado na listbox e removendo-o
            idx = listbox.get(0, END).index(item_listbox)
            listbox.delete(idx)
            listbox.insert(idx, item)
            limpar_campos()

def salvar_usuario():
    if(len(listbox.curselection()) > 0):
        atualizar_usuario()
    else:
        nome_input = nome.get().strip()
        endereco_input = endereco.get().strip()
        idade_input = idade.get().strip()
        cpf_input = cpf.get().strip()
        
        item = f"{nome_input} - {endereco_input} - {cpf_input} - {idade_input}"

        if(item.strip("-") == ""):
            messagebox.showwarning("Erro nos campos", "Os campos não podem estar vazios!")
            return
        
        lista = carregar_items()
        if(item in lista):
            # voltar aqui
            res = messagebox.showwarning("Valores duplicados não são aceitos!", f"'{item}' já existe na lista! Você está tentando atualizar o item?")
            if(res):
                lista.index(item)
            return

        with open(FILENAME,"a", encoding="utf-8") as arquivo:
            arquivo.write(item + "\n")

        listbox.insert(END, item)
        limpar_campos()
    
def deletar_usuario():
    try:
        item_to_delete = listbox.get(listbox.curselection())
        with open(FILENAME, "r+", encoding="utf-8") as arquivo:
            arquivoList = arquivo.readlines()
            lista = [line.replace("\n","") for line in arquivoList]

            # removendo o item da lista
            lista.pop(lista.index(item_to_delete))

            # setando o mouse no inicio e apagando todo o conteudo do arquivo
            arquivo.seek(0)
            arquivo.truncate(0)

            # escrevendo a nova lista, ja tendo removido o item deletado
            for i in lista:
                arquivo.write(i + "\n")
            
            # pegando o index do item a ser deletado na listbox e removendo-o
            idx = listbox.get(0, END).index(item_to_delete)
            listbox.delete(idx)
            limpar_campos()
    except TclError:
        messagebox.showwarning("Nenhum item selecionado!", "Para apagar um item, primeiro selecione algo a partir da lista!")
        return

window = Tk()
window.title("Agenda")
window.geometry('300x300')

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

listboxLabel = Label(window, text="Agenda")
listbox = Listbox(window, width=40,height=10, selectmode=SINGLE)

listbox.bind("<<ListboxSelect>>", onSelect)

salvar = Button(window,text="Salvar", command=salvar_usuario)
deletar = Button(window, text="Deletar", command=deletar_usuario)

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
listboxLabel.grid(row=5)
listbox.grid(row=6 ,column=0,columnspan=2)

carregar_listbox()
window.mainloop()