import random as rd

NOMBREARCHIVO = "Palabras.txt"


def CargarPalabras():
  try:
    with open(NOMBREARCHIVO, "r", encoding="utf-8") as ArchivoPalabras:
      return [linea.strip() for linea in ArchivoPalabras if linea.strip()]
  except FileNotFoundError:
    return []


def SeleccionarPalabra():
  ListaPalabras = CargarPalabras()
  if ListaPalabras:
    return rd.choice(ListaPalabras)
  return None


x = SeleccionarPalabra()
print(x)


def AdicionarArchivo(Palabra):
  """Agrega una palabra al archivo (si no está vacía)."""
  if not Palabra:
    return False
  with open(NOMBREARCHIVO, "a", encoding="utf-8") as f:
    f.write(str(Palabra).strip() + "\n")
  return True