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

Para poder correr este proyecto se necesita activar el entorno virtual, el cual es _venv_. Luego se realiza el siguiente comando:
```sh
python manage.py runserver
```

Ahora para poder consultar las urls/endpoints desde alguna herramienta de colaboración y prueba de API como Postman o Thunder client, se deben realizar las siguientes request para el modelo de _Employee_:
```sh
GET localhost:8000/api/employees/
```
```sh
GET localhost:8000/api/employees/1/
```
```sh
POST localhost:8000/api/employees/

//ejemplo json para registrar un empleado
{
  "name":"cris",
  "last_name":"Mora"
}
```
```sh
PUT localhost:8000/api/employees/2/
```
```sh
PATCH localhost:8000/api/employees/1/
```
```sh
DELETE localhost:8000/api/employees/1/
```
Como se puede ver todas estas son las urls/endpoints disponibles para realizar sobre _Employee_

Ahora sobre permitir contratar a empleados siempre y cuanto uno este logueado se realizo de dos formas diferentes:
#### Super Usuario y Interface de administrador
 La primera tiene que ver con el superusuario y la interface de administrador. Para crear un super usuario se ejecuto el siguiente comando: 
```sh
python manage.py createsuperuser
```
Luego hay que insertar en el navegador lo siguiente para poder ver la interface de administrador:
```sh
http://localhost:8000/admin
```
Despues te tienes que loguear con tu super usuario que acabas de crear. Cuando estes dentro, ya puedes crear un contrato para algun empleado existente en el sistema, y esto hace que el empleado este contratado!.

#### Autentincacion y logueo
La segunda es a traves de crear un usuario en el sistema a travez de el siguiente endpoint/url:
```sh
POST localhost:8000/create/

//Esto es un ejemplo del json para crear un usuario
{
  "email":"ejemplo3@ejemplo.com",
  "password":"pass1234",
  "name":"ejem3"
}
```
Luego se utiliza el siguiente endpoint/url para loguearse y obtener un token:
```sh
POST localhost:8000/token/
//ejemplo de logueo a travez de json
{
  "email":"ejemplo@ejemplo.com",
  "password":"pass1234"
}
```
Esto te dara un token con el cual ya podras contratar un empleado de la siguiente manera:
```sh
POST localhost:8000/api/contract/
//ejemplo json para contratar a un empleado
{
  "end_date":"2026-10-13 15:30:00",
  "employee":2
}
```
Y antes de hacer le request debes poner un header, ubicando donde esta la seccion de headers en postman o thunder client, de la siguiente manera:
```sh
//header
Authorization

//value
Token 7f679590c924f1422eb50201106466922499de89
```
Y asi puedes contratar a un empleado!

Cabe resaltar que si no lo haces de ninguna de estas dos manera no podras contratar a empleados, ya que te dara el siguiente error si tienes un token invalido o simplemente en el header no hay token:
```sh
{
  "detail": "Authentication credentials were not provided."
}

o

{
  "detail": "Invalid token."
}
```

Adicionalmente aqui esta el endpoint/url para ver la lista de contratos de un usuario:
```sh
GET localhost:8000/api/employees/1/contracts/
```