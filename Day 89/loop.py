class LinkedList:
	head = None

	class Node:
		data = 0
		next = None

		def __init__(self, d):
			self.data = d
			self.next = None

	@staticmethod
	def push(new_data):
		new_node = LinkedList.Node(new_data)
		new_node.next = LinkedList.head
		LinkedList.head = new_node

	def printList(self, node):
		while (node != None):
			print(node.data)
			node = node.next

	@staticmethod
	def removeLoop(h):
		s = set()
		prev = None
		while (h != None):
			if (h in s):
				prev.next = None
				return True
			else:
				s.add(h)
				prev = h
				h = h.next
		return False

	@staticmethod
	def main(args):
		llist = LinkedList()
		llist.push(20)
		llist.push(4)
		llist.push(15)
		llist.push(10)
		llist.head.next.next.next.next = llist.head
		if (LinkedList.removeLoop(LinkedList.head)):
			print("Linked List after removing loop")
			llist.printList(LinkedList.head)
		else:
			print("No Loop found")


if __name__ == "__main__":
	LinkedList.main([])
