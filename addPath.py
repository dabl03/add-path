from typing import TextIO
import os;

DIR_BASE=os.path.dirname(__file__);
REGISTER=f"{DIR_BASE}/query/compilerAdd.csv";
HEADER="NOMBRE-DEL-LENAGUAJE,RUTA1,RUTA2-OPCIONAL,RUTA3-OPCIONAL,..., Nota: \"Esta linea del archivo se ignora\", Siempre debe haber una linea de mas en el archivo.\n";
SEPARATOR=';' if os.name=="nt" else (
  ':' if os.name=="posix" else None
);
out_file=f"{DIR_BASE}/query/out.tmp";
P_HELP=('h','?',"help");
P_SILENT=('s', "silent");
P_OUT=("out","o");
P_SET=('n',"new","new-lang");
P_GET=('g',"get","get-lang");

def getPath(langs:list, file:TextIO=None)->list:
  """Obtenemos los paths ligado al los lenguajes pasados.

  Args:
      langs (list(str)): Lenguajes a buscar.
      file (TextIO): Archivo al leer. Default None. Nota: Cambia la ubicación del puntero por cada llamada a la funcion.

  Returns:
      list: Los paths ligado al los lenguajes.
  """;
  path=[];
  File=open(REGISTER,'r') if file==None else file;
  lines=File.read().split('\n');
  if file==None: File.close();# Si se paso el archivo no debemos cerrarlo.
  for lang in langs:
    lang=lang.lower();
    for line in lines:
      line=line.split(',');
      if line and line[0]==lang:
        path+=line[1:];
        break;
  return path;
def setPath(lang:str, silent_mode:bool=True, *paths:str)->bool:
  """Modifica el registro del lenguaje y los paths

  Args:
      lang (str): Lenguaje a agregar.
      silent_mode (bool): Si es True no pide confirmación para reemplazar el lenguaje.
      *paths (str): Paths ligado al lenguaje.

  Returns:
      bool: ¿Se guardó el cambio?
  """;
  lang=lang.lower();
  insert=False;
  with open(REGISTER,"r") as f: f_lines=f.readlines();
  for i in range(len(f_lines)):
    lang_path=f_lines[i].split(',');
    if lang_path[0]==lang:
      insert=i;
      break;
  if not silent_mode and not insert==False:
    # Pedimos confirmación.
    if not confirm("¿Deseas reemplazar los paths puesto a este lenguaje?"):
      print("No se ha reemplazado...");
      return False;
  if insert==False:
    # No existe: Agregamos.
    f_lines.append(f"{lang},{','.join(paths)}\n");
  else:
    # Existe: reemplazamos.
    f_lines[insert]=f"{lang},{','.join(paths)}\n";
  with open(REGISTER,'w') as f: f.writelines(f_lines);
  return True;

def out(paths:list):
  """Escribe en el archivo out_file los paths pasado separado por la variable SEPARATOR

  Args:
      paths (list(str)): Los paths a guardar en el archivo.
  """
  arr_out=[];
  environ_path=os.environ['PATH'].split(';');
  for path in paths:
    path=os.path.normcase(os.path.abspath(path));
    if path not in arr_out and path not in environ_path:
      arr_out.append(path);
  if not arr_out:
    return;
  print(out_file);
  with open(out_file,'w') as f:
    if os.name=="nt":
      f.write("set PATH=%PATH%;"+SEPARATOR.join(arr_out));
    elif os.name=="posix":
      f.write(("export PATH=\"$PATH:"+SEPARATOR.join(arr_out))+'"');
    else: raise OSError(f"Systema operativo basado en \"{os.name}\" no soportado.");

def viewLang(langs:tuple,s_mode:bool=False):
  """Muestra por consola una lista de los lenguajes con sus paths asociados.

  Args:
      langs (tuple(str)): Lenguajes a buscar.
      s_mode (bool): Para evitar confirmación en cada lenguaje. Default False.
  """;
  print("Lenguajes disponibles:");
  if '*' in langs:
    # Mostramos todos los lenguajes.
    F=open(REGISTER,'r');
    lines:list=F.readlines()[1:];
    F.close();
    for line in lines:
      p_lang=line.split(',');
      if p_lang:
        print(f"{p_lang[0]}:");
        for path in p_lang[1:]:
          print(f"|  - {path}");
      if not s_mode: input("[Enter para continuar]> ");
    return;
  with open(REGISTER,'r') as F:
    # Mostramos solo el asociado al los lenguajes.
    for lang in langs:
      print(f"{lang}:");
      paths=getPath(lang,F);
      for path in paths:
        print(f"|  - {path}");
      if not s_mode: input("[Enter para continuar]> ");
def confirm(msg:str=None)->bool:
  """Pide por consola una confirmación.

    msg (str): Mensaje a mostrar. Default None no hay que mostrar.
  Returns:
      bool: ¿Acepta el usuario?
  """;
  io="";
  if msg!=None:
    print(msg);
  while io=="" or io not in "ynYN": io=input("Para confirmar presione \"y\" y para negar \"n\"\n> ");
  return io in "yY";
def test():
  return None;
def help():
  print(f"""Bienvenido, esta es una herramienta para agregar los paths necesario 
para desarrollar en un lenguaje específico, en la ruta de entorno de la consola actual.

Parametros disponibles:
  {', '.join(P_HELP)} -- Mostramos esta ayuda.
  {', '.join(P_SILENT)} -- Evita pedir confirmación
                           al llamar la app
  {', '.join(P_OUT)} -- Donde guardamos los paths de salida.
  {', '.join(P_SET)} -- Creamos un nuevo lenguaje.
  {', '.join(P_GET)} -- Obtenemos una lista de los lenguajes guardados.
                        con sus paths.
Forma de usar este script:
  addPath.py LANG1 LANG2 LANG3
    Agregamos en la variable de entorno, si existe en el archivo "{REGISTER}"
    los paths asociados. Nota: Puedes agregar cualquier cantidad de lenguajes
  addPath.py --{P_OUT[0]} out.tmp C++ Python Java
  addPath.py C++ --{P_SILENT[0]} --{P_SET[0]} LANG Path1 path2 path3
    Aqui agregamos el path asociado al lenguaje C++ y guardamos un nuevo
    lenguaje con su path en el archivo "{REGISTER}" y --{P_SILENT[0]} para
    No pedir confirmación.
  addPath.py --{P_GET[0]} LANG1 LANG2 LANG3
    Solo muestra una lista de los lenguajes y sus paths si existe en el archivo
    "{REGISTER}", si no no se muestra.
  addPath.py --{P_GET[0]} * --{P_SILENT[0]}
    Muestra una lista completa de los lenguajes disponibles con sus paths asociados,
    sin esperar a que ingrese enter por cada lenguaje.
  """);
def interpret(param:dict)->dict:
  """Interpreta los pasados para retornar un diccionario de lo que se quiere hacer.

  Args:
      param (dict{--flag:value}): Parametro a interpretar.

  Returns:
      dict: Configuración de que quiere el usuario.
  """
  langs=[];# Lenguajes a sacar.
  newlang={};# Leguaje a agregar.
  getlang=[];# Mostramos los paths asociados a los lenguajes.
  silent_mode=False;
  ishelp=False;
  for p in param:
    if p[0:2]=="--":
      key=p.lower()[2:];
      if key in P_HELP:
        # Imprimimos la ayuda.
        ishelp=True;
      elif key in P_SILENT:
        # Imprimimos sin confirmación
        silent_mode=True;
      elif key in P_OUT:
        # Agregamos un archivo de salida.
        if param[p]:
          global out_file;
          out_file=param[p][0];
        langs+=param[p][1:];
        continue;
      elif key in P_SET:
        # Agregamos o insertamos un lenguaje.
        if param[p]: newlang[param[p][0]]=param[p][1:];
        continue;
      elif key in P_GET:
        # Mostramos los lenguajes.
        getlang+=param[p];
        continue;
      else:
        return {
          "err":True,
          "err-msg":f"Error: {p} no existe como parametros.\nPasar --h o --help para obtener ayuda."
        };
      langs+=param[p];
    else:
      langs.append(p);
      langs+=param[p];
  return {
    "langs":langs,
    "n-lang":newlang,
    "g-lang":getlang,
    "s-mode":silent_mode,
    "help":ishelp,
    "err":False
  };
if __name__=="__main__":
  import sys;
  if not os.path.exists(REGISTER):
    with open(REGISTER,'w') as f: f.write(HEADER);
  if len(sys.argv)>1:
    argv=sys.argv[2:];
    param={sys.argv[1]:[]};
    type_param=sys.argv[1];
    for arg in argv:
      if arg[0:2]=="--":
        type_param=arg;
        param[type_param]=[];
        continue;
      param[type_param].append(arg);
    all_data=interpret(param);
    if all_data["err"]:
      print(all_data["err-msg"]);
      exit(-1);
    if all_data["langs"]: out(getPath(all_data["langs"]));
    if all_data["n-lang"]:
      for name in all_data["n-lang"]:
        setPath(name,all_data["s-mode"],*all_data["n-lang"][name]);
    if all_data["g-lang"]: viewLang(all_data["g-lang"],all_data["s-mode"]);
    if all_data["help"]>0 and not all_data["s-mode"]: help();
  else: exit(-1);
