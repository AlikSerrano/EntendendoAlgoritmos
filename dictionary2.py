transacao = {
    "cliente": "Alik",
    "moeda_origem": "BRL",
    "moeda_destino": "EUR",
    "valor_enviado": 1000
}

# 2. Lendo a transação inteira
print("Todos os dados:", transacao)

# 3. Lendo apenas UMA etiqueta específica (Chave)
cliente_nome = transacao["cliente"]
print("Nome do cliente:", cliente_nome)

# 4. Busque o valor enviado e imprima na tela!
pegar_valor = transacao["valor_enviado"]
print("Valor enviado é de:", pegar_valor)

# 5. Mostre a moeda enviada
qual_moeda = transacao["moeda_origem"]
print("A moeda de origem é:", qual_moeda)   

#6. Mostre a moeda de destino
moeda_chegou = transacao["moeda_destino"]
print("A moeda de destino é:", moeda_chegou)