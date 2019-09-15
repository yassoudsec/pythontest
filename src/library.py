def increment(x):
    return x + 1

def sum_val(a, b):
    return a + b
#Fonction puissance
def puissance(x,n):
 if n==0:
 return 1
 elif n==1:
 return x
 elif n%2==0:
 return puissance(x*x, n/2)
 else:
 return puissance(x*x, n/2)*x
 #fin fonction