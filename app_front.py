from flask import Flask, json, render_template, request, jsonify
from datetime import datetime
import requests # Handling HTTP requests to the back end Flask app
import pymongo
from dotenv import load_dotenv
import os
load_dotenv()  # Load environment variables from .env file

MONGO_URI = os.getenv("MONGO_URI")  # Get the MongoDB URI from environment variables    
client = pymongo.MongoClient(MONGO_URI)
db = client.new_test # DB name
collection = db['FlaskApp_New']  # Replace 'your_collection_name' with your actual collection name  



app = Flask(__name__)

# Task 1: JSON API Route

@app.route('/api')
def api():
# Reads data from data.json and sends it as a JSON response

    try:
        with open('data.json', 'r') as file:
            data = json.load(file)  # Read the contents of the JSON file
            return jsonify(data)  # Return the data as a JSON response
    except FileNotFoundError:
        return jsonify({"error": "data.json file not found"}), 404  # Return an error message if the file is not found
    file.close()  # Close the file after reading


# Task 2: Frontend Form & MongoDB Atlas

@app.route('/')
def home():

    return render_template('index.html')  # Render the HTML template for the home page

@app.route('/submit', methods=['POST'])
def submit_form():

    try:

        form_data = dict(request.form)  # Convert form data to a dictionary
        collection.insert_one(form_data)  # Insert the form data into the MongoDB collection

        return "Data submitted successfully!"  # Return a success message along with the submitted data
    except Exception as e:
        return render_template('error.html', error_message=str(e))  # Render an error template with the exception message

if __name__ == '__main__':
    app.run(debug=True)



