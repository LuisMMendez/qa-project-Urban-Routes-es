# Urban Routes Automation Test

## Descripción: 
Este proyecto consiste en pruebas automatizadas para la aplicación web Urban Routes, utilizando Selenium WebDriver con Python. Este proyecto realiza pruebas automatizadas para verificar el funcionamiento correcto de las principales caracteristicas de la aplicación, como la búsqueda de rutas, la selección de tarifas, el ingreso de datos como el número telefónico, el proceso de pago y la interacción con el controlador.

## Requisitos:
- Python 3
- Selenium WebDriver
- Chrome WebDriver
- Pytest
- PyCharm (Opcional)

## Instalación
1. Clona este repositorio a tu directorio local.
```
git@github.com:LuisMMendez/qa-project-Urban-Routes-es.git
```
2. Asegúrate de tener Python instalado.
3. Se recomienda la instalación del entorno "PyCharm" para la ejecución de las pruebas
4. Descarga Chrome WebDriver y configura la ruta en tu sistema.
5. Instala Selenium (Verifica que la version sea compatible con tu version de Chrome)
```
pip install selenium
```
4. instala "pytest" utilizando pip en la terminal de comandos:
```
pip install pytest
```

## Contenido del proyecto:
- "data.py": Archivo de configuración con los datos de prueba
- "main.py": Archivo principal que contiene las pruebas automatización para el flujo de la aplicación.
- "urban_routes_page.py": Archivo que define la clase "UrbanRoutesPage", la cual contiene los selectores de elementos y métodos para interactuar con la aplicación.
- "helpers.py": Archivo que contiene las funciones de ayuda para interactuar con la aplicación.
## Ejecución de Pruebas
Para ejecutar las pruebas, simplemente utiliza el comando pytest en la terminal de comandos:
```
pytest
```
Asegúrate de estar en el directorio raíz del proyecto para ejecutar el comando.
Otra alternativa es utilizar el entorno "PyCharm" para correr las pruebas con Pytest.

## Pruebas Disponibles
 1. Establecer las direcciones de origen y destino.
 2. Seleccionar la tarifa "Comfort".
 3. Rellenar el número de teléfono.
 4. Agregar tarjeta de crédito.
 5. Escribir un mensaje para el controlador.
 6. Pedir manta y pañuelos.
 7. Pedir helados.
 8. Buscar un taxi.