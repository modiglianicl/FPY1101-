while True:
    try:
        precio = float(input("Ingrese el valor del producto"))
    except ValueError:
        print("no es float, favor ingrese un numero!")
        continue
    else:
        break

while True:
    try:
        descuento = float(input("Ingrese el porcentaj del descuento (numero decimal entre 0 y 1)"))
    except ValueError:
        print("No es float, ingrese un numero")
        continue
    else:
        break

valor_final = precio - (precio*descuento)
print(f"El valor final es :" f"${int(valor_final):,}".replace(",","."))