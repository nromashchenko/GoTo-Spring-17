
answer = "Хуммельс"
word = '_'*len(answer)

left = len(answer)

while left > 0:
    answer_letters = list(answer)
    print(answer_letters)

    word_letters = list(word)
    print(word_letters)


    letter = input()


    for i in range(len(answer_letters)):
        if answer_letters[i] == letter:
            word_letters[i] = letter
            left -= 1
    answer = "".join(answer_letters)
    word = "".join(word_letters)

print("win")