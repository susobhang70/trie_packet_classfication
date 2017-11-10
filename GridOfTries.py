import os

class Node():
	'''Node implementation'''
	def __init__(self):
		self.rules 		= []
		self.left 		= None
		self.right		= None
		self.trie_pointer = None

	def setLeft(self, obj):
		self.left = obj

	def setRight(self, obj):
		self.right = obj

	def addRule(self, rule):
		self.rules.append(rule)

	def setTrie(self, obj):
		self.trie_pointer = obj

	def getTrie(self):
		return self.trie_pointer

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

class Trie():
	'''Trie implementation'''
	def __init__(self, trie_type):
		self.__root = Node()
		self.__trie_type = trie_type

	def addNode(self, prefix, rule = None):
		if(self.__trie_type != "F2"):
			rule = None

		current_node = self.__root

		for i in range(len(prefix)):
			current_bit = prefix[i]
			if(current_bit == '0'):
				if(current_node.left == None):
					current_node.left = Node()
					current_node.left.addRule(rule)

				current_node = current_node.left

			elif(current_bit == '1'):
				if(current_node.right == None):
					current_node.right = Node()
					current_node.right.addRule(rule)

				current_node = current_node.right

	def updateSubTrie(self, prefix, subprefix, rule):

		for i in range(len(prefix)):
			current_bit = prefix[i]
			if(current_bit == '0'):
				current_node = current_node.left

			elif(current_bit == '1'):
				current_node = current_node.right

		if(current_node.trie_pointer == None):
			current_node.trie_pointer = Trie("F2")

		# current_node.trie_pointer.addNode(subprefix, rule)

		current_node = self.traverse(current_node, subprefix, rule)

	def traverse(self, node, subprefix, rule):

		node.trie_pointer.addNode(subprefix, rule)

		if node.left:
			node.left = self.traverse(node.left, subprefix, rule)

		if node.right:
			node.right = self.traverse(node.right, subprefix, rule)

		return node


def main():
	pass

if __name__ == '__main__':
	main()
