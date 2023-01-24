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

    # insert_data(cursor)

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

    # cursor.execute('ALTER TABLE users ADD CONSTRAINT unique_id UNIQUE (tg_id)')


# def insert_data(cursor):
#     cursor.execute('''INSERT INTO timetable (id, day_of_week) VALUES
#                       (1, 'Monday'),
#                       (2, 'Tuesday'),
#                       (3, 'Wednesday'),
#                       (4, 'Thursday'),
#                       (5, 'Friday'),
#                       (6, 'Saturday'),
#                       (7, 'Sunday')
#                       ON CONFLICT DO NOTHING
#                       ''')


def update_timetable(cursor, day_of_week, data, user_id):
    # cursor.execute(f'INSERT INTO users (tg_id) VALUES ({user_id}) ON CONFLICT DO NOTHING')
    cursor.execute(f'SELECT * FROM timetable WHERE day_of_week = \'{day_of_week}\' AND tg_id = {user_id}')
    if cursor.fetchone():
        cursor.execute(f'UPDATE timetable SET lessons = \'{data}\' WHERE day_of_week = \'{day_of_week}\' AND tg_id = {user_id}')
    else:
        cursor.execute(f'''INSERT INTO timetable (day_of_week, lessons, tg_id) VALUES (\'{day_of_week}\', \'{data}\', {user_id})''')


# def update_users(cursor, tg_id):
#     cursor.execute(f'INSERT INTO users (tg_id) VALUES ({tg_id}) ON CONFLICT DO NOTHING')


def get_timetable(cursor, day_of_week, tg_id):
    cursor.execute(f'SELECT lessons FROM timetable WHERE day_of_week = \'{day_of_week}\' AND tg_id = {tg_id}')
    try:
        return ', '.join(cursor.fetchone())
    except TypeError:
        return 'No lessons'


def get_all_from_timetable(cursor):
    cursor.execute(f'SELECT * FROM timetable')
    return cursor.fetchall()


# def get_all_from_users(cursor):
#     cursor.execute(f'SELECT * FROM users')
#     return cursor.fetchall()


if __name__ == '__main__':
    cursor = create_cursor()
    # update_timetable(cursor, 'Monday', 'asdasda', 1)
    # update_users(cursor, 0)
    # print(get_timetable(cursor, 'Friday'))
    print(get_all_from_timetable(cursor))
    # print(get_all_from_users(cursor))

