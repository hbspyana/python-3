"""Problem 03: Read data from `students` (SELECT basics).

Task:
1. Select all columns from all rows
2. Select only `name` and `email`
3. Select one row by email (`ana@example.com`) using parameterized query
4. Print query results in readable form
"""

import sqlite3

DB_PATH = "school.db"


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # TODO: SELECT * FROM students
<<<<<<< HEAD
    cur.execute('SELECT * FROM students')
    rows = cur.fetchall()
    print('\n')
    for row in rows:
        print(row)

    # TODO: SELECT name, email FROM students
    cur.execute('SELECT name, email FROM students')
    name_email_rows = cur.fetchall()
    print('\n')
    for email in name_email_rows:
        print(email)

    # TODO: SELECT one row for ana@example.com
    cur.execute('SELECT * FROM students WHERE email = ?', ('ana@example.com',))
    one_row = cur.fetchone()
    print('\n')
    print(row)
=======
    # rows = cur.fetchall()

    # TODO: SELECT name, email FROM students
    # name_email_rows = cur.fetchall()

    # TODO: SELECT one row for ana@example.com
    # one_row = cur.fetchone()
>>>>>>> 406e75da68cc14f1e4753c60ed7fe0df8bfaaa74

    conn.close()


if __name__ == "__main__":
    main()
