from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.data = []

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        if request.form.get('adddata') == 'Add Student Record':
            return render_template("adddata.html")
            
        elif request.form.get('getdata') == 'Get Student Record':
            return redirect(url_for("get_data"))
        
        else:
            return render_template("home.html")
        
    elif request.method == 'GET':
        return render_template("home.html")
    
    return render_template("home.html")

@app.route("/adddata", methods=['POST', 'GET'])
def add_data():
    if request.method == 'POST':
        data = request.form
        print(data)
        app.data.append(data)
        return redirect(url_for("home"))

@app.route("/getdata", methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        return render_template("getdata.html", data=app.data)


if __name__ == '__main__':
    app.run(debug = True)