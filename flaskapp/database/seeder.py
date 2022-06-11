import os
import random
import mariadb
import string
import hashlib
from pathlib import Path
from dotenv import load_dotenv


def main():
    static_dir = get_path_of_static_dir()
    env_file_path = os.path.join(os.getcwd(), '../.env')
    load_dotenv()

    conn = get_connection(os.getenv("host"), os.getenv("user"), os.getenv("password"), os.getenv("database"))

    create_user(conn, "admin", "admin", "admin@admin.org", 1)
    create_user(conn, "pim", "pim", "pim@bor.nl", 2)


def create_user(conn, username, password, email, pref_id):
    with conn.cursor() as cursor:
        encoded = password.encode()
        hashed_pass = hashlib.sha256(encoded)
        sql = f"""INSERT INTO Pim.User(username, password, email_address) VALUES(
            '{username}', '{hashed_pass.hexdigest()}', '{email}');
            """
        cursor.execute(sql)

    conn.commit()


def get_connection(host, user, password, database):
    try:
        return mariadb.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    except mariadb.Error as e:
        print(e)
        exit(-1)


def get_all_filenames_in_path(path) -> [str]:
    return [f"{os.path.basename(path)}/{f}" for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]


def get_path_of_static_dir() -> str:
    path = Path(os.getcwd())
    return os.path.join(path.parent.absolute(), "static")


def get_random_string() -> str:
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


if __name__ == '__main__':
    main()
