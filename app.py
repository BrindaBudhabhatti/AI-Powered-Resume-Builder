from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField


import pathlib
import textwrap

import google.generativeai as genai

#from IPython.display import display
#from IPython.display import Markdown


#def to_markdown(text):
#  text = text.replace('•', '  *')
#  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def add_prompt(field : str, value : str) -> str:
    if value.strip() != '' or value.lower() != 'blank':
        return f'{field}: {value}\n'

app = Flask(__name__)


@app.route('/generate_resume/<name>/<dob>/<phone>/<email>/<education_1>/<education_1_completion_year>/<education_1_school>/<prof_exp_1>/<role_prof_exp_1>/<company_prof_exp_1>/<worked_from_prof_exp_1>/<worked_till_prof_exp_1>/<expertise>/<apply_for_position>/<hobby>', methods=['GET'])
def generate_resume(name, dob, phone, email, education_1, education_1_completion_year, education_1_school, prof_exp_1, role_prof_exp_1, company_prof_exp_1, worked_from_prof_exp_1, worked_till_prof_exp_1, expertise, apply_for_position, hobby):    
     # Process the form data
    GOOGLE_API_KEY = "AIzaSyCFVprvVD5gy5C2ivoqEyMtyPIYZkO_L0g"
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')

    prompt = r'I want you to build a professional resume for ' + apply_for_position + ' position in a beautifully styled self contained HTML format, using the following information.  Include objective statement and professional summary. Resume should also have summary based on role and good things about the person.\n\n'
    prompt += add_prompt('Name', name)
    prompt += add_prompt('Date of Birth', dob)
    prompt += add_prompt('Phone', phone)
    prompt += add_prompt('Email', email)
    prompt += add_prompt('Education', education_1)
    prompt += add_prompt('Education Completion Year', education_1_completion_year)
    prompt += add_prompt('School', education_1_school)

    prompt += add_prompt('Professional Experience', prof_exp_1)
    prompt += add_prompt('Professional Experience', role_prof_exp_1)
    prompt += add_prompt('Company', company_prof_exp_1)
    prompt += add_prompt('Role', role_prof_exp_1)
    prompt += add_prompt('Worked From', worked_from_prof_exp_1)
    prompt += add_prompt('Worked Till', worked_till_prof_exp_1)

    prompt += add_prompt('Expertise', expertise)
    prompt += add_prompt('Apply For Position', apply_for_position)
    prompt += add_prompt('Hobby', hobby)

    response = model.generate_content(prompt)
    return response.text.replace("```html", ""), 200, {'Content-Type': 'text/html'}


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)

