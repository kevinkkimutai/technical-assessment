CREATE TABLE students (
    student_id   INTEGER PRIMARY KEY AUTOINCREMENT,  -- use SERIAL/IDENTITY on Postgres/MySQL
    full_name    TEXT NOT NULL,
    email        TEXT UNIQUE NOT NULL
);

CREATE TABLE courses (
    course_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name  TEXT NOT NULL,
    course_code  TEXT UNIQUE NOT NULL
);

CREATE TABLE enrollments (
    enrollment_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id     INTEGER NOT NULL REFERENCES students(student_id),
    course_id      INTEGER NOT NULL REFERENCES courses(course_id),
    enrolled_on    DATE DEFAULT CURRENT_DATE,
    UNIQUE (student_id, course_id)  
);

-- Sample data
INSERT INTO students (full_name, email) VALUES
    ('Amina Yusuf', 'amina@example.com'),
    ('Brian Otieno', 'brian@example.com');

INSERT INTO courses (course_name, course_code) VALUES
    ('Introduction to Programming', 'CS101'),
    ('Database Systems', 'CS201');

INSERT INTO enrollments (student_id, course_id) VALUES
    (1, 1),
    (2, 1),
    (2, 2);

-- list all students enrolled in "Introduction to Programming"
SELECT s.student_id, s.full_name, s.email
FROM students s
JOIN enrollments e ON e.student_id = s.student_id
JOIN courses c ON c.course_id = e.course_id
WHERE c.course_name = 'Introduction to Programming';
