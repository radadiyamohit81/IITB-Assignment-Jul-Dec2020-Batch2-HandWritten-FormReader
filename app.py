from PIL import Image
import os
import numpy as np
import glob
import sys,argparse
import tensorflow as tf
import flask
from flask import render_template, send_from_directory, request
from flask import redirect, url_for
from flask import jsonify
import base64
from io import StringIO
from werkzeug.utils import secure_filename
import requests
from io import BytesIO


app = flask.Flask(__name__)
UPLOAD_FOLDER=os.path.dirname(os.path.realpath(__file__))

sess = tf.Session(graph=tf.Graph())
tf.saved_model.loader.load(sess, ["serve"], os.path.dirname(os.path.realpath(__file__)) + "/exportedmodel")

def getImage(path):
    with open(path, 'rb') as img_file:
        img = img_file.read()
    return img

@app.route('/',methods=['POST','GET'])
def demo():
    if request.method == 'POST':
        url = request.form['text']
        response = requests.get(url)
        file = open("sample.png", 'wb')
        file.write(response.content)
        file.close()
        """upload_file = request.files['file']
        filename = secure_filename(upload_file.filename)
        upload_file.save(UPLOAD_FOLDER + '/' + filename)"""

        image = getImage("sample.png")
        send_res = {"response":[]}

        out = sess.run(['prediction:0', 'probability:0'], feed_dict={'input_image_as_bytes:0': image}) 
        
        if not type(out[1]) == np.ndarray:
            out[0] = [out[0]]
            out[1] = [out[1]]
        #temp = {"filename":image, "prediction":out[0][0].decode("utf-8"), "probability":out[1][0]}
        #send_res["response"].append(temp)
        result = {"prediction":str(out[0][0]), "prob":str(out[1][0])}
        
        return jsonify(result)
        



    return '''
     <!doctype html>
    <html lang="en">
    <head>
      <title>IITB Assignment</title>
    </head>
    <body>
    <div class="site-wrapper">
        <div class="cover-container">
          <div class="inner cover">
          </div>
          <div class="mastfoot">
          <hr />
            <div class="container">
              <div style="margin-top:5%">
		            <h1 style="color:black">Attention OCR Modified Model</h1>
		            <h4 style="color:black"> Upload the image URL (height <= 45px && width <= 650px) </h4>
		            <form method=post>
	                 <input name = "text">
                     <input type = "submit">
		            </form>
	            </div>
            </div>
        	</div>
     </div>
   </div>
</body>
</html>
    '''


if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)