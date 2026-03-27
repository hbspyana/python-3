"""Problem 05: Basic aggregates and GROUP BY.

Task:
1. Count all students
2. Compute average age
3. Compute min and max age
4. Count students per track (GROUP BY track)

Print each result.
"""

import sqlite3

DB_PATH = "school.db"


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # TODO: SELECT COUNT(*) FROM students
    cur.execute('SELECT COUNT(*) FROM students')
    print(cur.fetchone()[0])

    # TODO: SELECT AVG(age) FROM students
    cur.execute('SELECT AVG(age) FROM students')
    print(cur.fetchone()[0])
    
    # TODO: SELECT MIN(age), MAX(age) FROM students
    cur.execute('SELECT MIN(age),MAX(age) FROM students')
    print(cur.fetchall()[0])

    # TODO: SELECT track, COUNT(*) FROM students GROUP BY track
    cur.execute('SELECT track, COUNT(*) FROM students GROUP BY track')
    print(cur.fetchall())

    conn.close()


if __name__ == "__main__":
    main()
