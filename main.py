import sys
from random import choice

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QPushButton, QLabel


def isendgame(xs, os):
    # функция проверяет закончена ли игра
    if 1 in xs and 2 in xs and 3 in xs:
        return True
    elif 4 in xs and 5 in xs and 6 in xs:
        return True
    elif 7 in xs and 8 in xs and 9 in xs:
        return True
    elif 1 in xs and 4 in xs and 7 in xs:
        return True
    elif 2 in xs and 5 in xs and 8 in xs:
        return True
    elif 3 in xs and 6 in xs and 9 in xs:
        return True
    elif 1 in xs and 5 in xs and 9 in xs:
        return True
    elif 3 in xs and 5 in xs and 7 in xs:
        return True
    elif 1 in os and 2 in os and 3 in os:
        return True
    elif 4 in os and 5 in os and 6 in os:
        return True
    elif 7 in os and 8 in os and 9 in os:
        return True
    elif 1 in os and 4 in os and 7 in os:
        return True
    elif 2 in os and 5 in os and 8 in os:
        return True
    elif 3 in os and 6 in os and 9 in os:
        return True
    elif 1 in os and 5 in os and 9 in os:
        return True
    elif 3 in os and 5 in os and 7 in os:
        return True


class Choser(QMainWindow):  # класс, отвечающий за окно выбора режима игры
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Крестики нолики')
        self.helloword = QLabel(self)
        self.helloword.setText('Крестики Нолики!')
        self.helloword.resize(self.helloword.sizeHint())
        self.helloword.move(110, 20)
        self.chooseword = QLabel(self)
        self.chooseword.setText('Выберите режим игры:')
        self.chooseword.resize(self.chooseword.sizeHint())
        self.chooseword.move(95, 45)
        self.one = QLabel(self)
        self.one.setText('Одиночный:')
        self.one.resize(self.one.sizeHint())
        self.one.move(122, 65)
        self.two = QLabel(self)
        self.two.setText('Многопользовательский:')
        self.two.resize(self.two.sizeHint())
        self.two.move(93, 110)
        self.easy = QPushButton(self)
        self.easy.setText('Лёгкий')
        self.easy.resize(70, 25)
        self.easy.move(40, 80)
        self.easy.id = 1  # Каждая кнопка здесь имеет свой id, чтобы игра понимала какой режим запускать
        self.normal = QPushButton(self)
        self.normal.setText('Средний')
        self.normal.resize(70, 25)
        self.normal.move(120, 80)
        self.normal.id = 2
        self.hard = QPushButton(self)
        self.hard.setText('Сложный')
        self.hard.resize(70, 25)
        self.hard.move(200, 80)
        self.hard.id = 3
        self.double = QPushButton(self)
        self.double.setText('На Двоих')
        self.double.resize(90, 25)
        self.double.move(110, 125)
        self.double.id = 0
        self.easy.clicked.connect(self.start_game)
        self.normal.clicked.connect(self.start_game)
        self.hard.clicked.connect(self.start_game)
        self.double.clicked.connect(self.start_game)

    def start_game(self):
        # Функция отвечает за переход в окно игры
        gamemode = self.sender().id
        self.second_form = TicTacToe(gamemode)
        self.second_form.show()


class TicTacToe(QWidget):
    def __init__(self, gamemode):
        super().__init__()
        self.initUI(gamemode)

    def initUI(self, gamemode):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Крестики нолики')
        self.gamemode = gamemode  # Передаём id режима игры с кнопки в атрибут
        self.cnt = 0  # Инициализируем счётчик количества игр
        self.ep = 0  # Инициализируем так называемый счёт

        self.games = QLabel(self)
        self.games.setText(f"Игр сыграно: {self.cnt}")
        self.games.move(90, 10)

        self.exp = QLabel(self)
        self.exp.setText(f"Счёт: {self.ep}")
        self.exp.move(30, 10)

        self.b1 = QPushButton(self)
        self.b1.resize(50, 50)
        self.b1.move(30, 50)
        self.b1.id = 1  # Каждая кнопка здесь также имеет свой id

        self.b2 = QPushButton(self)
        self.b2.resize(50, 50)
        self.b2.move(80, 50)
        self.b2.id = 2

        self.b3 = QPushButton(self)
        self.b3.resize(50, 50)
        self.b3.move(130, 50)
        self.b3.id = 3

        self.b4 = QPushButton(self)
        self.b4.resize(50, 50)
        self.b4.move(30, 100)
        self.b4.id = 4

        self.b5 = QPushButton(self)
        self.b5.resize(50, 50)
        self.b5.move(80, 100)
        self.b5.id = 5

        self.b6 = QPushButton(self)
        self.b6.resize(50, 50)
        self.b6.move(130, 100)
        self.b6.id = 6

        self.b7 = QPushButton(self)
        self.b7.resize(50, 50)
        self.b7.move(30, 150)
        self.b7.id = 7

        self.b8 = QPushButton(self)
        self.b8.resize(50, 50)
        self.b8.move(80, 150)
        self.b8.id = 8

        self.b9 = QPushButton(self)
        self.b9.resize(50, 50)
        self.b9.move(130, 150)
        self.b9.id = 9

        self.new_game = QPushButton(self)
        self.new_game.move(60, 220)
        self.new_game.resize(90, 25)
        self.new_game.id = 0  # И даже кнопка "Новая игра", чтобы режим, в котором ИИ нападает работал корректно
        self.new_game.setText('Новая игра')

        self.win = QLabel(self)
        self.win.move(70, 250)

        self.whose = QLabel(self)
        self.whose.setText('Первыми ходят: Крестики')
        self.whose.move(40, 35)
        self.whose.resize(self.whose.sizeHint())

        '''self.test = QLabel(self)
        self.test.move(250, 250)'''  # временный автрибут, выводивший правильность действий ИИ

        self.b1.clicked.connect(self.tic)
        self.b2.clicked.connect(self.tic)
        self.b3.clicked.connect(self.tic)
        self.b4.clicked.connect(self.tic)
        self.b5.clicked.connect(self.tic)
        self.b6.clicked.connect(self.tic)
        self.b7.clicked.connect(self.tic)
        self.b8.clicked.connect(self.tic)
        self.b9.clicked.connect(self.tic)
        self.new_game.clicked.connect(self.reset)
        self.new_game.clicked.connect(self.tic)

        self.cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Список всех клеток, в которые можно поставить крестик или нолик
        self.xs, self.os = list(), list()  # Списки клеток, в которые были поставлены крестики или нолики
        self.turns = 0  # Счётчик ходов за игру
        self.attack = -1  # Атрибут, показывающий нападает ИИ или защищается
        self.right = 0  # Атрибут, который указывает ИИ правильное действие делать или нет
        self.who = 1  # Атрибут, указывающий кто ставит знак для режима "На двоих"

    def reset(self):
        # Функция сбрасывающая игру, возвращающая все атрибуты к исходным значениям (кроме счёта и счётчика игр)
        self.b1.setText('')
        self.b2.setText('')
        self.b3.setText('')
        self.b4.setText('')
        self.b5.setText('')
        self.b6.setText('')
        self.b7.setText('')
        self.b8.setText('')
        self.b9.setText('')
        self.cnt += 1  # Увеличивает значение счётчика игр
        self.games.setText(f"Игр сыграно: {self.cnt}")
        self.games.resize(self.games.sizeHint())
        self.cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.turns = 0
        self.xs.clear()
        self.os.clear()
        self.win.setText('')
        self.attack = -self.attack  # А вот показатель "Атаки" он меняет на противоположный
        self.who = 1

    def tic(self):
        # Функция, отвечающая непосредственно за игровой процесс
        if self.attack == -1:  # Сначала пишем, кто ходит первым
            if self.who == 1:
                self.whose.setText('Первыми ходят: Крестики')
                self.whose.move(40, 35)
            else:
                self.whose.setText('Первыми ходят: Нолики')
                self.whose.move(40, 35)
        else:
            if self.who == -1:
                self.whose.setText('Первыми ходят: Крестики')
                self.whose.move(40, 35)
            else:
                self.whose.setText('Первыми ходят: Нолики')
                self.whose.move(40, 35)
        if self.gamemode == 1:  # После, в зависимости от режима игры выбираем правильность хода ИИ
            self.right = choice([0, 0, 0, 1])  # Лёгкий - 25%, что бот поступит правильно
        elif self.gamemode == 2:
            self.right = choice([0, 1])  # Средний - 50%
        elif self.gamemode == 3:
            self.right = 1  # Сложный - 100%
        '''self.test.setText(f'{self.right}')'''
        if self.gamemode == 0:  # А вот если режим "На двоих", запускаем отдельный алгоритм
            if self.attack == -1:  # Смотрим, кто ходит первым
                if self.who == 1:
                    if self.sender().id in self.cells and not isendgame(self.xs, self.os):
                        # Даём первому поставить в выбранную клетку
                        myturn = self.sender().id
                        self.cells.pop(self.cells.index(myturn))
                        self.xs.append(myturn)
                        if myturn == 1:
                            self.b1.setText('X')
                        elif myturn == 2:
                            self.b2.setText('X')
                        elif myturn == 3:
                            self.b3.setText('X')
                        elif myturn == 4:
                            self.b4.setText('X')
                        elif myturn == 5:
                            self.b5.setText('X')
                        elif myturn == 6:
                            self.b6.setText('X')
                        elif myturn == 7:
                            self.b7.setText('X')
                        elif myturn == 8:
                            self.b8.setText('X')
                        else:
                            self.b9.setText('X')
                        if isendgame(self.xs, self.os):  # Проверяем на предмет конца игры всвязи с победой
                            self.win.setText('Крестики Выиграли!')
                            self.whose.setText('Игра окончена!')
                            self.whose.move(64, 35)
                            self.win.resize(self.win.sizeHint())
                            self.win.move(53, 250)
                            return 0
                        if len(self.cells) == 0:  # Или тем, что клетки закончились
                            self.win.setText('Ничья!')
                            self.whose.setText('Игра окончена!')
                            self.whose.move(64, 35)
                            self.win.resize(self.win.sizeHint())
                            self.win.move(90, 250)
                            return 0
                        self.who = -self.who  # Передаём ход следующему
                        self.whose.setText('Сейчас ходят: Нолики')
                        self.whose.move(43, 35)
                elif self.who == -1:  # Теперь ставит нолик
                    if self.sender().id in self.cells and not isendgame(self.xs, self.os):
                        myturn = self.sender().id
                        self.cells.pop(self.cells.index(myturn))
                        self.os.append(myturn)
                        if myturn == 1:
                            self.b1.setText('O')
                        elif myturn == 2:
                            self.b2.setText('O')
                        elif myturn == 3:
                            self.b3.setText('O')
                        elif myturn == 4:
                            self.b4.setText('O')
                        elif myturn == 5:
                            self.b5.setText('O')
                        elif myturn == 6:
                            self.b6.setText('O')
                        elif myturn == 7:
                            self.b7.setText('O')
                        elif myturn == 8:
                            self.b8.setText('O')
                        else:
                            self.b9.setText('O')
                        if isendgame(self.xs, self.os):
                            self.win.setText('Нолики Выиграли!')
                            self.whose.setText('Игра окончена!')
                            self.whose.move(64, 35)
                            self.win.resize(self.win.sizeHint())
                            self.win.move(58, 250)
                            return 0
                        if len(self.cells) == 0:
                            self.win.setText('Ничья!')
                            self.whose.setText('Игра окончена!')
                            self.whose.move(64, 35)
                            self.win.resize(self.win.sizeHint())
                            self.win.move(90, 250)
                            return 0
                        self.who = -self.who
                        self.whose.setText('Сейчас ходят: Крестики')
                        self.whose.move(43, 35)
            else:  # А это то же самое, но теперь первым ходит нолик, а не крестик
                if self.who == -1:
                    if self.sender().id in self.cells and not isendgame(self.xs, self.os):
                        myturn = self.sender().id
                        self.cells.pop(self.cells.index(myturn))
                        self.xs.append(myturn)
                        if myturn == 1:
                            self.b1.setText('X')
                        elif myturn == 2:
                            self.b2.setText('X')
                        elif myturn == 3:
                            self.b3.setText('X')
                        elif myturn == 4:
                            self.b4.setText('X')
                        elif myturn == 5:
                            self.b5.setText('X')
                        elif myturn == 6:
                            self.b6.setText('X')
                        elif myturn == 7:
                            self.b7.setText('X')
                        elif myturn == 8:
                            self.b8.setText('X')
                        else:
                            self.b9.setText('X')
                        if isendgame(self.xs, self.os):
                            self.win.setText('Крестики Выиграли!')
                            self.whose.setText('Игра окончена!')
                            self.whose.move(64, 35)
                            self.win.resize(self.win.sizeHint())
                            self.win.move(53, 250)
                            return 0
                        if len(self.cells) == 0:
                            self.win.setText('Ничья!')
                            self.whose.setText('Игра окончена!')
                            self.whose.move(64, 35)
                            self.win.resize(self.win.sizeHint())
                            self.win.move(90, 250)
                            return 0
                        self.who = -self.who
                        self.whose.setText('Сейчас ходят: Нолики')
                        self.whose.move(43, 35)
                elif self.who == 1:
                    if self.sender().id in self.cells and not isendgame(self.xs, self.os):
                        myturn = self.sender().id
                        self.cells.pop(self.cells.index(myturn))
                        self.os.append(myturn)
                        if myturn == 1:
                            self.b1.setText('O')
                        elif myturn == 2:
                            self.b2.setText('O')
                        elif myturn == 3:
                            self.b3.setText('O')
                        elif myturn == 4:
                            self.b4.setText('O')
                        elif myturn == 5:
                            self.b5.setText('O')
                        elif myturn == 6:
                            self.b6.setText('O')
                        elif myturn == 7:
                            self.b7.setText('O')
                        elif myturn == 8:
                            self.b8.setText('O')
                        else:
                            self.b9.setText('O')
                        if isendgame(self.xs, self.os):
                            self.win.setText('Нолики Выиграли!')
                            self.win.move(58, 250)
                            self.whose.setText('Игра окончена!')
                            self.whose.move(64, 35)
                            self.win.resize(self.win.sizeHint())
                            return 0
                        if len(self.cells) == 0:
                            self.win.setText('Ничья!')
                            self.whose.setText('Игра окончена!')
                            self.whose.move(64, 35)
                            self.win.resize(self.win.sizeHint())
                            self.win.move(90, 250)
                            return 0
                        self.who = -self.who
                        self.whose.setText('Сейчас ходят: Крестики')
                        self.whose.move(43, 35)

        else:  # А этот алгоритм отвечает за игру с ИИ
            if self.attack == -1:  # Если атакует игрок, то:
                if self.sender().id in self.cells and not isendgame(self.xs, self.os):  # Проверяем его адекватность
                    self.sender().setText('X')  # Даём ему поставить крестик
                    self.turns += 1
                    self.cells.pop(self.cells.index(self.sender().id))
                    self.xs.append(self.sender().id)
                    if isendgame(self.xs, self.os):  # Проверяем
                        self.win.setText('Вы выиграли!')
                        self.win.resize(self.win.sizeHint())
                        self.win.move(70, 250)
                        self.ep += 1
                        self.exp.setText(f"Счёт: {self.ep}")
                        return 0
                    if len(self.cells) == 0:
                        self.win.setText('Ничья!')
                        self.win.resize(self.win.sizeHint())
                        self.win.move(90, 250)
                        return 0
                    # Начинаем защищаться
                    if self.turns == 1:
                        if self.right == 1:  # Правильный первый ход очень важен в игре, его рассматриваем отдельно
                            if self.sender().id == 5:
                                myturn = choice([1, 3, 7, 9])
                                self.cells.pop(self.cells.index(myturn))
                                self.os.append(myturn)
                                if myturn == 1:
                                    self.b1.setText('O')
                                elif myturn == 3:
                                    self.b3.setText('O')
                                elif myturn == 7:
                                    self.b7.setText('O')
                                else:
                                    self.b9.setText('O')
                            else:
                                self.cells.pop(self.cells.index(5))
                                self.os.append(5)
                                self.b5.setText('O')
                        else:  # Ну или ставим в случайную клетку, если так велит режим игры
                            myturn = choice(self.cells)
                            self.cells.pop(self.cells.index(myturn))
                            self.os.append(myturn)
                            if myturn == 1:
                                self.b1.setText('O')
                            elif myturn == 2:
                                self.b2.setText('O')
                            elif myturn == 3:
                                self.b3.setText('O')
                            elif myturn == 4:
                                self.b4.setText('O')
                            elif myturn == 5:
                                self.b5.setText('O')
                            elif myturn == 6:
                                self.b6.setText('O')
                            elif myturn == 7:
                                self.b7.setText('O')
                            elif myturn == 8:
                                self.b8.setText('O')
                            else:
                                self.b9.setText('O')
                    else:  # Проверяем, можем ли мы закончить игру прямо сейчас и делаем это если можем
                        if 1 in self.os and 2 in self.os and 3 not in self.os and 3 not in self.xs:
                            self.cells.pop(self.cells.index(3))
                            self.os.append(3)
                            self.b3.setText('O')
                        elif 2 in self.os and 3 in self.os and 1 not in self.os and 1 not in self.xs:
                            self.cells.pop(self.cells.index(1))
                            self.os.append(1)
                            self.b1.setText('O')
                        elif 1 in self.os and 3 in self.os and 2 not in self.os and 2 not in self.xs:
                            self.cells.pop(self.cells.index(2))
                            self.os.append(2)
                            self.b2.setText('O')
                        elif 4 in self.os and 5 in self.os and 6 not in self.os and 6 not in self.xs:
                            self.cells.pop(self.cells.index(6))
                            self.os.append(6)
                            self.b6.setText('O')
                        elif 4 in self.os and 6 in self.os and 5 not in self.os and 5 not in self.xs:
                            self.cells.pop(self.cells.index(5))
                            self.os.append(5)
                            self.b5.setText('O')
                        elif 5 in self.os and 6 in self.os and 4 not in self.os and 4 not in self.xs:
                            self.cells.pop(self.cells.index(4))
                            self.os.append(4)
                            self.b4.setText('O')
                        elif 7 in self.os and 8 in self.os and 9 not in self.os and 9 not in self.xs:
                            self.cells.pop(self.cells.index(9))
                            self.os.append(9)
                            self.b9.setText('O')
                        elif 7 in self.os and 9 in self.os and 8 not in self.os and 8 not in self.xs:
                            self.cells.pop(self.cells.index(8))
                            self.os.append(8)
                            self.b8.setText('O')
                        elif 8 in self.os and 9 in self.os and 7 not in self.os and 7 not in self.xs:
                            self.cells.pop(self.cells.index(7))
                            self.os.append(7)
                            self.b7.setText('O')
                        elif 1 in self.os and 4 in self.os and 7 not in self.os and 7 not in self.xs:
                            self.cells.pop(self.cells.index(7))
                            self.os.append(7)
                            self.b7.setText('O')
                        elif 1 in self.os and 7 in self.os and 4 not in self.os and 4 not in self.xs:
                            self.cells.pop(self.cells.index(4))
                            self.os.append(4)
                            self.b4.setText('O')
                        elif 4 in self.os and 7 in self.os and 1 not in self.os and 1 not in self.xs:
                            self.cells.pop(self.cells.index(1))
                            self.os.append(1)
                            self.b1.setText('O')
                        elif 2 in self.os and 5 in self.os and 8 not in self.os and 8 not in self.xs:
                            self.cells.pop(self.cells.index(8))
                            self.os.append(8)
                            self.b8.setText('O')
                        elif 2 in self.os and 8 in self.os and 5 not in self.os and 5 not in self.xs:
                            self.cells.pop(self.cells.index(5))
                            self.os.append(5)
                            self.b5.setText('O')
                        elif 5 in self.os and 8 in self.os and 2 not in self.os and 2 not in self.xs:
                            self.cells.pop(self.cells.index(2))
                            self.os.append(2)
                            self.b2.setText('O')
                        elif 3 in self.os and 6 in self.os and 9 not in self.os and 9 not in self.xs:
                            self.cells.pop(self.cells.index(9))
                            self.os.append(9)
                            self.b9.setText('O')
                        elif 3 in self.os and 9 in self.os and 6 not in self.os and 6 not in self.xs:
                            self.cells.pop(self.cells.index(6))
                            self.os.append(6)
                            self.b6.setText('O')
                        elif 6 in self.os and 9 in self.os and 3 not in self.os and 3 not in self.xs:
                            self.cells.pop(self.cells.index(3))
                            self.os.append(3)
                            self.b3.setText('O')
                        elif 1 in self.os and 5 in self.os and 9 not in self.os and 9 not in self.xs:
                            self.cells.pop(self.cells.index(9))
                            self.os.append(9)
                            self.b9.setText('O')
                        elif 1 in self.os and 9 in self.os and 5 not in self.os and 5 not in self.xs:
                            self.cells.pop(self.cells.index(5))
                            self.os.append(5)
                            self.b5.setText('O')
                        elif 5 in self.os and 9 in self.os and 1 not in self.os and 1 not in self.xs:
                            self.cells.pop(self.cells.index(1))
                            self.os.append(1)
                            self.b1.setText('O')
                        elif 3 in self.os and 5 in self.os and 7 not in self.os and 7 not in self.xs:
                            self.cells.pop(self.cells.index(7))
                            self.os.append(7)
                            self.b7.setText('O')
                        elif 7 in self.os and 5 in self.os and 3 not in self.os and 3 not in self.xs:
                            self.cells.pop(self.cells.index(3))
                            self.os.append(3)
                            self.b3.setText('O')
                        elif 3 in self.os and 7 in self.os and 5 not in self.os and 5 not in self.xs:
                            self.cells.pop(self.cells.index(5))
                            self.os.append(5)
                            self.b5.setText('O')
                        # Проверяем не нужно ли нам экстренно защищаться, и делаем это если надо
                        elif 1 in self.xs and 2 in self.xs and 3 not in self.os:
                            self.cells.pop(self.cells.index(3))
                            self.os.append(3)
                            self.b3.setText('O')
                        elif 2 in self.xs and 3 in self.xs and 1 not in self.os:
                            self.cells.pop(self.cells.index(1))
                            self.os.append(1)
                            self.b1.setText('O')
                        elif 1 in self.xs and 3 in self.xs and 2 not in self.os:
                            self.cells.pop(self.cells.index(2))
                            self.os.append(2)
                            self.b2.setText('O')
                        elif 4 in self.xs and 5 in self.xs and 6 not in self.os:
                            self.cells.pop(self.cells.index(6))
                            self.os.append(6)
                            self.b6.setText('O')
                        elif 4 in self.xs and 6 in self.xs and 5 not in self.os:
                            self.cells.pop(self.cells.index(5))
                            self.os.append(5)
                            self.b5.setText('O')
                        elif 5 in self.xs and 6 in self.xs and 4 not in self.os:
                            self.cells.pop(self.cells.index(4))
                            self.os.append(4)
                            self.b4.setText('O')
                        elif 7 in self.xs and 8 in self.xs and 9 not in self.os:
                            self.cells.pop(self.cells.index(9))
                            self.os.append(9)
                            self.b9.setText('O')
                        elif 7 in self.xs and 9 in self.xs and 8 not in self.os:
                            self.cells.pop(self.cells.index(8))
                            self.os.append(8)
                            self.b8.setText('O')
                        elif 8 in self.xs and 9 in self.xs and 7 not in self.os:
                            self.cells.pop(self.cells.index(7))
                            self.os.append(7)
                            self.b7.setText('O')
                        elif 1 in self.xs and 4 in self.xs and 7 not in self.os:
                            self.cells.pop(self.cells.index(7))
                            self.os.append(7)
                            self.b7.setText('O')
                        elif 1 in self.xs and 7 in self.xs and 4 not in self.os:
                            self.cells.pop(self.cells.index(4))
                            self.os.append(4)
                            self.b4.setText('O')
                        elif 4 in self.xs and 7 in self.xs and 1 not in self.os:
                            self.cells.pop(self.cells.index(1))
                            self.os.append(1)
                            self.b1.setText('O')
                        elif 2 in self.xs and 5 in self.xs and 8 not in self.os:
                            self.cells.pop(self.cells.index(8))
                            self.os.append(8)
                            self.b8.setText('O')
                        elif 2 in self.xs and 8 in self.xs and 5 not in self.os:
                            self.cells.pop(self.cells.index(5))
                            self.os.append(5)
                            self.b5.setText('O')
                        elif 5 in self.xs and 8 in self.xs and 2 not in self.os:
                            self.cells.pop(self.cells.index(2))
                            self.os.append(2)
                            self.b2.setText('O')
                        elif 3 in self.xs and 6 in self.xs and 9 not in self.os:
                            self.cells.pop(self.cells.index(9))
                            self.os.append(9)
                            self.b9.setText('O')
                        elif 3 in self.xs and 9 in self.xs and 6 not in self.os:
                            self.cells.pop(self.cells.index(6))
                            self.os.append(6)
                            self.b6.setText('O')
                        elif 6 in self.xs and 9 in self.xs and 3 not in self.os:
                            self.cells.pop(self.cells.index(3))
                            self.os.append(3)
                            self.b3.setText('O')
                        elif 1 in self.xs and 5 in self.xs and 9 not in self.os:
                            self.cells.pop(self.cells.index(9))
                            self.os.append(9)
                            self.b9.setText('O')
                        elif 1 in self.xs and 9 in self.xs and 5 not in self.os:
                            self.cells.pop(self.cells.index(5))
                            self.os.append(5)
                            self.b5.setText('O')
                        elif 5 in self.xs and 9 in self.xs and 1 not in self.os:
                            self.cells.pop(self.cells.index(1))
                            self.os.append(1)
                            self.b1.setText('O')
                        elif 3 in self.xs and 5 in self.xs and 7 not in self.os:
                            self.cells.pop(self.cells.index(7))
                            self.os.append(7)
                            self.b7.setText('O')
                        elif 7 in self.xs and 5 in self.xs and 3 not in self.os:
                            self.cells.pop(self.cells.index(3))
                            self.os.append(3)
                            self.b3.setText('O')
                        elif 3 in self.xs and 7 in self.xs and 5 not in self.os:
                            self.cells.pop(self.cells.index(5))
                            self.os.append(5)
                            self.b5.setText('O')
                        elif self.turns == 2:  # Если не нужно защищаться, то второй ход тоже рассматриваем отдельно
                            if self.right == 1:  # Поступаем правильно
                                if 5 in self.xs:
                                    if 1 in self.cells:
                                        self.cells.pop(self.cells.index(1))
                                        self.os.append(1)
                                        self.b1.setText('O')
                                    elif 3 in self.cells:
                                        self.cells.pop(self.cells.index(3))
                                        self.os.append(3)
                                        self.b3.setText('O')
                                    elif 7 in self.cells:
                                        self.cells.pop(self.cells.index(7))
                                        self.os.append(7)
                                        self.b7.setText('O')
                                    elif 9 in self.cells:
                                        self.cells.pop(self.cells.index(9))
                                        self.os.append(9)
                                        self.b9.setText('O')
                                else:
                                    if 2 in self.cells and 8 not in self.xs:
                                        self.cells.pop(self.cells.index(2))
                                        self.os.append(2)
                                        self.b2.setText('O')
                                    elif 4 in self.cells and 6 not in self.xs:
                                        self.cells.pop(self.cells.index(4))
                                        self.os.append(4)
                                        self.b4.setText('O')
                                    elif 6 in self.cells and 4 not in self.xs:
                                        self.cells.pop(self.cells.index(6))
                                        self.os.append(6)
                                        self.b6.setText('O')
                                    elif 8 in self.cells and 2 not in self.xs:
                                        self.cells.pop(self.cells.index(8))
                                        self.os.append(8)
                                        self.b8.setText('O')
                                    elif 2 in self.xs and 4 in self.xs:
                                        myturn = choice([1, 3, 7])
                                        self.cells.pop(self.cells.index(myturn))
                                        self.os.append(myturn)
                                        if myturn == 1:
                                            self.b1.setText('O')
                                        elif myturn == 3:
                                            self.b3.setText('O')
                                        else:
                                            self.b7.setText('O')
                                    elif 8 in self.xs and 4 in self.xs:
                                        myturn = choice([1, 9, 7])
                                        self.cells.pop(self.cells.index(myturn))
                                        self.os.append(myturn)
                                        if myturn == 1:
                                            self.b1.setText('O')
                                        elif myturn == 9:
                                            self.b9.setText('O')
                                        else:
                                            self.b7.setText('O')
                                    elif 2 in self.xs and 6 in self.xs:
                                        myturn = choice([1, 3, 9])
                                        self.cells.pop(self.cells.index(myturn))
                                        self.os.append(myturn)
                                        if myturn == 1:
                                            self.b1.setText('O')
                                        elif myturn == 3:
                                            self.b3.setText('O')
                                        else:
                                            self.b9.setText('O')
                                    elif 6 in self.xs and 8 in self.xs:
                                        myturn = choice([9, 3, 7])
                                        self.cells.pop(self.cells.index(myturn))
                                        self.os.append(myturn)
                                        if myturn == 9:
                                            self.b9.setText('O')
                                        elif myturn == 3:
                                            self.b3.setText('O')
                                        else:
                                            self.b7.setText('O')
                            else:  # Или случайно
                                myturn = choice(self.cells)
                                self.cells.pop(self.cells.index(myturn))
                                self.os.append(myturn)
                                if myturn == 1:
                                    self.b1.setText('O')
                                elif myturn == 2:
                                    self.b2.setText('O')
                                elif myturn == 3:
                                    self.b3.setText('O')
                                elif myturn == 4:
                                    self.b4.setText('O')
                                elif myturn == 5:
                                    self.b5.setText('O')
                                elif myturn == 6:
                                    self.b6.setText('O')
                                elif myturn == 7:
                                    self.b7.setText('O')
                                elif myturn == 8:
                                    self.b8.setText('O')
                                else:
                                    self.b9.setText('O')
                        else:  # В противном случае ставим нолик в случайную клетку
                            myturn = choice(self.cells)
                            self.cells.pop(self.cells.index(myturn))
                            self.os.append(myturn)
                            if myturn == 1:
                                self.b1.setText('O')
                            elif myturn == 2:
                                self.b2.setText('O')
                            elif myturn == 3:
                                self.b3.setText('O')
                            elif myturn == 4:
                                self.b4.setText('O')
                            elif myturn == 5:
                                self.b5.setText('O')
                            elif myturn == 6:
                                self.b6.setText('O')
                            elif myturn == 7:
                                self.b7.setText('O')
                            elif myturn == 8:
                                self.b8.setText('O')
                            else:
                                self.b9.setText('O')

                    if isendgame(self.xs, self.os):  # Проверяем на предмет конца игры
                        self.win.setText('Вы проиграли!')
                        self.win.resize(self.win.sizeHint())
                        self.win.move(70, 250)
                        return 0
                    if len(self.cells) == 0:
                        self.win.setText('Ничья!')
                        self.win.resize(self.win.sizeHint())
                        self.win.move(90, 250)
            else:  # Режим, в котором ИИ атакует
                if self.sender().id in self.cells and not isendgame(self.xs, self.os) or self.sender().id == 0:
                    if self.turns > 0:  # Изначально счётчик ходов показывает 0
                        myturn = self.sender().id
                        self.cells.pop(self.cells.index(myturn))
                        self.xs.append(myturn)
                        if myturn == 1:
                            self.b1.setText('X')
                        elif myturn == 2:
                            self.b2.setText('X')
                        elif myturn == 3:
                            self.b3.setText('X')
                        elif myturn == 4:
                            self.b4.setText('X')
                        elif myturn == 5:
                            self.b5.setText('X')
                        elif myturn == 6:
                            self.b6.setText('X')
                        elif myturn == 7:
                            self.b7.setText('X')
                        elif myturn == 8:
                            self.b8.setText('X')
                        else:
                            self.b9.setText('X')
                        if isendgame(self.xs, self.os):
                            self.win.setText('Вы Выиграли!')
                            self.whose.setText('Игра окончена!')
                            self.whose.move(64, 35)
                            self.win.resize(self.win.sizeHint())
                            self.win.move(70, 250)
                            return 0
                        if len(self.cells) == 0:
                            self.win.setText('Ничья!')
                            self.whose.setText('Игра окончена!')
                            self.whose.move(64, 35)
                            self.win.resize(self.win.sizeHint())
                            self.win.move(90, 250)
                            return 0
                    self.turns += 1
                    if self.turns == 1:  # Обрабатываем дебют
                        if self.right == 1:
                            myturn = choice([1, 3, 7, 9, 5])  # Правильный
                        else:
                            myturn = choice([2, 4, 6, 8])  # И не правильный
                        self.cells.pop(self.cells.index(myturn))
                        self.os.append(myturn)
                        if myturn == 1:
                            self.b1.setText('O')
                        elif myturn == 2:
                            self.b2.setText('O')
                        elif myturn == 3:
                            self.b3.setText('O')
                        elif myturn == 4:
                            self.b4.setText('O')
                        elif myturn == 5:
                            self.b5.setText('O')
                        elif myturn == 6:
                            self.b6.setText('O')
                        elif myturn == 7:
                            self.b7.setText('O')
                        elif myturn == 8:
                            self.b8.setText('O')
                        else:
                            self.b9.setText('O')

                    elif self.turns == 2:
                        if self.right == 1:  # В соответсвии с первым ходом делаем правильный второй
                            if 5 in self.os:
                                if 1 in self.cells and 9 not in self.xs:
                                    self.cells.pop(self.cells.index(1))
                                    self.os.append(1)
                                    self.b1.setText('O')
                                elif 3 in self.cells and 7 not in self.xs:
                                    self.cells.pop(self.cells.index(3))
                                    self.os.append(3)
                                    self.b3.setText('O')
                                elif 7 in self.cells and 3 not in self.xs:
                                    self.cells.pop(self.cells.index(7))
                                    self.os.append(7)
                                    self.b7.setText('O')
                                elif 9 in self.cells and 1 not in self.xs:
                                    self.cells.pop(self.cells.index(9))
                                    self.os.append(9)
                                    self.b9.setText('O')
                            elif 1 in self.os:
                                if 9 in self.cells:
                                    self.cells.pop(self.cells.index(9))
                                    self.os.append(9)
                                    self.b9.setText('O')
                                else:
                                    myturn = choice([3, 7])
                                    self.cells.pop(self.cells.index(myturn))
                                    self.os.append(myturn)
                                    if myturn == 3:
                                        self.b3.setText('O')
                                    else:
                                        self.b7.setText('O')
                            elif 3 in self.os:
                                if 7 in self.cells:
                                    self.cells.pop(self.cells.index(7))
                                    self.os.append(7)
                                    self.b7.setText('O')
                                else:
                                    myturn = choice([1, 9])
                                    self.cells.pop(self.cells.index(myturn))
                                    self.os.append(myturn)
                                    if myturn == 1:
                                        self.b1.setText('O')
                                    else:
                                        self.b9.setText('O')
                            elif 7 in self.os:
                                if 3 in self.cells:
                                    self.cells.pop(self.cells.index(3))
                                    self.os.append(3)
                                    self.b3.setText('O')
                                else:
                                    myturn = choice([1, 9])
                                    self.cells.pop(self.cells.index(myturn))
                                    self.os.append(myturn)
                                    if myturn == 1:
                                        self.b1.setText('O')
                                    else:
                                        self.b9.setText('O')
                            elif 9 in self.os:
                                if 1 in self.cells:
                                    self.cells.pop(self.cells.index(1))
                                    self.os.append(1)
                                    self.b1.setText('O')
                                else:
                                    myturn = choice([3, 7])
                                    self.cells.pop(self.cells.index(myturn))
                                    self.os.append(myturn)
                                    if myturn == 3:
                                        self.b3.setText('O')
                                    else:
                                        self.b7.setText('O')
                            else:
                                myturn = choice(self.cells)
                                self.cells.pop(self.cells.index(myturn))
                                self.os.append(myturn)
                                if myturn == 1:
                                    self.b1.setText('O')
                                elif myturn == 2:
                                    self.b2.setText('O')
                                elif myturn == 3:
                                    self.b3.setText('O')
                                elif myturn == 4:
                                    self.b4.setText('O')
                                elif myturn == 5:
                                    self.b5.setText('O')
                                elif myturn == 6:
                                    self.b6.setText('O')
                                elif myturn == 7:
                                    self.b7.setText('O')
                                elif myturn == 8:
                                    self.b8.setText('O')
                                else:
                                    self.b9.setText('O')
                        else:  # Или не очень правильный
                            myturn = choice(self.cells)
                            self.cells.pop(self.cells.index(myturn))
                            self.os.append(myturn)
                            if myturn == 1:
                                self.b1.setText('O')
                            elif myturn == 2:
                                self.b2.setText('O')
                            elif myturn == 3:
                                self.b3.setText('O')
                            elif myturn == 4:
                                self.b4.setText('O')
                            elif myturn == 5:
                                self.b5.setText('O')
                            elif myturn == 6:
                                self.b6.setText('O')
                            elif myturn == 7:
                                self.b7.setText('O')
                            elif myturn == 8:
                                self.b8.setText('O')
                            else:
                                self.b9.setText('O')
                    # Заканчиваем игру, если можем
                    elif 1 in self.os and 2 in self.os and 3 not in self.os and 3 not in self.xs:
                        self.cells.pop(self.cells.index(3))
                        self.os.append(3)
                        self.b3.setText('O')
                    elif 2 in self.os and 3 in self.os and 1 not in self.os and 1 not in self.xs:
                        self.cells.pop(self.cells.index(1))
                        self.os.append(1)
                        self.b1.setText('O')
                    elif 1 in self.os and 3 in self.os and 2 not in self.os and 2 not in self.xs:
                        self.cells.pop(self.cells.index(2))
                        self.os.append(2)
                        self.b2.setText('O')
                    elif 4 in self.os and 5 in self.os and 6 not in self.os and 6 not in self.xs:
                        self.cells.pop(self.cells.index(6))
                        self.os.append(6)
                        self.b6.setText('O')
                    elif 4 in self.os and 6 in self.os and 5 not in self.os and 5 not in self.xs:
                        self.cells.pop(self.cells.index(5))
                        self.os.append(5)
                        self.b5.setText('O')
                    elif 5 in self.os and 6 in self.os and 4 not in self.os and 4 not in self.xs:
                        self.cells.pop(self.cells.index(4))
                        self.os.append(4)
                        self.b4.setText('O')
                    elif 7 in self.os and 8 in self.os and 9 not in self.os and 9 not in self.xs:
                        self.cells.pop(self.cells.index(9))
                        self.os.append(9)
                        self.b9.setText('O')
                    elif 7 in self.os and 9 in self.os and 8 not in self.os and 8 not in self.xs:
                        self.cells.pop(self.cells.index(8))
                        self.os.append(8)
                        self.b8.setText('O')
                    elif 8 in self.os and 9 in self.os and 7 not in self.os and 7 not in self.xs:
                        self.cells.pop(self.cells.index(7))
                        self.os.append(7)
                        self.b7.setText('O')
                    elif 1 in self.os and 4 in self.os and 7 not in self.os and 7 not in self.xs:
                        self.cells.pop(self.cells.index(7))
                        self.os.append(7)
                        self.b7.setText('O')
                    elif 1 in self.os and 7 in self.os and 4 not in self.os and 4 not in self.xs:
                        self.cells.pop(self.cells.index(4))
                        self.os.append(4)
                        self.b4.setText('O')
                    elif 4 in self.os and 7 in self.os and 1 not in self.os and 1 not in self.xs:
                        self.cells.pop(self.cells.index(1))
                        self.os.append(1)
                        self.b1.setText('O')
                    elif 2 in self.os and 5 in self.os and 8 not in self.os and 8 not in self.xs:
                        self.cells.pop(self.cells.index(8))
                        self.os.append(8)
                        self.b8.setText('O')
                    elif 2 in self.os and 8 in self.os and 5 not in self.os and 5 not in self.xs:
                        self.cells.pop(self.cells.index(5))
                        self.os.append(5)
                        self.b5.setText('O')
                    elif 5 in self.os and 8 in self.os and 2 not in self.os and 2 not in self.xs:
                        self.cells.pop(self.cells.index(2))
                        self.os.append(2)
                        self.b2.setText('O')
                    elif 3 in self.os and 6 in self.os and 9 not in self.os and 9 not in self.xs:
                        self.cells.pop(self.cells.index(9))
                        self.os.append(9)
                        self.b9.setText('O')
                    elif 3 in self.os and 9 in self.os and 6 not in self.os and 6 not in self.xs:
                        self.cells.pop(self.cells.index(6))
                        self.os.append(6)
                        self.b6.setText('O')
                    elif 6 in self.os and 9 in self.os and 3 not in self.os and 3 not in self.xs:
                        self.cells.pop(self.cells.index(3))
                        self.os.append(3)
                        self.b3.setText('O')
                    elif 1 in self.os and 5 in self.os and 9 not in self.os and 9 not in self.xs:
                        self.cells.pop(self.cells.index(9))
                        self.os.append(9)
                        self.b9.setText('O')
                    elif 1 in self.os and 9 in self.os and 5 not in self.os and 5 not in self.xs:
                        self.cells.pop(self.cells.index(5))
                        self.os.append(5)
                        self.b5.setText('O')
                    elif 5 in self.os and 9 in self.os and 1 not in self.os and 1 not in self.xs:
                        self.cells.pop(self.cells.index(1))
                        self.os.append(1)
                        self.b1.setText('O')
                    elif 3 in self.os and 5 in self.os and 7 not in self.os and 7 not in self.xs:
                        self.cells.pop(self.cells.index(7))
                        self.os.append(7)
                        self.b7.setText('O')
                    elif 7 in self.os and 5 in self.os and 3 not in self.os and 3 not in self.xs:
                        self.cells.pop(self.cells.index(3))
                        self.os.append(3)
                        self.b3.setText('O')
                    elif 3 in self.os and 7 in self.os and 5 not in self.os and 5 not in self.xs:
                        self.cells.pop(self.cells.index(5))
                        self.os.append(5)
                        self.b5.setText('O')
                    # Защищаемся
                    elif 1 in self.xs and 2 in self.xs and 3 not in self.os:
                        self.cells.pop(self.cells.index(3))
                        self.os.append(3)
                        self.b3.setText('O')
                    elif 2 in self.xs and 3 in self.xs and 1 not in self.os:
                        self.cells.pop(self.cells.index(1))
                        self.os.append(1)
                        self.b1.setText('O')
                    elif 1 in self.xs and 3 in self.xs and 2 not in self.os:
                        self.cells.pop(self.cells.index(2))
                        self.os.append(2)
                        self.b2.setText('O')
                    elif 4 in self.xs and 5 in self.xs and 6 not in self.os:
                        self.cells.pop(self.cells.index(6))
                        self.os.append(6)
                        self.b6.setText('O')
                    elif 4 in self.xs and 6 in self.xs and 5 not in self.os:
                        self.cells.pop(self.cells.index(5))
                        self.os.append(5)
                        self.b5.setText('O')
                    elif 5 in self.xs and 6 in self.xs and 4 not in self.os:
                        self.cells.pop(self.cells.index(4))
                        self.os.append(4)
                        self.b4.setText('O')
                    elif 7 in self.xs and 8 in self.xs and 9 not in self.os:
                        self.cells.pop(self.cells.index(9))
                        self.os.append(9)
                        self.b9.setText('O')
                    elif 7 in self.xs and 9 in self.xs and 8 not in self.os:
                        self.cells.pop(self.cells.index(8))
                        self.os.append(8)
                        self.b8.setText('O')
                    elif 8 in self.xs and 9 in self.xs and 7 not in self.os:
                        self.cells.pop(self.cells.index(7))
                        self.os.append(7)
                        self.b7.setText('O')
                    elif 1 in self.xs and 4 in self.xs and 7 not in self.os:
                        self.cells.pop(self.cells.index(7))
                        self.os.append(7)
                        self.b7.setText('O')
                    elif 1 in self.xs and 7 in self.xs and 4 not in self.os:
                        self.cells.pop(self.cells.index(4))
                        self.os.append(4)
                        self.b4.setText('O')
                    elif 4 in self.xs and 7 in self.xs and 1 not in self.os:
                        self.cells.pop(self.cells.index(1))
                        self.os.append(1)
                        self.b1.setText('O')
                    elif 2 in self.xs and 5 in self.xs and 8 not in self.os:
                        self.cells.pop(self.cells.index(8))
                        self.os.append(8)
                        self.b8.setText('O')
                    elif 2 in self.xs and 8 in self.xs and 5 not in self.os:
                        self.cells.pop(self.cells.index(5))
                        self.os.append(5)
                        self.b5.setText('O')
                    elif 5 in self.xs and 8 in self.xs and 2 not in self.os:
                        self.cells.pop(self.cells.index(2))
                        self.os.append(2)
                        self.b2.setText('O')
                    elif 3 in self.xs and 6 in self.xs and 9 not in self.os:
                        self.cells.pop(self.cells.index(9))
                        self.os.append(9)
                        self.b9.setText('O')
                    elif 3 in self.xs and 9 in self.xs and 6 not in self.os:
                        self.cells.pop(self.cells.index(6))
                        self.os.append(6)
                        self.b6.setText('O')
                    elif 6 in self.xs and 9 in self.xs and 3 not in self.os:
                        self.cells.pop(self.cells.index(3))
                        self.os.append(3)
                        self.b3.setText('O')
                    elif 1 in self.xs and 5 in self.xs and 9 not in self.os:
                        self.cells.pop(self.cells.index(9))
                        self.os.append(9)
                        self.b9.setText('O')
                    elif 1 in self.xs and 9 in self.xs and 5 not in self.os:
                        self.cells.pop(self.cells.index(5))
                        self.os.append(5)
                        self.b5.setText('O')
                    elif 5 in self.xs and 9 in self.xs and 1 not in self.os:
                        self.cells.pop(self.cells.index(1))
                        self.os.append(1)
                        self.b1.setText('O')
                    elif 3 in self.xs and 5 in self.xs and 7 not in self.os:
                        self.cells.pop(self.cells.index(7))
                        self.os.append(7)
                        self.b7.setText('O')
                    elif 7 in self.xs and 5 in self.xs and 3 not in self.os:
                        self.cells.pop(self.cells.index(3))
                        self.os.append(3)
                        self.b3.setText('O')
                    elif 3 in self.xs and 7 in self.xs and 5 not in self.os:
                        self.cells.pop(self.cells.index(5))
                        self.os.append(5)
                        self.b5.setText('O')
                    elif self.turns == 3:  # Третий ход тоже может быть очень важен, так что его тоже отдельно
                        if self.right == 1:
                            if 5 in self.os:
                                if 1 in self.os:
                                    if 4 not in self.os:
                                        self.cells.pop(self.cells.index(7))
                                        self.os.append(7)
                                        self.b7.setText('O')
                                    else:
                                        self.cells.pop(self.cells.index(3))
                                        self.os.append(3)
                                        self.b3.setText('O')
                                elif 3 in self.os:
                                    if 2 not in self.os:
                                        self.cells.pop(self.cells.index(1))
                                        self.os.append(1)
                                        self.b1.setText('O')
                                    else:
                                        self.cells.pop(self.cells.index(9))
                                        self.os.append(9)
                                        self.b9.setText('O')
                                elif 7 in self.os:
                                    if 4 not in self.os:
                                        self.cells.pop(self.cells.index(1))
                                        self.os.append(1)
                                        self.b1.setText('O')
                                    else:
                                        self.cells.pop(self.cells.index(9))
                                        self.os.append(9)
                                        self.b9.setText('O')
                                elif 9 in self.os:
                                    if 8 not in self.os:
                                        self.cells.pop(self.cells.index(7))
                                        self.os.append(7)
                                        self.b7.setText('O')
                                    else:
                                        self.cells.pop(self.cells.index(3))
                                        self.os.append(3)
                                        self.b3.setText('O')
                            else:
                                if 1 in self.os and 9 in self.os:
                                    if 3 not in self.xs:
                                        self.cells.pop(self.cells.index(3))
                                        self.os.append(3)
                                        self.b3.setText('O')
                                    else:
                                        self.cells.pop(self.cells.index(7))
                                        self.os.append(7)
                                        self.b7.setText('O')
                                elif 3 in self.os and 7 in self.os:
                                    if 1 not in self.xs:
                                        self.cells.pop(self.cells.index(1))
                                        self.os.append(1)
                                        self.b1.setText('O')
                                    else:
                                        self.cells.pop(self.cells.index(9))
                                        self.os.append(9)
                                        self.b9.setText('O')
                                elif 1 in self.os and 3 in self.os:
                                    if 7 in self.cells:
                                        self.cells.pop(self.cells.index(7))
                                        self.os.append(7)
                                        self.b7.setText('O')
                                    else:
                                        self.cells.pop(self.cells.index(9))
                                        self.os.append(9)
                                        self.b9.setText('O')
                                elif 9 in self.os and 3 in self.os:
                                    if 7 in self.cells:
                                        self.cells.pop(self.cells.index(7))
                                        self.os.append(7)
                                        self.b7.setText('O')
                                    else:
                                        self.cells.pop(self.cells.index(1))
                                        self.os.append(1)
                                        self.b1.setText('O')
                                elif 1 in self.os and 7 in self.os:
                                    if 3 in self.cells:
                                        self.cells.pop(self.cells.index(3))
                                        self.os.append(3)
                                        self.b3.setText('O')
                                    else:
                                        self.cells.pop(self.cells.index(9))
                                        self.os.append(9)
                                        self.b9.setText('O')
                                elif 7 in self.os and 9 in self.os:
                                    if 1 in self.cells:
                                        self.cells.pop(self.cells.index(1))
                                        self.os.append(1)
                                        self.b1.setText('O')
                                    else:
                                        self.cells.pop(self.cells.index(3))
                                        self.os.append(3)
                                        self.b3.setText('O')
                                else:
                                    myturn = choice(self.cells)
                                    self.cells.pop(self.cells.index(myturn))
                                    self.os.append(myturn)
                                    if myturn == 1:
                                        self.b1.setText('O')
                                    elif myturn == 2:
                                        self.b2.setText('O')
                                    elif myturn == 3:
                                        self.b3.setText('O')
                                    elif myturn == 4:
                                        self.b4.setText('O')
                                    elif myturn == 5:
                                        self.b5.setText('O')
                                    elif myturn == 6:
                                        self.b6.setText('O')
                                    elif myturn == 7:
                                        self.b7.setText('O')
                                    elif myturn == 8:
                                        self.b8.setText('O')
                                    else:
                                        self.b9.setText('O')
                        else:
                            myturn = choice(self.cells)
                            self.cells.pop(self.cells.index(myturn))
                            self.os.append(myturn)
                            if myturn == 1:
                                self.b1.setText('O')
                            elif myturn == 2:
                                self.b2.setText('O')
                            elif myturn == 3:
                                self.b3.setText('O')
                            elif myturn == 4:
                                self.b4.setText('O')
                            elif myturn == 5:
                                self.b5.setText('O')
                            elif myturn == 6:
                                self.b6.setText('O')
                            elif myturn == 7:
                                self.b7.setText('O')
                            elif myturn == 8:
                                self.b8.setText('O')
                            else:
                                self.b9.setText('O')
                    else:  # В противном случае ставим случайно
                        myturn = choice(self.cells)
                        self.cells.pop(self.cells.index(myturn))
                        self.os.append(myturn)
                        if myturn == 1:
                            self.b1.setText('O')
                        elif myturn == 2:
                            self.b2.setText('O')
                        elif myturn == 3:
                            self.b3.setText('O')
                        elif myturn == 4:
                            self.b4.setText('O')
                        elif myturn == 5:
                            self.b5.setText('O')
                        elif myturn == 6:
                            self.b6.setText('O')
                        elif myturn == 7:
                            self.b7.setText('O')
                        elif myturn == 8:
                            self.b8.setText('O')
                        else:
                            self.b9.setText('O')
                    if isendgame(self.xs, self.os):  # Проверяем
                        self.win.setText('Вы Проиграли!')
                        self.whose.setText('Игра окончена!')
                        self.whose.move(64, 35)
                        self.win.resize(self.win.sizeHint())
                        self.win.move(70, 250)
                        return 0
                    if len(self.cells) == 0:
                        self.win.setText('Ничья!')
                        self.whose.setText('Игра окончена!')
                        self.whose.move(64, 35)
                        self.win.resize(self.win.sizeHint())
                        self.win.move(90, 250)
                        return 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Choser()
    ex.show()
    sys.exit(app.exec())
