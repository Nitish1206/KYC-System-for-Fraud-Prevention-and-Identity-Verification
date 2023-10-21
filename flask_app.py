from flask import Flask, render_template, request,flash,redirect,url_for
import numpy as np
import cv2
import base64
import time
from face_recognition.face_recognition_helper import *
# from text_extractor.extract_doc_info import get_card_details
import easyocr
from match_helper import match_data
app = Flask(__name__)
#
app.config['SECRET_KEY'] = "d83f0d82a5c995fa664c517a88e4ae8ab57aca26d56c9fe6bf5bc0c65a705f86" #setup secret key

# from OpenSSL import SSL
# context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
# context.use_privatekey_file('server.key')
# context.use_certificate_file('server.crt')

@app.route('/')
def render_kyc_form():
    return render_template('index.html')

@app.route('/validate' , methods=['POST',"GET"])
def validate():
    if request.method == 'POST':
        # Retrieve form data from the request
        card_choice = request.form.get('card-choice')
        name = request.form.get('name')
        address = request.form.get('address')
        phone_number = request.form.get('phone-number')
        dob = request.form.get('dob')
        # print("===>>>",dob)
        date_parts = dob.split('-')
        dob = f"{date_parts[2]}/{date_parts[1]}/{date_parts[0]}"
        # print("===>>>2",dob)

        gender = request.form.get('gender')
        father_name = request.form.get('father-name')
        mother_name = request.form.get('mother-name')
        image_upload = request.files['image_upload']
        
        aadhar_number = None
        pan_number = None
        if card_choice == "Aadhar Card":
            aadhar_number = request.form.get('aadhar-card-number')
            input_data={"name":name,"address":address,"phone_number":phone_number,"dob":dob,"gender":gender,
                    "father_name":father_name,"mother_name":mother_name,"aadhar_number":aadhar_number}
        if card_choice == "PAN Card":
            pan_number = request.form.get('pan-card-number')
            input_data={"name":name,"address":address,"phone_number":phone_number,"dob":dob,"gender":gender,
                    "father_name":father_name,"mother_name":mother_name,"pan_number":pan_number}


        
        formdata=True

        print("#"*50,aadhar_number)

        if image_upload:
            # Read the uploaded image using OpenCV
            image_stream = image_upload.read()
            image_array = np.frombuffer(image_stream, np.uint8)
            image_ = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
            status,image=recognition_model.detect_and_store_embedding(image_,"aadhar")
            cv2.imwrite("card.jpg",image_)

            card_detail = reader.readtext('card.jpg')
            print("===>>>",card_detail)

            match_res=match_data(card_detail,input_data)
            print("***************",list(match_res.keys()),"***********************")
            if aadhar_number != None:

                match_keys=["name","aadhar_number","dob"]
            if pan_number != None:
                match_keys=["name","pan_number","dob"]


            # for key_ in match_keys:
            match_res_list=list(match_res.keys())

            if((set(match_keys) & set(match_res_list)) == set(match_keys)):
                formdata=True

            else:
                formdata=False


        if formdata== False:
            flash('Data did not matched', 'error')
            return redirect(url_for('render_kyc_form'))

        if formdata== True and status != "success":
            flash('face not found !', 'error')
            return redirect(url_for('render_kyc_form'))

        if formdata== True and status == "success":
            # flash('Data did not matched', 'error')
            return redirect(url_for('render_validator'))


@app.route('/verify' , methods=['POST','GET'])
def render_validator():
    return render_template('verification.html')

@app.route('/compare' , methods=["POST",'GET'])
def compare_embeddings():
    global acc
    acc=-1
    # time.sleep(3)
    if request.method == 'POST':
        data = request.json
        print(data.keys())
        if "image" in data:
            # try:
            # Extract and decode the base64 image data
            image_data = data["image"].split(",")[1]
            image_data = base64.b64decode(image_data)

            # You can save the image to a file, process it, or perform other operations here
            # For example, save the image to a file named 'snapshot.png'
            with open('snapshot.png', 'wb') as f:
                f.write(image_data)

            image_=cv2.imread("snapshot.png")

            status,image=recognition_model.detect_and_store_embedding(image_,"live")
            
            status,acc_=recognition_model.find_similarity()
            # print("accuracy==>>>",acc)
            if float(acc_) > 0.4:
                acc="auth"
            else:
                acc="denied"

            return {"redirect_url": '/message?acc={}'.format(acc)}
        


@app.route('/message')
def message_page():
    print("inside msg")
    acc = request.args.get('acc', '')

    if acc == "auth":

        message="verified! your face matches with ID card face"
    else:
        message="verification denied face does not match with ID card face"

    return render_template('auth_message.html', message=message)

if __name__ == '__main__':
    recognition_model=Face_recogntion()
    reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory

    app.run(host='0.0.0.0' , port=5000 , debug=False)
