# UOC - Tipología y Ciclo de vida de los datos - Práctica 1 (Web Scraping)

Autores: Gabriel Paladines y Jaime Pardo

Requisitos previos: instalar pip, builtwith, whois, requests, beautifulsoup4. Una vez instalado pip (https://www.liquidweb.com/kb/install-pip-windows/), el resto se pueden incluir mediante, por ejemplo, "pip install builtwith", y así sucesivamente.
Introducción: El objetivo de esta práctica es crear un dataset a partir de los datos contenidos en una página web.
1. Contexto. Explicar en qué contexto se ha recolectado la información. Explique por qué el sitio web elegido proporciona dicha información.

Actualmente existe una pandemia que está afectando a muchos países en distinto grado. Uno de los problemas generalizados es la falta o escasez de determinados bienes de consumo, en particular comidas, bebidas y productos para el cuidado de la higiene. Además, es posible que se produzca un aumento de precios debido al cambio en las demandas. 
El sitio web elegido es la página del centro comercial El Corte Inglés, que es uno de los centros de referencia en España para la adquisición de los productos que hemos nombrado.

2. Definir un título para el dataset. Elegir un título que sea descriptivo.

Evolución de los precios y la disponibilidad de alimentos y otros productos para el hogar.

3. Descripción del dataset. Desarrollar una descripción breve del conjunto de datos que se ha extraído (es necesario que esta descripción tenga sentido con el título elegido).

El dataset contiene un listado de productos (básicamente de alimentación y cuidado de la higiene), para los cuales se puede ver el precio, la categoría y si tiene o no descuento. En el punto 5 desarrollaremos esta información. 

La extracción de información se lleva a cabo cada 24h.  

4. Representación gráfica. Presentar una imagen o esquema que identifique el dataset visualmente.

 

5. Contenido. Explicar los campos que incluye el dataset, el periodo de tiempo de los datos y cómo se ha recogido.

 

El dataset incluye los siguientes campos: 
Nombre: nombre completo del producto, suele incluir el formato
Marca: marca del producto
Categorías: grupo de hasta 4 categorías, de más general a más específica
Precio original: el precio original aparece debido a que hemos decidido filtrar para mostrar únicamente productos en oferta. 
Precio final: precio de compra para el cliente
Moneda: Euro
Fecha de captura: 
 
El periodo de tiempo es de 24h (faltaría concretar de qué día a qué día se recogen los datos).

La recogida de datos se ha hecho, por simplicidad, únicamente con la primera página de la búsqueda.

6. Agradecimientos. Presentar al propietario del conjunto de datos. Es necesario incluir citas de investigación o análisis anteriores (si los hay).

Agradecemos a la compañía El Corte Inglés por facilitar la captura de datos desde su página web.

7. Inspiración. Explique por qué es interesante este conjunto de datos y qué preguntas se pretenden responder.

Este conjunto de datos es interesante porque permite obtener un listado de productos con descuento, así como hacer una comparativa de precios para ver su evolución. Es especialmente relevante en situación de pandemia.

8. Licencia. Seleccione una de estas licencias para su dataset y explique el motivo de su selección:
•	Released Under CC0: Public Domain License
•	Released Under CC BY-NC-SA 4.0 License
•	Released Under CC BY-SA 4.0 License
•	Database released under Open Database License, individual contents 
under Database Contents License
•	Other (specified above)
•	Unknown License

El trabajo realizado en esta práctica tiene una finalidad educativa, en ningún caso comercial. Es por ello que la licencia elegida ha sido CC BY-NC-SA 4.0 (“reconocimiento no comercial sin obra derivada”). Esta licencia permite compartir el dataset. Sin embargo, al contrario que la CC BY-SA 4.0, no permite un uso comercial. Por el mismo motivo se ha descartado ofrecer una licencia de dominio público.

9. Código. Adjuntar el código con el que se ha generado el dataset, preferiblemente en Python o, alternativamente, en R.

Se puede ver el código en el siguiente enlace:
https://github.com/gabrielpaladines/web-scraping

10. Dataset. Publicación del dataset en formato CSV en Zenodo con una pequeña descripción.

La publicación se ha llevado a cabo en https://zenodo.org/ y se puede encontrar en…
El formado es “.csv” separado por comas (no punto y coma).

PRUEBA: https://sandbox.zenodo.org/record/521204
DEFINITIVO no en sandbox

11. Entrega. Presentar el trabajo con el DOI del dataset en Github.
El DOI (Digital object identifier) proporcionado por Github/Zenodo es XXXXXXX

