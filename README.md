Este script tiene funciones como: 

la generación de Pares de Claves: Utiliza el algoritmo ECDSA (curva SECP256k1) para crear un par de claves privada y pública por cada nuevo registro.

firma Digital: se utiliza la llave privada para generar firmas sobre datos sensibles (como la contraseña y la llave pública).

Gestión de Cuentas: Almacena la información de la cuenta (usuario, llaves y firmas) en archivos JSON separados (PublicKey.json y PrivateKey.json).

Utilidad de Cifrado: Incluye una función de cifrado/descifrado simple (Cifrado Vigenère) para manipular mensajes una vez que el usuario ha iniciado sesión.
