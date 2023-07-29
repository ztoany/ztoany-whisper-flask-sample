from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import logging
import whisper
import tempfile
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.post('/stt')
def stt():
    data = {"text": ""}
    if request.data is None:
        print("can not find data")
        app.logger.info("can not find data")
    else:
        try:
            temp_file = tempfile.NamedTemporaryFile(delete=False)
            temp_file.write(request.data)
            temp_file.close()
            model = whisper.load_model(name="tiny", in_memory=True)
            result = model.transcribe(temp_file.name, language='en')
        finally:
            if temp_file is not None:
                os.remove(temp_file.name)
        data['text'] = result['text']
    return jsonify(data)


if __name__ == '__main__':
    CORS(app)
    handler = logging.FileHandler('flask.log')
    app.logger.addHandler(handler)
    app.run()
