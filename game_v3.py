"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""


import numpy as np


def random_predict(number: int = 1) -> int:
    count = 0
    max_value = 100
    min_value = 0
    check_number = max_value

    while check_number != number:
        count += 1
        # print(check_number, end = '')
        if check_number > number:
            max_value = check_number
            check_number = min_value + (max_value-min_value)//2
            # print(' > ', number, ', new check_number = ',check_number)
        else:
            # print(check_number, end = '')
            min_value = check_number
            check_number = min_value + (max_value-min_value)//2
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
