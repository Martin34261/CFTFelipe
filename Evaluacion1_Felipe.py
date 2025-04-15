print("Hola, aqui habla el asistente de este telefono.")
num1=int(input("Ingrese los sminutos que usted ha estado en el telefono en el DIA ¡EL MAXIMO ES DE 100!: "))
num2=int(input("Ingrese los minutos que usted ha estado en el telefono en la NOCHE ¡EL MAXIMO ES DE 80!: "))
num3=int(input("Ingrese los minutos EXTRA que usted ha estado en el telefono En el DIA:"))
num4=int(input("Ingrese los minutos EXTRA que usted ha estado en el telefono en la NOCHE:"))
#CALCULOS
total1= num1+num3
total2= num2+num4
result1=10*num1
result2=7*num2
result3=15*num3
result4=13*num4
totalpago1= result1+result2+result3+result4

#RESULTADOS
if num1 >= 100 and num2 >=80:
    print(f"DIA: SI EXCEDE: {total1}")
    print(f"NOCHE: SI EXCEDE: {total2}")
    print(f"CLIENTE PAGA: {totalpago1}")
elif num1 <=100 and num2 <=80:
    print(f"DIA: NO EXCEDE: {total1}")
    print(f"NOCHE: NO EXCEDE: {total2}")
    print(f"CLIENTE PAGA: {totalpago1}")
elif num1 <=100 and num2 >=80:
    print(f"DIA: NO EXCEDE: {total1}")
    print(f"NOCHE: SI EXCEDE: {total2}")
    print(f"CLIENTE PAGA: {totalpago1}")
elif num1 >=100 and num2 <=80:
    print(f"DIA: SI EXCEDE: {total1}")
    print(f"NOCHE: NO EXCEDE: {total2}")
    print(f"CLIENTE PAGA: {totalpago1}")

#ESTO ESTA MEDIO BUENO