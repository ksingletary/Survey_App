from flask import Flask, request, render_template, redirect, flash, jsonify, session
import surveys

app = Flask(__name__)
app.secret_key = "giggity"

responses = []

@app.route('/')
@app.route('/home')
def home_page():
    """Home page"""
    title = surveys.satisfaction_survey.title
    instructions = surveys.satisfaction_survey.instructions
    return render_template('home.html', title=title, instructions=instructions)

@app.route('/session-response', methods=['POST'])
def session_list():
    session["responses"] = []
    return redirect('/questions/0')


@app.route('/questions/<int:id>')
def show_question(id):
    """Shows each question with choices, and renders page"""
    question = surveys.satisfaction_survey.questions[id].question
    choices =  surveys.satisfaction_survey.questions[id].choices

    if id > len(responses):
        flash("Invalid question. Complete current question")
        return redirect(f"/questions/{len(responses)}")
    
    return render_template('questions.html', question=question, choices=choices)

@app.route('/answer', methods=['POST'])
def handle_answer():
    """Appends answer to responses list, and redirects to next question"""
    answer = request.form.get('answer')

    res = session["responses"]
    res.append(answer)
    session[answer] = res

    responses.append(answer)

    if len(responses) == 4:
        return redirect('/finished')
    else:
        return redirect(f"/questions/{len(responses)}")
        
@app.route('/finished')
def thank_you():
    return render_template('finished.html')








