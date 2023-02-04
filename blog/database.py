from sqlite3 import connect

conn = connect("blog.db")
cursor = conn.cursor()

conn.execute(
    """\
    CREATE TABLE if not exists post (
        id integer PRIMARY KEY AUTOINCREMENT,
        title varchar UNIQUE NOT NULL,
        content varchar NOT NULL,
        author varchar NOT NULL
    )
    """
)