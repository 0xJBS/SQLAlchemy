# Workout Tracker API Backend

A RESTful API built with Flask, SQLAlchemy, and Marshmallow for tracking workouts, exercises, and performance metrics.

## Features
- Complete CRUD operations for Workouts and Exercises (excluding update actions).
- Cascading deletions on join table entries when workouts or exercises are deleted.
- Three levels of data validation: Database Table Constraints, SQLAlchemy Model Validations, and Marshmallow Schema Validations.

## Installation Instructions

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd workout-tracker-backend