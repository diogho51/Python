Frutas=["Pera","Manzana", "Fresa", "Sandia", "Mora"]
print(Frutas[0])


Frutas.append("Banano")
print(Frutas[5])

print("----------")
Frutas[2]="Amarillo"
print(Frutas[2])
for fruta in Frutas:
    print(fruta)

print("----------")

DicFrutas={"Nombre":"Amarillo", "Color": "Naranja", "Tamaño": "Grande","Sabor":"Dulce"}
print(DicFrutas["Nombre"])
print(DicFrutas["Tamaño"])
print(DicFrutas.get("Tamaño"))

for clave in DicFrutas.items():
    # items() devuelve tuplas (clave, valor)
    clave, valor = clave
    print(clave, valor)

print("---------")


Dic1 = {"Fecha":"10/07/2026", "Tipo":"Electronico", "Monto":-93500}
Transacciones = [
    {"Fecha":"10/07/2026", "Tipo":"Electronico", "Monto":93500},
    {"Fecha":"10/07/2026", "Tipo":"Electronico", "Monto":130000},
    {"Fecha":"01/07/2026", "Tipo":"Electronico", "Monto":-66000},
    {"Fecha":"04/07/2026", "Tipo":"Electronico", "Monto":-1250000},
    {"Fecha":"09/07/2026", "Tipo":"Electronico", "Monto":193000},
]

print(Transacciones[2]["Monto"])
Total = 0

for T in Transacciones:
    print(T)
    Total += T["Monto"]

print("----------")
print(Total)
print("----------")

Total2 = sum(T["Monto"] for T in Transacciones)
print(f"Este es el segundo total: {Total2}")

Retiros = [T for T in Transacciones if T["Monto"] < 0]
print(Retiros)
