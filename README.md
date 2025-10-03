# Timed-Math-Challenge-for-Engineering-Students

A web-based quiz application built with Python and Flask, designed to test knowledge in various advanced engineering mathematics topics. Users can select a topic, answer multiple-choice questions, and receive immediate, detailed feedback on their performance.

**Features**

Topic Selection: Quizzes are categorized into subjects from Engineering Mathematics 3 and Engineering Mathematics 4.

Interactive Quiz: A clean interface for answering multiple-choice questions.

Instant Results: Users get their score and the total time taken immediately after submitting.

Detailed Feedback: Provides a question-by-question breakdown of correct and incorrect answers.

In-depth Explanations: For every incorrect answer, a detailed, step-by-step explanation is available to help with learning.

Responsive Design: A simple and intuitive UI that works on different screen sizes.


**Technologies Used**

Backend: Python, Flask

Frontend: HTML, CSS


**Project Structure**

For the application to run correctly, your project files should be organized in the following structure:

Math-Challenge-App/

├── app.py

├── static/

│   └── styles.css

└── templates/

    ├── index.html
    
    ├── topic_selection.html
    
    ├── quiz.html
    
    ├── result.html
    
    └── exit.html

   
To get the project running locally, make sure you have Python 3 installed
# Install the required package
pip install Flask

# Run the application
python app.py
