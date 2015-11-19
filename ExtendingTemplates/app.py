from flask import Flask, render_template  #NEW IMPORT!!

app = Flask(__name__)    #This is creating a new Flask object

#decorator that links...

@app.route('/')          								#This is the main URL
def default():
    return render_template("index.html", name = "Index", title = "HOME PAGE")			#The argument should be in templates folder


@app.route('/index')          							#This is the main URL
def index():
    return render_template("index.html", name = "Index", title = "HOME PAGE")			#The argument should be in templates folder


@app.route('/courses')          							#This is the main URL
def courses():
    return render_template("courses.html", name = "Courses", title = "COURSES PAGE")


@app.route('/interests')          							#This is the main URL
def interests():
    return render_template("interests.html", name = "Interests", title = "INTERESTS PAGE")

@app.route('/other')          							#This is the main URL
def other():
    return render_template("other.html", name = "Other", title = "OTHER PAGE")


#general approach:
#@app.route('/<name>')          							#This is the main URL
#def home(name):
    #return render_template("%s.html" % name, name = name)	#The argument should be in templates folder


if __name__ == '__main__':
    app.run(debug=True, port=4500)		#debug=True is optional
