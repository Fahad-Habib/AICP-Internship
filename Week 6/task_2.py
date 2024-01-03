NAMES = {'c': 'Cement', 's': "Sand", 'g': 'Gravel'}


def input_sack():
	limits = {
		'c': [24.9, 25.1], 
		'g': [49.9, 50.1], 
		's': [49.9, 50.1]
	}
	raw = input("Enter sack details: ").strip().lower().split()
	while True:
		if len(raw) == 2:
			if raw[0] in "cgs":
				try:
					weight = float(raw[1])
					sack = raw[0]
					if weight <= limits[sack][0]:
						print(f"[SACK REJECTED] Sack is underweight.")
						return
					if weight >= limits[sack][1]:
						print(f"[SACK REJECTED] Sack is overweight.")
						return
					return sack, weight
				except ValueError:
					print("[INVALID] Invalid input. Please follow the given format.")
			else:
				print("[INVALID] Invalid input. Please follow the given format.")
		else:
			print("[INVALID] Invalid input. Please follow the given format.")
		raw = input("Enter sack details: ").strip().lower().split()
		

if __name__ == '__main__':
	print("""Follow the following format for adding sack details:
"X W" where W is the weight and X can be C, G and S for Cement, Gravel and Sand respectively\n""")
	N, inputs, rejected, total = {}, {i: 0 for i in NAMES}, 0, 0
	for i in NAMES:
		while True:
			try:
				N[i] = int(input(f"Enter number of sacks of {NAMES[i]}: ").strip())
				break
			except ValueError:
				print("[INVALID] Enter a valid number.")
	print()
	while any([N[i] != inputs[i] for i in NAMES]):
		sack = input_sack()
		if sack:
			t, w = sack
			if N[t] == inputs[t]:
				print(f"[INVALID] {NAMES[t]} sacks already complete.")
			else:
				inputs[t] += 1
				total += w
		else:
			rejected += 1
	
	print("\nTotal weight of the order:", total, 'kg')
	print("Number of sacks rejected:", rejected)
	
