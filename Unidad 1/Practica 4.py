DicM =  {}
def Menu() :
    print("\n\n------- Seleccione una opcion --------")
    print(" 1 - Ingresar Asignaturas")
    print(" 2 - Salir" )
    op = int(input("Teclee el valor: "))
    if op not in [1,2]:
        Menu()
    else:
        if op == 1: Captura()
        if op == 2: exit()

def Captura():
    lista = []
    print("\n------- Rellene los campos --------")
    numSemestre = int(input("Ingrese el numero del semestre: "))
    if numSemestre >= 8 :
        print("\n *** El semestre debe ser inferior a 8vo ***")
        Menu()
    else:
        exit = True
        while (exit):
            nomMateria = input("Ingrese el nombre de la Asignatura: ")
            numCredito = int(input("Ingrese los creditos: "))
            DicM[nomMateria] = int(numCredito)
            print("\n\n------- ¿Quiere agregar otra materia? --------")
            print(" 1 - Si")
            print(" 2 - No" )
            exit = int(input("Teclee el valor: "))
            if exit not in [1,2]:
                break
            else:
                if exit == 2: exit = False
            
        print("\n+---------- Mostrando Asignaturas ----------+")
        Creditos = 0
        for key, value in DicM.items():
            Creditos = Creditos + value 
            print(f'Asignatura: {key} tiene {value} créditos.') 
            print("+---------------------------------------+")   
        print(f'\nEl total de creditos es: {Creditos}') 
Menu()
