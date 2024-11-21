n1 = int(input(""))
n2 = int(input(""))

list_1 = []
list_2 = []

for i in range(n1):
    list_1.append(input(""))
    
for i in range(n2):
    list_2.append(input(""))
    
uniao = []
intersecao = []
diferenca = []

for i in list_1:
    if(i not in uniao):
        uniao.append(i)

for i in list_2:
    if(i not in uniao):
        uniao.append(i)
        
# intersecao
for i in list_1:
    for j in list_2:
        if(i == j):
            intersecao.append(i)
        
# diferenca
for i in list_1:
    if(i not in list_2 and i not in diferenca):
        diferenca.append(i)
        
print(uniao)
print(intersecao)
print(diferenca)