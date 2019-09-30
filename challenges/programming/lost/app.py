from flask import Flask, request
from solve import get_solution

directions  = get_solution()

app = Flask(__name__)

PORT = 8000
FLAG = "FLAG-WH3R3TH3R31S4W1LLTH3R31S4W4Y"

@app.route('/', methods = ['GET'])
def get():
    return 'Hello there! Use POST / to send your directions!'

@app.route('/', methods = ['POST'])
def post():
    body = request.get_json(force=True)
    if body == directions:
        return FLAG
    else:
        return 'Not quite! If you think you have the right solution, don\'t hesitate to contact staff!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
