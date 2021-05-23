from Main_Logic import Word, Session, Language
from sqlalchemy import or_
from logging import basicConfig, DEBUG, exception

basicConfig(filename="logging.log", level=DEBUG, format='\n %(asctime)s:%(levelname)s:%(message)s')


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

    def add_word(self, base_word: str, translated_word: str) -> [tuple[str or None, str or None]] or False:

        """
        If one of this words is in data base this value becomes "None".

        If the both words is in data base return False.

        :param base_word: This is a word for translate.
        :param translated_word: This is a word after translate.
        :return: tuple(base_word/ None, translated_word/ None) [When None, this data is in data base. Read higher]
        or False when data is in data base.
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

    def edit_word(self, old_data_value: str, new_data_value: str) -> tuple[str, str] or False:
        """
        :param old_data_value: Actual word value.
        :param new_data_value: New word value.
        :return: tuple(base_word, translated_word) while is successful otherwise False
        or None when searching(old_data_value) data isn't on data base.
        """

        data_base_record = self.session.query(Word).filter(or_(Word.base_word == old_data_value,
                                                               Word.translated_word == old_data_value)).first()

        if data_base_record is not None:
            row_value = ""
            if data_base_record.base_word == old_data_value:
                row_value = "base_word"

            elif data_base_record.translated_word == old_data_value:
                row_value = "translated_word"

            try:
                setattr(data_base_record, row_value, new_data_value)

            except AttributeError as attrerror:
                exception(str(attrerror))

            else:
                update_checkout = self.session.query(Word).filter(or_(Word.base_word == new_data_value,
                                                                      Word.translated_word == new_data_value)).first()

                if update_checkout is not None:
                    return old_data_value, new_data_value

                else:
                    return False
        else:
            return None

    def delete_word(self, data_for_del: str):
        """

        :param data_for_del: This value is data for deleting
        :return: str of deleting data when deleting is successful or None while data_for_del isn't in data base
        """
        data_base_record = self.session.query(Word).filter(or_(Word.base_word == data_for_del,
                                                               Word.translated_word == data_for_del)).first()
        if data_base_record is not None:

            self.session.delete(data_base_record)

            return data_for_del

        else:
            return None

    def edit_language(self, word_id,  old_language, new_language) -> tuple[str, str] or False:
        """

        :param word_id: This value is a id of word
        :param old_language: This value is string of old data from language label.
        :param new_language: This value is string of new data from language label.
        :return: The tuple(old_language, new_language) if editing is successful, otherwise return False
        or None when searching(old_data_value) data isn't on data base.
        """
        old_language_record_id = self.session.query(Language).filter(Language.name == old_language).first().id

        if old_language_record_id is not None:
            row_value = ""
            if old_language_record_id == self.base_language_id:
                row_value = "base_language_id"

            elif old_language_record_id == self.foreign_language_id:
                row_value = "foreign_language_id"

            try:
                new_language_record_id = self.session.query(Language).filter(Language.name ==
                                                                             new_language).first().id

                main_object = self.session.query(Word).filter(Word.id == word_id).first()

                setattr(main_object, row_value, new_language_record_id)

            except AttributeError as attrerror:
                exception(str(attrerror))

            else:
                update_checkout = self.session.query(Word).filter(Word.id == word_id).first()
                if update_checkout is not None:
                    return old_language, new_language

                else:
                    return False

        else:
            return None


class Automatic_Translate:
    pass
