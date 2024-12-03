# README: IRWA-2024 Project 4

## Project Overview

This project, developed as part of the IRWA 2024 course, demonstrates a search engine and analytics system designed to find documents containing specific query terms and rank them based on relevance. The system integrates data visualization, user interaction tracking, and session management to enhance the search experience.

## Authors

- Bernat Quintilla (ID: 254530)  
- Eugeni Soler (ID: 253566)  
- Roger Viader (ID: 252282)  

## Requirements

Ensure the following dependencies are installed before running the application:

- **Python 3.x**
- **Flask**: For web application framework
- **httpagentparser**: For analyzing user-agent details
- **NLTK**: (optional) For sentiment analysis
- Additional Libraries: pandas, numpy

## Dataset

The dataset used for this project contains tweets related to the Farmers' Protest, stored in JSON format (farmers-protest-tweets.json). Ensure the dataset is available in the correct directory for the application to load.

## How to Run the Application

1. Clone the repository to your local machine.

2. Ensure the dataset (farmers-protest-tweets.json) is located in the correct directory or update the file path in the script.

3. Install the required libraries (refer to the Requirements section).

4. Start the Flask application by running: python web_app.py

5. Open your browser and navigate to http://127.0.0.1:8088/ to access the application.

