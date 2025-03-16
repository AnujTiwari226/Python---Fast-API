from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Anuj'}}

@app.get('/about')
def about():
    return {'data': 'About Page'}

@app.get('/blog/unpublished')
def get_unpublished_blogs():
    return {'data': 'All the unpublished blogs'}

@app.get('/blog/{blog_id}')
def show_blogs(blog_id: int):
    return {'Blog': {'Displaying Blog with id' :blog_id}}

@app.get('/blog')
def blogs_home(limit: int | None, published: Optional[bool]= True, sort: str | None = None):
    if published:
        return {'data': f' Fetching only {limit} blogs from DB where the blogs are published'}
    
    return {'data': f' Fetching only {limit} blogs from DB where the blogs are not published'}

# Post methods

class Blog(BaseModel):
    title: str
    publisher_name: str
    published : Optional[bool]

@app.post('/blog')
def add_new_blog(blog: Blog):
    return {'data': {"New Entry": f'New Blog has been created with title "{blog.title}"'}}



