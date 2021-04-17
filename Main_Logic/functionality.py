import sqlite3


class Word:

    def __init__(self, word, connection, cursor):
        """

        :param word: Take a word from user
        :param connection: Take a connection from data_base_decorator argument "connection"
        :param cursor: Take a cursor from data_base_decorator argument "cursor"
        """
        self.word = word
        self.cursor = cursor
        self.connection = connection

    def word_valid(self):
        return True

    def add_word(self) -> str:
        if self.word_valid():
            with self.connection:
                self.cursor.execute("INSERT INTO words VALUES (:base_word ,:translated_word)",
                                    {"base_word": self.word, "translated_word": "Word"})

                self.cursor.execute("SELECT * FROM words WHERE base_word=:base_word",
                                    {"base_word":self.word})

            return f"Dodano pomyślnie słówko {list(self.cursor.fetchone())[0]}, tłumaczenie:{list(self.cursor.fetchone())[1]}"

        else:

            return "Nie udało się dodać słówka"

    def edit_word(self) -> None:
        pass

    def delete_word(self) -> None:
        pass


class Manual_Translate:
    pass


class Automatic_Translate:
    pass


def data_base_decorator(func):
    """This decorator open and close connection with sqlite3 data base \n
    :param func: Main(Core) function
    func take 2 arguments connection and cursor from sqlite3 data base
    """
    def wrapper():
        connection = sqlite3.connect("Local_words.db")
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS words (base_word TEXT,
                        translated_word TEXT)""")

        func(connection, cursor)
        connection.close()

    return wrapper
