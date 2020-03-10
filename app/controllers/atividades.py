from app import app
from flask import render_template
from app.models.tables import Atividade

# Listando todas as atividades
@app.route('/atividades')
def listar_atividades():
    # Pega todos os dados do banco de dados
    a = Atividade.query.all()
    for i in range(len(a)):
        a[i].data = a[i].data.strftime('%d/%m/%Y')


    return render_template("atividades_listar.html", atividades=a)