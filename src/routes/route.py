import os
from src import app
from flask import render_template

path = "./static"
CSV=os.path.join(path, "csv", "provincias.csv")
print(CSV)

#Methods['GET','POST', 'PUT', 'DELETE']
@app.route('/datos', methods=[ 'GET'])
def get():
    context={
        'csv': 'CSV'
    }
    return render_template('home/inicio.html', params=context)

@app.route('/datos-fake')
def post():
    return "Este es el datos_fake_post"

@app.route('/datos-fake')
def put():
    return "Este es el datos_fake_put"

@app.route('/datos-fake')
def delete():
    return "Este es el datos_fake_delete"

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404/error.html'), 404