from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from db import db

from resources.exercise import blp as ExerciseBlueprint
from resources.plan import blp as PlanBlueprint
from resources.exercise_plan import blp as ExercisePlanBluePrint
from resources.user import blp as UserBlueprint
from resources.tracking_goals import blp as TrackingGaolBluePrint
from resources.workout_mode import blp as WorkoutModeBluePrint
from blocklist import BlocklistedToken

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        token_jti = get_jwt()["jti"]

        if BlocklistedToken.query.filter_by(jti=token_jti).first():
            return jsonify({'message': 'Token is blacklisted'}), 401

        try:
            data = jwt.decode(token, app.config['JWT_SECRET_KEY'])
            current_user = User.query.get(data['user_id'])
        except:
            return jsonify({'message': 'Token is invalid'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Personalized Workout Plan system REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
    db.init_app(app)

    api = Api(app)

    app.config["JWT_SECRET_KEY"] = 'jose'
    jwt=JWTManager(app)


    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        jti = jwt_payload['jti']
        return BlocklistedToken.query.filter_by(jti=jti).first() is not None


    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401
        )

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )

    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "description": "The token is not fresh",
                    "error": "fresh_token_required",
                }
            ),
            401,
        )

    with app.app_context():
        db.create_all()


    api.register_blueprint(ExerciseBlueprint)
    api.register_blueprint(PlanBlueprint)
    api.register_blueprint(ExercisePlanBluePrint)
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(TrackingGaolBluePrint)
    api.register_blueprint(WorkoutModeBluePrint)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)











































