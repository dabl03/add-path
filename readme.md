# Add Path
<p>
  Esta es una herramienta para poder solo agregar la variable de entorno PATH
  solo las rutas necesarias para llamar a los intérpretes o compiladores necesarios
  para que pueda programar en ellos.
</p>

## Requisitos

Debes tener instalado python 3 o superior.

## Meta

<p>
  Cuando desarrollas en muchos lenguajes, terminas agregándolos al la ruta de búsqueda y mientras más usa, más se satura y pareciera que se pone más lenta la consola. Aquí está un ejemplo de lo que se quiere evitar:
</p>
<pre><code>
  --Rutas del sistema--
  C:\ruta\PowerShell\
  C:\ruta\python\Scripts\
  C:\ruta\Python\
  C:\ruta\mingw\bin
  C:\ruta\dotnet
  C:\ruta\NASM\bin
  C:\ruta\perl\bin
  C:\ruta\haxe
  C:\ruta\haxe\neko
  C:\ruta\Git\cmd
  C:\ruta\curl\bin
  C:\ruta\java\bin
  C:\ruta\CMake\bin
  C:\ruta\rust\bin
</code></pre>
<p>
  Nota: Por privacidad cambio la ruta absoluta por "ruta". También mencionaré que en linux debería ser lo mismo sin "c:\" y con "/" en lugar de "\". 
</p>
<p>Para solo tener lo que necesito en la sesion de la consola, he desarrollado esta herramienta.</p>

## ¿Como usarlo?

<p>
  Debes llamar solo al script .bat o .bash (dependiendo de tu sistema operativo), y pasar el lenguaje para agregar en el path y listo. Claro, debes tener el lenguaje con sus path asociado en el archivo "compilerAdd.csv". 
</p>
Agregar un lenguaje:
<pre><code>
  echo addPath LANG LANG LANG ...
  addPath c
</code></pre>
Almacenar un lenguaje y sus paths:
<pre><code>
  echo addPath --new-lang LANG path1 PATH2 ...
  addPath --new-lang c C:/ruta/mingw/bin C:/ruta/mingw/include ...
</code></pre>
Obtener una ayuda mas completa:
<pre><code>
  addPath --h
</code></pre>

## ¿Cómo funciona?

El archivo addPath.py trata la entrada del usuario, mientras que el script altera la variable del entorno. El archivo addPath.py genera un archivo script temporal que tendrá todas las url a agregar. Si no se creo el archivo, es porque no hay nada que agregar en el path.

## Sistema operativos soportados:

- Windows
- Linux

> Nota: Si quieres para otro OS, deberás crear un nuevo script (que se pueda interpretar en tu OS). El script debe llamar al archivo python con el parametro "--OUT "you_file_temp_script.script_extension"", el archivo python generará un script con el mismo nombre que el parametro --OUT, debes comprobar si se generó, depues de llamar a ese script, el archivo temporal se elimina (ya no es necesario que se quede).
> 
> También debes modificar la función out y la variable global "SEPARATOR" del archivo python, para adaptar al nuevo sistema operativo.
