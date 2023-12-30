names = []
totals = {}

for i in range(3):
	names.append(input(f"Enter name of charity no. {i+1}: "))
	totals[names[i]] = 0

for i in range(3):
	print(f"{i+1}. {names[i]}")

while True:
	choice = input("Enter which charity you want to donate to (1, 2, 3): ")
	while True:
		try:
			choice = int(choice)
			if 1 <= choice <= 3 or choice == -1:
				break
			print("[INVALID] Please enter a valid choice.")
		except:
			print("[INVALID] Please enter a valid choice.")
		choice = input("Enter which charity you want to donate to (1, 2, 3): ")
	if choice == -1:
		break
	bill = input("Enter customer's bill: ")
	while True:
		try:
			bill = float(bill)
			break
		except:
			print("[INVALID] Enter a valid number.")
		bill = input("Enter customer's bill: ")

	donation = bill * 0.01  # 1 %
	totals[names[choice-1]] += donation

temp = [(-value, key) for key, value in totals.items()]
temp = sorted(temp)
keys = [key for _, key in temp]
print("\nAmounts Donated:")
for i in keys:
	print(f"{i}: {round(totals[i], 2)} $")

print("GRAND TOTAL DONATED TO CHARITY:", round(sum(totals.values()), 2), "$")
