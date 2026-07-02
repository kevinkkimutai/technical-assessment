# Technical Assessment Submission

Written answers are in [`answers.md`](./answers.md). Below is how to actually
run the code for each question


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

## Question 3: Mobile App Design

Thinking about this from the shop owner's side rather than a developer's side most of these owners are busy, might not be big on typing, and just want to know how much did I make today without digging.

**1. Screens I'd build**
1. **Home / Dashboard** — three big buttons: Add Product, Record Sale, Today's Sales. Today's total sits right at the top so it's the first thing they see.
2. **Add Product** — quick form: name, price, and optionally starting stock.
3. **Product List** — shows what they've already added, doubles as the picker screen when recording a sale.
4. **Record Sale** — pick the product, adjust the quantity, price and total fill in automatically, then confirm.
5. **Today's Sales** — a running list of what's sold so far today, with a total at the bottom.

**2. What's on each screen**
- Home: today's running total + the three main buttons.
- Add Product: name, price, stock (optional).
- Product List: name, price, stock left.
- Record Sale: product name, unit price, quantity, calculated total, a confirm button.
- Today's Sales: each sale (item, qty, amount, time it was recorded), a total, and an option to start fresh the next day.

**3. Two things that would actually make this usable for a non-technical owner**

First: cut down typing wherever possible. If they can tap a product from a list instead of typing its name every time, do that. Typing on a small phone keyboard is where most people get frustrated and start making mistakes.

Second: bigger buttons, icons alongside text, and language support for Swahili as well as English. A lot of the friction with apps like this isn't the logic, it's that the screen is cluttered or the text is too small to read quickly in a shop that's busy or not well lit.

**4. A mistake that's likely to happen, and how to guard against it**

The one I'd worry about most is a **double-recorded sale** - someone taps "Confirm" twice because the screen was slow to respond, or their finger slipped, and now the same sale shows up twice in the total. It's an easy thing to miss until the totals look wrong at the end of the day.

To stop that:
- Show a quick confirmation ("2 x Sugar 1kg = KES 240 - Confirm?") before it actually saves, so there's a moment to catch an obvious mistake before it's locked in.
- Disable the Confirm button right after the first tap so a double-tap physically can't create two entries.
- Add an "undo last sale" option on the Today's Sales screen, so if something does slip through, fixing it is one tap instead of a support call.

---


## Question 4: Relational Databases

SQL: [`sql/schema_and_query.sql`](./sql/schema_and_query.sql)

**1. Tables:** `students`, `courses`, and a junction table `enrollments`
(because one student can take many courses, and one course has many
students which is a many-to-many relationship needs a link table, not a direct
column on either side).

**2. Columns**
- `students`: `student_id`, `full_name`, `email`
- `courses`: `course_id`, `course_name`, `course_code`
- `enrollments`: `enrollment_id`, `student_id` (FK), `course_id` (FK),
  `enrolled_on`

**3. Primary keys**
- `students.student_id`
- `courses.course_id`
- `enrollments.enrollment_id` (with a `UNIQUE(student_id, course_id)`
  constraint so the same student can't be enrolled twice in the same course)

**4. Connecting students to courses**
The `enrollments` table holds a `student_id` and a `course_id` as foreign
keys, one row per enrollment. This is the standard way to model a
many-to-many relationship in a relational database instead of a course
column on the student table (which couldn't hold multiple courses) or vice
versa, the join table stores each student–course pairing as its own row.

**5. Query students enrolled in "Introduction to Programming"**
```sql
SELECT s.student_id, s.full_name, s.email
FROM students s
JOIN enrollments e ON e.student_id = s.student_id
JOIN courses c ON c.course_id = e.course_id
WHERE c.course_name = 'Introduction to Programming';
```
