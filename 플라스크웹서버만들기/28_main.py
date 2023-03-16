#28 플라스크 웹서버 만들기

## pip install flask - 파이썬 언어를 이용하여 웹을 개발할 수 있게 해주는 웹 개발 프레임워크 / 가볍게 동작이 가능하고 사용도 쉬운 플라스크


### flask로 간단한 웹서버 만들고 구동하는 코드 만들기

from flask import Flask
from flask import render_template
import time

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/1')
def test1page():
    return "1page ok"

@app.route('/2')
def test2page():
    return "2page ok"

@app.route('/map')
def mapPage():
    return render_template("uni_map.html")

def main():
    app.run(debug=True, port=80)
    time.wait(100)
    
    

if __name__ == '__main__':
    main()