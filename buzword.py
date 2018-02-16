in_list=['Hazem', 'Sara', 'Sirin', 'Layan', 'Hiba']

def letter_freq(word_input):
    letter_list={}
    for i in range(len(word_input)):

        if word_input[i] in letter_list:
            letter_list[word_input[i]] = letter_list[word_input[i]]+1
        else:
            letter_list[word_input[i]] =1
        if letter_list[word_input[i]] == 2:
            print(word_input)

def buzzword(in_list):
    for words in in_list:
        letter_freq(words)
        
        

buzzword(in_list)
        
