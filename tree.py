class Node:
  def __init__(self, val):
    self.left = None # is a Node
    self.right = None # is a Node
    self.value = val

# ABR : 
# left.val <= val <= righ.val
class Tree:
  def __init__(self, node):
    self.root = node
  
  def add(self, val, root = None):
  	#si la methode est appelée pour la première fois on utilise le sommet de l'arbre comme noeud de début
  	if (root == None):
  		root = self.root
  	if root.value > val:
  		if root.left is None:
  			#si la valeur à insérer est inférieure à celle du noeud et que le noeud n'a pas de fils gauche on insere la valeur dans le fils gauche
  			root.left = Node(val)
  		else:
  			#sinon on execute la méthode de nouveau en utilisant le fils gauche comme neoud de départ 
  			self.add(val, root.left)
  	else:
  		#le même principe appliqué au fils droite
  		if root.right is None:
  			root.right = Node(val)
  		else:
  			self.add(val, root.right)

class RechercheABR():
	def __init__(self, arbre, val):
		self.arbre = arbre
		self.val = val

	def run(self, root = None):
		#si la methode est appelée pour la première fois on utilise le sommet de l'arbre comme noeud de début
		if (root == None):
			root = self.arbre.root
		#Si on trouve la valeur recherchée la methode retourne True
		if (root.value == self.val):
			return True
		#sinon si la valeur recherchée est inférieure à celle du noeud et le noeud a un fils gauche
		elif(self.val < root.value and root.left != None):
			#on execute la méthode run avec le fils gauche comme noeud de départ
			root = root.left
			return self.run(root)
		#sinon si la valeur recherchée est supérieure à celle du noeud et le noeud a un fils droite
		elif(self.val > root.value and root.right != None):
		#on execute la méthode run avec le fils droite comme noeud de départ
			root = root.right
			return self.run(root)
		#Si aucune des conditions n'est vérifiée la methode retourne False
		return False