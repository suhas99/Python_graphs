class LinkedList:
	def __init__(self, val):
		self.val = val
		self.next = None


def count(root):
	count1 = 1
	l = []
	while root.next is not None:
		count1 += 1
		l.append(root.val)
		root = root.next
	if root.next is None:
		l.append(root.val)
	print(count1, l)
  
  
  
ll = LinkedList(1)
ll.next = LinkedList(2)
ll.next.next = LinkedList(3)
ll.next.next.next = LinkedList(4)
ll.next.next.next.next = LinkedList(5)
count(ll)
