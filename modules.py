
#todo Own modules
#todo thirdy party modules
#todo python modules

#* Módulos pre-construido desde python

import datetime
import myMath # importando módulo propio.


#from datetime import timedelta, importa la función timedelta.

print(datetime.date.today())
print(datetime.timedelta(minutes = 60))

myMath.add(2,3)#Impporte método del módulo myMath

#Todo instalar módulos de terceros.
#*Escribir en la consola, la instrucción: pip install + <nombre del modulo>

from colorama import Fore, Style #*Especifica los módulos que se utilizaran en el proyecto.

print(Fore.RED + "Hello World")
