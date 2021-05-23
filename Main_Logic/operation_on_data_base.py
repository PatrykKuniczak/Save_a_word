from Main_Logic import Base, Session, Engine, Language


def data_base_decorator(func, global_session=Session):
    """
    This decorator open a connection (session) on data base and close it.

    :param func: The main function of program.
    :param global_session: This param take a reference to session from sqlalchemy.
    """

    def wrapper():
        actual_session = global_session
        func()
        actual_session.close()

    return wrapper


def create_tables(Global_Engine=Engine, Global_Base=Base) -> None:
    """
    This function create a tables in data_base, use it at the beginning of the program.

    :param Global_Engine: This param take a engine from sqlalchemy (sqlite3).
    :param Global_Base: This param take a Base from sqlalchemy.
    """
    Global_Base.metadata.create_all(Global_Engine)


def create_languages(Language_Class=Language) -> None:
    """
    This function make a all supporting language at this moment.

    :param Language_Class: This param take a reference to Language table class.
    """

    first_language = Language_Class(name="Polski", code="pl")
    second_language = Language_Class(name="Angielski", code="en")

    Session.add_all([first_language, second_language])
