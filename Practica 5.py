def ImprimirDic(**n):
    for a in n:
        print(f'{a} : {n[a]}')
        
ImprimirDic(Jose="Estudiante",Pepe="Ingeniero")