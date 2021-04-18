from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def publish():
    payload = {"identifier": "12343","customer": "Customer X", "value": 1500}
    url = "http://producer:8080/orders"
    r = requests.post(url,data=payload)

    if r.status_code == 200:
        return "Your message has been delivered"
    else:
        return "Sorry, your message wasn't delivered"

if __name__ == '__main__':
    app.run(host='0.0.0.0')