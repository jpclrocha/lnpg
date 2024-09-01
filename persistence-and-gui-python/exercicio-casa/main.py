def getTelefonePessoaMaisNova():
    with open("ex-casa.txt", "r", encoding="utf-8") as arquivo:
        lista = arquivo.read().split("\n")
        idadeRef = 999
        telefoneMaisNova = ""
        for item in lista:
            pessoa = item.split("|")
            if(len(pessoa) > 1):
                idade = int(pessoa[1])
                if(idade < idadeRef):
                    idadeRef = idade
                    telefoneMaisNova = pessoa[3]
        print(f"Telefone da pessoa mais nova: {telefoneMaisNova}")

def getNomePessoaMaisVelha():
    with open("ex-casa.txt", "r", encoding="utf-8") as arquivo:
        lista = arquivo.read().split("\n")
        idadeRef = 0
        nomeMaisVelha = ""
        for item in lista:
            pessoa = item.split("|")
            if(len(pessoa) > 1):
                idade = int(pessoa[1])
                if(idade > idadeRef):
                    idadeRef = idade
                    nomeMaisVelha = pessoa[0]
        print(f"Telefone da pessoa mais velha: {nomeMaisVelha}")

def getMediaIdade():
    with open("ex-casa.txt", "r", encoding="utf-8") as arquivo:
        lista = arquivo.read().split("\n")
        somaIdade = 0
        for item in lista:
            pessoa = item.split("|")
            if(len(pessoa) > 1):
                somaIdade += int(pessoa[1])
        media = somaIdade / (len(lista) - 1)
        print(f"Media de idade: {media}")
        print(lista)

            

def adicionarPessoas():
    nome  = ""
    while True:
        nome = str(input("Digite o nome: "))
        
        if(nome == "0"):
            print("Voce voltou ao menu principal!")
            break
        
        idade = int(input("Digite a idade: "))
        sexo = str(input("Digite o sexo (M ou F): "))
        telefone = str(input("Digite o telefone: "))


        with open("ex-casa.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{nome}|{idade}|{sexo}|{telefone}\n")

def menu():
    opcao = ""
    while(opcao != "5"):
        print("1 - Adicionar pessoas")
        print("2 - Telefone da pessoa mais nova")
        print("3 - Nome da pessoa mais velha")
        print("4 - Media de idade")
        print("5 - Sair")
        opcao = str(input("Digite sua escolha: "))

        if(opcao == "1"):
            adicionarPessoas()
        elif(opcao == "2"):
            getTelefonePessoaMaisNova()
        elif(opcao == "3"):
            getNomePessoaMaisVelha()
        elif(opcao == "4"):
            getMediaIdade()
        elif(opcao == "5"):
            print("Voce escolheu sair")
        else:
            print("Opcao invalida!")

menu()