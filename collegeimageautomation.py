
from waitress import serve
from lib.face.api import faceapp
serve(faceapp.app, host='0.0.0.0', port=7055)
