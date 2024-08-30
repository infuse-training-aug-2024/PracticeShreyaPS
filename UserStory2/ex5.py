import json 

# class GuessingGame:
#     def __init__(self, secret_word, lives):
#         self.secret_word = secret_word
#         self.lives = lives
#         self.display = ['?','?','?','?','?']
        

#     def is_guess_match(self, guess):
#         return guess == self.secret_word

#     def is_char_present(self, guess):
#         found = False
#         for j in range(len(self.secret_word)):
#             for k in range(len(guess)):
#                 if guess[k] == self.secret_word[j]:
#                     self.display[j] = guess[k]
#                     found = True
#         return found

#     def show_status(self):
#         print(self.display)
#         print("Lives left:", self.lives)

#     def play(self):
#         while self.lives != 0:
#             guess = input("Enter your guess: ")
#             guess_list = list(guess)
            
#             if self.is_guess_match(guess_list):
#                 print("You won!")
#                 break

#             elif self.is_char_present(guess_list):
#                 self.show_status()
#                 if self.display == self.secret_word:
#                     print("You won!")
#                     break
#             else:
#                 print("Wrong guess\n")
#                 self.lives -= 1
#                 self.show_status()

#         if self.lives == 0:
#             print("You lost!")


# def take_choice(choice):
#     if(choice==1):
#         view_score()
#     else:
#         game.play()


# userName=input("Enter your name-")
# print("---------enter 1 to view score---------\n")
# print("---------enter 2 to play game---------\n")
# take_choice(input())
# game = GuessingGame(['s', 'h', 'i', 'r', 't'], 3)


	
# Python program to demonstrate 
# writing to CSV 
	
	
import csv

data = [
    {'name': 'Nikhil', 'score': 3}
]

with open('scores.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'score']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

