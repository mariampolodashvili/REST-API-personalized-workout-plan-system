from  marshmallow import  Schema, fields



class PlainPlanExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    repetitions = fields.Int(required=False)
    sets = fields.Int(required=False)
    duration = fields.Int(required=False)
    distance = fields.Int(required=False)
    exercise = fields.Str(required=False)

class PlainPlanSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    goals = fields.Str(required=True)
    workout_frequency = fields.Str(required=True)
    daily_session_duration = fields.Str(required=True)


class PlainTrackingGoalsSchema(Schema):
    id=fields.Int(dump_only=True)
    date=fields.Str(required=True)
    current_weight=fields.Float(required=True)
    weight_goal=fields.Float(required=True)



class ExerciseSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    descriptions = fields.Str(required=True)
    instructions = fields.Str(required=True)
    target_muscles =fields.Str(required=True)


class PlainUpdatePlan(Schema):
    name = fields.Str()
    goals = fields.Str()
    workout_frequency = fields.Str()
    daily_session_duration = fields.Str()



class UpdatePlanExerciseSchema(Schema):
    repetitions = fields.Int()
    sets = fields.Int()
    duration = fields.Int()
    distance = fields.Float()
    plan_id=fields.Int()



class PlanSchema(PlainPlanSchema):
    exercise_plans=fields.List(fields.Nested(PlainPlanExerciseSchema()))
    user_id=fields.Integer(required=True)


class PlanExerciseSchema(PlainPlanExerciseSchema):
    plan_id = fields.Integer(required=True)


class UserSchema(Schema):
    id=fields.Int(dump_only=True)
    username=fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class TrackingGoalsSchema(PlainTrackingGoalsSchema):
    user_id = fields.Integer(required=True)

class UpdatePlan(PlainUpdatePlan):
    user_id = fields.Integer(required=True)