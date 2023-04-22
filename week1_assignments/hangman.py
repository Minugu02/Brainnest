import random

# word pool
words = ["dog", "cat", "elephant", "rabbit", "tiger", "lion", "giraffe", "leopard", "sheep"]

# select random word from the list
word = random.choice(words)

# string of underscores suggesting the user for number of letters
display_word = "_" * len(word)

# number of guesses allowed
num_guesses = 6
incorrect_guesses = []

while num_guesses > 0 and "_" in  display_word:
    print("The word is: ", display_word)
    print("Incorrect guesses: ", incorrect_guesses)
    print("Guesses remaining: ", num_guesses)

# user's input
    guess = input("Guess a letter: ")

# check if user's guess is in the word
    if guess in  word:

#update the display_word with correct guess
        for  i in  range(len(word)):
            if word[i] == guess:
                display_word = display_word[:i] + guess + display_word[i+1:]
    else:

# add incorrect guesses to the list and decrement it
        incorrect_guesses.append(guess)
        num_guesses -= 1

# printing blank line for spacing
    print()

# print the final state of the game
print("The word is: ", display_word)
print("Incorrect guesses: ", incorrect_guesses)
print("Guesses remaining: ", num_guesses)

#check if the user won or lost
if "_" not in  display_word:
    print("Congratulations, you won!")
else:
    print("You lost the game! The word was: ", word)



# output1

'''
The word is:  _______
Incorrect guesses:  []
Guesses remaining:  6
Guess a letter: a

The word is:  ____a__
Incorrect guesses:  []
Guesses remaining:  6
Guess a letter: l

The word is:  l___a__
Incorrect guesses:  []
Guesses remaining:  6
Guess a letter: e

The word is:  le__a__
Incorrect guesses:  []
Guesses remaining:  6
Guess a letter: o

The word is:  leo_a__
Incorrect guesses:  []
Guesses remaining:  6
Guess a letter: p

The word is:  leopa__
Incorrect guesses:  []
Guesses remaining:  6
Guess a letter: r

The word is:  leopar_
Incorrect guesses:  []
Guesses remaining:  6
Guess a letter: d

The word is:  leopard
Incorrect guesses:  []
Guesses remaining:  6
Congratulations, you won!
'''

# output2

'''
The word is:  ___
Incorrect guesses:  []
Guesses remaining:  6
Guess a letter: e

The word is:  ___
Incorrect guesses:  ['e']
Guesses remaining:  5
Guess a letter: b

The word is:  ___
Incorrect guesses:  ['e', 'b']
Guesses remaining:  4
Guess a letter: h

The word is:  ___
Incorrect guesses:  ['e', 'b', 'h']
Guesses remaining:  3
Guess a letter: m

The word is:  ___
Incorrect guesses:  ['e', 'b', 'h', 'm']
Guesses remaining:  2
Guess a letter: l

The word is:  ___
Incorrect guesses:  ['e', 'b', 'h', 'm', 'l']
Guesses remaining:  1
Guess a letter: x

The word is:  ___
Incorrect guesses:  ['e', 'b', 'h', 'm', 'l', 'x']
Guesses remaining:  0
You lost the game! The word was:  cat
'''
