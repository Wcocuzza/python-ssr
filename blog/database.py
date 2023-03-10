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

posts = [
    {
    "title": "Python e eleita a linguagem mais popular",
    "content": """\
		A linguagem Python foi eleita a linguagem mais popular pela revista tech masters
        e segue dominando o mundo.
    """,
    "author": "Satoshi Namamoto",
	},
    {
    "title": "Como criar um blog utilizando Python",
    "content": """\
        Neste tutorial você aprenderá como criar um blog utilizando Python.
        <pre>import make_a_blog</pre>    
    """,
    "author": "Guido Van Rossum",
    },
]

#Inserindo os posts caso o banco esteja vazio.
count = cursor.execute("SELECT * FROM post;").fetchall()
if not count:
    cursor.executemany(
        """\
        INSERT INTO post (title, content, author)
        VALUES (:title, :content, :author);    
        """,
        posts, 
    )
    conn.commit()

#Validando que foi realmente inserido os dados.
posts = cursor.execute("SELECT * FROM post;").fetchall()
assert len(posts) >= 2