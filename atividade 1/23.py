valor_saque = int(input("Digite o valor do saque: "))

notas_100 = valor_saque // 100
resto = valor_saque % 100

notas_50 = resto // 50
resto %= 50

notas_20 = resto // 20
resto %= 20

notas_10 = resto // 10
resto %= 10

notas_5 = resto // 5

print("* Resultado *")
print("Notas de 100:", notas_100)
print("Notas de 50:", notas_50)
print("Notas de 20:", notas_20)
print("Notas de 10:", notas_10)
print("Notas de 5:", notas_5)
