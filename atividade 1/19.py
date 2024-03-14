largura = float(input("Digite a largura do cômodo em metros: "))
comprimento = float(input("Digite o comprimento do cômodo em metros: "))


area = largura * comprimento


potencia_iluminacao = area * 18

print("A área do cômodo é:", area, "metros quadrados")
print("A potência de iluminação necessária é:", potencia_iluminacao, "Watts")
