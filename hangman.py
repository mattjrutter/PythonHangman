#MATT RUTTER
#Homework 1
#CSCI 310 2/15/16
import random

def welcome():   #Welcomes the player to the game and gets desired difficulty
    print("""
 __          __  _                            _        
 \ \        / / | |                          | |       
  \ \  /\  / ___| | ___ ___  _ __ ___   ___  | |_ ___  
   \ \/  \/ / _ | |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \ 
    \  /\  |  __| | (_| (_) | | | | | |  __/ | || (_) |
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/ 
        ,--,                                                                     
      ,--.'|                                         ____                        
   ,--,  | :                                       ,'  , `.                      
,---.'|  : '                ,---,               ,-+-,.' _ |               ,---,  
|   | : _' |            ,-+-. /  | ,----._,. ,-+-. ;   , ||           ,-+-. /  | 
:   : |.'  | ,--.--.   ,--.'|'   |/   /  ' /,--.'|'   |  ||,--.--.   ,--.'|'   | 
|   ' '  ; :/       \ |   |  ,"' |   :     |   |  ,', |  |/       \ |   |  ,"' | 
'   |  .'. .--.  .-. ||   | /  | |   | .\  |   | /  | |--.--.  .-. ||   | /  | | 
|   | :  | '\__\/: . .|   | |  | .   ; ';  |   : |  | ,   \__\/: . .|   | |  | | 
'   : |  : ;," .--.; ||   | |  |/'   .   . |   : |  |/    ," .--.; ||   | |  |/  
|   | '  ,//  /  ,.  ||   | |--'  `---`-'| |   | |`-'    /  /  ,.  ||   | |--'   
;   : ;--';  :   .'   |   |/      .'__/\_: |   ;/       ;  :   .'   |   |/       
|   ,/    |  ,     .-.'---'       |   :    '---'        |  ,     .-.'---'        
'---'      `--`---'                \   \  /              `--`---'                
                                    `--`-'
""")
    difficulty = input('Please type desired difficulty (1 = Easy, 2 = Normal, 3 = Hard): ')
    return difficulty

def words(difficulty):    #Randomly selects a word in the desired difficulty
    d = random.randrange(0, 30, 1)
    if difficulty == '1':
        easy = ['across', 'against', 'another', 'became', 'become', 'because', 'between',
                'certain', 'children', 'country', 'different', 'example', 'family',
                'father', 'found', 'ground', 'himself', 'however', 'important',
                'money', 'morning', 'mother', 'number', 'people', 'remember',
                'school', 'sentence', 'thought', 'through', 'together']
        return easy[d]
    elif difficulty == '2':
        normal = ['arrangment', 'constantly', 'contrast', 'damage', 'discussion',
                  'essential','exchange', 'explanation', 'grandmother', 'independent',
                  'manufacturing', 'mathematics', 'mysterious', 'neighborhood',
                  'occasionally', 'policeman', 'practical', 'relationship', 'rhyme',
                  'satellites', 'satisfied', 'selection', 'shallow', 'simplest', 'species',
                  'tobacco', 'university', 'remarkable', 'practical', 'ourselves']
        return normal[d]
    else:
        hard = ['jazziest', 'zigzagging', 'buzzing', 'wigwagging', 'beekeeping',
                'mummifying', 'fluffiness', 'fuzziness', 'revivified', 'shabbiness',
                'hobnobbing', 'wooziness', 'sleeveless', 'juddering', 'jemmying',
                'skyjacking', 'muffling', 'parallaxes', 'giggliest', 'yammering', 'kookiest',
                'quizzers', 'fizzed', 'fizzes', 'jugged', 'razzing', 'bubbliest', 'huffing',
                'shivving', 'jemmying']
        return hard[d]

#The hanging man progressive picture
HANGINGMAN = ['''
|----------|
|          |
|          |
|          |
|          |
|          |
|          |
|----------|''', '''
|----------|
|          |
|          |
|          |
|          |
|          |
|==========|
|----------|''', '''
|----------|
|      |   |
|      |   |
|      |   |
|      |   |
|      |   |
|==========|
|----------|''', '''
|----------|
|   ---|   |
|      |   |
|      |   |
|      |   |
|      |   |
|==========|
|----------|''', '''
|----------|
|  |---|   |
|  |   |   |
|      |   |
|      |   |
|      |   |
|==========|
|----------|''', '''
|----------|
|  |---|   |
|  |   |   |
|  0   |   |
|      |   |
|      |   |
|==========|
|----------|''', '''
|----------|
|  |---|   |
|  |   |   |
|  0   |   |
|  |   |   |
|      |   |
|==========|
|----------|''', '''
|----------|
|  |---|   |
|  |   |   |
|  0   |   |
|  |\  |   |
|      |   |
|==========|
|----------|''', '''
|----------|
|  |---|   |
|  |   |   |
|  0   |   |
| /|\  |   |
|      |   |
|==========|
|----------|''', '''
|----------|
|  |---|   |
|  |   |   |
|  0   |   |
| /|\  |   |
|   \  |   |
|==========|
|----------|''', '''
|----------|
|  |---|   |
|  |   |   |
|  0   |   |
| /|\  |   |
| / \  |   |
|==========|
|----------|''']

def gameinfo(HANGINGMAN, wrongletters, rightletters, hiddenword):
    print(HANGINGMAN[len(wrongletters)]) #Displays the current progression of the hanging man
    print()
    print('Wrong Letters: ', end=' ')
    for letter in wrongletters:   #Displays the wrongly guessed letters
        print(letter, end=' ')
    print()
    blanks = '_' * len(hiddenword)  #Initializes a string of blanks for the hidden word
    for i in range(len(hiddenword)):#Modifies the blanks string to reveal the correctly guessed letters in their respective possition
        if hiddenword[i] in rightletters:
            blanks = blanks[:i] + hiddenword[i] + blanks[i + 1:]
    for letter in blanks: #Displays the modified blanks string
        print(letter, end=' ')
    print()

def retrieveguess(guessed): #Gets the guesses from the player
    while True:
        guess = input('Guess a letter: ')
        guess = guess.lower()         #Forces the guessed letter into lower case
        if len(guess) != 1:           #Checks that the player only entered one letter
            print('Please, enter a single letter.')
        elif guess in guessed:        #Checks if the letter has already been guessed
            print('You have guessed that letter already. Try again. ')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':    #Checks if the character is a letter
            print('Please, enter a letter.')
        else:
            return guess

def again(): #checks to see if the player wants to play another round
    print('Do you want to play again? (y or n): ', end=' ')
    return input().lower().startswith('y') #Whether the player enters Y or yes, any y will start it again

difficulty = welcome() #Starts the game the first round
hiddenword = words(difficulty)
wrongletters = ''
rightletters = ''
gamefinished = False

while True:
    gameinfo(HANGINGMAN, wrongletters, rightletters, hiddenword) #Displays the current progress of the player
    guess = retrieveguess(wrongletters + rightletters) #Gets a valid guess from the player
    if guess in hiddenword:                            #Checks if the player has a correct guess
        rightletters = rightletters + guess            #Adds the corrctly guessed letter to the list of rightletters
        worddone = True
        for i in range(len(hiddenword)):               #If blanks are found, it loops again
            if hiddenword[i] not in rightletters:
                worddone = False
                break
        if worddone:                                   #If the word is finished, it keeps worddone as true and finishes the round
            print('Congratulations! The word was "' + hiddenword + '."')
            gamefinished = True
    else:
        wrongletters = wrongletters + guess            #Adds the wrongly guessed letter to the list of wrongletters
        if len(wrongletters) == len(HANGINGMAN) - 1:   #Detects if the player has run out of guesses, else it loops again
            gameinfo(HANGINGMAN, wrongletters, rightletters, hiddenword)
            print('You have run out of guesses!\nAfter ' + str(len(wrongletters)) +
                  ' wrong guesses and ' + str(len(rightletters)) +
                  ' correct guesses, the word was "' + hiddenword + '"')
            gamefinished = True                        #Finishes out the game
    if gamefinished:     #This decides what to do at the end of each round based on player input
        if again():      #If the player wants to play again, it reinitializes the variables and starts the new round
            difficulty = welcome()
            hiddenword = words(difficulty)
            wrongletters = ''
            rightletters = ''
            gamefinished = False
        else:            #If the player decides not to play again, it thanks the player and closes the loop
            print('THANKS FOR PLAYING!')
            break
    

