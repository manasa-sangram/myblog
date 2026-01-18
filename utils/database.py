#sqlite connection inorder for the blogs to get saved there
import sqlite3
from datetime import datetime

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


def insert_blog(title, content, category):
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
        INSERT INTO blogs (title, content, category, date)
        VALUES (?, ?, ?, ?)
    """, (title, content, category, datetime.now().strftime("%Y-%m-%d %H:%M")))

    conn.commit()
    conn.close()


def get_blogs_by_category(category):
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
        SELECT id, title, content, date
        FROM blogs
        WHERE category = ?
        ORDER BY id DESC
    """, (category,))

    blogs = c.fetchall()
    conn.close()
    return blogs
