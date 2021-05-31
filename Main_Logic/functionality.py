from Main_Logic import Word, Session, Language
from sqlalchemy import or_
# from PyDictionary import PyDictionary


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

    def add_word(self, base_word: str, translated_word: str) -> list[str or None, str or None] or False:
        """

        If one of this words is in data base this value becomes "None".

            If the both words is in data base return False.

        :param base_word: This is a word for translate.
        :param translated_word: This is a word after translate.

        :return: List [base_word/ None, translated_word/ None] or False.
        """

        base_word = base_word.title()
        translated_word = translated_word.title()

        base_word_checkout = self.session.query(Word).filter(Word.base_word == base_word).first()
        translated_word_checkout = self.session.query(Word).filter(Word.translated_word == translated_word).first()

        if base_word_checkout is None and translated_word_checkout is None:
            word = Word(base_word=base_word, base_language_id=self.base_language_id,
                        translated_word=translated_word, foreign_language_id=self.foreign_language_id)

            self.session.add(word)

            word_record = self.session.query(Word).filter(Word.base_word == base_word).first()

            return [word_record.base_word, word_record.translated_word]

        else:
            if base_word_checkout is None:
                return [None, translated_word]

            elif translated_word_checkout is None:
                return [base_word, None]

            else:
                return False

    def edit_word(self, old_data_value: str, new_data_value: str) -> list[str, str] or False:
        """

        When editing was successful function return list of the both words, otherwise return False.

            When input data isn't on data base function return None.

        :param old_data_value: Actual word value.
        :param new_data_value: New word value.

        :return: List [base_word, translated_word] or False or None (Read Higher)
        """

        data_base_record = self.session.query(Word).filter(or_(Word.base_word == old_data_value,
                                                               Word.translated_word == old_data_value)).first()

        if data_base_record is not None:
            row_value = ""
            if data_base_record.base_word == old_data_value:
                row_value = "base_word"

            elif data_base_record.translated_word == old_data_value:
                row_value = "translated_word"

            setattr(data_base_record, row_value, new_data_value)

            update_checkout = self.session.query(Word).filter(Word.base_word == new_data_value).first()

            if update_checkout is not None:
                return [old_data_value, new_data_value]

            else:
                return False
        else:
            return None

    def delete_word(self, data_for_del: str):
        """

        :param data_for_del: This value is data for deleting.

        :return: Deleting data(string) when deleting is successful or None while data_for_del isn't in data base.
        """

        data_for_del = data_for_del.title()
        word_record = self.session.query(Word).filter(or_(Word.base_word == data_for_del,
                                                          Word.translated_word == data_for_del)).first()
        if word_record is not None:
            self.session.delete(word_record)
            return data_for_del

        else:
            return None

    def edit_language(self, word_id: int, old_language: str, new_language: str) -> list[str, str] or False:

        """
        When editing was successful function return list of the both languages, otherwise return False.

            When input data isn't on data base function return None.

        :param word_id: This value is a id of word
        :param old_language: This value is string of old data from language label.
        :param new_language: This value is string of new data from language label.

        :return: List [old_language, new_language]
        """

        old_language_record_id = self.session.query(Language).filter(Language.name == old_language).first().id

        if old_language_record_id is not None:
            row_value = ""
            if old_language_record_id == self.base_language_id:
                row_value = "base_language_id"

            elif old_language_record_id == self.foreign_language_id:
                row_value = "foreign_language_id"

            new_language_record_id = self.session.query(Language).filter(Language.name == new_language).first().id

            word_record = self.session.query(Word).filter(Word.id == word_id).first()

            setattr(word_record, row_value, new_language_record_id)

            update_record_checkout = self.session.query(Word).filter(Word.id == word_id).first()

            if update_record_checkout is not None:
                return [old_language, new_language]

            else:
                return False

        else:
            return None


class Automatic_Translate(Manual_Translate):
    pass
#     def __init__(self, base_language_id: int, foreign_language_id: int):
#         super().__init__(base_language_id, foreign_language_id)
#         self.dictionary = PyDictionary()
#
#     def add_word(self, base_word: str, **kwargs) -> list[str or None, str or None] or False:
#         language_record = self.session.query(Language).filter(Language.id == self.foreign_language_id).first()
#
#         super().add_word(base_word, translated_word)
