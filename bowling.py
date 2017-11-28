def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):

        if game[i] == '/':
            result += get_value(game[i]) - last_game_point
        else:
            result += get_value(game[i])

        if frame < 10 and get_value(game[i]) == 10:
            if game[i] == '/':
                result += get_value(game[i + 1])
            elif game[i] == 'X' or game[i] == 'x':
                result += get_value(game[i + 1])
                if game[i + 2] == '/':
                    result += 10 - get_value(game[i + 1])
                else:
                    result += get_value(game[i + 2])

        last_game_point = get_value(game[i])
        if not in_first_half:
            frame += 1
        in_first_half = not in_first_half
        if game[i] == 'X' or game[i] == 'x':
            in_first_half = True
            frame += 1

    return result


def get_value(char):
    if char in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        return int(char)
    elif char == 'X' or char == 'x':
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
