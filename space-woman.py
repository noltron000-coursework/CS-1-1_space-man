import random

# To be honest, I've been trying to move this dictionary to an external file...
# ...but I've been failing to reformat everything to be properly deliminated,
# since the dictionary list is so massive (270,000+ words).

# I've reduced the list to a much more maneagable portion
dictionary_primary = ["a", "cat","pineapple", "juice", "china", "ramen", "orange", "computer", "amazing", "be", "honorificabilitudinitatibus" "supercalifragilisticexpialidocious", "apple"]


# This function cleans the dictionary.
# First, it removes words with invalid character.
# Then, it converts each word to lowercase.
# " " and "-" are valid white-space characters.
def dctCleaner(dictionary):
	return dictionary



# This filters out hard words.
def easier(dictionary, difficulty):
	iterator = 0
	easyDict = []
	for word in dictionary:
		if len(word) <= difficulty:
			easyDict.append(word)
		iterator += 1
	return easyDict




# This function simply picks a word at random.
# Its input is a dictionary list.
# Its output is a random word from the list.
def randomWord(dictionary):
	return random.choice(dictionary)



# This function has an input of a word, in string format.
# It keeps valid whitespace characters as-is.
# It replaces all alphabetical characters with underscores.
# It returns each character with a space inbetween.
def redact(word):
	redacted = ""
	iterator = 0
	for grapheme in list(word):
		if iterator == 0:
			if grapheme == " " or grapheme == "-":
				redacted += grapheme
			else:
				redacted += "_"
		else:
			if grapheme == " " or grapheme == "-":
				redacted += " " + grapheme
			else:
				redacted += " _"
		iterator += 1
	return redacted



# This function is a sister of redact.
# However, it does not redact the word.
# It just adds the whitespace and capitilizes
def extend(word):
	extended = ""
	iterator = 0
	word = word.upper()
	for grapheme in list(word):
		if iterator == 0:
			extended += grapheme
		else:
			extended += " " + grapheme
		iterator += 1
	return extended



# This function checks the turn number...
# ...and returns cute art based on it :)
def textArtist(turnNumber):
	return '\x1b[2J'



# This function reveals letters that are correctly guessed.
def revelation(guessedLtr, secretWord, publicWord, charsWrong):
	iterator = 0
	publicWord = list(publicWord)
	goodLetter = False
	for letter in secretWord:
		if letter == guessedLtr:
			publicWord[iterator] = letter
			goodLetter = True
		iterator += 2
	publicWord = ''.join(publicWord)
	if goodLetter:
		charsWrong -= 1
	return [publicWord, charsWrong]



# This function  will take an input from a user.
# It needs to be one letter long.
# It also must be a alphabetical character.
def userLetter(letterList):
	invalid = True
	guessed = False
	while invalid:
		guessedLtr = input("INPUT LETTER: ").upper()
		if len(guessedLtr) == 1:
			if guessedLtr.isalpha():
				for letter in letterList:
					if letter == guessedLtr:
						guessed = True
				if guessed:
					print("You already guessed that letter! Try again.")
					guessed = False
				else:
					invalid = False
			else:
				print("That's not a letter! Try again.")
		else:
			print("You need to input a single letter! Try again.")
	return guessedLtr



# This function will take in one number from the user.
# It needs to be greater than or equal to 1.
# It also cannot be blank.
def userNumber():
	invalid = True
	while invalid:
		wordLength = input("INPUT NUMBER: ")
		if len(wordLength) > 0:
			if wordLength.isdigit():
				wordLength = float(wordLength)
				if wordLength.is_integer():
					invalid = False
				else:
					print("That's not a whole number! Try again.")
			else:
				print("That's not even a number! Try again.")
		else:
			print("You need to input a number! Try again.")
	return wordLength



# This function takes the input of a secret word, public word, and an array of letters used
# It checks the length of the array for turns used.
# It displays a space-man depending on the turns used.
# It displays the public word, which has been redacted.
# It displays used letters.
# It displays turns remaining.
# Finally, it calls another function to ask for a letter.
def turn(secretWord, publicWord, letterList, charsWrong):
	turnNumber = len(letterList) + 1
	charsWrong = charsWrong + 1
	print(textArtist(turnNumber))
	print("LETTERS USED: " + str(letterList))
	print("CURRENT WORD: " + publicWord)

	if charsWrong >= 8:
		extendGame = False
		print("THE SOLUTION: " + extend(secretWord))
		print("= GAME OVER =")

	else:
		extendGame = True
		print("GUESSES LEFT: " + str(7 - charsWrong))
		print("ROUND NUMBER: " + str(turnNumber))
		guessedLtr = userLetter(letterList)
		revealings = revelation(guessedLtr, secretWord, publicWord, charsWrong)
		publicWord = revealings[0]
		charsWrong = revealings[1]
		letterList += guessedLtr

	if publicWord == extend(secretWord):
		print()
		print("CURRENT WORD: " + publicWord)
		print("THE SOLUTION: " + extend(secretWord))
		print('YOU WON GAME!')
		extendGame = False

	return([publicWord, letterList, extendGame, charsWrong])



# This function will start the space-man game.
# It has no input, but can use options to browse different dictionaries.
# It runs until the player has lost or won.
def spaceWoman():
	# Choose dictionary.
	dictionary = dictionary_primary
	# Clean the dictionary.
	dictionary = dctCleaner(dictionary)
	# Input maximum length.
	print('''Space Woman can be a very difficult game!
To make it easier, type the maximum number
of letters your random word can have...''')
	difficulty = userNumber()
	# Filter dictionary to max length.
	dictionary = easier(dictionary, difficulty)
	# Pick a random word from dictionary.
	secretWord = randomWord(dictionary).upper()
	# Create a string of underscores to show player .
	publicWord = redact(secretWord)
	# Create an empty array, representing letters guessed.
	letterList = []
	# This is the meat of the turn.
	extendGame = True
	# You start with no incorrect guesses.
	charsWrong = 0
	while extendGame:
		turnResult = turn(secretWord, publicWord, letterList, charsWrong)
		publicWord = turnResult[0]
		letterList = turnResult[1]
		extendGame = turnResult[2]
		charsWrong = turnResult[3]

spaceWoman()
