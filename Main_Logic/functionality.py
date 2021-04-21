import sqlite3


def data_base_decorator(func):
    """This decorator open and close connection with sqlite3 data base. \n
    :param func: Main(Core) function.
    func take 2 arguments connection and cursor from sqlite3 data base.
    """

    def wrapper():
        connection = sqlite3.connect("Words.db")
        cursor = connection.cursor()

        func(connection, cursor)
        connection.close()

    return wrapper


class Word:

    def __init__(self, connection, cursor, base_language: str, foreign_language: str) -> None:
        """
        :param connection: Take a connection from data_base_decorator argument "connection".
        :param cursor: Take a cursor from data_base_decorator argument "cursor".
        :param base_language: It is a language from which the user translating.
        :param foreign_language: It is a language in which the user translating.
        """
        self.connection = connection
        self.cursor = cursor
        self.base_language = base_language.title()
        self.foreign_language = foreign_language.title()
        self.languages = self.base_language + "_" + self.foreign_language

        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self.languages} (base_word TEXT,
                        translated_word TEXT)""")

    def add_word(self, base_word: str, translated_word: str) -> str:
        """
        :param base_word: This is a word from first(base) language.
        :param translated_word: This is a word from second(foreign) language.
        :return: String that told the user that the addition was successful.
        """

        base_word = base_word.title()
        translated_word = translated_word.title()

        self.cursor.execute(f"SELECT base_word FROM {self.languages} WHERE base_word=:base_word",
                            {"base_word": base_word})

        if not self.cursor.fetchone():
            with self.connection:
                self.cursor.execute(f"INSERT INTO {self.languages} VALUES (:base_word ,:translated_word)",
                                    {"base_word": base_word, "translated_word": translated_word})

            return f"Pomyślnie dodano słówko '{base_word}' z tłumaczeniem:'{translated_word}'"

        else:
            return f"Podane słowo '{base_word}' oraz tłumaczenie '{translated_word}' znajduję się już w bazie słówek"

    def edit_word(self, row_value: str, old_data_value: str, new_data_value: str) -> str:
        """
        :param row_value: Name of data base row 'base_word' or 'translated_word'.
        :param old_data_value: Actual value for chosen data.
        :param new_data_value: New value for chosen data.
        :return: String that told the user that the edition was successful.
        """
        new_data_value = new_data_value.title()
        self.cursor.execute("SELECT * FROM words")
        if old_data_value in list(self.cursor.fetchall()):
            with self.connection:
                self.cursor.execute(f"UPDATE words SET {row_value}= :new_data WHERE :old_data ",
                                    {"new_data": new_data_value, "old_data": old_data_value})

            return f"Wartość {old_data_value}, została zmieniona na: {new_data_value}"

        else:
            return "Podana wartość nie znajduje się w bazie słówek!"

    def delete_word(self, data_for_del: str) -> str:
        data_for_del = data_for_del.title()

        self.cursor.execute("SELECT * FROM words")
        print(self.cursor.fetchall()[0])
        if data_for_del in self.cursor.fetchall():
            with self.connection:
                self.cursor.execute("DELETE from words WHERE base_word=:data_for_del OR translated_word=:data_for_del",
                                    {"data_for_del": data_for_del})

            return f"Słowo {data_for_del} zostało usunięte"

        else:
            return "Podana wartość nie znajduje się w bazie słówek!"


class Manual_Translate(Word):
    def __init__(self, connection, cursor, base_language: str, foreign_language: str):
        super().__init__(connection, cursor, base_language, foreign_language)


class Automatic_Translate:
    pass
