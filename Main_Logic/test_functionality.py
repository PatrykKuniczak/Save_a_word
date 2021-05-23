from unittest import TestCase, main
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Main_Logic import Manual_Translate, Language, Base, Word
import os


# LITERY ZARAZ PO 'TEST' ODPOWIADAJĄ ZA KOLEJNOŚĆ WYKONYWANIA METOD W TESTACH
class TestWord(TestCase):
    Engine = create_engine("sqlite:///Test.db")

    Base.metadata.create_all(Engine)
    session = sessionmaker(bind=Engine)()

    Manual_Translate._session = session

    @classmethod
    def setUpClass(cls) -> None:
        cls.session = TestWord.session

        cls.first_lang = Language(name='Polski', code='pl')
        cls.second_lang = Language(name='Angielski', code='en')
        cls.third_lang = Language(name='Niemiecki', code="de")
        cls.session.add_all([cls.first_lang, cls.second_lang, cls.third_lang])
        cls.session.commit()

        cls.manual = Manual_Translate(cls.first_lang.id, cls.second_lang.id)

    def test_a_add_word(self) -> None:
        self.session = TestWord.session

        base_word = "Jaśko".title()
        translated_word = "Bogdanowicz".title()

        new_base_word = base_word
        new_translated_word = translated_word

        test_word = Word(base_word=new_base_word, translated_word=new_translated_word,
                         base_language_id=self.first_lang.id, foreign_language_id=self.second_lang.id)

        self.session.add(test_word)
        self.session.commit()

        self.assertEqual(self.manual.add_word(base_word, translated_word), False)

    def test_b_edit_word(self) -> None:
        old_value = "Jaśko".title()
        new_value = "Bogdan".title()

        self.assertEqual(self.manual.edit_word(old_value, new_value), (old_value, new_value))
        self.session.commit()

    def test_c_edit_language(self):
        old_language = "Polski"
        new_language = "Niemiecki"
        word_id = 1

        self.assertEqual(self.manual.edit_language(word_id, old_language, new_language),
                         (old_language, new_language))

        self.session.commit()

    def test_d_delete_word(self) -> None:
        data_for_del = "Bogdan".title()

        self.assertEqual(self.manual.delete_word(data_for_del), data_for_del)
        self.session.commit()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.session = TestWord.session

        cls.session.close()
        os.remove("Test.db")


if __name__ == '__main__':
    main()
