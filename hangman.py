import random

def hangman():
    lists = [
        "    O     ",
        "    |     ",
        " =======  ",
        "/   |   \ ",
        "   / \    ",
        "  |   |   "
        ]
    print("========================")
    print("Welcome to Hangman Game.")
    print("========================")

    #Save the word_list.txt in the directory.
    filename = 'C:/Users/markf/Desktop/word_list.txt'
    with open(filename) as f: #get list of words from filename with no white spaces or anything
        words = f.read().split() 
    random_number = random.randint(0, len(words) - 1)
    word_answer = words[random_number]
    display_lines = []
    display_lines.extend(word_answer)

    #this takes number of lines from unique word
    for i in range(len(display_lines)):
        display_lines[i] = '-'
    print(''.join(display_lines)) #displays number of '-'  rather than lists

    guess_count = 6
    count = 0

    while guess_count > 0:
        print("Number of guesses: %d" % guess_count)
        flag = False
        guess = input("Please guess a letter: ")
        guess = guess.lower()

        #CHeck if user enters a letter. If the user enters anything not a letter, then re-promt for input
        if len(guess) != 1 or guess.isdigit():
            print("Letters only please")
            continue
        if guess in display_lines:
            print("Letter '%s' has already been guessed." % guess)
            continue
        
        for i in range(len(word_answer)):
            if word_answer[i] == guess:
                flag = True
                display_lines[i] = guess

        if flag:
            print("\nYup.")
        else:
            print("\nIncorrect guesses: ")
            count += 1
            for i in range(count):
                print(lists[i])
            guess_count -= 1

        print("\nWord so far: ")
        print(''.join(display_lines))
        #if statement goal is to check number of '-' cleared up then ends while loop.
        if '-' not in display_lines:
            break
    #End while
    #print results depends on remaining guess count.
    if guess_count > 0:
        print("\nYou Won!!")
        print("You have used %d of six guesses." % guess_count)
    else:
        print("\nPlayer won.")
        print("The word was '%s'" % word_answer)


'''
String method:
.join(seq)
.lower() 
.split([white space]) 
'''
