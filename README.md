Online Learning Platform Backend
===

## Description
This project is a backend system for an online learning platform developed using **Django REST Framework (DRF)** and **PostgreSQL**. The project has been dockerized for easy deployment.

## API ENDPOINTS
### Course
- **GET /courses:** Retrieves a list of available courses.

- **GET /courses/id:** Retrieves a specific course by its ID.
- **POST /courses:** Create a new course.

### Enrollment
- **POST /enrollments:** Allows students to enroll in a course.

## Getting Started

To set up and run the project locally, follow these steps:

1. Clone the project.
```bash
git clone https://github.com/kaziiriad/django_ols.git
``` 
2. Navigate to the project directory:
```bash
cd django_ols
```
3. Modify the `env.example` to `.env` and add API credentials:

4. Build and run the Docker containers:

```bash
docker-compose up --build
```
5. Access the API endpoints through the appropriate URLs:

- Course API: `http://localhost:8000/api/courses`
- Enrollment API: `http://localhost:8000/api/enrollments`

## Dependencies
- **Django**
- **Django REST Framework**
- **PostgreSQL**
- **Docker**

## Usage
- Retrieve a list of courses: Send a **GET** request to `/courses`.
- Retrieves a filtered list of available courses using properties like *instructor*, *price* or *duration*: **GET** `/courses/?{query_params}`
- Retrieve a specific course by ID: Send a **GET** request to `/courses/id`, replacing `id` with the ID of the course.
- Create a new course: Send a **POST** request to `/courses` with the required course details in the request body.
- Enroll in a course: Send a **POST** request to `/enrollments` with the necessary enrollment information in the request body.

## Testing

Testing has been conducted to ensure the expected behavior of the backend system. You can run the tests using the following command:

1. Start the database
```bash
docker compose -d up db
```
2. Run the test
```bash
python manage.py test
```

## Contributors
- [Sultan Mahmud](https://github.com/kaziiriad)

## License
This project is licensed under the [MIT License](https://opensource.org/license/mit).
