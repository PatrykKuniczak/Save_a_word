from unittest import TestCase, main
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Main_Logic import Manual_Translate, Automatic_Translate, Language, Base
import os


# LITERY ZARAZ PO 'TEST' ODPOWIADAJĄ ZA KOLEJNOŚĆ WYKONYWANIA METOD W TESTACH
class TestManual_Translate(TestCase):
    Engine = create_engine("sqlite:///Test.db")

    Base.metadata.create_all(Engine)
    session = sessionmaker(bind=Engine, autocommit=True)()

    Manual_Translate._session = session
    Automatic_Translate._session = session

    @classmethod
    def setUpClass(cls) -> None:
        cls.session = TestManual_Translate.session

        cls.first_lang = Language(name='Polski', code='pl')
        cls.second_lang = Language(name='Angielski', code='en')
        cls.third_lang = Language(name='Niemiecki', code="de")

        cls.session.add_all([cls.first_lang, cls.second_lang, cls.third_lang])
        pl_record = cls.session.query(Language).filter(Language.name == "Polski").first()
        en_record = cls.session.query(Language).filter(Language.name == "Angielski").first()
        de_record = cls.session.query(Language).filter(Language.name == "Niemiecki").first()

        cls.manual = Manual_Translate(pl_record.id, en_record.id)
        cls.automatic = Automatic_Translate(pl_record.id, en_record.id)

    def test_a_add_word(self) -> None:

        base_word = "Jaśko".title()
        translated_word = "Bogdanowicz".title()

        self.assertEqual(self.manual.add_word(base_word, translated_word), [base_word, translated_word])
    #
    # def test_b_automatic_add_word(self):
    #
    #     base_word = "Jabłko".title()
    #
    #     self.assertEqual(self.automatic.add_word(base_word), [base_word, "Apple"])

    def test_c_edit_word(self) -> None:
        old_value = "Jaśko".title()
        new_value = "Bogdan".title()

        self.assertEqual(self.manual.edit_word(old_value, new_value), [old_value, new_value])

    def test_d_edit_language(self):
        old_language = "Polski".title()
        new_language = "Angielski".title()
        word_id = 1

        self.assertEqual(self.manual.edit_language(word_id, old_language, new_language),
                         [old_language, new_language])

    def test_e_delete_word(self) -> None:
        data_for_del = "Bogdan".title()

        self.assertEqual(self.manual.delete_word(data_for_del), data_for_del)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.session = TestManual_Translate.session

        cls.session.close()
        os.remove("Test.db")


if __name__ == '__main__':
    main()
