from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

# Initialize the Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/', methods=['GET'])
def get_info():
    """ Prepare the response data """
    data = {
        "email": "uthmanghamzaki@gmail.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/Ghamzaki/public-api"
    }
    # Return the data as JSON with a 200 OK status
    return jsonify(data), 200

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000) # Render required port