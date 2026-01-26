import math

# log2 calcula: 2 elevado a que número dá X?
# Isso é exatamente a pergunta "Quantas divisões por 2 eu preciso fazer?"

passos_128 = math.log2(128)
print(f"Passos para 128: {passos_128}")

passos_256 = math.log2(256)
print(f"Passos para 256: {passos_256}")

passos_grande = math.log2(4000000000)
print(f"Passos para 4 bilhões: {passos_grande}")

bob_nasa = math.log2(1000000000)
print(f"Pesquisa binária para 1 bilhão:{bob_nasa}")