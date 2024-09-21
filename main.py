from flask import Flask, request, jsonify, make_response, redirect, url_for, render_template


app = Flask(__name__)

@app.route('/')
def index():
    response = make_response(redirect('/login'))
    return response

userip = False

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('information.html', userip=userip)


app.run(host='0.0.0.0',port=5000, debug=True)


