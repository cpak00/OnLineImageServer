#! /usr/bin/python3
# this python code use decode function, which must be used in python3.x
from bottle import route, run, request, static_file, get
from config import IP_ADDRESS
import os


@route('/static/img/<filename>')
def server_static(filename):
    # currentPath = os.path.dirname(os.path.realpath(__file__))
    return static_file(filename, root='./static/img')


@route('/static/js/<filename>')
def server_static(filename):
    # currentPath = os.path.dirname(os.path.realpath(__file__))
    return static_file(filename, root='./static/js')


#文件上传的HTML模板，这里没有额外去写html模板了，直接写在这里，方便点吧
@route('/upload')
def upload():
    return '''
        <html>
            <head>
            </head>
            <body>
                <form action"/upload" method="post" enctype="multipart/form-data">
                    <input type="text" name="filename" />
                    <input type="file" name="data" />
                    <input type="submit" value="Upload" />
                </form>
            </body>
        </html>
    '''


#文件上传，overwrite=True为覆盖原有的文件，
#如果不加这参数，当服务器已存在同名文件时，将返回“IOError: File exists.”错误
@route('/upload', method='POST')
def do_upload():
    upload = request.files.get('data')
    path = "./static/img/" + request.forms.get('filename')
    upload.save(path, overwrite=True)  #把文件保存到save_path路径下
    return 'ok'


run(host=IP_ADDRESS, port=80)
