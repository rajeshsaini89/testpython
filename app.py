from flask import Flask, redirect, url_for, request,render_template

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
	return "welcome %s" % name

@app.route('/login',methods=['POST','GET'])
def login():
	if request.method == 'POST':
		username = request.form['nm']
		return redirect(url_for('success',name = username))
	else:
		username = request.args.get('nm')
		return redirect(url_for('success',name = username))

@app.route('/')
def index():
	#return render_template('hello.html')
	return "This is a template"





if __name__ == '__main__':
	app.run()	