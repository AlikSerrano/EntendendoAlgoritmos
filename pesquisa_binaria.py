lista = [0, 1, 2, 3]
item = [1]

baixo = 0
alto = len(lista) - 1

meio = ( baixo + alto) // 2  
chute = lista[meio]

#meio será arredondado para baixo automaticamente pelo Python se (baixo + alto) não for um número par

if chute < item:
    baixo = meio + 1

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1 

    while baixo <=alto:
        meio = (baixo + alto) / 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio -1
        else:
            baixo = meio + 1
    return None

my_list = [1, 3, 5, 7, 9]

print (pesquisa_binaria(my_list, 3)) # =>1
print (pesquisa_binaria(my_list, - 1)) # => None


        

