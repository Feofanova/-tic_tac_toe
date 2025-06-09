# Объявить клаcc
from gameparts import Board
from gameparts.exceptions import FieldIndexError, CellOccupiedError


def main():
    game = Board()
# Отрисовать поле в терминале.
    current_player = 'X'
    running = True
    game.display()

    while running:
        print(f'Ход делают {current_player}')
        while True:
            try:
                row = int(input('Введите номер строки:'))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца:'))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue
            except ValueError:
                print('Буквы вводить нельзя, только числа.')
                print('Пожалуйста, введите значения для строки и столбца заново')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break
# Разместить на поле символ по указанным координатам - сделать ход.
        game.make_move(row, column, current_player)
# Перерисовать поле с учётом сделанного хода.
        game.display()
# Создать игровое поле - объект класса Board.
        current_player = '0' if current_player == 'X' else 'X'

if __name__ == '__main__':
    main()
    