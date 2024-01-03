import re

print("""
Boats cannot be hired before 10:00 or returned after 17:00.
Boats can only be hired in intervals of 30 minutes such as:
10:00, 10:30, 11:00, 11:30, 12:00, 12:30, 13:00, 14:00 etc.
Cost of a boat for one hour is $20 or $12 for half an hour.
""")
N = 10  # Number of boats
pattern = re.compile(r'^1[0-7]:[03]0$')  # 10:00 - 17:00 pattern
slots = {int(f"{10+(i//2)}{30*(i%2)}")*(10**((i+1)%2)): 0 for i in range(15)}
boats = {i: [0, 0] for i in range(N)}
prices = [20, 12]


def get_choice():
	c = input("Enter 1 to hire a boat or 0 to end the day: ")
	while c not in '01':
		print("[INVALID] Please enter a valid choice.")
		c = input("Enter 1 to hire a boat or 0 to end the day: ")
	return int(c)


def get_hours():
	c = input("Enter 1 for an hour or 2 for half an hour: ")
	while c not in '12':
		print("[INVALID] Please enter a valid choice.")
		c = input("Enter 1 for an hour or 2 for half an hour: ")
	return int(c)


def get_time():
	t = input("Enter hiring time slot: ")
	while not pattern.match(t):
		print("[INVALID] Please enter a valid time slot.")
		t = input("Enter hiring time slot: ")
	return int("".join(t.split(":")))


def get_end_time(t, s):
	if s == 1700:
		return
	if t == 1 and s == 1630:
		return
	if t == 1:
		return s + 100
	if s % 100 == 0:
		return s + 30
	return s + 70


def check_slot(t, s, n):
	if slots[s] < n:
		if s % 100 == 0:
			if t == 1:
				return slots[s+30] < n and slots[s+100] < n
			return slots[s+30] < n
		else:
			if t == 1:
				return slots[s+70] < n and slots[s+100] < n
			return slots[s+70] < n


def update_slots(t, s):
	slots[s] += 1
	if s % 100 == 0:
		slots[s+30] += 1
		if t == 1:
			slots[s+100] += 1
	else:
		slots[s+70] += 1
		if t == 1:
			slots[s+100] += 1


choice = get_choice()

while choice:
	end_time = None
	while not end_time:
		time = get_hours()
		start_time = get_time()
		end_time = get_end_time(time, start_time)
		if not end_time:
			print("[INVALID] Boat cannot be returned after 17:00.")
	if check_slot(time, start_time, N):
		boats[slots[start_time]][0] += prices[time-1]
		boats[slots[start_time]][1] += 1 / (2**(time-1))  # 1 for 1, 0.5 for 2
		update_slots(time, start_time)
		print("\n[SUCCESS] Boat has been hired!\n")
	else:
		print("\n[404] Sorry, no boat is available for this time slot.")
		temp = sorted(slots)
		ind = temp.index(start_time)
		for i in temp[ind+1:-time]:
			if check_slot(time, i, N):
				next_time = f"{i//100}:{i%100}"
				if i % 100 == 0:
					next_time += '0'
				print(f"[MESSAGE] Next earliest boat will be available at {next_time}.\n")
				break
		else:
			print("[MESSAGE] All the boats after this time slot have been pre-booked.")
	choice = get_choice()

print("Total money:", sum([i for i, _ in boats.values()]), "$")
print("Total number of hours:", sum([i for _, i in boats.values()]))
print(f"{[i for _, i in boats.values()].count(0)} boats went unused.")
hours = sorted([(boats[key][1], key) for key in boats], reverse=True)
print("Most used boat was boat no.", hours[0][1]+1)
