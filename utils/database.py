#sqlite connection inorder for the blogs to get saved there
import sqlite3

def get_connection():
  return sqlite3.connect("blog.db")

def create_table():
  conn = get_connection()
  c = conn.cursor()

  c.execute("""CREATE TABLE IF NOT EXISTS blogs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT,
        category TEXT,
        date TEXT
    )
    """)
  conn.commit()
  conn.close()

def delete_blog(blog_id):
    conn = get_connection()
    c = conn.cursor()

    c.execute("DELETE FROM blogs WHERE id = ?", (blog_id,))

    conn.commit()
    conn.close()

