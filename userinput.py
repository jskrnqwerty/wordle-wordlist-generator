'''A function to take user input.
Reads one square at a time and determines two things:
1- Letter in the square
2- Colour of the square
'''


def take_input():
    '''Take input'''

    global green
    global yellow
    global grey
    global sq_g1
    global sq_g2
    global sq_g3
    global sq_g4
    global sq_g5 
    global sq_y1
    global sq_y2
    global sq_y3
    global sq_y4
    global sq_y5
    global entered_word
    global grellow

    green = ''
    yellow = ''  
    grey = ''
    grellow = ''
        
    print_instructions()

    # assign each square's info to respective variable
    sq_1_input = input_sq(1)
    sq_2_input = input_sq(2)
    sq_3_input = input_sq(3)
    sq_4_input = input_sq(4)
    sq_5_input = input_sq(5)
    sq_all_inputs = [sq_1_input, sq_2_input, sq_3_input, sq_4_input, sq_5_input]
    
    # returned list contents are:
    # (entered_word, green_extract, yellow_extract, grey_extract, grellow_extract, sq_info_lol)
    breakup_sq_inputs_output = breakup_sq_inputs(sq_all_inputs)
    
    # list structure is as follows
    # sq_row_lol = [['entered_letter', 'colour'], ['entered_letter', 'colour'], [] , [] , []]
    sq_row_lol = breakup_sq_inputs_output[-1]

    # COLOUR ASSIGNMENT BLOCK
    #################################################################################
    # assign the input letter to unique variable IF square is green
    sq_g1 = ''.join([sq_row_lol[0][0] if sq_row_lol[0][1] == 'green' else ''])
    sq_g2 = ''.join([sq_row_lol[1][0] if sq_row_lol[1][1] == 'green' else ''])
    sq_g3 = ''.join([sq_row_lol[2][0] if sq_row_lol[2][1] == 'green' else ''])
    sq_g4 = ''.join([sq_row_lol[3][0] if sq_row_lol[3][1] == 'green' else ''])
    sq_g5 = ''.join([sq_row_lol[4][0] if sq_row_lol[4][1] == 'green' else ''])
    
    # assign the input letter to unique variable IF square is yellow
    sq_y1 = ''.join([sq_row_lol[0][0] if sq_row_lol[0][1] == 'yellow' else ''])
    sq_y2 = ''.join([sq_row_lol[1][0] if sq_row_lol[1][1] == 'yellow' else ''])
    sq_y3 = ''.join([sq_row_lol[2][0] if sq_row_lol[2][1] == 'yellow' else ''])
    sq_y4 = ''.join([sq_row_lol[3][0] if sq_row_lol[3][1] == 'yellow' else ''])
    sq_y5 = ''.join([sq_row_lol[4][0] if sq_row_lol[4][1] == 'yellow' else ''])

    #################################################################################

    # grey: string of characters that must not be in any of the words.
    grey = breakup_sq_inputs_output[3].lower()
    # grey = sq_g1 + sq_g2 + sq_g3 + sq_g4 + sq_g5

    # yellow: string of characters that must be included in the word, but not at its current spot.
    yellow = breakup_sq_inputs_output[2].lower()
    # yellow = sq_y1 + sq_y2 + sq_y3 + sq_y4 + sq_y5

    # green: string of characters that must be included in the word, and at the current spot.
    green = breakup_sq_inputs_output[1].lower()

    # word string entered by user.
    entered_word = breakup_sq_inputs_output[0].upper()

    # a special kind of grey string, consisting one grey letter that is in greens but will have characteristics of a yellow letter.
    grellow = breakup_sq_inputs_output[4]


def print_instructions():
    '''Print instructions on screen'''

    print("for Green  -> 'g'\nfor Yellow -> 'y'\nfor Grey   -> ''\n")
    print("Suffix the letter with colour indicator, like:")
    print("For 'A' in GREEN square : ag")
    print("For 'B' in YELLOW square: by")
    print("For 'C' in GREY square  : c\n")
    

def input_sq(count):
    '''Take input from user'''
    return input(f"LetterColour in Square {count}: ").lower()


def breakup_sq_inputs(sq_all_inputs):
    '''Break down user input into separate lists of greens, yellow, greys, and a lol of all user info'''
    
    entered_word = ''
    green_extract = ''
    yellow_extract = ''
    grey_extract_temp = ''
    sq_info = []
    sq_info_lol = []
    
    # Structure: sq_all_inputs = [sq_1_input, sq_2_input, sq_3_input, sq_4_input, sq_5_input]
    # Structure: sq_1_input = 'ag'
    for item in sq_all_inputs:
        '''Separate the yelow, green and grey letters.'''

        if len(item) == 2 and item[1] == 'g': green_extract += item[0]
        if len(item) == 2 and item[1] == 'y': yellow_extract += item[0]
        if len(item) == 1 : grey_extract_temp += item
    
        # Organize above data into lists 
        if item[0] in green_extract.lower(): sq_info = [f'{item[0]}', 'green']
        if item[0] in yellow_extract.lower(): sq_info = [f'{item[0]}', 'yellow']
        if item[0] in grey_extract_temp.lower(): sq_info = [f'{item[0]}', 'grey']
        
        # capitalize green and yellow letters in the entered word
        if item[0] in green_extract or item[0] in yellow_extract:
            temp = item[0]
            entered_word += temp.upper()
        else:
            entered_word += item[0]

        sq_info_lol.append(sq_info)
    
    def find_grellow():
        '''Grello = Grey + Yellow
        If a grey letter is already in Greens
        grellow output is going to be ne like 'e2' 
        where 'e' is the grellow letter and '2' is it's spot inside the entered word.'''
        grellow_extract = ''
        
        try:
            if green_extract:
                for g in grey_extract_temp:        
                    if g in green_extract.lower():                     
                        grellow_extract = g
                        g_spot = str(entered_word.index(g) + 1)
                        grellow_extract = g + g_spot

                if grellow_extract: return grellow_extract
                else: return ''
        except ValueError:
            print("Contradicting input received. Try again.")
            exit()

    grellow_extract = find_grellow()

    green_extract = green_extract.upper()
    yellow_extract = yellow_extract.upper()
    grey_extract = check_greys_in_greens_yellows(grey_extract_temp, green_extract, yellow_extract)

    return entered_word, green_extract, yellow_extract, grey_extract, grellow_extract, sq_info_lol


def check_greys_in_greens_yellows(grey_temp, green_extract, yellow_extract):
    '''Remove greys that are in greens or yellows lists'''

    grey_extract = ''
    for g_letter in grey_temp:
        if g_letter not in (green_extract.lower() + yellow_extract.lower()): grey_extract += g_letter    
    return grey_extract




    

# COLOUR ASSIGNMENT BLOCK - AUTOMATED
#################################################################################
# def scan_squares_for_greens(sq_row_lol):
#     green_squares_list = []
#     c = 0
#     for letter_g in sq_row_lol:
#         letter_g = ''.join([sq_row_lol[c][0] if sq_row_lol[c][1] == 'green' else ''])
#         green_squares_list.append(letter_g)
#         c += 1
#     return green_squares_list
# sq_g1 = green_squares_list[0]
# sq_g2 = green_squares_list[1]
# sq_g3 = green_squares_list[2]
# sq_g4 = green_squares_list[3]
# sq_g5 = green_squares_list[4]

# def scan_squares_for_yellows(sq_row_lol):
#     yellow_squares_list = []
#     c = 0
#     for letter_g in sq_row_lol:
#         letter_g = ''.join([sq_row_lol[c][0] if sq_row_lol[c][1] == 'yellow' else ''])
#         yellow_squares_list.append(letter_g)
#         c += 1
#     return yellow_squares_list
# sq_y1 = yellow_squares_list[0]
# sq_y2 = yellow_squares_list[1]
# sq_y3 = yellow_squares_list[2]
# sq_y4 = yellow_squares_list[3]
# sq_y5 = yellow_squares_list[4]

# green_squares_list = scan_squares_for_greens(sq_row_lol)
# yellow_squares_list = scan_squares_for_yellows(sq_row_lol)
#################################################################################
