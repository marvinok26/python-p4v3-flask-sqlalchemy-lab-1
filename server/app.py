from flask import Flask, jsonify, request, make_response
from app import db
from models import Earthquake

app = Flask(__name__)
app.config['http//localhost:5555'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/earthquakes/<int:id>')
def get_earthquake_by_id(id):
    earthquake = Earthquake.query.get(id)
    if earthquake:
        return jsonify(earthquake.__dict__)
    else:
        response = make_response(jsonify({"message": f"Earthquake {id} not found."}), 404)
        return response

# ... (other parts of the code)

if __name__ == '__main__':
    app.run(debug=True)
    


