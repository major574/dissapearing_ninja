from flask import Flask, session, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key='whatever'
@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")
@app.route('/ninjas')
def ninjaturtles():
	return render_template("ninjas.html", color = "turtles")
@app.route('/ninjas/<color>')
def turtle(color):
	rendercolor = "meg"
	print color
	if color.lower() == "red":
		rendercolor = "raph"
	elif color.lower() == "blue":
		rendercolor = "leo"
	elif color.lower() == "orange":
		rendercolor = "mike"
	elif color.lower() == "purple":
		rendercolor = "don"
	return render_template("ninjas.html", color = rendercolor)
app.run(debug=True)
