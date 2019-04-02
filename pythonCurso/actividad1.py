'''
Actividad

Realizar un programa
Que pida el nombre de 3 personas
A cada persona se le pedira que ingrese sus calificaciones (5 calificaciones)
Sacar el promedio de calificaciones de cada persona
Desplegar un mensaje con el nombre de la persona y su promedio
'''

'''
Metodos:
len(lista) ---> obtiene el tamaño de la lista (cantidad de elemtnos)
lista.append(elemento) --> agrega elemento a lista
lista.pop() --> elimina el ultimo elemento agregado a la lista
'''
ListaAlumno = []
ListaCalificaciones = [[],[],[]]
x = 0
y = 0
while(x<3):
    ListaAlumno.append(input("Ingrese su nombre")
    while(y<5):
        ListaCalificaciones[x][y].append(int(input(f"Ingrese su calificacion numero {y+1}")))
        y++
    x++
print(ListaAlumno)
print(ListaCalificaciones)