# 1. Carregando os dados do cliente (Dicionário)
cliente = {
    "nome": "Alik Serrano",
    "saldo": 500.00
}

# 2. O cliente tentou enviar 800 euros no aplicativo!
valor_enviado = 800.00

print("Iniciando transferência para", cliente["nome"], cliente["saldo"])

# 3. A Lógica de Decisão (Preencha as lacunas!)
# SE o saldo do cliente for maior ou igual ao valor enviado:
if cliente["saldo"] >= valor_enviado:
    print("✅ Transferência Aprovada! O dinheiro está a caminho.")
# SENÃO:
else:
    print("❌ Transferência Recusada. Saldo insuficiente.")


    cliente = {
    "nome": "Alik Serrano",
    "saldo": 500.00
}

# 1. Vamos testar uma transferência que VAI SER APROVADA agora
valor_enviado = 200.00 

print("Iniciando transferência para", cliente["nome"])

# SE o saldo for suficiente:
if cliente["saldo"] >= valor_enviado:
    
    # 2. A MÁGICA: Atualizamos a gaveta "saldo", subtraindo o valor enviado
    cliente["saldo"] = cliente["saldo"] - valor_enviado
    
    print("✅ Transferência Aprovada! O dinheiro está a caminho.")
    print("Seu novo saldo é de:", cliente["saldo"])

# SENÃO:
else:
    print("❌ Transferência Recusada. Saldo insuficiente.")