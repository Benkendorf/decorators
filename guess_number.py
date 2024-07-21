from datetime import datetime as dt
from random import randint

from access_control import access_control
from constants import ADMIN_USERNAME, UNKNOWN_COMMAND


class NumberGame():
    def __init__(self) -> None:
        self.start_time = dt.now()
        self.username = self.get_username()
        self.total_games = 0

    @access_control
    def get_statistics(self, *args, **kwargs) -> None:
        game_time = dt.now() - self.start_time
        print(f'Общее время игры: {game_time}, '
              f'текущая игра - №{self.total_games}')

    @access_control
    def get_right_answer(self, *args, **kwargs) -> None:
        print(f'Правильный ответ: {self.number}')

    def check_number(self, guess: int) -> bool:
        # Если число угадано...
        if guess == self.number:
            print(f'Отличная интуиция, {self.username}! Вы угадали число :)')
            # ...возвращаем True
            return True

        if guess < self.number:
            print('Ваше число меньше того, что загадано.')
        else:
            print('Ваше число больше того, что загадано.')
        return False

    def game(self) -> None:
        # Получаем случайное число в диапазоне от 1 до 100.
        self.number = randint(1, 100)
        print(
            '\nУгадайте число от 1 до 100.\n'
            'Для выхода из текущей игры введите команду "stop"'
        )
        while True:
            # Получаем пользовательский ввод,
            # отрезаем лишние пробелы и переводим в нижний регистр.
            user_input = input('Введите число или команду: ').strip().lower()

            if user_input == 'stop':
                break
            elif user_input == 'stat':
                self.get_statistics()
            elif user_input == 'answer':
                self.get_right_answer()
            else:
                try:
                    guess = int(user_input)
                except ValueError:
                    print(UNKNOWN_COMMAND)
                    continue

                if self.check_number(guess):
                    break

    def get_username(self) -> str:
        username = input('Представьтесь, пожалуйста, как Вас зовут?\n').strip()
        if username == ADMIN_USERNAME:
            print(
                '\nДобро пожаловать, создатель! '
                'Во время игры вам доступны команды "stat", "answer"'
            )
        else:
            print(f'\n{username}, добро пожаловать в игру!')
        return username

    def guess_number(self) -> None:
        # username = get_username()
        # Счётчик игр в текущей сессии.

        while True:
            self.total_games += 1
            self.game()
            play_again = input('\nХотите сыграть ещё? (yes/no) ')
            if play_again.strip().lower() not in ('y', 'yes'):
                break


if __name__ == '__main__':
    print(
        'Вас приветствует игра "Угадай число"!\n'
        'Для выхода нажмите Ctrl+C'
    )
    new_game = NumberGame()
    new_game.guess_number()
