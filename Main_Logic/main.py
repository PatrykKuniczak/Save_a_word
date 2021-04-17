from Main_Logic import *


@data_base_decorator
def main(data_base_connection, data_base_cursor):
    word = Word("Nowe słowo", data_base_connection, data_base_cursor)
    print(word.add_word())


if __name__ == '__main__':
    main()
