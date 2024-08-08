# actividad 5 Definimos las variables
#variable valor de compra
valor_compra = int(input("escriba el valor de compra"))
#variable valor de descunto
descuento = int(input("escriba el valor del descuento"))

# Calculamos el valor final a pagar
valor_final = valor_compra - descuento

# Imprimimos el resultado
print(f"La compra fue {valor_compra} unidades monetarias, con un descuento de {descuento} unidades monetarias "
      f"y el valor final a pagar es {valor_final} unidades monetarias.")