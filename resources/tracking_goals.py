from flask.views import MethodView
from flask_smorest import Blueprint,abort
from flask_jwt_extended import jwt_required
from db import db
from models import TrackingGoalsModel
from schemas import TrackingGoalsSchema
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
blp=Blueprint("trackinggoals", __name__, description="operations on tracking goals")


@blp.route("/tracking_goals/<tracking_goals_id>")
class TrackingGoal(MethodView):
    @jwt_required()
    @blp.response(200, TrackingGoalsSchema)
    def get(self, tracking_goals_id):
        tracking_goal = TrackingGoalsModel.query.get_or_404(tracking_goals_id)
        return tracking_goal

    @jwt_required()
    def delete(self, tracking_goals_id):
        tracking_goal= TrackingGoalsModel.query.get_or_404(tracking_goals_id)
        db.session.delete(tracking_goal)
        db.session.commit()
        return {"message": "tracking goal deleted"}


    @jwt_required()
    @blp.arguments(TrackingGoalsSchema)
    @blp.response(200, TrackingGoalsSchema)
    def put(self, tracking_goal_data, tracking_goals_id):
        tracking_goal = TrackingGoalsModel.query.get(tracking_goals_id)
        if tracking_goal:
            tracking_goal.date=tracking_goal_data['date']
            tracking_goal.current_weight=tracking_goal_data['current_weight']
            tracking_goal.weight_goal = tracking_goal_data['weight_goal']

        else:
            tracking_goal=TrackingGoalsModel(id=tracking_goals_id, **tracking_goal_data)

        db.session.add(tracking_goal)
        db.session.commit()

        return tracking_goal



@blp.route("/tracking_goal")
class TrackingGoalList(MethodView):

    @jwt_required()
    @blp.response(200, TrackingGoalsSchema(many=True))
    def get(self):
        return TrackingGoalsModel.query.all()

    @jwt_required()
    @blp.arguments(TrackingGoalsSchema)
    @blp.response(200, TrackingGoalsSchema)
    def post(self, tracking_goal_data):
        tracking_goal=TrackingGoalsModel(**tracking_goal_data)
        try:
            db.session.add(tracking_goal)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message = "A plan with that name already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the plan")


        return tracking_goal