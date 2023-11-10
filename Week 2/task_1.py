from tabulate import tabulate


trains = {
	i: {
		'up': {'tickets': 480, 'total': 0}, 
		'down': {'tickets': 480, 'total': 0}
	} for i in range(1, 5)
}
trains[4]['down']['tickets'] += 160  # 2 extra coaches on the last train

table = [
	['', 'Departure', 'Return', 'Tickets (Departure)', 'Tickets (Return)']
] + [[f'Train {i}', f'{7+(i*2)}:00', f'{8+(i*2)}:00', trains[i]['up']['tickets'], trains[i]['down']['tickets']] for i in trains]

print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'), '\n')
