from typing import List
from fastapi import FastAPI, status, Response, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import get_db

router = APIRouter(
    prefix = "/posts",
    tags=["Posts"]
)



# read all posts
@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    # posts = db.query(models.Post).all()
    # return {"data": posts}

    posts = db.query(models.Post).all()
    return posts

# pydantic model has a model called .dict(), so we can convert any pydantic model to dictionary using this .dict()
# create posts
# @app.post("/posts", status_code = status.HTTP_201_CREATED)                                           
# def create_posts(new_post: Post):
#     cursor.execute(""" insert into posts (title, content, published) values (%s, %s, %s) returning * """, (new_post.title, new_post.content, new_post.published))
#     created_post = cursor.fetchone()
#     conn.commit()  
#     return {"data": created_post}

@router.post("/", status_code = status.HTTP_201_CREATED, response_model= schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):

    new_post = models.Post(**post.dict()) # unpacking the dictionary
    db.add(new_post)
    db.commit()
    db.refresh(new_post) # to get the latest data from the database

    return new_post



# read a post
@router.get("/{id}", response_model=schemas.Post)
# def get_posts(id: int, response:Response):
def get_post(id:int, db: Session = Depends(get_db)):
    # cursor.execute(""" select * from posts where id = %s """, (str(id),))
    # post = cursor.fetchone()
    # print(post)

    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"post with id {id} was not found")
    return post


# delete a post
@router.delete("/{id}")
def delete_posts(id:int, db: Session = Depends(get_db)):
    # cursor.execute(""" delete from posts where id = %s returning * """, (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    deleted_post = db.query(models.Post).filter(models.Post.id == id).delete()
    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")

    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# update a post
@router.put("/{id}", response_model=schemas.Post)
def update_posts(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute(""" update posts set title = %s, content = %s, published = %s where id = %s returning * """, (post.title, post.content, post.published, str(id),))

    # updated_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")
    
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()


    return post_query.first()
    