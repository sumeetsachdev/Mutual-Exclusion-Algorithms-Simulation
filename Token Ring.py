#Token Ring Algorithm
from random import choice
from time import sleep

choices = [True,False]

class process:
	def __init__(self,name,choice):
		self.data = name
		self.next = None
		self.choice = choice
	
class topology:
	def __init__(self):
		self.head = process(None,False)
		self.tail = process(None,False)
		self.head.next = self.tail
		self.tail.next = self.head

	def append(self,name,choice):
		newnode = process(name,choice)
		if self.head.data is None:
			self.head = newnode
			self.tail = newnode
			newnode.next = self.head
		else:
			self.tail.next = newnode
			self.tail = newnode
			newnode.next = self.head
	
	def printlist(self):
		curr = self.head
		if self.head == None:
			print("Empty List")
		else:
			print(str(curr.data) + " " + str(curr.choice))
			while curr.next != self.head:
				curr = curr.next				
				print(str(curr.data) + " " + str(curr.choice))
	def find(self,data):
		curr = self.head
		if self.head == None:
			print("Empty List")
		else:
			while curr.next != self.head:
				if curr.data == data:
					return [curr.data,curr.choice]
				curr = curr.next



t = topology()
	

for i in range(1,11):
	t.append(i,choice(choices))

token = 1	

t.printlist()


p = int(input("Which process wants to enter the critical section? "))
z = t.find(p)[0]

if token == z:
	print("Process already in Critical Section")
else:
	while(token != z):
		token = token + 1
		temp = t.find(token)
		if temp[1] == False:
			pass
		else:
			print("Currently at node ", temp[0])
			sleep(2)
		
		

