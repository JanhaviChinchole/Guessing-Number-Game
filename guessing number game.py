#consider secreat number,guess limit,guess count as per our choice.
secreat_num=10
guess_limit =3
guess_count=0

while guess_count<guess_limit:
    guess = int(input("Enter guess: "))
    guess_count=guess_count+1
    if guess==secreat_num:
        print("you win!")
        break
    else:
        print("you loose!")
