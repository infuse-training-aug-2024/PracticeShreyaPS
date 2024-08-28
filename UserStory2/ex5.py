secret_word=['s','h','i','r','t']
display=['*','*','*','*','*']
lives=5
for i in range(5):
    print(display)
    guess=input("enter your guess: ")
    guess_list=list(guess)
    if(guess_list==secret_word):
        print("you won")
        break
    for j in range(len(secret_word)):
        if(guess==secret_word[j]):
            display[j]=guess
        
if(display==secret_word):
    print("you won")
else:
    print("you lost")
