'''A class to represent word operations'''


class WordOps:
    '''A class to represent word operations'''
    
    def __init__(self, green, yellow, grey, wordlist, word_length, green_1, green_2, green_3, green_4, green_5 , yellow_1, yellow_2, yellow_3, yellow_4, yellow_5, grellow):
        '''Initialize attributes for class Word'''

        self._green = green
        self._yellow = yellow
        self._grey = grey
        self._wordlist = wordlist
        self._word_length = word_length
        self._green_1 = green_1
        self._green_2 = green_2
        self._green_3 = green_3
        self._green_4 = green_4
        self._green_5 = green_5
        self._yellow_1 = yellow_1
        self._yellow_2 = yellow_2
        self._yellow_3 = yellow_3
        self._yellow_4 = yellow_4
        self._yellow_5 = yellow_5
        self._grellow = grellow


    def get_words_of_len_n(self):
        '''Create list of words of length 5 only'''
        wordlist_n = []

        for word in self._wordlist:
            if len(word) == self._word_length: wordlist_n.append(word)
        return wordlist_n


    def filter_out_greys(self, wordlist_to_filter):
        '''Remove all words containing any of the Grey letters'''
        
        words = []
        for word in wordlist_to_filter:
            if set(self._grey).intersection(set(word)): continue
            else: words.append(word)
        return words


    def filter_in_greens(self, wordlist_to_filter):
        '''Filter in words containing Green letters'''
        
        g1_list, g2_list, g3_list, g4_list, g5_list =  [], [], [], [], []
        g_lol = []

        for word in wordlist_to_filter:
            if self._green_1 and word[0] == self._green_1: g1_list.append(word)
            if self._green_2 and word[1] == self._green_2: g2_list.append(word)
            if self._green_3 and word[2] == self._green_3: g3_list.append(word)
            if self._green_4 and word[3] == self._green_4: g4_list.append(word)
            if self._green_5 and word[4] == self._green_5: g5_list.append(word)

        g_lol_temp = [ g1_list, g2_list, g3_list, g4_list, g5_list ]

        for list_item in g_lol_temp:
            if list_item: g_lol.append(list_item)
        
        if g_lol:
            final_list = list(set.intersection(*map(set, g_lol)))
            return sorted(final_list)
        else:
            return


    def filter_in_yellows(self, wordlist_to_filter):
        '''Filter in words containing Yellow letters'''

        y1_list, y2_list, y3_list, y4_list, y5_list = [], [], [], [], []
        y_lol = []

        for word in wordlist_to_filter:
            if self._yellow_1 and self._yellow_1 in word and word[0] != self._yellow_1: y1_list.append(word)
            if self._yellow_2 and self._yellow_2 in word and word[1] != self._yellow_2: y2_list.append(word)
            if self._yellow_3 and self._yellow_3 in word and word[2] != self._yellow_3: y3_list.append(word)
            if self._yellow_4 and self._yellow_4 in word and word[3] != self._yellow_4: y4_list.append(word)
            if self._yellow_5 and self._yellow_5 in word and word[4] != self._yellow_5: y5_list.append(word)
                
        y_lol_temp = [ y1_list, y2_list, y3_list, y4_list, y5_list ]

        for list_item in y_lol_temp:
            if list_item: y_lol.append(list_item)

        if y_lol:
            final_list = list(set.intersection(*map(set, y_lol)))
            return sorted(final_list)
        else:
            return None

    def filter_out_grellow(self, wordlist_to_filter):
        '''Filter out words containing grellows
        - A grellow is a string like 'e2', where 'e' is the letter and '2' is its spot inside there word'''
        
        words_wo_grellows = []

        print("This is filter_out_grellow() function.")
        # if self._grellow != '':
        grellow_letter = self._grellow[0]
        grellow_index = int(self._grellow[1]) - 1

        for word in wordlist_to_filter:
            if word[grellow_index] != grellow_letter: words_wo_grellows.append(word)

        if words_wo_grellows: return words_wo_grellows
        else: return None

        
        


        