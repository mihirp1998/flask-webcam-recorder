from flask import Flask,render_template,request,send_from_directory
app = Flask(__name__)
 
@app.route("/")
def hello():
    return render_template("temp.html")

@app.route("/whammy.js")
def wham():
    return render_template("whammy.js")

@app.route("/jquery-3.2.1.min.js")
def jq():
    return render_template("jquery-3.2.1.min.js")

@app.route("/style.css")
def style():
	return send_from_directory('./static', 'style.css')	

@app.route('/upload', methods = [ 'POST'])
def upload_file(): 
	print(request.files,request.form)
	request.files['data'].save("/home/mihir/projects/new/{}.webm".format(request.form["fname"]))
	return "success"

if __name__ == "__main__":
    app.run()

