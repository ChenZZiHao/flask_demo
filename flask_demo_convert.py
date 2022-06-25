from flask import Flask
from werkzeug.routing import BaseConverter


app = Flask(__name__)

class RegexConverter(BaseConverter):

    def __init__(self, url_map, regex):
        """继承通用转换器类"""
        super(RegexConverter, self).__init__(url_map)
        self.regex = regex

    def to_python(self, value):
        """父类的方法"""
        return value

"""实例化对象"""
app.url_map.converters['re'] = RegexConverter

"""自定义规则,正则"""
@app.route('/keji/<re("6\d{2}"):value>')
def index(value):
    return "success"

"""已有规则"""
@app.route("/demo/<int:id>")
def demo(id):
    if id == 1:
        return "success"
    else:
        return "error"

if __name__ == '__main__':
    app.run()