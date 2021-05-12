import os
import routes
from flask import Flask, render_template

app = Flask(__name__)
#Methods['GET','POST', 'PUT', 'DELETE']
@app.route('/', methods=[ 'GET'])
def get():
    return render_template('home/inicio.html')

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





if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='127.0.0.1', port=port)