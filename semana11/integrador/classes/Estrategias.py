from abc import ABC, abstractmethod
from contextlib import closing
import sqlite3
import csv


class Estrategia(ABC):
    """
    Classe Base para as estratégias (algoritmos)

    """
    @abstractmethod
    def execute(self, dados):
        """ Método em que o algoritmo é contido.
        Implementação do algoritmo na classe filha deve
        sobreescrever este método."""
        pass

    @abstractmethod
    def parametros_necessarios(self):
        """Sobreescrever este método para que retorne uma tupla
        com a lista de parâmetros necessários.
        Exemplo:
        ('algoritmo', 'dbname', 'host', 'user', 'password')
        """
        pass

    @abstractmethod
    def nome(self):
        """Sobreescrever este método para que
        retorne o nome do algoritmo utilizado."""
        pass


class Estrategia_SQLite(Estrategia):
    def execute(self, dados):
        lista_registros = []
        db = dados['db']
        with closing(sqlite3.connect(db)) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vendas;")
            for linha in cursor.fetchall():
                lista_registros.append(linha)
        return lista_registros

    def parametros_necessarios(self):
        return ('algoritmo', 'db')

    def nome(self):
        return 'Algoritmo SQLite'


class Estrategia_CSV(Estrategia):
    def execute(self, dados):
        lista_registros = []
        arquivo = dados['arquivo']
        with open(arquivo, newline='\n') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                lista_registros.append(line)
        return lista_registros

    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')

    def nome(self):
        return 'Algoritmo CSV'


class Estrategia_Texto1(Estrategia):
    def execute(self, dados):
        lista_registros = []
        arquivo = dados['arquivo']
        with open(arquivo, newline='\n') as txtfile:
            reader = csv.reader(txtfile)
            for line in reader:
                replaced = line[0].replace('       ',';')
                splitted = replaced.split(';')
                try:
                    data = splitted[0].strip()
                    valor = splitted[3].strip()
                    produto = splitted[-1].replace('\n', '').strip()
                    dados = (produto, valor, data)
                    lista_registros.append(dados)
                except IndexError:
                    continue

        return lista_registros

    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')

    def nome(self):
        return 'Algoritmo TXT'


class Estrategia_Texto2(Estrategia):
    def execute(self, dados):
        lista_registros = []
        arquivo = dados['arquivo']
        with open(arquivo, newline='\n') as txtfile:
            reader = csv.reader(txtfile)
            for line in reader:
                replaced = line[0].replace('       ',';')
                splitted = replaced.split(';')
                try:
                    data = splitted[0].strip()
                    valor = splitted[2].strip()
                    produto = splitted[1].strip()
                    dados = (produto, valor, data)
                    lista_registros.append(dados)
                except IndexError:
                    continue

        return lista_registros

    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')

    def nome(self):
        return 'Algoritmo TXT'