#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 15:21:26 2020

@author: root
"""

from text import filet

import os
from flask import Flask, flash, request, redirect, url_for,render_template,send_file,jsonify
from werkzeug.utils import secure_filename
from flask import send_from_directory
import zipfile


'''
#For cloud inclusion

import pyrebase


config= {
  "apiKey": "AIzaSyDm74MstaU-s9QYT14Bl5yu8fBoax9GjRY",
  "authDomain": "silfra-test.firebaseapp.com",
  "databaseURL": "https://silfra-test.firebaseio.com",
  "projectId": "silfra-test",
  "storageBucket": "silfra-test.appspot.com",
  "messagingSenderId": "1095851913479",
  "appId": "1:1095851913479:web:b269fb5363df9b31f715a2",
  "measurementId": "G-BYPZXRVM84"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
storage.child('/images/foo.txt').put('requirements.txt')

storage.child('/images/foo.txt').download('a.txt')
'''


app = Flask(__name__)
email = "null"
global dict1
dict1 ={}
msg = " "
#SHOW_FOLDER = '/root/ODU/Subjective-Answer- mod/DataSetCollectorFlaskApp/'
UPLOAD_FOLDER = '/root/Silfra'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config['SHOW_FOLDER'] = SHOW_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/')
def Base():
    return render_template('form.html',msg="")




@app.route('/sub_form', methods=['POST', 'GET'])
def sub_form():
    msg=""
    
    if request.method == 'POST':
      if 'file' not in request.files:
        msg = "No file part"
        return render_template('form.html', msg =msg)
  
      file = request.files['file']
      '''
      if request.form['lang']=='english':
          lang = 'english'
      if request.form['lang']=='hindi':
          lang = 'hi'
      if request.form['lang']=='kannada':
          lang='kannada'
      if request.form['lang']=='malyalam':
          lang='malayalam'
      if request.form['lang']=='gujarati':
          lang='gujarati' 
      if request.form['lang']=='telugu':
          lang='telugu' 
      if request.form['lang']=='tamil':
          lang='tamil' 
          '''
      if 'lang' not in request.form:
          msg="No input language"
          return render_template('form.html',msg=msg)
      if 'to_lang' not in request.form:
          msg = "NO from language"
          return render_template('form.html',msg=msg)
      lang=request.form['lang']
      
      
      
      to_lang = request.form['to_lang']
      
      
      
      
      
      
      if request.form['lang']=='pa':
          lang='pa' 
      
          
      '''    
      if request.form['to_lang']=='english':
          lang = 'english'
      if request.form['to_lang']=='hindi':
          lang = 'hi'
      if request.form['to_lang']=='kannada':
          lang='kannada'
      if request.form['to_lang']=='malyalam':
          lang='malayalam'
      if request.form['to_lang']=='gujarati':
          lang='gujarati' 
      if request.form['to_lang']=='telugu':
          lang='telugu' 
      if request.form['to_lang']=='tamil':
          lang='tamil' 
      if request.form['to_lang']=='pa':
          lang='pa' 
          
       '''
      #to_lang = request.form['to_lang']
       
          
      if file.filename == '':
            
            return render_template('form.html', msg ="no selection")
      if (allowed_file(file.filename)==False):
          return render_template('form.html',msg="Unsupported file choosen")  
      if file and allowed_file(file.filename):
            global filename 
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename,lang=lang,to_lang=to_lang))  
    
      
      
    return render_template('form.html')     
     
    
@app.route('/uploads/<filename>/<lang>/<to_lang>')
def uploaded_file(filename,lang,to_lang):
    filet(filename,lang,to_lang)
    
    
    '''
    
    zipf = zipfile.ZipFile('/root/Silfra/'+filename.rsplit( ".", 1 )[ 0 ]+'.zip','w', zipfile.ZIP_DEFLATED)
    for root,dirs, files in os.walk('/root/Silfra'):
        for file in files:
            zipf.write('/root/Silfra/'+file)
    zipf.close()
    '''
    '''
    return send_file('/root/Silfra/Name.zip',
            mimetype = 'zip',
            attachment_filename= 'Name.zip',
            as_attachment = True)
    
    '''
    
    return render_template('Submit.html')
    
   # filename='Name.zip'
   # return send_from_directory(app.config['UPLOAD_FOLDER'],
   #                           filename)


@app.route('/show_form', methods=['POST', 'GET'])
def show_form():
    
    if request.form['submit']=='original':
         return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

    if request.form['submit'] == 'text':
        fild = filename
        fild= fild.rsplit( ".", 1 )[ 0 ]
        fild = fild+".txt"
        return send_from_directory(app.config['UPLOAD_FOLDER'],fild)

    if request.form['submit'] == 'transe':
        fild = filename
        fild= fild.rsplit( ".", 1 )[ 0 ]
        fild = fild+"new.txt"
        return redirect(url_for('get_json'))
        #return send_from_directory(app.config['UPLOAD_FOLDER'],fild)

    if request.form['submit'] == 'another':
        return render_template('form.html')

@app.route('/get_json')
def get_json():
        dict1["status"]="fail"
        fild = filename
        fild= fild.rsplit( ".", 1 )[ 0 ]
        fild = fild+"new.txt"
        fopen = open('/root/Silfra/'+fild)
        content = fopen.read()
        n=fild
        
        
        
        dict1["output"] = content
        
        fopen.close()
        fild = filename
        fild= fild.rsplit( ".", 1 )[ 0 ]
        fild = fild+".txt"
        fopen = open('/root/Silfra/'+fild)
        content = fopen.read()
        n=fild
        
        dict1["input"] = content
        dict1["status"]="success"
        return jsonify(dict1)
    
if __name__ == '__main__':
    app.run(debug=True)
    
