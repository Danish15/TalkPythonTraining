import random


print('-----------------------------------')
print('GUESS THAT NUMBER GAME')
print('-----------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1
name = input("Player what is your name?")

while guess != the_number:
	guess_text = input('Guess a number between 0 and 100: ')
	guess = int(guess_text)

	if guess < the_number:
		print('sorry {1} guess of {0} was too LOW.'.format(guess,name))
	elif guess > the_number:
		print('sorry {1} guess of {0} was too HIGH.'.format(guess,name))
	else:
		print('you win, excellent work {0} it was {1}!'.format(name,guess))

print('done')