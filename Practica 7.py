from datetime import datetime


opcion = input("Escoger\n1.- Imprimir YYYY/MM/DD \n2.- Imprimir MM/DD/YYYY\n")
if opcion == "1":
    print(datetime.today().strftime('%Y/%m/%d'))
elif opcion == "2":
    print(datetime.today().strftime('%m/%d/%Y'))
else:
    print("Opcion no valida")
