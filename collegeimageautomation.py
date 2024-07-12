
from waitress import serve
from lib.api import app
serve(app.app, host='0.0.0.0', port=7055)
