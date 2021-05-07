from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from Main_Logic import Base, Engine


class Language(Base):
    """
       This table have a row:

       - id: (Primary)
       - name: This param take a language name.
       - code: This param take a language shortcut e.g. "en".
       """
    __tablename__ = 'languages'

    id = Column(Integer, primary_key=True)
    name = Column(String(25), unique=True)
    code = Column(String(5), unique=True)


class Word(Base): 
    """
    This table have a row:

    - id (Primary)
    - base_word,
    - base_language_id,
    - translated_word,
    - foreign_language_id.
    """
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True)

    base_word = Column(String(100), unique=True)
    base_language_id = Column(Integer, ForeignKey('languages.id'))
    base_language_relation = relationship(Language, foreign_keys=[base_language_id])

    translated_word = Column(String(100), unique=True)
    foreign_language_id = Column(Integer, ForeignKey('languages.id'))
    foreign_language_relation = relationship(Language, foreign_keys=[foreign_language_id])


if __name__ == "__main__":
    Base.metadata.create_all(Engine)
