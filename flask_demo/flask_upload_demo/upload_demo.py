from flask import Flask,request,render_template,send_from_directory
from werkzeug.utils import secure_filename    #生成安全的文件名
from forms import Uploadform   #导入自定义的文件验证器
from werkzeug.datastructures import CombinedMultiDict #将两个不可变的类型组合在一起
import os

UPLOAD_PATH=os.path.join(os.path.dirname(__file__),"images")  #定义要存放的文件夹路径

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/upload/',methods=['GET','POST'])
def Upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        #验证文件，后再执行下面的代码
        form = Uploadform(CombinedMultiDict([request.form,request.files]))
        #注释：因为request.form,是不可变类型，所有使用CombinedMultiDict方法将文件描述信息和文件组合在一起，
        # 然后传给Uploadform去验证。
        if form.validate():  #如果验证通过，则执行下面的代码
            #1、获取描述信息 2、获取文件
            # (另外一种通过表单获取信息的方式：desc=form.desc.data 和 avatar=form.avatar.data)
            desc = request.form.get("desc")     #获取上传文件的描述信息
            avatar = request.files.get("avatar")   #获取用户上传的文件

            filename = secure_filename(avatar.filename)  #安全验证文件名称
            print(filename)
            avatar.save(os.path.join(UPLOAD_PATH,filename))  #保存客户端上传的文件，参数1是存放路径，2是文件名称
            print(desc)
            return "上传成功"
        else:
            print(form.errors)
            return "上传失败  原因：%s" % form.errors


@app.route('/images/<filename>/')
def get_images(filename):
    #客户端获取文件，使用send_form_directory函数
    return send_from_directory(UPLOAD_PATH,filename)

if __name__ == '__main__':
    app.run(debug=True)
