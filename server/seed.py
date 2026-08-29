#!/usr/bin/env python3

import os
import sys
from datetime import date

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import app, db
from models import Exercise, Workout, WorkoutExercise

with app.app_context():
    print("Clearing database tables...")
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    print("Seeding exercises...")
    ex1 = Exercise(name="Push Up", category="Strength", equipment_needed=False)
    ex2 = Exercise(name="Running", category="Cardio", equipment_needed=False)
    ex3 = Exercise(name="Bench Press", category="Strength", equipment_needed=True)
    
    db.session.add_all([ex1, ex2, ex3])

    print("Seeding workouts...")
    w1 = Workout(date=date(2026, 8, 20), duration_minutes=45, notes="Upper body day")
    w2 = Workout(date=date(2026, 8, 22), duration_minutes=30, notes="Morning cardio session")
    
    db.session.add_all([w1, w2])
    db.session.commit()

    print("Seeding workout exercises...")
    we1 = WorkoutExercise(workout_id=w1.id, exercise_id=ex1.id, reps=15, sets=3, duration_seconds=0)
    we2 = WorkoutExercise(workout_id=w1.id, exercise_id=ex3.id, reps=10, sets=4, duration_seconds=0)
    we3 = WorkoutExercise(workout_id=w2.id, exercise_id=ex2.id, reps=0, sets=1, duration_seconds=1800)

    db.session.add_all([we1, we2, we3])
    db.session.commit()

    print("Seeding successfully completed!")