''' Wordle Helper_4.3

Wordle Rules:
Guess the WORDLE in six tries.
Each guess must be a valid five-letter word.
After each guess, the color of the tiles change to show how close your guess was to the word.
Examples
The letter W is GREEN  : It's in the correct spot.
The letter I is YELLOW : It's in the wrong spot.
The letter U is GREY   : It's not in the word in any spot.
'''

'''Update:

'''


import userinput
from word import WordOps


def header():
    '''Print header on putput screen'''

    print('\n\n---Wordle Helper v4.3.0---')#.center(50)
    print('---Because NYT Sucks---\n')#.center(50)


def footer():
    '''Print footer on putput screen'''

    print('\n\n---Wordle Helper---')#.center(50)


def read_wordfile():
    '''Read the file containing all words'''

    all_words = []

    with open('data/wordfile.txt') as f: lines = f.readlines()
    for line in lines: all_words.append(line.strip().lower())
    return all_words


def read_current_list_file():
    '''Read from the list of words saved from the previous while loop'''

    with open('data/temp_current_list.txt', 'r') as f: data_str = f.read()
    data_list = convert_str_to_list(data_str)
    return data_list


def write_current_list_file(data):
    '''Write the current word like to file'''

    data_str = convert_list_to_str(data)
    with open('data/temp_current_list.txt', 'w') as f: f.write(data_str)
    

def convert_list_to_str(wordlist):
    '''Conver a list to a string'''
    data_str = ''
    for word in wordlist: data_str += word + ' '
    return data_str
    

def convert_str_to_list(data_str):
    '''Convert a string to a list'''

    return data_str.split(' ')


def print_current_list(current_list):
    '''Print the list of words after analyzing input values'''

    print("\nList of words:\n")
    print(current_list)
    print(f'\n{len(current_list)} words found')


def condition_check(word_count, another_word, current_list):
    '''Condition check for while loop'''
        
    if current_list == []:
        another_word = input(f"\nInput 'q' to quit.\nHit enter to try word {word_count}\nWhat do you wanna do?: ")
        print("I like your enthusiasm.")
        print("But as you see, we're out of words to filter.")
        print("So, Bye bye!!!")
        print("See you tomorrow")
        return exit()
    
    if word_count == 6:
        print("I don't see the point in trying another word.")
        print("But sure, go ahead if you want.")
        another_word = input("Enter whatever to continue: ")
        return another_word

    if word_count > 6:        
        print("Now this is getting silly!")
        print("Bye!!!")
        print("See you tomorrow!")
        return exit()

    another_word = input(f"\nInput 'q' to quit.\nHit enter to try word {word_count}\nWhat do you wanna do?: ")

    if another_word == 'q' and word_count < 6:
        
        print("\nOkay!\nHope you found the word.\nSee you tomorrow!")
        return exit()

    
def print_output(wordlist, words_per_line=6):
    count = 0
    word_str = ''

    for word in wordlist:
        count += 1
        word_str += word.lower() + ', '        
        if count % words_per_line == 0:
            word_str += '\n'
    
    if word_str:
        # print(f'{len(wordlist)} words found:\n')
        print(f'{word_str}')
        print(f'\n{len(wordlist)} words found.\n')
    else:
        print("No matches found. You're on your own!")
    

def main():
    '''Main body of the program'''
    word_length = 5
    word_count = 1
    another_word = ''
    current_list = []    

    header()
    
    while another_word != 'q':
        '''Controlled loop to check if usre needs help with another words.'''
        
        write_current_list_file(current_list)

        # INPUT BLOCK
        ##########################################################
        print(f'\n------Word {word_count}------\n')
        userinput.take_input()

        green_1 = userinput.sq_g1
        green_2 = userinput.sq_g2
        green_3 = userinput.sq_g3
        green_4 = userinput.sq_g4
        green_5 = userinput.sq_g5

        yellow_1 = userinput.sq_y1
        yellow_2 = userinput.sq_y2
        yellow_3 = userinput.sq_y3
        yellow_4 = userinput.sq_y4
        yellow_5 = userinput.sq_y5

        green   = userinput.green
        yellow  = userinput.yellow
        grey    = userinput.grey
        grellow = userinput.grellow

        entered_word = userinput.entered_word
        ##########################################################
        
        print(f"\nWord entered: {entered_word.upper()}\n")

        # choose whilch list of words to read from
        if word_count == 1: all_words = read_wordfile()                
        elif word_count > 1: all_words = read_current_list_file()

        # create instance of class WordOps
        word_1 = WordOps(
            green=green, yellow=yellow, grey=grey, wordlist=all_words, word_length=word_length,
            green_1=green_1, green_2=green_2, green_3=green_3,
            green_4=green_4, green_5=green_5, 
            yellow_1=yellow_1, yellow_2=yellow_2, yellow_3=yellow_3,
            yellow_4=yellow_4, yellow_5=yellow_5, grellow=grellow
            )

        # get words of length 5
        len5_words = word_1.get_words_of_len_n()
        current_list = len5_words[:]

        # operating with grey letters
        greys = word_1.filter_out_greys(current_list)
        current_list = greys[:]

        #operating with green letters
        greens = word_1.filter_in_greens(current_list)
        if greens: current_list = greens[:]

        # operating with grey letters
        yellows = word_1.filter_in_yellows(current_list)
        if yellows: current_list = yellows[:]

        # removing grellow letters
        if grellow != None and grellow != '':
            grellows = word_1.filter_out_grellow(current_list)
            if grellows: current_list = grellows[:]

        # output final list to screen
        # print_current_list(current_list)        
        print_output(current_list)
        


        # condition check for while loop
        word_count += 1
        condition_check(word_count, another_word, current_list)
        
    footer()


if __name__ == '__main__': main()


    #     # MANUAL INPUT BLOCK
    # ######################################################################
    # word_length = 5
    # green_1, green_2, green_3, green_4, green_5      = '', '', '', '', ''
    # yellow_1, yellow_2, yellow_3, yellow_4, yellow_5 = '', '', '', '', ''
    # yellow = ''
    # grey = 'dremblckouij'
    # grellow = ''
    # ######################################################################
