# Technical Assessment Submission

Written answers are in [`answers.md`](./answers.md). Below is how to actually
run the code for each question, in case you want to try it yourself.


## Question 1 — Programming Fundamentals
Requires Python 3.

```bash
python3 duplicate_sort.py
```
Expected output:
```
Original list: [12, 7, 12, 3, 5, 7, 8, 3, 9]
Deduplicated & sorted: [3, 5, 7, 8, 9, 12]
```

## Question 2 — Django API
The blog API is available in the Django project under [`django_blog_api`](./django_blog_api).

1. Start the server:
   
```bash
cd django_blog_api
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
2. For authenticated requests, first create a user account or log in with the JWT endpoints:
   - `POST /api/register`
   - Body:
    ```json
    {
      "username": "Kelvin Kimutai",
      "email": "kiruikevinkim@gmail.com",
      "password": "Password1"
    }
    ```
   - `POST /api/login`
3. After login, copy the access token and add an `Authorization` header:
   ```http
   Authorization: Bearer YOUR_ACCESS_TOKEN
   ```

### Example requests
- List posts: `GET http://127.0.0.1:8000/api/posts/`
- Create a post: `POST http://127.0.0.1:8000/api/posts/`
  - Body:
    ```json
    {
      "title": "My first post",
      "content": "Hello from Thunder Client"
    }
    ```
- View one post: `GET http://127.0.0.1:8000/api/posts/1/`
- Update a post: `PATCH http://127.0.0.1:8000/api/posts/1/`
- Delete a post: `DELETE http://127.0.0.1:8000/api/posts/1/`
