import random

OSError
def obtener_palabra_secreta() -> str:
    palabras = ['charlie', 'ozzy', 'jajai', 'hanatarash']
    return random.choice(palabras) 

def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ''
    
    
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra + " "
        else:
            adivinado += "_"
         
    return adivinado.strip()
  

def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 20
    juego_terminado = False
    
    
    print("Bienvenido compadre, ahoracate")
    print(f"Tienes {intentos} intentos para amarrar la cabuya")
    print(mostrar_progreso(palabra_secreta, letras_adivinadas), "La cantidad de letras en la palabra es:", len(palabra_secreta))

    
    while not juego_terminado and intentos > 0:
        adivinanza = input("amarra la cabuyita (letra): ").lower()
        
        if len(adivinanza) != 1 or not adivinanza.isalpha():
          print("Porfa tratame serio el juego, 1 letra dije, aver: ")   
        elif adivinanza in letras_adivinadas:
            print("Ya dijiste esa letra crack")
            
        else: 
            letras_adivinadas.append(adivinanza)
                
                
            if adivinanza in palabra_secreta:
                    print(f"Very gud has acertado la letra '{adivinanza}' alejaste la muerte unos centimetros!")
            else:
                     intentos -= 1
                     print(f"la letra {adivinanza} no esta en la palabra compa")
                     print (f"Te quedan {intentos} amarres de cabuyita")
                    
                                
        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)     
        print(progreso_actual)
       
        if "_" not in progreso_actual:
              juego_terminado = True
              palabra_secreta = palabra_secreta.capitalize()
              print(f"Very gutten viviras un poco más la palabra secreta es '{palabra_secreta}'")
              
    if intentos == 0:
        palabra_secreta = palabra_secreta.capitalize()
        print(f"Murido, la salvacion estaba en '{palabra_secreta}'")     
       
       
juego_ahorcado()           