from marshmallow import fields, validate
from config import ma
from models import Exercise, Workout, WorkoutExercise


class ExerciseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Exercise
        load_instance = True

    name = fields.String(required=True, validate=validate.Length(min=1))
    category = fields.String(
        required=True, 
        validate=validate.OneOf(['Cardio', 'Strength', 'Flexibility', 'Balance'])
    )
    equipment_needed = fields.Boolean(required=True)


class WorkoutExerciseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WorkoutExercise
        load_instance = True
        include_fk = True

    reps = fields.Integer(validate=validate.Range(min=0))
    sets = fields.Integer(validate=validate.Range(min=0))
    duration_seconds = fields.Integer(validate=validate.Range(min=0))

    exercise = fields.Nested(ExerciseSchema, only=('id', 'name', 'category'), dump_only=True)


class WorkoutSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Workout
        load_instance = True

    date = fields.Date(required=True)
    duration_minutes = fields.Integer(required=True, validate=validate.Range(min=1))
    notes = fields.String()

    workout_exercises = fields.Nested(WorkoutExerciseSchema, many=True, dump_only=True)


exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

workout_exercise_schema = WorkoutExerciseSchema()