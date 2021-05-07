from unittest import TestCase, main
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Main_Logic import Manual_Translate, Language, Base, Word
import os


class TestWord(TestCase):

    def setUp(self) -> None:
        Engine = create_engine("sqlite:///Test.db")

        Base.metadata.create_all(Engine)
        self.session = sessionmaker(bind=Engine)()
        Manual_Translate._session = self.session

        self.first_lang = Language(name='Polski', code='pl')
        self.second_lang = Language(name='Niemiecki', code='de')
        self.session.add_all([self.first_lang, self.second_lang])
        self.session.commit()

        self.manual = Manual_Translate(self.first_lang.id, self.second_lang.id)

    def test_add_word(self) -> None:
        base_word = "Jaśko".title()
        translated_word = "Bogdanowicz".title()

        new_base_word = base_word
        new_translated_word = translated_word

        test_word = Word(base_word=new_base_word, translated_word=new_translated_word, base_language_id=self.first_lang.id,
                         foreign_language_id=self.second_lang.id)

        self.session.add(test_word)
        self.session.commit()

        self.assertEqual(self.manual.add_word(base_word, translated_word), False)

    def tearDown(self) -> None:
        self.session.close()
        os.remove("Test.db")


if __name__ == '__main__':
    main()
