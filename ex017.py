from math import hypot
catop = float(input("Qual o comprimento do cateto oposto? "))
catad = float(input("Qual o comprimento do cateto adjacnte? "))
#hi = (cat1*cat1 + cat2*cat2)
print(" A hipotenusa vai medir {:.2f}".format(hypot(catop, catad)))
