from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/home')
def home():
    title = "Atividades Complementares"
    e = ['SINPRAD', 'Semana ADS', 'Semana de Ciência e Tecnologia']
    return render_template("index.html", eventos=e, titulo=title)