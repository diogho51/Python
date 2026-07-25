Archivo = "Palabras.txt"

import random

def Adicionar():
    NuevasPalabras = ["Draw", "Sleep", "Sing", "Write", "Work"]
    with open(Archivo, "a") as File:
        File.writelines(p + "\n" for p in NuevasPalabras)



def ObtenerLetra():
    while True:
        Letra = input("Digite una letra: ").upper().strip()
        if len(Letra) != 1:
            print("Por favor, introduzca solo un caracter.")
        elif not Letra.isalpha():
            print("Debe ser un caracter alfabetico.")
        else:
            return Letra
        


def jugar():
    # Selecionar Palabra al azar 
    
    PalabraScreta = SeleccionarPalabra()
    print(PalabraScreta)
    MaximoIntentos = 9
    LetrasAdivinadas = set()
    IntentosFallidos = 0
    while IntentosFallidos < MaximoIntentos:
        print(Mostrapalabra(PalabraScreta, LetrasAdivinadas))
        letra = ObtenerLetra()
        if letra in LetrasAdivinadas:
            print("Ya ha intentado esa letra.")
            continue
        if letra in PalabraScreta:
            LetrasAdivinadas.add(letra)
            if all(l in LetrasAdivinadas for l in PalabraScreta):
                print(Mostrapalabra(PalabraScreta, LetrasAdivinadas))
                print("¡Ganaste!")
                return
        else:
            IntentosFallidos += 1
            print(f"Intentos fallidos: {IntentosFallidos}/{MaximoIntentos}")
    print(f"Perdiste. La palabra era: {PalabraScreta}")



def Mostrapalabra(PalabraSecreta, LetrasAdivinadas):
    Resultado = []
    for Letra in PalabraSecreta:
        if Letra in LetrasAdivinadas:
            Resultado.append(Letra)
        else:
            Resultado.append("_")
    return " ".join(Resultado)


# ["_", "A","_","A"]
# "_A_ A _"
def SeleccionarPalabra():
    try:
        with open(Archivo, "r") as f:
            palabras = [w.strip().upper() for w in f if w.strip()]
    except FileNotFoundError:
        palabras = ["DRAW","SLEEP","SING","WRITE","WORK"]
    return random.choice(palabras)

if __name__ == "__main__":
    Adicionar()
    jugar()
    