from config_reader import host_config
import psycopg2


class DataBase():
    def __init__(self):
        self.__rus_letter = dict()
        self.__en_letter = dict()
        self.__signs_letter = dict()

        self.load_data()

    def get_rus_letter(self):
        return self.__rus_letter

    def get_en_letter(self):
        return self.__en_letter

    def get_signs_letter(self):
        return self.__signs_letter

    def load_data(self):
        try:
            connection = psycopg2.connect(
                host=host_config.host,
                user=host_config.user,
                password=host_config.password,
                database=host_config.db_name
            )

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM english_letters;"
                )
                for i in cursor.fetchall():
                    self.__en_letter.update({i[1]: i[2]})

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM russian_letters;"
                )
                for i in cursor.fetchall():
                    self.__rus_letter.update({i[1]: i[2]})

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM signs_symbols;"
                )
                for i in cursor.fetchall():
                    self.__signs_letter.update({i[1]: i[2]})

        except Exception as e:
            raise e
        finally:
            connection.close()
            print("[INFO] PostgreSQL connection closed.")


db = DataBase()
