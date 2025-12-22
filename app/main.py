from fastapi import FastAPI, status, Response, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel #pydantic helps to create schema
from typing import Optional,List
from random import randrange
import psycopg2  
from psycopg2.extras import RealDictCursor
from . import models, schemas, utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine) # create the tables in the database

app = FastAPI()

    
while True:
    try:
        conn = psycopg2.connect(
            host = "localhost",
            database = "fastapi",
            user = "postgres",
            password = "password123",
            cursor_factory = RealDictCursor
        )
        cursor = conn.cursor()
        print("Connection successful")
        break

    except Exception as error:
        print("Connection failed")
        print("Error:", error)
        

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Hi"}




