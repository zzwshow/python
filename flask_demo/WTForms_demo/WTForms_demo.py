from flask import Flask,request,render_template
from forms import SettingForm
app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World!'






if __name__ == '__main__':
    app.run(debug=True)
