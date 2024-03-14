salario = float(input("Digite o seu salario:"))

conta1 = float(input("Digite o valor da primeira conta:"))

conta2 = float(input("Digite o valor da segunda conta:"))

calculo1 = 2 / 100 * conta1 + conta1
calculo2 = 2 / 100 * conta2 + conta2

total = salario - (calculo1 + calculo2)

print (total)