transacoes = [200, 50 , 100]

# 1. Chegou uma nova transferência de 300 no final do dia. (Entrar no fim)
transacoes.append(300)

# 2. O CEO da Wise mandou uma transferência urgente de 999. Ela precisa furar a fila e ser a PRIMEIRA (Posição 0).
transacoes.insert(0, 999)

# 3. O cliente cancelou a transferência de 50. Ache ela pelo NOME/VALOR e remova.
transacoes.remove(50)

# 4. A última transferência da fila (aquela no finalzinho) deu erro no sistema e precisa ser expulsa.
transacoes.pop()

# 5. O time de auditoria quer ver a lista organizada do menor para o maior valor.
transacoes.sort()

# 6. O seu gerente mudou de ideia e quer a lista de trás para frente (do maior para o menor).
transacoes.reverse()

# 7. Imprima o resultado final
print("Lote final para o Banco Central:", transacoes)
