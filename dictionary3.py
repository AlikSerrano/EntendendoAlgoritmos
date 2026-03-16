# A transação acabou de ser criada no sistema
transacao = {
    "cliente": "Alik",
    "moeda_origem": "BRL",
    "moeda_destino": "EUR",
    "valor_enviado": 1000
}

# 1. O cliente mudou de ideia e quer enviar mais dinheiro. 
# Atualize o "valor_enviado" para 1500.
transacao["valor_enviado"] = 1500

# 2. O time de Compliance exigiu uma etiqueta nova de segurança.
# Crie a chave "status" e dê o valor de "aprovado" (lembre das aspas em textos!).
transacao["status"] = "aprovado"

# 3. Imprima o dicionário inteiro para ver as mudanças!
print("Transação atualizada:", transacao)

# O sistema carrega o perfil atual do cliente
perfil_cliente = {
    "nome": "Alik Serrano",
    "plano": "Standard",
    "saldo_euros": 250.00
}

# 1. O cliente fez um depósito e o saldo aumentou em 100 euros.
# Sabendo que o saldo era 250.00, atualize a chave do saldo para 350.00.
perfil_cliente["saldo_euros"] = 350.00

# 2. O cliente decidiu fazer um upgrade na conta!
# Atualize a chave "plano" de "Standard" para "Premium" (lembre-se das aspas!).
perfil_cliente["plano"] = "Premium"

# 3. O departamento de impostos precisa de uma nova informação no sistema.
# Crie uma NOVA chave chamada "pais_residencia" e atribua o valor "Portugal" (ou "Brasil").
perfil_cliente["pais_residencia"] = "Portugal"

# 4. Imprima o dicionário inteiro para garantir que tudo está correto!
print("Perfil atualizado no sistema:", perfil_cliente)

print("ESTOU NO UNIVERSO PARALELO E NADA PODE ME ATINGIR")