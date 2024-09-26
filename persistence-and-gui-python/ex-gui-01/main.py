from tkinter import *
from tkinter import messagebox

FILENAME = "ex.txt"
is_updating = False
selected_index = None

def carregar_items():
    with open(FILENAME, "r", encoding="utf-8") as file:
        lista = file.readlines()
        return [line.replace("\n","") for line in lista]

def carregar_listbox():
    itemList = carregar_items()
    for item in itemList:
        listbox.insert(END, item)

def limpar_campos():
    global is_updating
    nome.delete(0, END)
    endereco.delete(0, END)
    cpf.delete(0, END)
    idade.delete(0, END)
    is_updating = False

def salvar_lista(lista):
    with open(FILENAME, "w", encoding="utf-8") as arquivo:
        for i in lista:
            arquivo.write(i + "\n")

        limpar_campos()

def onSelect(event):
    global is_updating, selected_index
    try:
        selected_index = listbox.curselection()[0]
        item = listbox.get(selected_index).split(" - ")

        nomeVar.set(item[0])
        enderecoVar.set(item[1])
        cpfVar.set(item[2])
        idadeVar.set(item[3])

        is_updating = True
    except IndexError:
        pass

def atualizar_usuario():
    lista = carregar_items()

    nome_input = nome.get().strip()
    endereco_input = endereco.get().strip()
    idade_input = idade.get()
    cpf_input = cpf.get().strip()

    if(nome_input == "" or endereco_input == "" or cpf_input == ""):
        messagebox.showwarning("Erro nos campos", "Os campos não podem estar vazios!")
        return
    
    try:
        idade_input = int(idade_input)
    except ValueError:
        messagebox.showwarning("Erro nos campos", "Idade precisa ser um numero inteiro!")
        return

    new_item = f"{nome_input} - {endereco_input} - {cpf_input} - {idade_input}"

    if(new_item in lista):
        messagebox.showwarning("Valores duplicados não são aceitos!", f"'{new_item}' já existe na lista!")

    lista[selected_index] = new_item
    listbox.delete(selected_index)
    listbox.insert(selected_index, new_item)
    salvar_lista(lista)

def cadastrar_usuario():
    nome_input = nome.get().strip()
    endereco_input = endereco.get().strip()
    idade_input = idade.get()
    cpf_input = cpf.get().strip()
        
    if(nome_input == "" or endereco_input == "" or cpf_input == ""):
        messagebox.showwarning("Erro nos campos", "Os campos não podem estar vazios!")
        return
    
    try:
        idade_input = int(idade_input)
    except ValueError:
        messagebox.showwarning("Erro nos campos", "Idade precisa ser um numero inteiro!")
        return
    
    
    item = f"{nome_input} - {endereco_input} - {cpf_input} - {idade_input}"

    lista = carregar_items()
    if(item in lista):
        messagebox.showwarning("Valores duplicados não são aceitos!", f"'{item}' já existe na lista!")

    with open(FILENAME,"a", encoding="utf-8") as arquivo:
        arquivo.write(item + "\n")

    listbox.insert(END, item)
    limpar_campos()

def save_button():
    if(is_updating):
        atualizar_usuario()
    else:
        cadastrar_usuario()
    
def deletar_usuario():
    global is_updating
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

salvar = Button(window,text="Salvar", command=save_button)
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
listbox.grid(row=6 ,column=0,columnspan=2, padx=(10,0))

carregar_listbox()
window.mainloop()