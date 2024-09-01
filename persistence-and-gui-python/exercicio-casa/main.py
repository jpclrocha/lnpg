def getTelefonePessoaMaisNova():
    with open("ex-casa.txt", "r", encoding="utf-8") as arquivo:
        lista = arquivo.read().split("\n")
        lista.pop()
        idadeRef = 999
        telefoneMaisNova = ""
        for item in lista:
            pessoa = item.split("|")
            idade = int(pessoa[1])
            if(idade < idadeRef):
                idadeRef = idade
                telefoneMaisNova = pessoa[3]
        print(f"Telefone da pessoa mais nova: {telefoneMaisNova}")

def getNomePessoaMaisVelha():
    with open("ex-casa.txt", "r", encoding="utf-8") as arquivo:
        lista = arquivo.read().split("\n")
        lista.pop()
        idadeRef = 0
        nomeMaisVelha = ""
        for item in lista:
            pessoa = item.split("|")
            idade = int(pessoa[1])
            if(idade > idadeRef):
                idadeRef = idade
                nomeMaisVelha = pessoa[0]
        print(f"Telefone da pessoa mais velha: {nomeMaisVelha}")

def getMediaIdade():
    with open("ex-casa.txt", "r", encoding="utf-8") as arquivo:
        lista = arquivo.read().split("\n")
        lista.pop()
        somaIdade = 0
        for item in lista:
            somaIdade += int(item.split("|")[1])
        media = somaIdade / len(lista)
        print(f"Media de idade: {media}")

def buscaUsuariosPeloSexo(sexo):
    with open("ex-casa.txt", "r", encoding="utf-8") as arquivo:
        lista = arquivo.read().split("\n")
        lista.pop()
        userList = []
        for item in lista:
            if(item.split("|")[2] == sexo):
                userList.append(item)

        if(len(userList) < 1):
            print("Nao existe nenhum usuario com esse sexo!")
        else:
            print(userList)

def busca_usuario_pelo_nome(nome_procurado: str):
    with open("ex-casa.txt", "r", encoding="utf-8") as arquivo:
        lista = arquivo.read().split("\n")
        lista.pop()
        userList = []
        for item in lista:
            if(nome_procurado.lower() in item.split("|")[0].lower()):
                userList.append(item)
            
        if(len(userList) < 1):
            print("Nao existe nenhum usuario com esse nome!")
        else:
            print(userList)
                

def adicionarPessoas():
    nome  = ""
    while True:
        nome = str(input("Digite o nome: "))
        
        if(nome == "0"):
            print("Voce voltou ao menu principal!")
            break
        
        idade = int(input("Digite a idade: "))
        sexo = str(input("Digite o sexo (M ou F): ")).upper()
        while sexo != "M" and sexo != "F":
            print("Apenas M ou F sao respostas validas!")
            sexo = str(input("Digite o sexo (M ou F): ")).upper()
        telefone = str(input("Digite o telefone: "))


        with open("ex-casa.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{nome}|{idade}|{sexo}|{telefone}\n")

def listarPessoas():
    with open("ex-casa.txt", "r", encoding="utf-8") as arquivo:
        lista = arquivo.read().split("\n")
        lista.pop()
        for item in lista:
            pessoa = item.split("|")
            print(f"Nome: {pessoa[0]}")
            print(f"Idade: {pessoa[1]} anos")
            if(pessoa[2].upper() == "M"):
                print(f"Sexo: Masculino")
            elif(pessoa[2].upper() == "F"):
                print(f"Sexo: Feminino")
            print(f"Telefone: {pessoa[3]} \n")

def menu():
    opcao = ""
    while(opcao != "7"):
        print("1 - Adicionar pessoas")
        print("2 - Listar pessoas")
        print("3 - Telefone da pessoa mais nova")
        print("4 - Nome da pessoa mais velha")
        print("5 - Media de idade")
        print("6 - Buscar usuarios pelo sexo")
        print("7 - Buscar usuario por nome")
        print("8 - Sair")
        opcao = str(input("Digite sua escolha: "))

        if(opcao == "1"):
            adicionarPessoas()
        elif(opcao == "2"):
            listarPessoas()
        elif(opcao == "3"):
            getTelefonePessoaMaisNova()
        elif(opcao == "4"):
            getNomePessoaMaisVelha()
        elif(opcao == "5"):
            getMediaIdade()
        elif(opcao == "6"):
            sexo = str(input("Digite o sexo (M ou F): ")).upper()
            while sexo != "M" and sexo != "F":
                print("Apenas M ou F sao respostas validas!")
                sexo = str(input("Digite o sexo (M ou F): ")).upper()
            buscaUsuariosPeloSexo(sexo)
        elif(opcao == "7"):
            nome = input("Digite o nome que deseja ser buscado: ")
            busca_usuario_pelo_nome(nome)
        elif(opcao == "8"):    
            print("Voce escolheu sair")    
        else:
            print("Opcao invalida!")

menu()