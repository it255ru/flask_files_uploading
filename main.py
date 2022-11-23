import os
from flask import Flask,render_template,request

app = Flask(__name__)
app.config['UPLOAD_PATH']='/home/runner/Hello/downloads/'

@app.route('/')
def index():
	return render_template('upload.html')

@app.route('/', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      uploaded_file = request.files['file']
      uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'],uploaded_file.filename))
      return 'file uploaded successfully'
		
if __name__ == '__main__':
	app.run('0.0.0.0',8080)
