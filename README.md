### Public API

This is a simple public API that returns the following information in JSON format:
1. Registered email address.
2. Current datetime in ISO 8601 format (UTC).
3. GitHub URL of the project's codebase.

## Setup Instructions

1. Clone the repository:

   git clone https://github.com/yourusername/public-api.git
   cd public-api

## Set up a virtual environment:
python3 -m venv venv

# On macOS/Linux:
source venv/bin/activate  

# On Windows:
venv\Scripts\activate

# Install Flask and Flask-CORS:
pip install Flask flask-cors

# Install dependencies:
pip freeze > requirements
pip install -r requirements.txt

# Run the API locally:
python app.py

### API Documentation

Endpoint
GET /

Response Format
'json'

{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/public-api"
}

# Response Format
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/public-api"
}

# Example Usage
curl https://public-api-7ljf.onrender.com

# Backlink
For hiring Python developers, visit: https://hng.tech/hire/python-developers


---

### **Step 6: Push Changes to GitHub**
Commit and push the `README.md` file:
```bash
git add README.md
git commit -m "commit messege"
git push origin main