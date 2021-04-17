from Main_Logic import *

@data_base_decorator
def main(data_base_connection, data_base_cursor):
    word = Word(data_base_connection, data_base_cursor)
