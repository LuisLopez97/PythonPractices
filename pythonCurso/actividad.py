ListaAlumno = []
ListaCalificaciones = []
x = 0
while(x < 3):
   y = 0
   promedio = 0
   ListaAlumno.append(input("Alumno, ingrese su nombre: "))
   while(y < 5):
      promedio+=float(input(f"Ingrese su calificacion {y+1} :"))
      y+=1
   ListaCalificaciones.append(promedio/5)
   print(ListaAlumno[x])
   print(ListaCalificaciones[x])
   x+=1