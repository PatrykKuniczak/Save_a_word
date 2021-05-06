from Main_Logic import Word, Session, Language


class Manual_Translate:
    _session = Session

    def __init__(self, base_language_id: int, foreign_language_id: int) -> None:
        """
        :param base_language_id: It's id of language from which the user translating.
        :param foreign_language_id: It's id of language in which the user translating.
        """
        self.session = Manual_Translate._session
        self.base_language = base_language_id
        self.foreign_language = foreign_language_id

    def add_word(self, base_word: str, translated_word: str) -> str:
        """
        :param base_word: This is a word from first(base) language.
        :param translated_word: This is a word from second(foreign) language.
        :return
        """

        base_word = base_word.title()
        translated_word = translated_word.title()

        base_language_checkout = self.session.query(Language).filter(Language.id == self.base_language).first()
        foreign_language_checkout = self.session.query(Language).filter(Language.id == self.foreign_language).first()

        if base_language_checkout and foreign_language_checkout is not None:
            word = Word(base_word=base_word, base_language=self.base_language,
                        translated_word=translated_word, foreign_language=self.foreign_language)

            self.session.add(word)

            search = self.session.query(Word).filter(Word.base_word == base_word).first()

            return search.base_word

        else:
            return "Wybrany język nie znajduje się na liście!"

        # searching = Session.query(Word).filter(Word.base_word == base_word).first()

        # print(searching.base_word)

        # self.cursor.execute("SELECT base_word FROM words WHERE base_word=:base_word AND
        # base_language_checkout=:base_language_checkout", {"base_word": base_word, "base_language_checkout":
        # self.base_language_checkout})

        # if not self.cursor.fetchone(): with self.connection: self.cursor.execute("INSERT INTO words VALUES (
        # :base_word ,:translated_word," ":base_language_checkout, :foreign_language_checkout)", {"base_word":
        # base_word, "translated_word": translated_word, "base_language_checkout": self.base_language_checkout,
        # "foreign_language_checkout": self.foreign_language_checkout})

        #     return f"Pomyślnie dodano słówko '{base_word} - {translated_word}'"

        # else:
        #     return f"Podane słowo '{base_word} - {translated_word}' znajduję się już w bazie słówek"

    # def edit_word(self, row_value: str, old_data_value: str, new_data_value: str) -> str:
    #     """
    #     :param row_value: Name of data base row 'base_word' or 'translated_word'.
    #     :param old_data_value: Actual value for chosen data.
    #     :param new_data_value: New value for chosen data.
    #     :return:
    #     """
    #     new_data_value = new_data_value.title()
    #
    #     self.cursor.execute("SELECT base_word FROM words WHERE base_word=:base_word AND base_language=:base_language",
    #                         {"base_word": base_word, "base_language": self.base_language})
    #
    #     if old_data_value in list(self.cursor.fetchall()):
    #         with self.connection:
    #             self.cursor.execute(f"UPDATE words SET {row_value}= :new_data WHERE :old_data ",
    #                                 {"new_data": new_data_value, "old_data": old_data_value})
    #
    #         return f"Wartość {old_data_value}, została zmieniona na: {new_data_value}"
    #
    #     else:
    #         return "Podana wartość nie znajduje się w bazie słówek!"
    #
    # # TODO: EDIT_LANGUAGE KIEDY UŻYTKOWNIK WYBRAŁ BY ZŁY JĘZYK, TO DAĆ MU NAST. ROZWIJANĄ LISTĘ W ZAAWANSOWANY OPCJACH
    # def delete_word(self, data_for_del: str) -> str:
    #     data_for_del = data_for_del.title()
    #
    # self.cursor.execute("SELECT * FROM words") print(self.cursor.fetchall()[0]) if data_for_del in
    # self.cursor.fetchall(): with self.connection: self.cursor.execute("DELETE from words WHERE
    # base_word=:data_for_del OR translated_word=:data_for_del", {"data_for_del": data_for_del})
    #
    #         return f"Słowo {data_for_del} zostało usunięte"
    #
    #     else:
    #         return "Podana wartość nie znajduje się w bazie słówek!"


class Automatic_Translate:
    pass
