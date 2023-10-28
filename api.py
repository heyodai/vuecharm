from fastapi import FastAPI, Query
from typing import List, Optional
import sqlite3
from pydantic import BaseModel

app = FastAPI()

# Create classes for the models
class Post(BaseModel):
    id: int
    author_id: int
    published: str
    title: str
    body: str

class Author(BaseModel):
    id: int
    name: str
    email: str


# Function to connect to the database
def connect_db():
    return sqlite3.connect("fake_data.db")

# Function to execute a single query
def execute_query(query: str, values: tuple = None):
    conn = connect_db()
    c = conn.cursor()
    if values:
        c.execute(query, values)
    else:
        c.execute(query)
    conn.commit()
    conn.close()

# Function to fetch results from the database
def fetch_results(query: str, values: tuple = None):
    conn = connect_db()
    c = conn.cursor()
    if values:
        c.execute(query, values)
    else:
        c.execute(query)
    results = c.fetchall()
    conn.close()
    return results

@app.get("/posts/", response_model=List[Post])
async def get_posts(skip: int = 0, limit: int = 10, sort: Optional[str] = 'asc', author_id: Optional[int] = None):
    sort_order = 'ASC' if sort == 'asc' else 'DESC'
    
    # Base query string
    query = "SELECT * FROM posts"
    
    # If an author_id is provided, add a WHERE clause to the query
    if author_id is not None:
        query += f" WHERE author_id = {author_id}"
    
    # Add ORDER BY and LIMIT, OFFSET clauses
    query += f" ORDER BY published {sort_order} LIMIT ? OFFSET ?"
    
    posts = fetch_results(query, (limit, skip))
    return [{"id": post[0], "author_id": post[1], "published": post[2], "title": post[3], "body": post[4]} for post in posts]

@app.get("/authors/", response_model=List[Author])
async def get_authors():
    query = '''SELECT * FROM authors'''
    authors = fetch_results(query)
    return [{"id": author[0], "name": author[1], "email": author[2]} for author in authors]
