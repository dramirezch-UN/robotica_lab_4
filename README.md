# Laboratorio 4
## Introduccion
### Cinematica directa
#### Mediciones
Inicialmente, se deben realizar las respectivas caracterizaciones del pincher. Para ello se realizo la cinematica directa por medio de la herramienta de Peter Corke en Matlab.
Lo primero que se realizo fue la medicion del pincher para poder caracterizarlo y proceder a su analisis DV.
![dimensiones](https://hackmd.io/_uploads/S1uxNRCV2.jpg)
Para el diagrama anterior, obtuvimos las siguientes dimensiones:
l1=40.6 mm
l2=l3=107 mm
l4=69.5 mm
No se tuvo en cuenta la altura de la base para la realizacion de la cinematica directa.

#### Cinematica Directa DHstd
Primero se realizo la graficacion de los marcos de referencia para poder realizar la tabla.
![MarcosReferencia](https://hackmd.io/_uploads/ByUM4AA4h.jpg)

Con los marcos de referencia se procedio a realizar la tabla DHstd

#### ToolBox
Una vez con la table realizada, se procedió a simular las posiciones del manipulador por medio del toolbox de Peter Corke, por medio del comando del SerialLink.



| Theta    | d (mm) | a (mm) | alpha (deg) | offset (deg) |
| -------- | -------- | -------- | -------- | -------- |
| q1     | 40.6     | 0     | 90° | 0 |
| q2     | 0     | 107     | 0 | 90° |
| q3     | 0     | 107     | 0 | 0 |
| q4     | 0     | 0     | 90° | 90° |
| q5     | 69.5     | 0     | 0 | 0 |


Las posiciones por simular fueron las siguientes


| Posicion | Art 1 | Art 2 | Art 3 | Art 4 | Art 5 |
| -------- | -------- | -------- | -------- | -------- | -------- |
| 0   | 0° | 0° | 0° | 0° | 0° |
| 1   | -25° | 15° | -20° | 20° | 0° |
| 2   | 35° | 15° | -20° | 20° | 0° |
| 3   | -85° | 15° | -20° | 20° | 0° |
| 4   | -80° | 15° | -20° | 20° | 0° |

Con las posiciones definidas, se procedio a realizar la validacion de las posiciones acorde a la tabla DHstd por medio del toolbox, obteniendo los siguientes resultados:


##### Posición Home
![PosHome](https://hackmd.io/_uploads/rkO9-RCEh.jpg)

![PosHomeReal](https://hackmd.io/_uploads/r1d6VCR43.jpg)

##### Posición 1
![Pos1](https://hackmd.io/_uploads/rJt9ZRC43.jpg)

![Pos1Real](https://hackmd.io/_uploads/rJ0RVC043.jpg)


##### Posición 2
![Pos2](https://hackmd.io/_uploads/HkK9bARV3.jpg)

![Pos2Real](https://hackmd.io/_uploads/HygeHCREn.jpg)


##### Posición 3
![Pos3](https://hackmd.io/_uploads/Sktcb0RN3.jpg)

![Pos3Real](https://hackmd.io/_uploads/H1XZS004n.jpg)

##### Posición 4
![Pos4](https://hackmd.io/_uploads/SJeYq-ACVn.jpg)

![Pos4Real](https://hackmd.io/_uploads/HklVBR0E3.jpg)


Con las posiciones definidas y validadas, el paso a seguir fue la integracion con ROS y el robot Pincher para poder ubicarlo en las posiciones requeridas.

## Programa en Python
### Multi Motor
Modificamos [dynamixel_one_motor](https://github.com/fegonzalez7/dynamixel_one_motor) para que pudiera controlar los 5 servos. Para esto solo fue necesario editar el archivo de configuración del proyecto. El código modificado se puede encontrar en la carpeta `codigo/dynamixel_multi_motor`.
### Scripts
En la carpeta `codigo/lab_4/scripts` se pueden encontrar los scripts escritos para este laboratorio:
- `go_home.py` Mueve todos los motores a su posición de home. Realiza el movimiento de manera secuencial.
- `move_all.py` Mueve todos los motores a una posición dada. Todos los servos realizan su movimiento al mismo tiempo.
- `move_servo.py` Lo mismo que `go_home.py` pero la posición definida no es home.
- `read_angs.py` Es el código del subscriber con su callback. Imprime la posición (ángulos) de todos los servos en consola.
### HMI
El código de la HMI se puede encontrar en `codigo/lab_4/scripts/gui`.

El desarrollo de la interfaz de usuario (HMI) se hizo por medio de la librería Tkinter de Python. Se hizo un diseño sencillo. Con título y subtítulos con la información relevante del laboratorio. Se dispusieron 5 botones con las 5 posiciones requeridas en el Laboratorio 4. Se habilitó un espacio para mostrar como texto plano los resultados de los valores articulares. Y además se dispuso un espacio para presentar el logo de la Universidad Nacional y que al seleccionar cualquiera de los botones con posiciones mostrara una imagen de referencia de la posición a la que se desea llegar.

![HMI1](https://hackmd.io/_uploads/B1-dl13Vn.png)

El código comienza importando las bibliotecas necesarias, incluyendo sys, tkinter y PIL. tkinter es una biblioteca gráfica de Python, mientras que PIL es una biblioteca para manipular imágenes en Python.

Luego, se crea la ventana principal de la aplicación utilizando tkinter.Tk(). El título y el tamaño de la ventana se establecen utilizando root.title() y root.geometry(), respectivamente.

A continuación, se crean tres etiquetas tkinter.Label, que se utilizan para mostrar texto en la ventana. La primera etiqueta muestra el título principal de la ventana, la segunda etiqueta muestra los nombres de los autores del código y la tercera etiqueta muestra un título para una sección de botones. Los parámetros font y place se utilizan para establecer el tamaño de fuente y la posición de la etiqueta en la ventana, respectivamente.

Se crea un marco tkinter.Frame para contener los botones que se crean más adelante en el código. Los botones se crean utilizando tkinter.Button y se agregan al marco utilizando pack(). Cada botón tiene un texto y un comando asociado que se ejecuta cuando se hace clic en el botón.

Se crea un widget tkinter.Text para mostrar la salida del código. Este widget se coloca en la ventana utilizando pack(). A continuación, se crea una etiqueta de imagen tkinter.Label y se agrega a la ventana utilizando pack(). La etiqueta de imagen se utiliza para mostrar imágenes que se cargan más adelante en el código.

Finalmente, se inicia el bucle principal de la aplicación utilizando root.mainloop(). Esto hace que la ventana se muestre en la pantalla y espere a que el usuario interactúe con ella. Cuando se hace clic en uno de los botones, se ejecuta la función correspondiente que actualiza la salida del texto y carga una imagen en la etiqueta de imagen.

![HMI2](https://hackmd.io/_uploads/rkd5eJhE2.png)

La logica para controlar el motor a partir de la HMI es una mezcla de los scripts listados en la sección anterior.