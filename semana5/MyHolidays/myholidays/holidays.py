import datetime


class MyCalendar:

    # Converte string para datas se for válido, se não for válido, zera o campo
    def convertdate(self, args):
        if type(args) == str:
            try:
                args = datetime.datetime.strptime(args, '%d/%m/%Y').date()
            except ValueError:
                args = 0
        return args

    def __init__(self, *args):
        self.datas = []
        self.temp = []

        # Adiciona a data em uma lista self.temporária
        for dt in args:
            self.temp.append(self.convertdate(dt))

        # Lê as datas da lista temp e adiciona somente os valores válidos
        for dt in self.temp:
            if type(dt) != int and type(dt) != list and type(dt) != tuple:
                self.datas.append(self.convertdate(dt))

    def add_holiday(self, *args):

        # Adiciona a data em uma lista self.temporária sem duplicar
        for dt in args:
            if self.convertdate(dt) not in self.temp:
                self.temp.append(self.convertdate(dt))

        # Lê as datas da lista temp e adiciona somente os valores válidos
        for dt in self.temp:
            if self.convertdate(dt) not in self.datas and type(dt) != int:
                self.datas.append(self.convertdate(dt))

    def check_holiday(self, args):
        if self.convertdate(args) in self.datas:
            print(args)
            isholiday = True
        else:
            isholiday = False

        return isholiday
