from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

#Temporary home page
@app.route('/')
@cross_origin(supports_credentials=True)
def hello():
    asd = request.json
    print(asd)
    return 'hi'
#Test home page


if __name__ == '__main__':
    app.run()