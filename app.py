from flask import Flask, request, render_template, redirect, flash, jsonify
import surveys

app = Flask(__name__)
app.secret_key = "giggity"

responses = []

@app.route('/')
@app.route('/home')
def home_page():
    title = surveys.satisfaction_survey.title
    instructions = surveys.satisfaction_survey.instructions
    return render_template('home.html', title=title, instructions=instructions)

@app.route('/questions/<int:id>')
def show_question(id):
    question = surveys.satisfaction_survey.questions[id].question
    choices =  surveys.satisfaction_survey.questions[id].choices
    return render_template('questions.html', question=question, choices=choices)


