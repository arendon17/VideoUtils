import logging
from flask import Flask, request

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health():
    return {'Message': 'Hello from VideoUtils'}

@app.route('/trim_video/', methods=['POST'])
def send_email():
    pass


if __name__ == '__main__':
    app.run()
