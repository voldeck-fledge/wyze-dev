from flask import Flask, render_template, request
from wyze_sdk import Client
from wyze_sdk.errors import WyzeApiError

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/wyzelock', methods=['GET','POST'])
def wyzelock():
    client = Client(email='jerry@thefledge.com', password='1Daniell@')
    
    if request.method == 'GET':
        lock = client.locks.info(device_mac='YD.LO1.1397b0af09d32be01181f9cac482b914')
        client.locks.unlock(device_mac='YD.LO1.1397b0af09d32be01181f9cac482b914')
        return(f"is open: {lock.is_locked}")

    elif request.method == 'POST':
        return("post")

if __name__ == '__main__':
   app.run()