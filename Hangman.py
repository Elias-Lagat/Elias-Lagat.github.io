# import additional functions
from random import choice
from IPython.display import clear_output

# declare game variables
words = ['tree', 'basket', 'chair', 'paper', 'python']
word = choice(words)
guessed, lives, game_over = [], 7, False

# create a list of underscores to the length of the word
for x in word:
    guesses = [0], ['_ '] * (len(word) - 1)


# create main game loop
while not game_over:
    # output game information
    hidden_word = ''.join(guesses)
    print('Your guessed letters: {}'.format(guessed))
    print('Word to guess: {}'.format(hidden_word))
    print('Lives: {}'.format(lives))
    
    ans = input('Type quit or guess a letter: ').lower()
    
    clear_output()     # clear all previous output
    
    if ans == 'quit':
        print('Thanks for playing.')
        game_over = True
    elif ans in word and ans not in guessed:
        print('You guessed correctly!')
           # create a loop to change underscore to proper letter
        for i in range(len(word)):
            if word[i] == ans:
                guesses[i] = ans
    elif ans in guessed:
        print('You already guessed that. Try again.')
    else:                 # otherwise lose life
        lives -= 1
        print('Incorrect, you lost a life.')
        
    if ans not in guessed:
        guessed.append(ans)    # add guess to guessed list
        
    if lives <= 0:
        print('You lost all your lives, you lost!')
        game_over = True
    elif word == ''.join(guesses):
        print('Congratulations, you guessed it correctly!')
        game_over = True