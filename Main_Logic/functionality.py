from Main_Logic import Word, Session, Language


class Manual_Translate:
    _session = Session

    def __init__(self, base_language_id: int, foreign_language_id: int) -> None:
        """
        :param base_language_id: It's id of language from which the user translating.
        :param foreign_language_id: It's id of language in which the user translating.
        """
        self.session = Manual_Translate._session
        self.base_language_id = base_language_id
        self.foreign_language_id = foreign_language_id

    def add_word(self, base_word: str, translated_word: str) -> [tuple[str, str]] or [tuple[None, str]] \
                                                                or [tuple[str, None]] or False:

        """
        If one of this words is into data base this value becomes "None".

        If the both words is into data base return False.

        :param base_word: This is a word for translate.
        :param translated_word: This is a word after translate.
        :return: tuple(base_word / None, translated_word / None) or False (Read higher).
        """

        base_word = base_word.title()
        translated_word = translated_word.title()

        base_word_checkout = self.session.query(Word).filter(Word.base_word == base_word).first()
        translated_word_checkout = self.session.query(Word).filter(Word.translated_word == translated_word).first()

        if base_word_checkout is None and translated_word_checkout is None:
            word = Word(base_word=base_word, base_language_id=self.base_language_id,
                        translated_word=translated_word, foreign_language_id=self.foreign_language_id)

            self.session.add(word)

            search = self.session.query(Word).filter(Word.base_word == base_word).first()

            return search.base_word, search.translated_word

        else:
            if base_word_checkout is None:
                return None, translated_word

            elif translated_word_checkout is None:
                return base_word, None

            else:
                return False

    def edit_word(self, row_value: str, old_data_value: str, new_data_value: str) -> tuple[str, str] or False:
        """
        :param row_value: Name of data base row 'base_word' or 'translated_word'.
        :param old_data_value: Actual word value.
        :param new_data_value: New word value.
        :return:
        """

        old_data_checkout = self.session.query(Word).filter(Word.base_word == old_data_value).first()

        if old_data_checkout is not None:
            search_data = self.session.query(Word).filter(Word.base_word == old_data_value).first()
            search_data.base_word = new_data_value

            new_data_checkout = self.session.query(Word).filter(Word.base_word == new_data_value).first()

            if new_data_checkout.base_word == new_data_value:
                return old_data_value, new_data_value

        else:
            return False

    # def edit_word(self, row_value: str, old_data_value: str, new_data_value: str) -> str:
    #
    #     new_data_value = new_data_value.title()
    #
    # self.cursor.execute("SELECT base_word FROM words WHERE base_word=:base_word AND
    # base_language_id=:base_language_id", {"base_word": base_word, "base_language_id": self.base_language_id})
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
