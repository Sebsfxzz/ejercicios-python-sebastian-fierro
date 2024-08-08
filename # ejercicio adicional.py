# ejercicio adicional 
# Solicitar datos al usuario
#definir variable del nombre
nombre_estudiante = input("Ingrese el nombre del estudiante: ")
#definir variable de la nota de actividades
nota_actividades = float(input("Ingrese la calificación promedio de las actividades en clase: "))
#definir variable de la nota del proyecto
nota_proyecto_final = float(input("Ingrese la calificación del proyecto final: "))
#definir la nota de la evaluacion fh
nota_evaluaciones = float(input("Ingrese la calificación promedio de las evaluaciones parciales: "))

# Calcular la nota final
nota_final = (nota_actividades * 0.3) + (nota_proyecto_final * 0.5) + (nota_evaluaciones * 0.2)

# Mostrar el resultado
print(f"La nota final de algoritmia del estudiante {nombre_estudiante} es: {nota_final:.2f}")