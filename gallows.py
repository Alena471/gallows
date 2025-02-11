import random

def get_random_word():
    """
    Функция выбирает случайное слово из списка.
    """
    words = ["python", "разработка", "виселица", "программирование", "код", "алгоритм", "функция", "переменная"]
    return random.choice(words)

def display_hangman(tries):
    """
    Функция возвращает текущее состояние рисунка виселицы в зависимости от оставшихся попыток.
    Индексы списка соответствуют количеству оставшихся попыток:
      6 - пустые виселица,
      5 - добавлена голова,
      4 - добавлено тело,
      3 - добавлена одна рука,
      2 - добавлены обе руки,
      1 - добавлена одна нога,
      0 - добавлена вторая нога (проигрыш).
    """
    stages = [
        # 0 попыток - полное изображение виселицы (проигрыш)
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # 1 попытка
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # 2 попытки
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        # 3 попытки
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |      
           -
        """,
        # 4 попытки
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |      
           -
        """,
        # 5 попыток
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # 6 попыток - начальное состояние (ничего не нарисовано)
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]

def play_hangman():
    """
    Основная функция игры «Виселица».
    """
    word = get_random_word()
    word_completion = "_" * len(word)  # строка с символами "_" для отображения неоткрытых букв
    guessed = False                   # флаг, угадано ли слово
    guessed_letters = []              # список уже названных букв
    guessed_words = []                # список уже названных слов
    tries = 6                         # количество попыток (начинаем с 6)

    print("Давайте сыграем в Виселицу!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    # Пока слово не угадано и есть оставшиеся попытки
    while not guessed and tries > 0:
        guess = input("Угадайте букву или слово: ").lower()
        if len(guess) == 1 and guess.isalpha():
            # Если пользователь ввёл одну букву
            if guess in guessed_letters:
                print(f"Вы уже называли букву '{guess}'.")
            elif guess not in word:
                print(f"Буквы '{guess}' нет в слове.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Отлично! Буква '{guess}' присутствует в слове.")
                guessed_letters.append(guess)
                # Обновляем отображение угаданных букв
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            # Если пользователь пытается угадать всё слово
            if guess in guessed_words:
                print(f"Вы уже называли слово '{guess}'.")
            elif guess != word:
                print(f"Слово '{guess}' неверное.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Некорректный ввод. Попробуйте снова.")
        
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    
    # Вывод результата игры
    if guessed:
        print("Поздравляем, вы угадали слово! Вы победили!")
    else:
        print(f"К сожалению, вы проиграли. Загаданное слово было: '{word}'.")

def main():
    """
    Функция для запуска игры и предложения сыграть ещё раз.
    """
    play_hangman()
    while input("Хотите сыграть ещё раз? (Y/N): ").upper() == "Y":
        play_hangman()

if __name__ == "__main__":
    main()
