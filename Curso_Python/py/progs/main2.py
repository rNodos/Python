import sys, os

sys.path.append(os.path.abspath("/home/dan/Documents/Python/Curso_Python/py/packages"))

#RUTA HASTA EL FINAL DEL ARBOL
import extra.good.best.sigma
from extra.good.best.tau import funT
 
print(extra.good.best.sigma.funS())
print(funT())

# USO DE ALIAS
import extra.good.best.sigma as sig
import extra.good.alpha as alp
 
print(sig.funS())
print(alp.funA())