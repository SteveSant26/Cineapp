* Activacion o desactivacion de entorno virtual:

Para activar el entorno virtual, ejecuta el siguiente comando desde la terminal:

```bash
source . env/Scripts/activate
```

Para desactivar el entorno virtual, ejecuta el siguiente comando desde la terminal:

```bash
deactivate
```

* Instalar las dependencias:

Para instalar las dependencias del proyecto, ejecuta el siguiente comando desde la terminal:

```bash
pip3 install -r requirements.txt
```


* Ejecutar el programa:

Para ejecutar el programa, utiliza el siguiente comando desde la terminal:

```bash
python3 main.py
```
* Configuración de la conexión a la base de datos MySQL:

La configuración de la conexión a la base de datos MySQL se encuentra en el archivo crear_conexion.py, ubicado en la carpeta backend/database. Para ajustar los parámetros de conexión, sigue el formato mostrado a continuación en crear_conexion.py:

``` bash
conexion = mysql.connector.connect(
    host=os.getenv('MYSQL_HOST', 'nuevo_host_mysql(ip local)'),
    user=os.getenv('MYSQL_USER', 'nuevo_usuario_mysql'),
    password=os.getenv('MYSQL_PASSWORD', 'nueva_contraseña_mysql'),
    database=os.getenv('MYSQL_DB', 'nuevo_nombre_base_de_datos'),
    port=os.getenv('MYSQL_PORT', 'nuevo_puerto_mysql')
)
```
Asegúrate de reemplazar nuevo_host_mysql, nuevo_usuario_mysql, nueva_contraseña_mysql, nuevo_nombre_base_de_datos, y nuevo_puerto_mysql con los valores correspondientes de tu configuración.




* Uso del backup de la base de datos: 

Para restaurar la base de datos desde un backup, utiliza el archivo backup.sql que se encuentra en la carpeta backend/database.


