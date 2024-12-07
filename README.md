Book Recommendation System

Overview

The Book Recommendation System is an AI-driven application that provides personalized book suggestions by analyzing user ratings through collaborative filtering. It helps users discover new books based on their individual interests and the preferences of similar users. Additionally, it showcases popular books trending in the community, providing a dynamic, community-driven recommendation experience.

Features

1. Personalized Recommendations:

    Users receive tailored book suggestions based on their individual ratings and preferences.

    Collaborative filtering is used to find similar users and recommend books they may like.

2. Popular Books List:
   
   Displays a list of the top 50 trending books, allowing users to explore the most popular titles in the community.
3. User-Friendly Interface:

   A simple, easy-to-use web application built with Flask that allows users to interact with the system seamlessly.

Technologies
This application uses the following technologies:

Python 3.10: The programming language used for the backend logic and AI-driven recommendations.

Flask: A lightweight web framework used to build the web server and handle HTTP requests.

Pandas & Numpy: Libraries for efficient data manipulation and analysis.

Scikit-Learn: Used for implementing collaborative filtering and similarity computations.

Docker: For containerization of the application, making it easy to run in different environments.

Pickle: For saving and loading the machine learning model used to generate recommendations.

Installation and Usage

Option 1: Run the Application Locally

Follow the steps below to set up the Book Recommendation System on your local machine:

Clone the Repository:

git clone https://github.com/niranjan-17/book-recommendation-system

cd book-recommendation-system

Install Dependencies: Ensure you have Python 3.10 or higher installed on your system. Then, install the required dependencies using pip:

pip install -r requirements.txt

Run the Flask Application: Start the Flask web server by running the following command:

python3 app.py

Access the Application: Open your web browser and navigate to the following address:
 http://127.0.0.1:5000


Option 2: Run the Application with Docker

To run the Book Recommendation System using Docker, you can either pull the image from Docker Hub or build the image locally.

Option 2.1: Pull the Docker Image from Docker Hub

Pull the Docker Image:

docker run -td -p 5000:5000 --name book-recommendation-app /book-recommendation-app:3.0-1

Access the Application: Open your browser and visit the following URL:
http://127.0.0.1:5000

Option 2.2: Build the Docker Image Locally

Build the Docker Image:

docker build -t book-recommendation-app .

Run the Docker Container:

docker run -td -p 5000:5000 --name book-recommendation-app niranjan17kumar/book-recommendation-app:1.0

Access the Application: Open your browser and navigate to:
http://127.0.0.1:5000

Contributing
We welcome contributions to the Book Recommendation System! To contribute, please follow these steps:

Fork the Repository: Click on the "Fork" button at the top of the repository page.

Clone Your Fork: Clone the repository to your local machine.

Create a New Branch: Create a new branch for your changes.

Make Your Changes: Modify the code as needed and commit your changes.

Push Your Changes: Push your changes back to your forked repository.

Create a Pull Request: Submit a pull request to the main repository.
