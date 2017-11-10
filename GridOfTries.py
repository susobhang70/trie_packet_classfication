import csv

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

		current_node = self.__root

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

def csvimp():
	dictofrules = {}
	with open('rulefile', 'r') as f:
		reader = csv.reader(f,delimiter=" ")
		for row in reader:
			# print row
			rulenumber = int(row[0])
			dest = row[1]
			destlen = int(row[2])
			src = row[3]
			srclen = int(row[4])
			
			destrow = dest.split('.')
			destrow = [int(i) for i in destrow]
			srcrow = src.split('.')
			srcrow = [int(i) for i in srcrow]
			
			destbin = [0 for i in destrow]
			srcbin = [0 for i in srcrow]
			
			deststr = ''
			for i in xrange(len(destrow)):
				destbin[i] = "{0:b}".format(destrow[i])
				temp = len(destbin[i])
				if temp != 8:
					tempstr = ''
					for j in xrange(8-temp):
						tempstr += '0'
					destbin[i] = tempstr + destbin[i]
				deststr += destbin[i]
			deststr = deststr[0:destlen]
			# print deststr

			srcstr = ''
			for i in xrange(len(srcrow)):
				srcbin[i] = "{0:b}".format(srcrow[i])
				temp = len(srcbin[i])
				if temp != 8:
					tempstr = ''
					for j in xrange(8-temp):
						tempstr += '0'
					srcbin[i] = tempstr + srcbin[i]
				srcstr += srcbin[i]
			srcstr = srcstr[0:srclen]
			# print srcstr

			dictofrules[rulenumber] = [deststr,srcstr]
	# print dictofrules
	return dictofrules

def inputimp():
	with open('inputaddrfile', 'r') as f:
		reader = csv.reader(f,delimiter=" ")
		for row in reader:
			# print row
			dest = row[0]
			src = row[1]
			
			destrow = dest.split('.')
			destrow = [int(i) for i in destrow]
			srcrow = src.split('.')
			srcrow = [int(i) for i in srcrow]
			
			destbin = [0 for i in destrow]
			srcbin = [0 for i in srcrow]
			
			deststr = ''
			for i in xrange(len(destrow)):
				destbin[i] = "{0:b}".format(destrow[i])
				temp = len(destbin[i])
				if temp != 8:
					tempstr = ''
					for j in xrange(8-temp):
						tempstr += '0'
					destbin[i] = tempstr + destbin[i]
				deststr += destbin[i]
			deststr = deststr[0:16]
			# print deststr

			srcstr = ''
			for i in xrange(len(srcrow)):
				srcbin[i] = "{0:b}".format(srcrow[i])
				temp = len(srcbin[i])
				if temp != 8:
					tempstr = ''
					for j in xrange(8-temp):
						tempstr += '0'
					srcbin[i] = tempstr + srcbin[i]
				srcstr += srcbin[i]
			srcstr = srcstr[0:16]
			# print srcstr

def createTree(rules):

	F1Trie = Trie("F1")

	records = rules.values()
	for record in records:
		F1Trie.addNode(record[0])

	for rule, record in rules.items():
		F1Trie.updateSubTrie(record[0], record[1], rule)

	return F1Trie

def main():
	rules = csvimp()
	trie = createTree(rules)
	# inputimp()

if __name__ == '__main__':
	main()
