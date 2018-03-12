from flask import Flask,request,render_template
from forms import SettingsForm


app = Flask(__name__)



@app.route('/')
def hello_world():
	return 'Hello World!'


@app.route("/settings/",methods=['GET','POST'])
def Settings():
	if request.method == "GET":
		form =SettingsForm()
		return render_template('settings.html',form=form)
	else:

		form = SettingsForm(request.form)
		pass




if __name__ == '__main__':
	app.run(debug=True,port=4000)
