!pip install flask-ngrok

from flask import Flask, send_from_directory
from flask import request
from flask_ngrok import run_with_ngrok
import base64

app = Flask(__name__)
run_with_ngrok(app)

@app.route("/image", methods=['POST'])
def root():
    main()
    return 'yo'

def main():
    imgdata = request.get_data()
    print(type(imgdata))
    # imgdata = bytes(imgdata, 'utf-8')
    imgdata = base64.b64decode(imgdata)
    with open('/content/b64.png', 'wb') as f:
        f.write(imgdata)

app.run()
