import logging
from flask import Flask, request
from src.video_trimmer import VideoTrimmer

app = Flask(__name__)
logging.basicConfig(format='%(levelname)s %(asctime)s : %(message)s', level=logging.INFO)


def _prepate_data(event):
    data = event
    data['debug'] = event['debug'] if 'debug' in event else False

    return data


@app.route('/health', methods=['GET'])
def health():
    return {'Message': 'Hello from VideoUtils'}


@app.route('/trim_video', methods=['POST'])
def trim_video():
    health()
    try:
        event = _prepate_data(request.data)
        vt = VideoTrimmer(logging, event)
        vt.work_queue()
        return {'status': 200, 'Message': f'Successful Trim'}
    except Exception as err:
        return {'status': 400, 'Message': f'{err}'}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003, debug=True)