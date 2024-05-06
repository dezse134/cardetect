'''Flask server to handle file uploads'''

from os import getenv
from os.path import join
from tempfile import TemporaryDirectory

from flask import Flask, redirect, request, url_for
from detection import detect_cars
from notification import publish_notification

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = getenv('CARDETECT_UPLOAD_PATH')
app.config['OUTPUT_FOLDER'] = getenv('CARDETECT_OUTPUT_PATH')

@app.route("/")
def index():
    '''Redirect to nginx frontend'''
    return redirect('http://localhost/?' + request.query_string.decode())

@app.post('/upload')
def upload_file():
    '''Handle file upload'''
    f = request.files['image']
    if f.filename == '':
        return redirect(url_for('index'))
    f.save(join(app.config['UPLOAD_FOLDER'], f.filename))
    counts = detect_cars(app.config['UPLOAD_FOLDER'], app.config['OUTPUT_FOLDER'])
    app.logger.info('%s: %s', f.filename, counts[f.filename])
    notify(counts, request.form.get('description'))
    result_name = f'result_{f.filename}'
    return redirect(url_for('index', result=result_name))

def notify(counts, desc):
    '''Publish message to queue'''
    publish_notification(desc, list(counts.values())[0])

if __name__ == '__main__':
    with TemporaryDirectory() as td:
        print('Upload folder is:', td)
        app.config['UPLOAD_FOLDER'] = td
        app.run(host='0.0.0.0')
