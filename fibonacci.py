from datetime import datetime

#Méthode run récursive
#Pour les grands nombres cette méthodes déclenche une erreur de dépassement du nombre maximal de niveaux de récursivité
#Pour n = 30, le temps d'exécution dépasse 1s. Cette méthode n'est pas performante. 
class Fibo1:
  def __init__(self, n):
    self.n = n
  
  def run(self):
    if (self.n == 1) or (self.n == 2):
      return 1
    return Fibo1(self.n-1).run() + Fibo1(self.n-2).run()

#Méthode run itérative
#Pour 10 exécutions avec n = 10000, la moyenne du temps d'exécution est 2553 microsecondes
class Fibo2:
  def __init__(self, n):
    self.n = n
  
  def run(self):
    a = 1
    b = 1
    for i in range(self.n-1):
      a,b = b, b+a
    return a

#Utilisation d'un générateur/d'une fonction génératrice
#Pour 10 exécutions avec n = 10000, la moyenne du temps d'exécution est 4.303 microsecondes
class Fibo3:
  def __init__(self, n):
    self.n = n
  
  def run(self):
    a,b = 0,1

    def GenFib(a,b):
      while True:
        a,b = b, a+b
        yield a
    
    fib = GenFib(a,b)
    for i in range(self.n - 1):
      next(fib)
    return next(fib)

#D'après les résultats des benchmarks, la méthode itérative est la plus performante parmis les 3 méthodes