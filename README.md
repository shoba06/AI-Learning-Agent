Intelligent Personalized Learning Agent
Project Overview

The Intelligent Personalized Learning Agent is an AI-based educational application designed to provide learning content based on individual learning preferences. The system identifies how a user prefers to learn and adapts the learning material accordingly. Instead of offering uniform content to all learners, this project focuses on personalized and adaptive learning.

The application works completely offline and integrates machine learning with a locally hosted large language model for content generation.

Objective

The main objectives of this project are:

To detect the preferred learning style of a learner

To generate educational content based on the selected topic and difficulty level

To provide visual learning support when required

To avoid unnecessary redirection to external websites

To build a practical AI-based learning system without paid APIs

Learning Style Identification

The system determines the learning style using four preference-based questions:

Preference for watching videos

Preference for listening to lectures

Interest in practical activities

Preference for reading notes

These inputs are converted into numerical values and passed to a trained machine learning model, which predicts the dominant learning style.

System Architecture
User Interface

The user interface is developed using Streamlit. It allows users to:

Enter the topic they want to learn

Select a difficulty level

Answer learning preference questions

View generated learning content and videos when applicable

Machine Learning Model

A supervised machine learning classification model is trained using a custom dataset containing learning preferences. The trained model is saved as a file and loaded during runtime to predict the learning style.

Content Generation

The system uses a locally hosted large language model through Ollama to generate academic explanations. The content is structured into definition, core concepts, examples, applications, and summary. The explanation adapts to the difficulty level selected by the user.

Video Integration

If the predicted learning style is visual and the user prefers video-based learning, the system automatically embeds a relevant tutorial video related to the topic on the same page. No additional explanation is provided for the video, allowing the learner to focus on the content.

Workflow

The user enters a topic and selects a difficulty level

The user answers learning preference questions

The machine learning model predicts the learning style

The system generates topic-specific educational content

If required, a relevant video is embedded

The final personalized learning output is displayed

Technologies Used

Python

Streamlit

Scikit-learn

Pandas

Joblib

Ollama (LLaMA-3)

YouTube video embedding

Project Structure

AI-Learning-Agent
app.py
model.pkl
train_model.py
learning_data.csv
requirements.txt
README.md

Key Features

Personalized learning content

Offline AI processing

Machine learning-based decision making

Adaptive multimedia support

Clean and user-friendly interface

Conclusion

This project demonstrates how artificial intelligence can be applied to personalize education. By combining machine learning and natural language generation, the Intelligent Personalized Learning Agent provides an adaptive learning experience that improves engagement and understanding.

The project is suitable for academic submissions and as a foundational prototype for intelligent educational systems.
