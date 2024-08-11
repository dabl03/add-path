# Add Path
<p>
  Esta es una herramienta para poder solo agregar la variable de entorno PATH
  solo las rutas necesarias para llamar a los intérpretes o compiladores necesarios
  para que pueda programar en ellos.
</p>
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
## Problemas:
<ul>
  <li>Al llamar una segunda vez con el mismo lenguaje se corrompe el path en windows</li>
</ul>
