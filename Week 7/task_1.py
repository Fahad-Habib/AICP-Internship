names = []
charity = {}

for i in range(3):
	names.append(input(f"Enter the name of your charity number {i+1}: "))
	charity[names[i]] = 0

for i in range(3):
	print(f"{i+1}. {names[i]}")

choice = input("Enter which charity you want to donate to (1, 2, 3): ")
while True:
	try:
		choice = int(choice)
		if 1 <= choice <= 3:
			break
		print("[INVALID] Please enter a valid choice.")
	except:
		print("[INVALID] Please enter a valid choice.")
	choice = input("Enter which charity you want to donate to (1, 2, 3): ")
