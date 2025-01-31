# Public API

This is a simple public API that returns the following information in JSON format:
1. Registered email address.
2. Current datetime in ISO 8601 format (UTC).
3. GitHub URL of the project's codebase.

## Setup Instructions

1. Clone the repository:

   git clone https://github.com/yourusername/public-api.git
   cd public-api

Set up a virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:
pip freeze > requirements
pip install -r requirements.txt

Run the API locally:
python app.py

