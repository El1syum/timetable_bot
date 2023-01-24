import psycopg2
from dotenv import dotenv_values

POSTGRES_PASSWORD = dotenv_values().get('POSTGRES_PASSWORD')
user = 'postgres'
host = 'localhost'
port = 5432


def create_cursor():
    connection = psycopg2.connect(host=host, port=port, user=user, password=POSTGRES_PASSWORD)
    connection.autocommit = True

    cursor = connection.cursor()
    # cursor.execute('DROP TABLE IF EXISTS timetable CASCADE ')
    # cursor.execute('DROP TABLE IF EXISTS users CASCADE ')

    create_table(cursor)

    return cursor


def create_db(cursor):
    cursor.execute('CREATE DATABASE IF NOT EXISTS timetable_bot')


def create_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS timetable(
                      id BIGSERIAL NOT NULL,
                      day_of_week VARCHAR(9) NOT NULL,
                      lessons VARCHAR(150),
                      tg_id BIGINT
                      )''')


def update_timetable(cursor, day_of_week, data, user_id):
    cursor.execute(f'SELECT * FROM timetable WHERE day_of_week = \'{day_of_week}\' AND tg_id = {user_id}')
    if cursor.fetchone():
        cursor.execute(
            f'UPDATE timetable SET lessons = \'{data}\' WHERE day_of_week = \'{day_of_week}\' AND tg_id = {user_id}')
    else:
        cursor.execute(
            f'''INSERT INTO timetable (day_of_week, lessons, tg_id) VALUES (\'{day_of_week}\', \'{data}\', {user_id})''')


def get_timetable(cursor, day_of_week, tg_id):
    cursor.execute(f'SELECT lessons FROM timetable WHERE day_of_week = \'{day_of_week}\' AND tg_id = {tg_id}')
    try:
        return ', '.join(cursor.fetchone())
    except TypeError:
        return 'No lessons'


def get_all_from_timetable(cursor):
    cursor.execute(f'SELECT * FROM timetable')
    return cursor.fetchall()


if __name__ == '__main__':
    cursor = create_cursor()
    # update_timetable(cursor, 'Monday', 'asdasda', 1)
    # update_users(cursor, 0)
    # print(get_timetable(cursor, 'Friday'))
    print(get_all_from_timetable(cursor))
    # print(get_all_from_users(cursor))
