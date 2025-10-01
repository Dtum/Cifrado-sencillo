import json
import base64
import ecdsa
import re


menu  = int(input("[1].-Registrarse\n[2].-Iniciar Sesion\nEliga una opcion: "))
if menu == 1:
    #Pedimos los datos
    usuario = input("Introduce tu usuario: ")
    contraseña = input("Introduce la contraseña: ")
    #Cargamos la curva
    curva = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    #Generamos la llave privada
    private_key = curva.to_string().hex()
    curva = curva.get_verifying_key()
    #Generamos la llave publica
    public_key = curva.to_string().hex()
    public_key = base64.b64encode(bytes.fromhex(public_key))

    #Generamos la firma
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
    firma = base64.b64encode(sk.sign(contraseña.encode()))
    usuario_firmado = base64.b64encode(sk.sign(f"{public_key}".encode()))

    #Ciframos la llave privada por contraseña
    shift = len(contraseña)
    text = f"{private_key}"
    encryption = ""
    for c in text:

        if c.isupper():
            c_unicode = ord(c)
            c_index = ord(c) - ord("A")
            new_index = (c_index + shift) % 26
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
            encryption = encryption + new_character
        else:
            encryption += c


    #Guardamos los datos en JSON
    Public_key = {"Usuario": usuario,
                "usuario Firmado": f"{usuario_firmado}",
                "Llave publica" : f"{public_key}"
                }
    headers = {"Content-Type": "application/json"}
    with open('PublicKey.json', 'w') as file:
        json.dump(Public_key, file, indent=4)


    Private_key = {"Llave Privada": f"{encryption}",
                    "firma": f"{firma}",
                   "Contrasena": f"{contraseña}"
                }
    headers = {"Content-Type": "application/json"}
    with open('PrivateKey.json', 'w') as file:
        json.dump(Private_key, file, indent=4)


elif menu == 2:

    usuario = input("Introduce el usuario: ")
    contraseña_ = input("Introduce la contraseña: ")
    archivo_publico = input("Introduce el archivo de la llave publica: ")
    try:
        with open(f'{archivo_publico}') as file:
            data = json.load(file)

    except:
        print("ERROR EN LA CARGA DE ARCHIVOS")


    #Verificamos que el usuario sea el correcto
    texto_publico = json.dumps(data)
    texto_publico = f"{texto_publico}"
    buscar_1 = '"Usuario"' + ':' +" "+f'"{usuario}"'
    a = re.search(buscar_1,texto_publico)
    if a == None:
        print("Usuario Incorrecto")
        exit()
    else:
        print("ARCHIVO VALIDADO ")

    try:
        archivo_privado = input("Introduce el archivo de la llave privada: ")
        with open(f'{archivo_privado}') as file:
            dataa = json.load(file)
    except:
        print("ERROR EN LA CARGA DE ARCHIVOS")

    texto_privado = json.dumps(dataa)
    texto_privado = f"{texto_privado}"
    buscar_2 = '"Contrasena"' + ':' + " " + f'"{contraseña_}"'
    a = re.search(buscar_2, texto_privado)

    if a == None:
        print("Contraseña Incorrecto")
        exit()
    else:
        print("ARCHIVO PRIVADO VERIFICADO")

    print("LLAVE Privada CARGADA CON EXITO")
    print("=================================")
    print("CERTIFICADO CARGADO CON EXITO")
    print("=================================")


    LETRAS = ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
    def main():

        mensaje = input("Mensaje: ")
        myKey = "addsgO"
        print("encriptar o descifrar")
        accion = input("Mode: ")

        if accion == 'encriptar':
            traducido = cifrar_mensaje(myKey, mensaje)
        elif accion == 'descifrar':
            traducido = descifrar_mensaje(myKey, mensaje)
        print(traducido)


    def cifrar_mensaje(clave, mensa):
        return traductor_mensaje(clave, mensa, 'encriptar')


    def descifrar_mensaje(clave, mensa):
        return traductor_mensaje(clave, mensa, 'descifrar')


    def traductor_mensaje(clave, mensa, accion):
        traducido = []
        indice_clave = 0
        clave = clave.upper()

        for symbol in mensa:
            num = LETRAS.find(symbol.upper())
            if num != -1:
                if accion == 'encriptar':
                    num += LETRAS.find(clave[indice_clave])
                elif accion == 'descifrar':
                    num -= LETRAS.find(clave[indice_clave])
                num %= len(LETRAS)
                if symbol.isupper():
                    traducido.append(LETRAS[num])
                elif symbol.islower():
                    traducido.append(LETRAS[num].lower())
                indice_clave += 1
                if indice_clave == len(clave):
                    indice_clave = 0

            else:
                traducido.append(symbol)
        return ('').join(traducido)


    if __name__ == '__main__':
        main()
