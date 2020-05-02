import random as r


def get_char_index(in_word, in_char):
    char_nums = in_word.count(in_char)
    indexes = []
    index = 0
    for i in range(0, char_nums):
        if index < len(in_word) - 1:
            index = in_word.index(in_char, index + i)
            indexes.append(index)
    return indexes


def hide_word(in_word):
    hidden_word = ''
    for i in range(0, len(in_word)):
        hidden_word = hidden_word + '-'
    return hidden_word


def unmask_char(hidden_word, unhidden_char, char_positions):
    hidden_word = list(hidden_word)
    for i in char_positions:
        hidden_word[i] = unhidden_char
    return ''.join(hidden_word)


def game(w_list):
    word = r.choice(w_list)
    char_set = set(word)
    p_word = hide_word(word)

    attempts = 8
    wrong_letters = set()
    while attempts > 0:
        answer = str(input(f"\n{p_word}\nInput a letter: "))

        if len(answer) > 1:
            print("You should print a single letter")

        elif not answer.isalpha() or not answer.islower():
            print("It is not an ASCII lowercase letter")


        elif answer in char_set:
            answer_indexes = get_char_index(word, answer)
            p_word = unmask_char(p_word, answer, answer_indexes)
            char_set.remove(answer)

            if p_word == word:
                print(f"\n{word}\nYou guessed the word!\nYou survived!")
                break

        elif answer not in char_set and (answer in p_word) or (answer in wrong_letters):
            print("You already typed this letter")
            # attempts -= 1

        else:
            print('No such letter in the word')
            wrong_letters.add(answer)
            attempts -= 1

        if attempts == 0:
            print("You are hanged!")
            break


print("H A N G M A N")

word_list = ['python', 'java', 'kotlin', 'javascript']

while True:
    menu_choice = ((str(input('Type "play" to play the game, "exit" to quit:'))).strip()).lower()
    if menu_choice == 'play':
        game(word_list)
        break
    elif menu_choice == 'exit':
        break
    else:
        pass
