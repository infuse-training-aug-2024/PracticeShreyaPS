import csv
import os
score_file='UserStory2\scores.csv'
class GuessingGame:
    def __init__(self, secret_word, lives):
        self.secret_word = secret_word
        self.lives = lives
        self.display = ['?' for _ in range(len(secret_word))]  
        
    def is_guess_match(self, guess):
        return guess == self.secret_word

    def is_char_present(self, guess):
        found = False
        for j in range(len(self.secret_word)):
            for k in range(len(guess)):
                if guess[k] == self.secret_word[j]:
                    self.display[j] = guess[k]
                    found = True
        return found

    def show_status(self):
        print(self.display)
        print("Lives left:", self.lives)

    def view_score(self,username):
        try:

            file_exists = os.path.isfile(score_file)
            rows = []
            isNameExisting=False
            if file_exists:
                with open(score_file, 'r', newline='') as file:
                    reader = csv.reader(file)
                    rows = list(reader)
                for row in rows:
                    if row and row[0] == username:
                        isNameExisting=True
                        print("your score:",row[1])
                        break
                if(isNameExisting==False):
                    print("no scores yet")
        except FileNotFoundError:
            print("file not found")

        

    def update_csv(self, username):
        try:
            file_exists = os.path.isfile(score_file)
            updated = False
            rows = []
            if file_exists:
                with open(score_file, 'r', newline='') as file:
                    reader = csv.reader(file)
                    rows = list(reader)
                for row in rows:
                    if row and row[0] == username:
                        row[1] = str(self.lives)
                        updated = True
                        break

            if not updated:
                rows.append([username, str(self.lives)])

            with open(score_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)

        except FileNotFoundError:
            print("file not found")

    def play(self,username):
        try:

            while self.lives != 0:
                guess = input("Enter your guess: ")
                if not isinstance(guess,int) :
                    raise TypeError("enter valid integer")

                guess_list = list(guess)

                if self.is_guess_match(guess_list):
                    self.update_csv(username)
                    print("You won!")
                    break

                elif self.is_char_present(guess_list):
                    self.show_status()
                    if self.display == list(self.secret_word):
                        self.update_csv(username)
                        print("You won!")
                        break
                else:
                    print("Wrong guess\n")
                    self.lives -= 1
                    self.show_status()

            if self.lives == 0:
                self.update_csv(username)
                print("You lost!")

        except Exception as e:
            print("encontered error:",e)

def read_secret_word_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            secret_word = file.read().strip()
            return list(secret_word)  
    except FileNotFoundError:
        print("Error: Secret word file not found!")
        return None
    



def take_choice(choice, game):
    if choice == '1':
        game.view_score(userName)
        pass
    elif choice == '2':
        game.play(userName)
    else:
        print("Invalid choice")


userName = input("Enter your name: ")
print("---------enter 1 to view score---------")
print("---------enter 2 to play game---------")

secret_word_list = read_secret_word_from_file('UserStory2\secret_word.txt') 

if secret_word_list:
    game = GuessingGame(secret_word_list, 3)  
    take_choice(input(), game)
