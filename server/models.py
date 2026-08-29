from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint, UniqueConstraint
from config import db


class Exercise(db.Model):
    __tablename__ = 'exercises'

    __table_args__ = (
        UniqueConstraint('name', name='uq_exercise_name'),
        CheckConstraint('length(name) > 0', name='check_exercise_name_not_empty'),
    )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.Boolean, default=False, nullable=False)

    workout_exercises = db.relationship(
        'WorkoutExercise', 
        back_populates='exercise', 
        cascade='all, delete-orphan'
    )
    workouts = db.relationship(
        'Workout', 
        secondary='workout_exercises', 
        back_populates='exercises', 
        viewonly=True
    )

    @validates('name')
    def validate_name(self, key, value):
        if not value or not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Exercise name must be a non-empty string.")
        return value.strip()

    @validates('category')
    def validate_category(self, key, value):
        valid_categories = ['Cardio', 'Strength', 'Flexibility', 'Balance']
        if value not in valid_categories:
            raise ValueError(f"Category must be one of: {', '.join(valid_categories)}")
        return value


class Workout(db.Model):
    __tablename__ = 'workouts'

    __table_args__ = (
        CheckConstraint('duration_minutes > 0', name='check_workout_duration_positive'),
    )

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)

    workout_exercises = db.relationship(
        'WorkoutExercise', 
        back_populates='workout', 
        cascade='all, delete-orphan'
    )
    exercises = db.relationship(
        'Exercise', 
        secondary='workout_exercises', 
        back_populates='workouts', 
        viewonly=True
    )

    @validates('duration_minutes')
    def validate_duration(self, key, value):
        if value is None or value <= 0:
            raise ValueError("Workout duration must be greater than 0 minutes.")
        return value


class WorkoutExercise(db.Model):
    __tablename__ = 'workout_exercises'

    __table_args__ = (
        CheckConstraint('reps >= 0', name='check_reps_non_negative'),
        CheckConstraint('sets >= 0', name='check_sets_non_negative'),
        CheckConstraint('duration_seconds >= 0', name='check_duration_seconds_non_negative'),
    )

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    reps = db.Column(db.Integer, default=0)
    sets = db.Column(db.Integer, default=0)
    duration_seconds = db.Column(db.Integer, default=0)

    workout = db.relationship('Workout', back_populates='workout_exercises')
    exercise = db.relationship('Exercise', back_populates='workout_exercises')

    @validates('reps', 'sets', 'duration_seconds')
    def validate_metrics(self, key, value):
        if value is not None and value < 0:
            raise ValueError(f"{key} cannot be negative.")
        return value