import sqlite3


class Word:

    def __init__(self, connection, cursor) -> None:
        """
        :param connection: Take a connection from data_base_decorator argument "connection"
        :param cursor: Take a cursor from data_base_decorator argument "cursor"
        """
        self.connection = connection
        self.cursor = cursor

    def add_word(self, word: str) -> str:
        """
        :param word: The word for translating
        :return: String that told the user that the addition was successful
        """
        word = word.capitalize()

        with self.connection:
            self.cursor.execute("INSERT INTO words VALUES (:base_word ,:translated_word)",
                                {"base_word": word, "translated_word": "Word"})

        self.cursor.execute("SELECT * FROM words WHERE base_word=:base_word",
                            {"base_word": word})

        return f"Dodano pomyślnie słówko {list(self.cursor.fetchone())[0]}," \
               f" tłumaczenie:{list(self.cursor.fetchone())[1]}"

    def edit_word(self, row_value: str, old_data_value: str, new_data_value: str) -> str:
        """
        :param row_value: Name of data base row 'base_word' or 'translated_word'
        :param old_data_value: Actual value for chosen data
        :param new_data_value: New value for chosen data
        :return: String that told the user that the edition was successful
        """
        new_data_value = old_data_value.capitalize()

        self.cursor.execute("SELECT * FROM words")
        if old_data_value in self.cursor.fetchall()[0] or self.cursor.fetchall()[1]:
            with self.connection:
                self.cursor.execute(f"UPDATE words SET {row_value}= :new_data WHERE :old_data ",
                                    {"new_data": new_data_value, "old_data": old_data_value})

            self.cursor.execute(f"SELECT * FROM words WHERE {row_value}= :base_word",
                                {"base_word": new_data_value})

            return f"Wartość {old_data_value}, została zmieniona na: {new_data_value}"

        else:
            return "Podana wartość nie znajduje się w bazie słówek!"

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
