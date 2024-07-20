# Intercines

## Activacion y desactivacion de entorno virtual:
* Para activar el entorno virtual, ejecuta el siguiente comando desde la terminal:

```bash
.\env\Scripts\activate
```

* Para desactivar el entorno virtual, ejecuta el siguiente comando desde la terminal:

```bash
deactivate
```
## Dependencias de Python:
1. [Customtkinter](https://github.com/TomSchimansky/CustomTkinter)
2. [CTkSpinbox](https://github.com/Sheikh-Rashdan/CTkSpinbox)
3. [Jinja2](https://github.com/pallets/jinja/)
4. [Mysql-connector-python](https://pypi.org/project/mysql-connector-python/)
5. [Plllow](https://github.com/python-pillow/Pillow)
6. [PyAutoGUI](https://github.com/asweigart/pyautogui?tab=readme-ov-file)
7. [Requests](https://github.com/psf/requests)
8. [Tkcalendar](https://github.com/j4321/tkcalendar)

## Instalar las dependencias:

* Para instalar las dependencias del proyecto, ejecuta el siguiente comando desde la terminal:

```bash
pip3 install -r requirements.txt
```


## Uso del backup de la base de datos: 

* Para restaurar la base de datos desde un backup, utiliza el archivo `backup.sql` que se encuentra en la carpeta `backend/database` y importalo a tu base de datos mysql.

## Configuración de la conexión a la base de datos MySQL:

* La configuración de la conexión a la base de datos MySQL se encuentra en el archivo `crear_conexion.py`, ubicado en la carpeta `backend/database`. Para ajustar los parámetros de conexión, sigue el formato mostrado a continuación en `crear_conexion.py`:

``` bash
conexion = mysql.connector.connect(
    host=os.getenv('MYSQL_HOST', 'nuevo_host_mysql(ip local)'),
    user=os.getenv('MYSQL_USER', 'nuevo_usuario_mysql'),
    password=os.getenv('MYSQL_PASSWORD', 'nueva_contraseña_mysql'),
    database=os.getenv('MYSQL_DB', 'nuevo_nombre_base_de_datos'),
    port=os.getenv('MYSQL_PORT', 'nuevo_puerto_mysql')
)
```
* Asegúrate de reemplazar `nuevo_host_mysql`, `nuevo_usuario_mysql`, `nueva_contraseña_mysql`, `nuevo_nombre_base_de_datos`, y `nuevo_puerto_mysql` con los valores correspondientes de tu configuración.


## Ejecutar el programa:

Para ejecutar el programa, asegurate de que el servicio de mysql esta corriendo y utiliza el siguiente comando desde la terminal:

```bash
python3 main.py
```
