from flask import Flask, request
#from flask import Flask, render_template, request, redirect, url_for, send_from_directory,jsonify



app = Flask(__name__)

@app.route("/communicate", methods=['POST'])
def communicate():
    some_json=request.get_json()
    #sessionid = some_json['session']
    #text = some_json['text']  
    response = "YOLO"  
    return str(response)

if __name__=='__main__':
    app.run(debug=True)


"""
app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host=0.0.0.0, port=8080, debug=True)

"""