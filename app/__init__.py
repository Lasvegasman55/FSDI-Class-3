from flask import g
import sqlite3

DATABASE_uri = "main.db"


def get_db():
    db =getattr(g, "_database", None)
    if not db:
        db = g.database = sqlite3.connect(DATABASE_URI)
        return db
