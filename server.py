from flask import Flask, request, Response, render_template
import time
import os, os.path

FILE_NAME = 'temp'
PATH_TO_SAVE_IMAGE = ' '
NAME = ' '

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/createDir', methods=['POST'])
def createDir():
    global PATH_TO_SAVE_IMAGE, NAME
    NAME = request.form['name']
    PATH_TO_SAVE_IMAGE = './images/' + NAME + '/'
    if not os.path.exists(PATH_TO_SAVE_IMAGE):
        os.makedirs(PATH_TO_SAVE_IMAGE)
    return render_template("getImage.html")

@app.route('/image', methods = ['POST'])
def image():
	global f, counter
	i = request.files['image']
	FILE_NAME = ('%s.jpeg' % time.strftime("%Y%m%d-%H%M%S"))
	i.save('%s%s' % (PATH_TO_SAVE_IMAGE, FILE_NAME))
	return Response('%s saved' % FILE_NAME)

@app.route('/check', methods=['POST'])
def check():
    DIR = '/home/aravinda/Image Acquisition/images/' + NAME
    counter = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    return render_template("getImage.html", action="Add", counter=counter)

@app.route('/favicon.ico')
def favicon():
    return Response(open('./favicon.ico').read(), mimetype = "image/ico")
if __name__ == '__main__':
	app.run(debug = True, threaded = True, host = '0.0.0.0', ssl_context = 'adhoc') 
