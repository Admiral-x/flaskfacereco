
import facereco
from flask import Flask, jsonify
from flask import request
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/recognize', methods=['POST'])
def recognizeFaces():
    if request.method == 'POST':
        try:
            data = request.json
            allimages = list()
            for base64image in data:
                res = facereco.readFacesFromImg(base64image)
                allimages.append(res)
            return jsonify(allimages)
        except Exception as e:
            print(e)
            return "Please Provide a Valid Data"
if __name__ == '__main__':
   app.run()