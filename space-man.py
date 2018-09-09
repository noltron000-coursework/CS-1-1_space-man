

# Here is a couple of dictionaries.
dictionary_primary = ["worda","wordb"]


# This function cleans the dictionary.
# First, it removes words with invalid character.
# Then, it conversts each word to lowercase.
# " " and "-" are valid white-space characters.
def cleanup(dictionary):
	return dictionary


# This function simply picks a word at random.
# Its input is a dictionary list.
# Its output is a random word from the list.
def randomWord(dictionary):
	return dictionary[0]


# This function has an input of a word, in string format.
# It keeps valid whitespace characters as-is.
# It replaces all alphabetical characters with underscores.
# It returns each character with a space inbetween.
def censor(word):
	return word


def asciiArt(turnNumber):
	return '''
1
2
3
'''


# This function takes the input of a secret word, public word, and an array of letters used
# It checks the length of the array for turns used.
# It displays a space-man depending on the turns used.
# It displays the public word.
# It displays used letters.
# It displays turns remaining.
# Finally, it calls another function to ask for a letter.
def turnLoop(secretWord, publicWord, letterList):
	turnNumber = len(letterList) + 1
	print(asciiArt(turnNumber))
	print("CURRENT WORD: " + publicWord)
	print("LETTERS USED: " + str(letterList))
	print("ROUND NUMBER: " + str(turnNumber))




# This function will start the space-man game.
# It has no input, but can use options to browse different dictionaries.
# It runs until the player has lost or won.
def spaceMan():
	# Choose dictionary.
	dictionary = dictionary_primary

	# Clean the dictionary.
	dictionary = cleanup(dictionary)

	# Pick a random word from dictionary.
	secretWord = randomWord(dictionary)

	# Create a string of underscores to show player.
	publicWord = censor(secretWord)

	# Create an empty array, representing letters guessed.
	letterList = []

	# This is the meat of the turn.
	turnLoop(secretWord, publicWord, letterList)

spaceMan()
