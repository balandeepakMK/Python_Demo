Setup Instructions

1. Clone the repo
git clone https://github.com/balandeepakMK/Python_Demo.git
cd travel-api
2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables
Create a .env file in the project root:

DATABASE_URI=mysql+mysqlconnector://root:yourpassword@localhost:3306/travel
💡 Make sure MySQL server is running and the database travel exists.
5. Run the application
python app.py
Visit the app:
Home: http://localhost:5000
Swagger Docs: http://localhost:5000/apidocs
📡 API Endpoints


Method	Endpoint	Description
GET	/	Welcome message
GET	/destinations	List all destinations
GET	/destinations/<id>	Get destination by ID
POST	/destinations	Create new destination
PUT	/destinations/<id>	Update destination
DELETE	/destinations/<id>	Delete destination
🧪 Sample JSON for POST/PUT

{
  "destination": "Paris",
  "country": "France",
  "rating": "5 stars"
}
🧱 Tech Stack

Python 3.12+
Flask
SQLAlchemy
Flasgger (Swagger UI)
MySQL


mysql -u root -p

"CREATE DATABASE travel;" #creating the new database
exit;

Summary
Model = models.py (Data schema)
Controller = controllers.py (Logic)
View = views.py (Routes/Endpoints)
App = app.py (Bootstrapping)