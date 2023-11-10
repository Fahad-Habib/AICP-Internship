from tabulate import tabulate


trains = {
	str(i): {
		'up': {'tickets': 480, 'total': 0}, 
		'down': {'tickets': 480, 'total': 0}
	} for i in range(1, 5)
}
trains['4']['down']['tickets'] += 160  # 2 extra coaches on the last train


def display():
	table = [
		['', 'Departure', 'Return', 'Tickets (Departure)', 'Tickets (Return)']
	] + [[
		f'Train {i}', f'{7+(int(i)*2)}:00', f'{8+(int(i)*2)}:00', 
		trains[i]['up']['tickets'] if trains[i]['up']['tickets'] else 'Closed', 
		trains[i]['down']['tickets'] if trains[i]['down']['tickets'] else 'Closed'
	] for i in trains]

	print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'), '\n')


def purchase_ticket():
	s = input('Enter the train number for your journey up the hill: ').strip()
	while s not in trains:
		s = input('Please enter a valid train number: ').strip()
	e = input('Enter the train number for your journey down the hill: ').strip()
	while e not in trains:
		e = input('Please enter a valid train number: ').strip()
	if s > e:
		print("[INVALID] You cannot return on a train that is returning before your departure.\n")
		return
	while True:
		try:
			n = int(input("Enter the number of tickets that you want to purchase: "))
			break
		except ValueError:
			print("[INVALID] Please enter a valid integer.")
	if n > trains[s]['up']['tickets'] or n > trains[e]['down']['tickets']:
		print("[OVERLOAD] The required number of tickets exceed the available.\n")
		return

	cost = (n * 50) - (int(n//10) * 50)  # Tenth passenger travels free
	print("Your total cost is:", cost, "$\n")

	trains[s]['up']['tickets'] -= n
	trains[e]['down']['tickets'] -= n
	trains[s]['up']['total'] += cost
	trains[e]['down']['total'] += cost


if __name__ == '__main__':
	while True:
		display()
		purchase_ticket()
