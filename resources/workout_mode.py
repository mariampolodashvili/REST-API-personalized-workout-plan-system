from flask.views import MethodView
from flask import request, jsonify
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required
from models import ExercisePlanModel

blp=Blueprint("workout_mode", __name__, description="operations on workout_mode")


@blp.route("/workout_mode/<int:plan_id>")
class PlansList(MethodView):
    @jwt_required()
    def post(self, plan_id):
        workout_mode_data = request.json
        completed = workout_mode_data.get('completed', 'False')

        if completed.lower() == 'true':

            exercise_id = workout_mode_data.get('exercise_plan_id')
            next_exercise_plan = ExercisePlanModel.query.filter_by(plan_id=plan_id).filter(
                ExercisePlanModel.id > exercise_id).order_by(ExercisePlanModel.id.asc()).first()

            if next_exercise_plan:
                return jsonify({"next_exercise_plan": next_exercise_plan.serialize()})
            else:
                return jsonify({"message": "No more exercises in the plan"}), 200
        else:

            exercise_id = workout_mode_data.get('exercise_plan_id')
            if exercise_id is None:
                return jsonify({"error": "exercise_plan_id is required in the request data"}), 400

            exercise_plan = ExercisePlanModel.query.filter_by(plan_id=plan_id, id=exercise_id).first()
            if not exercise_plan:
                return jsonify({"error": "Exercise plan not found"}), 404

            return jsonify({"exercise_plan": exercise_plan.serialize()})




