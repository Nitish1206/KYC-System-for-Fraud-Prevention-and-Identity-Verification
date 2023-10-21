# Importing flask module in the project is mandatory
# # An object of Flask class is our WSGI application.
# from flask import Flask
# from flask import Flask, render_template

# from face_recognition.face_recognition_helper import Face_recogntion
 
# # Flask constructor takes the name of
# # current module (__name__) as argument.
# app = Flask(__name__)
 
# # The route() function of the Flask class is a decorator,
# # which tells the application which URL should call
# # the associated function.
# @app.route('/')
# # ‘/’ URL is bound with hello_world() function.
# def kyc_valdator():
#     return render_template('kyc_validator.html')

# @app.route('/info')
# # ‘/’ URL is bound with hello_world() function.
# def kyc_valdator():
#     return render_template('kyc_validator.html')

# @app.route('/validate')
# # ‘/’ URL is bound with hello_world() function.
# def kyc_valdator():
#     return render_template('kyc_validator.html')
 
# # main driver function
# if __name__ == '__main__':
 
#     # run() method of Flask class runs the application
#     # on the local development server.
#     app.run()

# face_recognition_object=Face_recogntion()

pan="BUIPJ8414N"

aadhar="41613 2116 6461"

print(pan.lower())


date_="12/06/1998"
print(aadhar.lower())

print(date_.lower())

from difflib import SequenceMatcher

def similar(str1, str2):
    return SequenceMatcher(None, str1, str2).ratio()


ex_text="apurvasachinjoshi"
current_data="  apurvasachinjoshi "

ss=similar(ex_text,current_data)
print(ss)