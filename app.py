import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from flask import Flask
from flask import render_template , request
from price_prediction.cabbage import Cabbage
from member.member import Student, StudentService
app =Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('join.html')
@app.route('/move/<path>')
def move(path):
    return render_template(f'{path}.html')

@app.route("/cabbage", methods =['POST'])
def cabbege():
    print('UI~API Connect Success')
    avgTemp = request.form['avgTemp']
    minTemp = request.form['minTemp']
    maxTemp = request.form['maxTemp']
    rainFall = request.form['rainFall']
    print(f'favgTemp:  {avgTemp}')
    print(f'minTemp:  {minTemp}')
    print(f'maxTemp:  {maxTemp}')
    print(f'rainFall:  {rainFall}')
    cabbage = Cabbage() 
    cabbage.avgTemp = avgTemp
    cabbage.minTemp = minTemp
    cabbage.maxTemp = maxTemp
    cabbage.rainFall = rainFall
    result= cabbage.service()
    print(f'***********   {result}')
    render_params ={}
    render_params['result'] = result
    return render_template('index.html', **render_params)
@app.route('/signup',methods =['POST'])
def signup():
    print(' ####### SIGHNUP########')
    id = request.form['id']
    pwd = request.form['pwd']
    name = request.form['name'] 
    birth = request.form['birth'] 
    student = Student()
    student.id = id
    student.pwd = pwd
    student.name = name
    student.birth = birth
    service = StudentService()
    service.add_students(student)
    student = service.login(id,pwd)
    
    print(f'{student} 접속중....')

    return render_template(f'login.html')
@app.route('/signin', methods=['POST'])
def signin():
    print(' ######  SIGNIN #########')
    id = request.form['id']
    pwd = request.form['pwd']
    service = StudentService()
    name = service.login(id, pwd)
    render_params = {}
    render_params['name'] = name
    return render_template(f'index.html', **render_params)
 

if __name__ == "__main__":
    app.run()
    
