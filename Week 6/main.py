def input_sack():
	contents = {i: 0 for i in "cgs"}
	limits = {
		'c': [24.9, 25.1], 
		'g': [49.9, 51.1], 
		's': [49.9, 51.1]
	}
	names = {'c': 'Cement', 's': "Sand", 'g': 'Gravel'}
	while True:
		raw = input().strip().lower()
		if raw == 'done':
			if all([limits[i][0] < contents[i] < limits[i][1] for i in contents]):
				for i in contents:
					print(f"{names[i]}: {round(contents[i], 2)} kg")
				return contents
			else:
				for i in names:
					if contents[i] <= limits[i][0]:
						print(f"[SACK REJECTED] {names[i]} is underweight.")
					if contents[i] >= limits[i][1]:
						print(f"[SACK REJECTED] {names[i]} is overweight.")
				break
		raw = raw.split()
		if len(raw) == 2:
			if raw[0] in "cgs":
				try:
					weight = float(raw[1])
					contents[raw[0]] += weight
				except:
					print("[INVALID] Invalid input. Please follow the given format.")
			else:
				print("[INVALID] Invalid input. Please follow the given format.")
		else:
			print("[INVALID] Invalid input. Please follow the given format.")
		

if __name__ == '__main__':
	sack = input_sack()
