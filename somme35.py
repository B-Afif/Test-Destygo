class Somme35:
  def __init__(self, n):
    self.n = n
  
  def run(self):
    somme = 0
    for i in range(0,self.n+1):
    	if (i%3 == 0) or (i%5 == 0):
    		somme += i
    return somme