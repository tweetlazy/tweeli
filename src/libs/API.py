
import uuid, json, tweepy
from flask import Flask, request, session, send_from_directory
from .Core import TwitterCore

app = Flask(__name__)

objectStorage = {}

def isLoggedIn():
    if 'sessionID' in session:
        return True
    else:
        return False

def login(params):
    if isLoggedIn():
        errorMsg = {'status_code':'4401', 'description':'You are already logged in!'}
        return json.dumps(errorMsg)
    else:
        action = "login"
        twitterCore = TwitterCore()
        sessionID = uuid.uuid1()
        session['sessionID'] = sessionID
        objectStorage[sessionID] = twitterCore
        method = getattr(twitterCore, action)
        try:
            method(**params)
            response = {'status_code':'2200', 'description':'Login successfully!'}
            return json.dumps(response)
        except:
            response = {'status_code':'4500', 'description':'Internal error!'}
            return json.dumps(response)

@app.route('/html/<path:path>')
def send_js(path):
    return send_from_directory('html', path)

@app.route("/", methods=['GET', 'POST'])
def index():
    welcomeMsg = "Welcome to Twitter App!"
    return welcomeMsg

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
    app.secret_key = 'lvkjlfLJLJEIOFs;ffiojsfjelsk'
    app.run(host='0.0.0.0')

if __name__ == "__main__":
    runServer()
