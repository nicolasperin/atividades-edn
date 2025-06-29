tipo_temperatura = int(input("Você deseja entrar com uma temperatura em qual unidade?\n\n1 - Celsius\n2 - Fahrenheit\n3 - Kelvin\n\n"))

if tipo_temperatura != 1 and tipo_temperatura != 2 and tipo_temperatura != 3:
    print("Tipo inválido!")
    temperatura = 0
else:
    temperatura = float(input("Informe a temperatura: "))

    if tipo_temperatura == 1:
        print(f"{temperatura} °C equivalem a {((temperatura*9.5) + 32):.2f}°F e {(temperatura + 273.15):.2f} K")
    elif tipo_temperatura == 2:
        print(f"{temperatura} °F equivalem a {((temperatura - 32)*5/9):.2f} °C e {((temperatura - 32)*5/9 + 273.15):.2f} K")
    else:
        print(f"{temperatura} K equivalem a {(temperatura - 273.15):.2f} °C e {((temperatura - 273.15)*9/5 + 32):.2f} °F")
        