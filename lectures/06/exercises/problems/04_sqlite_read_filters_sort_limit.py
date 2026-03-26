"""Problem 04: Practice WHERE, ORDER BY, LIMIT.

Task:
1. Get students with age >= 22
2. Sort students by age DESC
3. Return only top 3 oldest students
4. Get backend students younger than 23

Use parameterized queries for filter values.
"""

import sqlite3

DB_PATH = "school.db"


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # TODO 1: age >= 22
    cur.execute('SELECT id, name, age FROM students WHERE age >= 22 ORDER BY age DESC LIMIT 3')
    below_age = cur.fetchall()
    for i in below_age:
        print(i)

    # TODO 2 + 3: order by age desc, limit 3

    # TODO 4: track='backend' and age < 23
    cur.execute('SELECT id, name, age FROM students WHERE age < 23 and track = ?', ('backend',))
    backends = cur.fetchall()
    print('\n')
    for i in backends:
        print(i)

    conn.close()


if __name__ == "__main__":
    main()
