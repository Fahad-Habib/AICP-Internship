from tabulate import tabulate

grid = [[f'{i}{j}' for j in range(1, 4)] for i in range(1, 4)]  # Initialise grid
valid_moves = []  # Keep track of remaining moves
for i in grid:
	valid_moves += i

players = ['X', 'O']
current_player = 0

print(tabulate(grid, tablefmt='fancy_grid'), '\n')

while valid_moves:
	move = input(f"Player {current_player+1}'s move: ")
	if move not in valid_moves:
		print("[ERROR] Invalid Move!")
		continue
	valid_moves.remove(move)  # Remove the move from valid
	i, j = int(move[0])-1, int(move[1])-1
	grid[i][j] = players[current_player]  # Place X or O at the given place
	print(tabulate(grid, tablefmt='fancy_grid'), '\n')
	winner = None

	for i in grid:  # Check rows of the grid
		if "".join(i) == players[current_player]*3:
			winner = current_player+1
			break
	for i in range(3):  # Check columns of the grid
		if "".join([grid[j][i] for j in range(3)]) == players[current_player]*3:
			winner = current_player+1
			break
	if "".join([grid[i][i] for i in range(3)]) == players[current_player]*3:  # Check diagonal 1
		winner = current_player+1

	if "".join([grid[i][2-i] for i in range(3)]) == players[current_player]*3:  # Check diagonal 2
		winner = current_player+1

	if winner:  # Break the loop if there is a winner
		print(f"[WINNER] Player {current_player+1} Won!")
		break
	
	current_player += 1
	current_player %= 2

else:
	print("[DRAW] It's a draw!")

