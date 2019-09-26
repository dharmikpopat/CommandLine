from flask import Flask, render_template, request
from main import fetch


app = Flask(__name__)


# @app.route('/',methods=['POST'])
# def hello():
# 	cmd = request.args.get('Command')
# 	Fetch = fetch(cmd)
  

# @app.route('/')
# def index():
# 	return render_template('index.html')

@app.route('/', methods=['GET'])
def ice():	
	return render_template('index.html')

@app.route('/login', methods=['GET'])
def fire():
	cmd = request.args.get('command')
	#fetch = Fetch(cmd)
	return render_template('layout.html' , var = cmd)


if __name__ == '__main__':
	app.run(debug = True)