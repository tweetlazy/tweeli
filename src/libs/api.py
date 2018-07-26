import json
import uuid

# third-party imports
import tweepy
from flask import Flask, redirect, request, send_from_directory, session
from flask_session import Session

# from .core import TwitterCore

app = Flask(__name__)

objectStorage = {}

def isLoggedIn():
    app.logger.debug("login state : %s",str('twt_user' in session))
    if 'twt_user' in session:
        return True
    else:
        return False

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect("/html/login.html",code=302)
@app.route("/login", methods=['POST'])
def login():
    session['twt_user']=request.form.to_dict()
    if isLoggedIn():
        return redirect("/html/index.html",code=302)
    return '';
@app.route('/html/<path:path>')
def send_js(path):
    if (path != "login.html")and ('html' in path):
        if not isLoggedIn():
            return redirect("/html/login.html",code=302)
    if (path == "login.html") and isLoggedIn():
        return redirect("/html/index.html",code=302)
    return send_from_directory('html', path)

@app.route("/data/chart", methods=['GET'])
def chart_data():
    if not isLoggedIn():
        return redirect("/html/login.html",code=302)
    return """var followers = {
              x: [1, 2, 3, 4, 5, 6, 7],
              y: [4, 5, 3, 1, -1, 2, 1],
              type: 'scatter',
              name: 'Followers'
            };
            var following = {
              x: [1, 2, 3, 4, 5, 6, 7],
              y: [2, 5, 3, 2, 1, -2, 3],
              type: 'scatter',
              name: 'Following'
            };
            var tweets = {
              x: [1, 2, 3, 4, 5, 6, 7],
              y: [16, 5, 11, 9, 14, 7, 2],
              type: 'scatter',
              name: 'Tweets'
            };
            var data = [followers, following, tweets];
            var layout = {
              title: 'Changes during last week',
              xaxis: {
                title: 'Days of the Week',
                showgrid: false,
                zeroline: false
              },
              yaxis: {
                title: 'Numbers',
                showline: false
              }
            };
            Plotly.newPlot('myDiv', data, layout);
    """
    
@app.route("/", methods=['GET', 'POST'])
def index():

    return redirect("/html/index.html",code=302)

@app.route("/api", methods=['GET', 'POST'])
def api():
    if 'action' in request.form:
        params = request.form.to_dict()
        action = params["action"]
        if action == "login":
            return login(params)
        else:
            if isLoggedIn():
                sessionID = session['sessionID']
                twitterCore = objectStorage[sessionID]
            else:
                errorMsg = {'status_code':'4401', 'description':'First you must log in!'}
                return json.dumps(errorMsg)
        if action in dir(twitterCore):
            method = getattr(twitterCore, action)
            try:
                result = method(**params)
            except Exception as e:
                errorMsg = {'status_code':'4400', 'description':str(e)}
                return json.dumps(errorMsg)
            if type(result) == tweepy.cursor.ItemIterator:
                results = []
                for res in result:
                    results.append(res._json)
                finalRes = {"status_code":"2200", "response":results}
                return json.dumps(finalRes)
            if "_json" in dir(result):
                finalRes = {"status_code":"2200", "response":result._json}
            else:
                finalRes = {"status_code":"2200", "response":result}
            return json.dumps(finalRes)
        else:
            errorMsg = {'status_code':'4401', 'description':'Action %s is not defined!'%action}
            return json.dumps(errorMsg) 
    else:
        errorMsg = {'status_code':'4400', 'description':'Param action is not exist!'}
        return json.dumps(errorMsg)

def runServer():
    # import logging
    # log = logging.getLogger('werkzeug')
    # log.disabled = True
    # Session(app)
    app.secret_key = 'lvkjlfLJLJEIOFs;ffiojsfjelsk'
    app.config['SESSION_TYPE']='filesystem'
    Session(app)
    app.run(host='0.0.0.0',debug=True)

if __name__ == "__main__":
    runServer()
