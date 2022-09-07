from crypt import methods
from flask import Flask, jsonify, request
from models import setup_db, Plant
from flask_cors import CORS, cross_origin


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
        response.headers.add("Access-Control-Allow-Headers", "GET, POST, PATCH, DELETE, OPTIONS")
        return response

    @app.route("/plants", methods=["GET", "POST"])
    def get_plants():
        # implement pagination
        page = request.args.get("page", 1, type=int)
        start = (page - 1) * 10
        end = start + 10

        plants = Plant.query.all()
        formated_plants = [plant.format() for plant in plants]
        return jsonify({
            "success": True,
            "plants": formated_plants[start:end],
            "total_plants": len(formated_plants)
        })
    return app