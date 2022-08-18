def hello():
	print("Hello world!")

hello()

def pack(item1, item2, item3):
	return [item1, item2, item3]

print(pack("A", "B", "C"))

def eat_lunch(list):
	if len(list) == 0:
		print("My lunchbox is empty!")
		return
	
	print("First I eat " + list[0])
	for i in range(1, len(list)):
		print("Next I eat " + list[i])

eat_lunch([])
eat_lunch(["pizza"])
eat_lunch(["crackers", "potatoes", "apples", "hamburgers"])