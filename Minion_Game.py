def minion_game(string):
    k_score = 0
    s_score = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    string = string.upper()
    substrings = []
    if string.isalpha():
        for element in range(0, len(string)):
            for next_element in range(0, element + 1):
                substrings.append(string[next_element:element + 1])

    print(substrings)

    for i in range(0, len(substrings)):
        if substrings[i][0] in vowels:
            k_score += 1
        else:
            s_score += 1
    if k_score > s_score:
        print('Kevin', k_score)
    elif k_score < s_score:
        print('Stuart', s_score)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
