from flask import Flask
import json
import urllib.request


app = Flask(__name__)


@app.route('/')
def nasa_data():
    
    myobj = urllib.request.urlopen("https://api.nasa.gov/planetary/earth/imagery?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=DEMO_KEY", verify = False)
    
    objread = myobj.read()

    data = json.loads(objread.decode('utf-8'))

    return data

if __name__ == '__main__':
    app.run()

