# Prueba flare

## _Punto 1_
El algoritmo fue resuelto de una de las formas mas eficientes y rapidas. Se utilizo basicamente un `join` el cual dentro de su parentesis se recorre la cadena caracter por caracter filtrando solo los caracteres que no sean espacios y los digitos que no sean mayores a 5. Luego sea hace una lista de esa nueva cadena para poder mostrarlo como lo requeiren. 

Para poder correr el algoritmo debes dirigirte a la carpeta `punto-1-algoritmo` y hacer el siguiente comando:

```sh
python algoritmoFlare.py
```

## _Punto 2_
En respuesta a "_¿Puedo ejecutar el siguiente código para acceder a la lista de contratos de un 
empleado?_" la respuesta es que no, y hay varias razones y recomendaciones:
- La variable _contracts_, va a dar error porque _employee_ no tiene un atributo contracts
- Seguramente si no hay algun empleado en la base de datos va a dar error la variable employee

Entonces como el modelo _Contract_ tiene una llave foranea llamada _employee_, que referencia al id del modelo _Employee_, podemos filtrar por esa llave. Podemos obtener la lista de contratos de un empleado de la siguiente manera:

```sh
employee_id = self.kwargs['pk'] 
Contract.objects.filter(empleado=employee_id)
```

Esto filtra segun el id de Employee que le enviemos y de eso sale la lista de contratos segun el id de ese empleado

Asi tambien se veria el path en el doc donde esten las urls/endpoints
```sh
path('api/employees/<int:pk>/contracts/', EmployeeContractsViewSet.as_view(), name='employee-contracts'),
```
Esto se puede evidenciar en el api que se realizo para el punto 3, entonces si se requiere tambien se puede probar

## _Punto 3_
