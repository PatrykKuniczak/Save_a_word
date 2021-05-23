from unittest import TestCase, main
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Main_Logic import Manual_Translate, Language, Base
import os


# LITERY ZARAZ PO 'TEST' ODPOWIADAJĄ ZA KOLEJNOŚĆ WYKONYWANIA METOD W TESTACH
class TestWord(TestCase):
    Engine = create_engine("sqlite:///Test.db")

    Base.metadata.create_all(Engine)
    session = sessionmaker(bind=Engine, autocommit=True)()

    Manual_Translate._session = session

    @classmethod
    def setUpClass(cls) -> None:
        cls.session = TestWord.session

        cls.first_lang = Language(name='Polski', code='pl')
        cls.second_lang = Language(name='Angielski', code='en')
        cls.third_lang = Language(name='Niemiecki', code="de")

        cls.session.add_all([cls.first_lang, cls.second_lang, cls.third_lang])

        cls.manual = Manual_Translate(cls.first_lang.id, cls.second_lang.id)

    def test_a_add_word(self) -> None:
        self.session = TestWord.session

        base_word = "Jaśko".title()
        translated_word = "Bogdanowicz".title()

        self.assertEqual(self.manual.add_word(base_word, translated_word), [base_word, translated_word])

    def test_b_edit_word(self) -> None:
        old_value = "Jaśko".title()
        new_value = "Bogdan".title()

        self.assertEqual(self.manual.edit_word(old_value, new_value), [old_value, new_value])

    def test_c_edit_language(self):
        old_language = "Polski".title()
        new_language = "Niemiecki".title()
        word_id = 1

        self.assertEqual(self.manual.edit_language(word_id, old_language, new_language),
                         [old_language, new_language])

    def test_d_delete_word(self) -> None:
        data_for_del = "Bogdan".title()

        self.assertEqual(self.manual.delete_word(data_for_del), data_for_del)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.session = TestWord.session

        cls.session.close()
        os.remove("Test.db")


if __name__ == '__main__':
    main()
