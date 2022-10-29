from usuario import usuario
lstUsuarios = {}

def registro():
    print('--------------Registro de un nuevo usuario------------------')
    user = input("Ingrese su usuario: ")
    pwd = input("Ingrese su contrasena: ")
    name = input("Ingrese su nombre: ")
    curp = input("Ingrese su CURP: ")
    city = input("Ingrese su ciudad: ")
    nuevoUsuario = usuario(user,pwd, name, curp, city)
    for valor in lstUsuarios.values():
        if valor.curp == curp:
            print("El usuario ya existe")
            Menu()
    lstUsuarios[nuevoUsuario.user] = nuevoUsuario
    Menu()

def inicio():
    print('--------------------Inicio de Sesion--------------------')
    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contrasena: ")

    if usuario in lstUsuarios:
        usuario = lstUsuarios[usuario]
        if usuario.pwd == contrasena:
            if usuario.rol == 'Administrador':
                print("\n\n +--------- Hola, Administrador; Los usuarios en la lista son: ----------+ \n")
                i = 0
                for user in lstUsuarios:
                    datos = lstUsuarios[user] 
                    i = i+1
                    print("Nombre de usuario:"+ datos.user + "; Contrasena:" + datos.pwd + "; Nombre:"+ datos.name + "; CURP:"+ datos.curp + "; Ciudad: "+ datos.city +"; Rol: "+ datos.rol) 
                print(f'\n+----------Se encontraron {i} resultados. Fin de los resultados------------+ \n\n')
                Menu()
            else:
                print("+--------------------Datos del usuario-----------------+")
                print("Su usuario es: "+ usuario.user + "\nSu rol es: "+ usuario.rol +"\nSu nombre es:"+ usuario.name+ "\nSu CURP es:"+ usuario.curp)
                print("+------------------------------------------------------+")
                Menu()
        else:
            print("Datos incorrectos")
            Menu()

    else:
        print("Cuenta inexistente")
        Menu()

def Menu():
    op = int(input("\n-------------------------Menu--------------------------- \n 1.-Registro \n 2.-Inicio Sesion \n 3.-Salida \n: "))
    if op not in [1,2,3]:
        Menu()
    else:
        if op == 1: registro()
        if op == 2: inicio()
        if op == 3: exit()

administrador = usuario('admin', 'admin', 'Administrador', 'ADMIN233R4D4F43', 'Nuevo Laredo', 'Administrador')
lstUsuarios[administrador.user] = administrador
Menu()
