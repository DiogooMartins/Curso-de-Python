#from math import radians, sin, cos, tan
import math
ang = float(input("Digite um angulo: "))
sin = math.sin(math.radians(ang))
print("O angulo de {} tem o Seno {:.2f}" .format(ang, sin))
cos = math.cos(math.radians(ang))
print("O angulo de {} tem o Cosseno {:.2f}" .format(ang, cos))
tan = math.tan(math.radians(ang))
print("O angulo de {} tem a Tangente {:.2f}" .format(ang, tan))
