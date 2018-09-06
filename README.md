# CS-1-1_space-man

# Pseudocode
1. Have a list or object prepared.
2. Randomly (and secretly) get an item from that list.
	- Declare a 'secret string' variable hidden from the player.
	- Declare a 'progress string' variable, set to a number of underscores equal to the length of secret word.
	- If there are any spaces, they are revealed to the player. in progress string.
3. Display terminal UI to player.
	- includes CURRENT WORD
	- includes REMAINING GUESSES
	- includes MISSED LETTERS
	- * includes ASCII ART
4. Ask player for an input.
5. Check if input is valid.
	- If input is not 1 letter in length, it is invalid.
	- If input is not an english letter, it is invalid.
	- If letter has been input already, it is invalid.
	- If letter is invalid, then display an error.
	- If letter is invalid, then go back to step 4.
6. Search for the input in the secret string.
	- For every match, update progress string to reveal the letters.
	- Append input letter to a list, so that step-5 can refer to them.
7. If there are no matches...
	- then update the failure counter.
	- check if the player has lost.
8. If there is a match...
	- check if the player has won.
9. Loop back to step 3 until player has won or lost.
