hora = int(input("Digite a hora: "))
minutos = int(input("Digite os minutos: "))


hora_em_minutos = hora * 60


total_minutos = hora_em_minutos + minutos


total_segundos = total_minutos * 60


print("Hora convertida em minutos:", hora_em_minutos, "minutos")
print("Total de minutos:", total_minutos, "minutos")
print("Total de minutos convertidos em segundos:", total_segundos, "segundos")
