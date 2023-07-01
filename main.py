from flask import Flask ,request,render_template
  
app = Flask(__name__) #creating the Flask class object   
import qrcode
 
# Data to be encoded
def get_getqr(data):

# Encoding data using make() function
    img = qrcode.make(data) 
 
# Saving as an image file
    img.save('./static/pic.png')
@app.route('/',methods =['GET', 'POST'])#decorator drfines the   
def home():
    if request.method=="POST":
        Data=request.form["link"]
        get_getqr(Data)

    return render_template("home.html",bata=Data) 
  
if __name__ =='__main__':  
    app.run(debug = True)  