#O O(1) é o Tempo Constante.É o sonho de todo programador. É a melhor classificação possível.O que significa "Constante"?Significa que não importa o tamanho da sua lista (se tem 10 itens ou 10 bilhões), o código vai levar exatamente o mesmo tempo para rodar. Ele é instantâneo.A Analogia da Vida RealImagine que você entra em uma sala escura e quer acender a luz.Sala pequena: Você aperta o interruptor. A luz acende.Galpão gigante: Você aperta o interruptor. A luz acende.O tempo que você leva para apertar o botão é o mesmo, não importa o tamanho da sala. Isso é $O(1)$.


#Como identificar $O(1)$ no seu código (Python)
#Existem duas situações clássicas onde o $O(1)$ aparece. Pode testar no seu VS Code:1. Acessar uma posição específica (Índice)Quando você sabe exatamente onde o dado está, o computador vai direto lá. Ele não procura, ele "teletransporta".

lista = [10, 20, 30, 40, 50]

# Isso é O(1)
# O computador pula direto para a gaveta 0.
print(lista[0])

#2. Usar Dicionários (Hash Maps) - Muito importante para Backend
#Isso é o que você mais vai usar na Wise. Dicionários em Python (ou Hash Maps em Java) encontram valores instantaneamente baseados em uma chave.
# Tabela de preços
precos = {
    "arroz": 20.00,
    "feijao": 8.50,
    "carne": 45.00
}

# Isso é O(1)
# Você não lê a lista de produtos. Você vai direto na etiqueta "feijao".
valor = precos["feijao"]

#Por que isso é crucial na sua transição de carreira?Se um entrevistador te perguntar:"Como podemos verificar se um usuário existe no nosso banco de dados da forma mais rápida possível?"A resposta de Junior brilhante é:"Devemos usar uma estrutura de Hash Map (Dicionário) ou um Índice no banco de dados, para que a busca seja O(1) (tempo constante), em vez de varrer a lista toda ($O(n)$)."Ficou claro agora? O(1) = Acesso imediato, sem "loop".
