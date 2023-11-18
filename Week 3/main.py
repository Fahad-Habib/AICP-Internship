print("My Student ID is XY12345678")

data = [
	[55,	65,		75],
	[120,	150,	170],
	[210,	230,	240]
]
costs = [10, 15, 20]


def costSlab1():
	print("Bill for Slab 1 is")
	print("\t".join([str(i*costs[0]) for i in data[0]]))


def costSlab2():
	print("Bill for Slab 2 is")
	print("\t".join([str(i*costs[1]) for i in data[1]]))


def costSlab3():
	print("Bill for Slab 3 is")
	print("\t".join([str(i*costs[2]) for i in data[2]]))


if __name__ == '__main__':
	while True:
		print("""Enter your choice
Press 1 to display the bill of slab 1 and slab 2.
Press 2 to display the bill of slab 3.
Press any other key to exit.""")
		choice = input()
		if choice == '1':
			costSlab1()
			costSlab2()
		elif choice == '2':
			costSlab3()
		else:
			break
		print()
