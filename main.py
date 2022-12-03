from knight import Knight

with open("datas.txt") as datas:
	english_alphabet = datas.readlines()

# Getting knight datas
knight_horizontal_input = input("Please enter horizontal position of the knight (a,b,c,d,e,f,g,h): ")
knight_vertical_input = int(input("Please enter vertical position of the knight (1,2,3,4,5,6,7,8): "))

# Getting bishop datas
bishop_horizontal_input = input("Please enter horizontal position of the bishop (a,b,c,d,e,f,g,h): ")
bishop_vertical_input = int(input("Please enter vertical position of the bishop (1,2,3,4,5,6,7,8): "))

horizontal_list = ["A", "B", "C", "D", "E", "F", "G", "H", "a", "b", "c", "d", "e", "f", "g", "h"]
vertical_list = [1, 2, 3, 4, 5, 6, 7, 8]


def validation(bead_name, bead_horizontal_input, bead_vertical_input)
	if bead_horizontal_input in english_alphabet:
		if len(bead_horizontal_input) != 1:
			print("Horizontal input is not a letter")
		if bead_horizontal_input not in horizontal_list:
			print("Horizontal input is not a proper letter")

	if bead_vertical_input < 0:
		print("Vertical input is not a number")
	else:
		if bead_vertical_input not in vertical_list:
			print(f"Vertical input for {bead_name} is not a proper number")

validation("Knight", knight_horizontal_input, knight_vertical_input)
validation("Bishop", bishop_horizontal_input, bishop_vertical_input)


Knight(knight_horizontal_input, knight_vertical_input).
def kill_bishop():
	knight_vert_pos_index = vertical_list.index(knight_vertical_input)
	bishop_ver_pos1 = vertical_list[knight_vert_pos_index + 2]
	bishop_ver_pos2 = vertical_list[knight_vert_pos_index - 2]
	bishop_ver_pos3 = vertical_list[knight_vert_pos_index - 1]
	bishop_ver_pos4 = vertical_list[knight_vert_pos_index + 1]
	knight_horiz_pos_index = horizontal_list.index(knight_horizontal_input)
	bishop_hor_pos1 = horizontal_list[knight_horiz_pos_index + 2]
	bishop_hor_pos2 = horizontal_list[knight_horiz_pos_index - 2]
	bishop_hor_pos3 = horizontal_list[knight_horiz_pos_index + 1]
	bishop_hor_pos4 = horizontal_list[knight_horiz_pos_index - 1]

	option1 = bishop_horizontal_input == bishop_hor_pos4 and bishop_vertical_input == bishop_ver_pos1
	option2 = bishop_horizontal_input == bishop_hor_pos3 and bishop_vertical_input == bishop_ver_pos1
	option3 = bishop_horizontal_input == bishop_hor_pos1 and bishop_vertical_input == bishop_ver_pos4
	option4 = bishop_horizontal_input == bishop_hor_pos1 and bishop_vertical_input == bishop_ver_pos3
	option5 = bishop_horizontal_input == bishop_hor_pos3 and bishop_vertical_input == bishop_ver_pos2
	option6 = bishop_horizontal_input == bishop_hor_pos4 and bishop_vertical_input == bishop_ver_pos2
	option7 = bishop_horizontal_input == bishop_hor_pos2 and bishop_vertical_input == bishop_ver_pos3
	option8 = bishop_horizontal_input == bishop_hor_pos2 and bishop_vertical_input == bishop_ver_pos4

	if bishop_vertical_input == bishop_ver_pos1 and bishop_vertical_input == bishop_ver_pos2:
		print("They can't be in the same square")
	elif option1 or option2 or option3 or option4 or option5 or option6 or option7 or option8:
		print("Knight can attack bishop")


kill_bishop()

def kill_knight():

