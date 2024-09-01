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
        print(f"Telefone da pessoa mais nova: {nomeMaisVelha}")

def getMediaIdade():
    with open("ex-casa.txt", "r", encoding="utf-8") as arquivo:
        lista = arquivo.read().split("\n")
        print(lista)
        # somaIdade = 0
        # for item in lista:
        #     pessoa = item.split("|")
        #     if(len(pessoa) > 1):
        #         somaIdade += int(pessoa[1])
        # media = somaIdade / len(lista)
        # print(f"Telefone da pessoa mais nova: {media}")

            

def main():
    nome  = ""
    while True:
        nome = str(input("Digite o nome: "))
        
        if(nome == "0"):
            print("Voce escolheu sair!")
            break
        
        idade = int(input("Digite a idade: "))
        sexo = str(input("Digite o sexo (M ou F): "))
        telefone = str(input("Digite o telefone: "))


        with open("ex-casa.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{nome}|{idade}|{sexo}|{telefone}\n")


main()
getTelefonePessoaMaisNova()
getNomePessoaMaisVelha()
getMediaIdade()