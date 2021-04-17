import sqlite3


class Word:

    def __init__(self, word, cursor):
        """

        :param word: Take a word from user
        :param cursor: Take a cursor from @data_base_decorator argument "cursor"
        """
        self.word = word
        self.cursor = cursor

    def word_valid(self):
        return True

    def add_word(self) -> None:
        if self.word_valid():
            pass

    def edit_word(self) -> None:
        pass

    def delete_word(self) -> None:
        pass


class Manual_Translate:
    pass


class Automatic_Translate:
    pass


def data_base_decorator(func):
    """This decorator open and close connection with sqlite3 data base
    :param - func, have two arguments it's 'cursor' and 'connection' from data base
    """
    def wrapper():
        connection = sqlite3.connect("Local_words.db")
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS words (base_word TEXT,
                        translated_word TEXT)""")
        func(connection, cursor)
        connection.close()

    return wrapper
