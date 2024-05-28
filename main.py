from fastapi import FastAPI, HTTPException, status
from fastapi_extras import Query
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from typing import List
import pymongo

app = FastAPI()

client = AsyncIOMotorClient("mongodb://mongodb:27017")
db = client["mydb"]
collection = db["books"]


@app.post("/books/")
async def create_book(book: dict):
    title = book.get("title")
    author = book.get("author")
    if title and author:
        try:
            result = await collection.insert_one({"title": title, "author": author})
            return {"id": str(result.inserted_id), "title": title, "author": author}
        except pymongo.errors. pymongo.errors.PyMongoError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}
    else:
        return {"error": "Invalid request body"}



@app.get("/books/{book_id}")
async def get_book(book_id: str):
    try:
        book = await collection.find_one({"_id": ObjectId(book_id)})
        if book:
            book['_id'] = str(book['_id'])
            return book
        else:
            return {"error": "Book not found"}
    except pymongo.errors. pymongo.errors.PyMongoError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}



@app.get("/books/", response_model=List[dict])
async def get_all_books():
    try:
        books = []
        async for book in collection.find({}):
            book['_id'] = str(book['_id'])
            books.append(book)
        return books
    except Exception as e:
        print(f"Error fetching books: {e}")
        return []



@app.put("/books/{book_id}")
async def update_book(book_id: str, book: dict):
    title = book.get("title")
    author = book.get("author")
    if title and author:
        try:
            result = await collection.update_one({"_id": ObjectId(book_id)}, {"$set": {"title": title, "author": author}})
            if result.modified_count == 1:
                return {"message": "Book updated successfully"}
            else:
                return {"error": "Book not found"}
        except Exception as e:
            return {"error": str(e)}
    else:
        return {"error": "Invalid request body"}

# @app.get("/books/search", response_model=List[dict])
# def search_books(query: str | None = Query(None, description="Search by book title or author")):
  
#     if not query:
#         return []  # Return empty list if no query provided
    
#     search_regex = {"$regex": query, "$options": "i"}  # Case-insensitive search
#     query = {"$or": [{"title": search_regex}, {"author": search_regex}]}

#     books = []
#     try:
#         for book in collection.find(query):
#             book["_id"] = str(book["_id"])
#             books.append(book)
#         return books
#     except Exception as e:
#         print(f"Error fetching books: {e}")
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail="An error occurred while searching for books.",
#         )