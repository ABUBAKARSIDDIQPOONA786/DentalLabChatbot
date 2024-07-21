# MyDental Labs

Welcome to MyDental Labs! This repository contains the code for our dental lab website, featuring a chatbot with advanced NLP capabilities to assist users with common dental inquiries.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the App Locally](#running-the-app-locally)
- [Deployment](#deployment)
  - [Deploying to Google App Engine](#deploying-to-google-app-engine)
  - [Deploying to Heroku](#deploying-to-heroku)
- [Usage](#usage)
  - [Chatbot Functionality](#chatbot-functionality)
  - [Quick Replies](#quick-replies)
- [Project Structure](#project-structure)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Chatbot with Predefined Responses:** Provides instant information about dental services, contact details, and general inquiries.
- **Advanced NLP Integration:** Capable of understanding and responding to a wide range of dental and medical terms.
- **Detailed Service Information:** Links to external resources for more in-depth information on services like Crown and Bridge, Implants, Orthodontics, and Dentures.
- **Responsive Design:** Ensures the website is accessible and usable on various devices.

## Getting Started

These instructions will help you set up and deploy the project on your local machine and on Google App Engine or Heroku.

### Prerequisites

- Python 3.8 or higher
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) (for Google App Engine deployment)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) (for Heroku deployment)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the App Locally

1. **Set the Flask app environment variable:**

    ```bash
    export FLASK_APP=app.py
    export FLASK_ENV=development
    ```

2. **Run the Flask app:**

    ```bash
    flask run
    ```

    The app will be available at `http://127.0.0.1:5000`.

## Deployment

### Deploying to Google App Engine

1. **Create an `app.yaml` file in the root directory of your project with the following content:**

    ```yaml
    runtime: python39

    entrypoint: gunicorn -b :$PORT app:app

    handlers:
      - url: /static
        static_dir: static

      - url: /.*
        script: auto

    env_variables:
      FLASK_ENV: 'production'
    ```

2. **Initialize the Google Cloud SDK:**

    ```bash
    gcloud init
    ```

3. **Create an App Engine application:**

    ```bash
    gcloud app create
    ```

4. **Deploy your application:**

    ```bash
    gcloud app deploy
    ```

5. **Open your deployed application:**

    ```bash
    gcloud app browse
    ```

### Deploying to Heroku

1. **Log in to Heroku:**

    ```bash
    heroku login
    ```

2. **Create a new Heroku app:**

    ```bash
    heroku create
    ```

3. **Deploy the app:**

    ```bash
    git add .
    git commit -m "Prepare for Heroku deployment"
    git push heroku master
    ```

4. **Open your Heroku app:**

    ```bash
    heroku open
    ```

## Usage

### Chatbot Functionality

The chatbot provides predefined responses to user inquiries. It can handle a variety of questions, including:

- Greetings and farewells
- Information about the dental lab
- Details about services
- Contact information

### Quick Replies

Quick replies are available to provide users with instant options for common inquiries. This improves user experience by allowing them to quickly select predefined questions.

## Project Structure

```plaintext
MyDental-Labs/
├── app.py
├── chatbot/
│   └── chatbot.js
├── static/
│   └── styles.css
├── templates/
│   └── index.html
├── requirements.txt
├── Procfile
├── app.yaml
└── README.md
