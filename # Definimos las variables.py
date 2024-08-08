# actividad 4 efinimos las variables
# variable del nombre
nombre_vendedor = input("escriba el nombre del vendedor: ")
#variable del sueldo
sueldo_base = int(input("escriba el valor del sueldo: "))
#variable de la comision
comision_ventas = int(input("escriba el valoe de la comicion de ventas: "))

# Calculamos el sueldo total
sueldo_total = sueldo_base + comision_ventas

# Imprimimos el resultado
print(f"El vendedor {nombre_vendedor}, tiene un sueldo de {sueldo_base} unidades monetarias, "
      f"durante el mes obtuvo una comisión de {comision_ventas} unidades monetarias "
      f"y el valor final a pagar es: {sueldo_total} unidades monetarias.")