with open("datas.txt") as datas:
	acceptable_horizontal_datas = datas.readlines()

# Getting knight datas
knight_horizontal_input = input("Please enter horizontal position of the knight (a,b,c,d,e,f,g,h): ")
knight_vertical_input = input("Please enter vertical position of the knight (1,2,3,4,5,6,7,8): ")

# Getting bishop datas
bishop_horizontal_input = input("Please enter horizontal position of the bishop (a,b,c,d,e,f,g,h): ")
bishop_vertical_input = input("Please enter vertical position of the bishop (1,2,3,4,5,6,7,8): ")

horizontal_list = ["A", "B", "C", "D", "E", "F", "G", "H", "a", "b", "c", "d", "e", "f", "g", "h"]
vertical_list = [1, 2, 3, 4, 5, 6, 7, 8]

def kill_bishop():
	bishop_ver_pos1 = int(knight_vertical_input) + 2
	bishop_ver_pos2 = int(knight_vertical_input) - 2
	knight_pos_index = horizontal_list[horizontal_list.index(knight_horizontal_input)]
	bishop_hor_pos1 = horizontal_list[knight_pos_index + 2]
	bishop_hor_pos2 = horizontal_list[knight_pos_index - 2]

	if bishop_vertical_input ==




def evaluating_game(knight_pos, bishop_pos):
	if knight_pos == bishop_pos:
		print("They can't be in the same square")



if len(knight_horizontal_input) == 1 and knight_vertical_input in vertical_list:
	if knight_horizontal_input in acceptable_horizontal_datas:
		if knight_horizontal_input in horizontal_list:
			evaluating_game()
		else:
			print("Horizontal input is not a proper letter")
