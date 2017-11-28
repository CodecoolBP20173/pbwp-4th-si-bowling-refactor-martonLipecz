def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        current_game_point = get_value(game[i])
        if game[i] == '/':
            result += current_game_point - last_game_point
        else:
            result += current_game_point

        if frame < 10 and current_game_point == 10:
            next_game_point = get_value(game[i + 1])
            if game[i] == '/':
                result += next_game_point
            elif game[i] in ('x', 'X'):
                result += next_game_point
                if game[i + 2] == '/':
                    result += 10 - next_game_point
                else:
                    result += get_value(game[i + 2])

        last_game_point = current_game_point
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
