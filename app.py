# -+- coding:'utf-8' -+-
import os
from src import app
from flask import render_template
from src.routes import route
from src.models import models


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='127.0.0.1', port=port)