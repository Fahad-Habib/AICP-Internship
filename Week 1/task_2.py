from tabulate import tabulate


with open('data.csv') as file:
	data = [i.split(',') for i in file.read().strip().split('\n')]
	items = {i[1]: [i[0], i[2], float(i[3])] for i in data[1:]}


print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'), '\n')

case = input('Please choose a case and enter the item code: ').upper()
while case[0] != 'A' or case not in items:
	print("[INVALID] Invalid code")
	case = input('Please enter a valid item code for a case: ').upper()

ram = input('Please choose a RAM and enter the item code: ').upper()
while ram[0] != 'B' or ram not in items:
	print("[INVALID] Invalid code")
	ram = input('Please enter a valid item code for a RAM: ').upper()

main_drive = input('Please choose a Main Hard Disk Drive and enter the item code: ').upper()
while main_drive[0] != 'C' or main_drive not in items:
	print("[INVALID] Invalid code")
	main_drive = input('Please enter a valid item code for a Main Hard Disk Drive: ').upper()

done = 'ABC'
extras = []
extra = input("Please choose any additional item and enter the item code, otherwise enter 0: ").upper()
while extra != '0':
	if extra not in items:
		print("[INVALID] Invalid code")
		extra = input('Please enter a valid item code or enter 0 if you do not want anything else: ').upper()
	elif extra[0] in done:
		extra = input('You have already bought an item from this category please select item from any other category if you want, else enter 0: ').upper()
	else:
		extras.append(extra)
		done += extra[0]
		extra = input("Please choose any additional item and enter the item code, otherwise enter 0: ").upper()

price = items[case][-1] + items[ram][-1] + items[main_drive][-1] + sum([items[i][-1] for i in extras])
purchases = [
	['Category', 'Description', 'Price ($)'],
	items[case],
	items[ram],
	items[main_drive],
] + [items[i] for i in extras]
purchases.append(['Total Cost', '', f'{price} $'])

print()
print(tabulate(purchases, headers='firstrow', tablefmt='fancy_grid'))
