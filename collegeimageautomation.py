
from waitress import serve
from lib.api import app

def main(): 
    serve(app.app, host='0.0.0.0', port=7055)
  
  
# Using the special variable  
# __name__ 
if __name__=="__main__": 
    main() 