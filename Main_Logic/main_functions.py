from Main_Logic import Word, Session, Language
from sqlalchemy import or_


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

        When editing was successful function return list of the both words.

            When input data isn't on data base function return None.

        :param old_data_value: Actual word value.
        :param new_data_value: New word value.

        :return: List [base_word, translated_word] or False or None (Read Higher)
        """

        data_base_record = self.session.query(Word).filter(or_(Word.base_word == old_data_value,
                                                               Word.translated_word == old_data_value)).first()

        if data_base_record is not None:
            row_value = str

            if data_base_record.base_word == old_data_value:
                row_value = "base_word"

            elif data_base_record.translated_word == old_data_value:
                row_value = "translated_word"

            setattr(data_base_record, row_value, new_data_value)

            return [old_data_value, new_data_value]

        else:
            return None

    def delete_word(self, data_for_del: str) -> str or None:
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
        When editing was successful function return list of the both languages.

            False when the new_language is the same of opposite language (ep. user editing base_language for 'polish'
            but foreign_language value is 'polish').

                When input data isn't on data base function return None.

        :param word_id: This value is a id of word.
        :param old_language: This value is string of old data from language label.
        :param new_language: This value is string of new data from language label.

        :return: List [old_language, new_language].
        """

        old_language_record_id = self.session.query(Language).filter(Language.name == old_language).first().id

        if old_language_record_id is not None:
            row_value = str

            word_record = self.session.query(Word).filter(Word.id == word_id).first()

            opposite_language_id = int

            if old_language_record_id == self.base_language_id:
                row_value = "base_language_id"
                opposite_language_id = word_record.foreign_language_id

            elif old_language_record_id == self.foreign_language_id:
                row_value = "foreign_language_id"
                opposite_language_id = word_record.base_language_id

            new_language_record_id = self.session.query(Language).filter(Language.name == new_language).first().id

            if new_language_record_id != opposite_language_id:

                setattr(word_record, row_value, new_language_record_id)

                return [old_language, new_language]

            else:
                return False

        else:
            return None

    @staticmethod
    def display_words_list() -> dict:
        """

        :return: Dictionary with each record {word_id: [base_word, translated_word, base_language, foreign_language]}.
        """
        session = Manual_Translate._session

        words = session.query(Word).all()

        main_dictionary = {}

        for word in words:
            base_language = session.query(Language).filter(Language.id == word.base_language_id).first().name
            foreign_language = session.query(Language).filter(Language.id == word.foreign_language_id).first().name

            main_dictionary[word.id] = \
                [word.base_word, word.translated_word, base_language, foreign_language]

        return main_dictionary

    @staticmethod
    def show_languages(word_id: int, row_value: str) -> list or False:
        """

        :param word_id: Current word id
        :param row_value: This value depends of currently editing value 'base_language' or 'foreign_language'.

        :return: List with all available languages, without opposite
            (like, base_language is "Polish" in foreign_language list user can't see and pick "Polish")
                or False when row_value is wrong.
        """

        session = Manual_Translate._session

        languages_record = session.query(Language).all()

        word_record = session.query(Word).filter(Word.id == word_id).first()

        languages_list = []

        for language in languages_record:
            if row_value == "base_language":
                if language.id != word_record.base_language_id:
                    languages_list.append(language.name)

            elif row_value == "foreign_language":
                if language.id != word_record.foreign_language_id:
                    languages_list.append(language.name)

            else:
                return False

        return languages_list


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
