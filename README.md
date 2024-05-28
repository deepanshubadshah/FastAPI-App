# FastAPI App
 
This is a simple CRUD App 

You can RUN the application using docker-compose file with command ```docker-compose up -d```

API Endpoints:

1. Create Book: 

   Method: POST

   Endpoint: http://localhost:8000/books/

   Body: {"title": "Outliers", "author": "Malcolm Gladwell"}


2. Get all Books: 

   Method: GET

   Endpoint: http://localhost:8000/books/


3. Get a Book by book_id: 

   Method: GET

   Endpoint: http://localhost:8000/books/{id_value}


4. Update Book: 

   Method: PUT

   Endpoint: http://localhost:8000/books/{id_value}

   Body: {"title": "Outliers", "author": "Malcolm Gladwell"}


5. Search By Book title or author:

   Method: GET

   Endpoint: http://localhost:8000/books/search?query=


