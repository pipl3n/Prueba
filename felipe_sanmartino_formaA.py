datos = {
    "usuarios": [
            
            
            
    ]
}


def verificar_numero_entero_positivo(mensaje_input:str):
    while True:
        try:
            numero = int(input(mensaje_input))
            if numero <= 0:
                print("Solo se permiten numeros positivos.")
                continue
            return numero
        except ValueError:
            print("Solo puede ingresar numeros enteros.")
            continue


def verificar_nombre():
    nombre=input("ingrese su nombre ")
    for i in datos["usuarios"]:
        if i["nombre"]==nombre:
            print("El nombre ya esta en uso")
        else:
            return nombre
    

def verificar_Sexo(mensaje_input):
    while True: 
        sexo=input(mensaje_input).upper()
        if len(sexo)==1:
            if sexo=="F":
                return sexo
            elif sexo=="M":
                return sexo
            else:
                print("solo ingrese F o M")
        else:
            print("solo ingrese F o M")

def valida_numeros_contraseña(contraseña:str):
   
    numero = "1234567890"
    for i in contraseña:
        for j in numero:
            if i == j:
                return True
    return False


def valida_letra_contraseña(contraseña:str):
    letra = "abcdefghijklmnñopqrstvwxyz"
    for i in contraseña:
        for j in letra:
            if i == j:
                return True
    return False



def eliminar_nombre(nombre:str):
    for i in datos["usuarios"]:
        if i["nombre"] == nombre:
            print("p")
        else:
            print("usario no encointrado")
        
def monstrar_nombre():
    nombre=input("ingrese su nombre ")
    for i in datos["usuarios"]:
        if i["nombre"]==nombre:
            print(f"{datos["nombre"]}- {datos["genero"]}")
        else:
            print("Usuario no encontrado")
            continue
   

def valida_texto(mensaje_input:str):
    while True:
        texto = input(mensaje_input)
        if len(texto) == 0:
            print("El texto, no puede estar vacio.")
            continue
        else:
            return texto
            
def agregar_usuario( nombre:str, genero:int, contraseña:str):
    usuario_agregar = {
                "nombre":nombre,
                "genero":genero,
                "contrseña":contraseña
            }
    datos["usuarios"].append(usuario_agregar)






while True:
    print("****REGISTRO****")
    print("[1] - Ingresar usuario")
    print("[2] - buscar usuario")
    print("[3] - eliminar usuario")
    print("[4] - salir")

    opcion=verificar_numero_entero_positivo("ingrese una opcion ")

    if opcion== 1:
        nombre=verificar_nombre()
        

        genero =verificar_Sexo("ingrese su genero ")

        while True:
            contraseña =valida_texto("ingrese su contraseña ")
            if valida_letra_contraseña(contraseña) == False:
                print("El id debe contener al menos una letra.")
                continue
            elif valida_letra_contraseña(contraseña) == False:
                    print("El id debe contener al menos un numero.")
                    continue
            else:
                break
        agregar_usuario(nombre, genero, contraseña)
        print("Usuario agregado correctamente")

    elif opcion==2:
       monstrar_nombre()
       
    
          
           
        
    elif opcion==3:
        nombre = input("Ingrese el nombre del usuario: ")
        eliminar_nombre(nombre)
           
           
    elif opcion==4:
        print("saliendo")
        break




