from app import app


"""from flask import Flask, make_response, jsonify
from flask_cors import CORS
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})"""


with app.app_context():
    db.create_all()

@app.errorhandler(404)
def not_found(error):
    """handle error 404: Not found"""
    return make_response(jsonify({"error": "Not found"}), 404)



if __name__ == '__main__':

    app.run(debug=True)
