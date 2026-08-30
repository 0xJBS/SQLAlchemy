# Fitness Tracker REST API

A clean, robust, and scalable backend RESTful API built with **Python**, **Flask**, **SQLAlchemy**, **Alembic**, and **Marshmallow**. This application manages workout routines, exercises, and performance tracking using relational database modeling and data validations.

---

## Project Overview

This application acts as the backend server for a Fitness Tracking application. It handles storing, retrieving, updating, and deleting fitness records through structured HTTP endpoints.

Key features include:
* **Relational Data Architecture:** Full Many-to-Many relationships between Workouts and Exercises using a join table with performance attributes (sets, reps, duration).
* **Automated Data Validation:** Ensures invalid data (e.g., negative duration, invalid exercise categories, blank names) is rejected with informative error messages.
* **Database Migrations:** Powered by Alembic / Flask-Migrate to maintain schema changes smoothly.
* **Marshmallow Serialization:** Encapsulates nested JSON formatting and handles data serialization/deserialization.

---

## Technology Stack

* **Language:** Python 3.10+
* **Framework:** Flask
* **ORM:** SQLAlchemy
* **Migrations:** Flask-Migrate / Alembic
* **Serialization & Validation:** Marshmallow
* **Database:** SQLite (Development)

---

## Database Architecture & ERD Concept

The API uses three core models:

1. **`Workout`**: Represents a single workout session.
   - `id`: Integer (Primary Key)
   - `date`: String / Date (Required)
   - `duration_minutes`: Integer (Must be > 0)
   - `notes`: Text (Optional session summary)

2. **`Exercise`**: Represents a physical exercise catalog item.
   - `id`: Integer (Primary Key)
   - `name`: String (Required, non-empty)
   - `category`: String (Validated choices: `Strength`, `Cardio`, `Flexibility`)
   - `equipment_needed`: Boolean

3. **`WorkoutExercise`**: Join table connecting `Workout` and `Exercise` (Many-to-Many relationship).
   - `id`: Integer (Primary Key)
   - `workout_id`: Foreign Key (`workouts.id`)
   - `exercise_id`: Foreign Key (`exercises.id`)
   - `reps`: Integer (Default: 0)
   - `sets`: Integer (Default: 0)
   - `duration_seconds`: Integer (Default: 0)

---

## API Endpoints Summary

### Workouts

| Method | Endpoint | Description | Status Code |
| :--- | :--- | :--- | :--- |
| **GET** | `/workouts` | Retrieve all workouts with nested exercises | `200 OK` |
| **GET** | `/workouts/<id>` | Retrieve a single workout by ID | `200 OK` / `404 Not Found` |
| **POST** | `/workouts` | Create a new workout session | `201 Created` / `400 Bad Request` |
| **DELETE** | `/workouts/<id>` | Delete a workout (cascades to join records) | `204 No Content` / `404 Not Found` |

### Exercises

| Method | Endpoint | Description | Status Code |
| :--- | :--- | :--- | :--- |
| **GET** | `/exercises` | Retrieve all available exercises | `200 OK` |
| **GET** | `/exercises/<id>` | Retrieve a single exercise by ID | `200 OK` / `404 Not Found` |

### Workout Exercises (Join Endpoint)

| Method | Endpoint | Description | Status Code |
| :--- | :--- | :--- | :--- |
| **POST** | `/workouts/<w_id>/exercises/<e_id>/workout_exercises` | Add an exercise entry to a workout | `201 Created` / `400 Bad Request` |

---

## Setup & Local Installation Instructions

Follow these steps to run the backend locally on your machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/0xJBS/SQLAlchemy.git](https://github.com/0xJBS/SQLAlchemy.git)
cd SQLAlchemy/server