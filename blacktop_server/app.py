from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
import serialize_from_excel as sfe


app = Flask(__name__)
CORS(app, support_credentials=True)

#Temporary home page
@app.route('/teams')
@cross_origin(supports_credentials=True)
def getTeams():
    overall_rating = request.args.get('rating', None)
    players_number  = request.args.get('players', None)
    print('SUMMARY ' + overall_rating + '>>>>> PLAYERS NUMBER ' + players_number)
    return sfe.gen_rtg_arrays(int(overall_rating), int(players_number))

    
#Test home page


if __name__ == '__main__':
    app.run()