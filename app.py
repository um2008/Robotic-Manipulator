from flask import Flask, jsonify, render_template
import RPi.GPIO as GPIO
from time import sleep

app = Flask(__name__)
app.config['DEBUG'] = True

servo1 = 17
servo2 = 22
servo3 = 18
servo4 = 24
grip = 25

dutycycle1 = 2.5
dutycycle2 = 2.5
dutycycle3 = 2.5
dutycycle4 = 2.5
dutycycle5 = 7.5

GPIO.setmode(GPIO.BCM) 

GPIO.setup(servo1, GPIO.OUT)
GPIO.setup(servo2, GPIO.OUT)
GPIO.setup(servo3, GPIO.OUT)
GPIO.setup(servo4, GPIO.OUT)
GPIO.setup(grip, GPIO.OUT)

p1 = GPIO.PWM(servo1, 50)
p2 = GPIO.PWM(servo2, 50)
p3 = GPIO.PWM(servo3, 50)
p4 = GPIO.PWM(servo4, 50)
p5 = GPIO.PWM(grip, 50)

p1.start(0)
p2.start(0)
p3.start(0)
p4.start(0)
p5.start(0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_dutycycle1')
def get_dutycycle1():
    global dutycycle1
    return jsonify({'dutycycle1': dutycycle1})

@app.route('/get_dutycycle2')
def get_dutycycle2():
    global dutycycle2
    return jsonify({'dutycycle2': dutycycle2})

@app.route('/get_dutycycle3')
def get_dutycycle3():
    global dutycycle3
    return jsonify({'dutycycle3': dutycycle3})

@app.route('/get_dutycycle4')
def get_dutycycle4():
    global dutycycle4
    return jsonify({'dutycycle4': dutycycle4})

@app.route('/get_grip')
def get_dutycycle5():
    global dutycycle5
    return jsonify({'dutycycle5': dutycycle5})

@app.route('/increment_dutycycle1', methods=['POST'])
def increment_dutycycle1():
    global dutycycle1
    dutycycle1 += 0.5
    p1.ChangeDutyCycle(float(dutycycle1))
    sleep(1)
    p1.ChangeDutyCycle(0)
    return jsonify({'dutycycle1': dutycycle1})

@app.route('/increment_dutycycle2', methods=['POST'])
def increment_dutycycle2():
    global dutycycle2
    dutycycle2 += 0.5
    # p2.ChangeDutyCycle(float(dutycycle2))
    # sleep(1)
    # p2.ChangeDutyCycle(0)
    return jsonify({'dutycycle2': dutycycle2})

@app.route('/increment_dutycycle3', methods=['POST'])
def increment_dutycycle3():
    global dutycycle3
    dutycycle3 += 0.5
    # p3.ChangeDutyCycle(float(dutycycle3))
    # sleep(1)
    # p3.ChangeDutyCycle(0)
    return jsonify({'dutycycle3': dutycycle3})

@app.route('/increment_dutycycle4', methods=['POST'])
def increment_dutycycle4():
    global dutycycle4
    dutycycle4 += 0.5
    # p4.ChangeDutyCycle(float(dutycycle4))
    # sleep(1)
    # p4.ChangeDutyCycle(0)
    return jsonify({'dutycycle4': dutycycle4})

@app.route('/grip', methods=['POST'])
def grip():
    global dutycycle5
    dutycycle5 += 5
    # p5.ChangeDutyCycle(float(dutycycle5))
    # sleep(1)
    # p5.ChangeDutyCycle(0)
    return jsonify({'dutycycle5': dutycycle5})

@app.route('/decrement_dutycycle1', methods=['POST'])
def decrement_dutycycle1():
    global dutycycle1
    if(dutycycle1>2):
        dutycycle1 -= 0.5
        p1.ChangeDutyCycle(float(dutycycle1))
        sleep(1)
        p1.ChangeDutyCycle(0)
    return jsonify({'dutycycle1': dutycycle1})

@app.route('/decrement_dutycycle2', methods=['POST'])
def decrement_dutycycle2():
    global dutycycle2
    if(dutycycle2>2):
        dutycycle2 -= 0.5
        # p2.ChangeDutyCycle(float(dutycycle2))
        # sleep(1)
        # p2.ChangeDutyCycle(0)
    return jsonify({'dutycycle2': dutycycle2})

@app.route('/decrement_dutycycle3', methods=['POST'])
def decrement_dutycycle3():
    global dutycycle3
    if(dutycycle3>2):
        dutycycle3 -= 0.5
        # p3.ChangeDutyCycle(float(dutycycle3))
        # sleep(1)
        # p3.ChangeDutyCycle(0)
    return jsonify({'dutycycle3': dutycycle3})

@app.route('/decrement_dutycycle4', methods=['POST'])
def decrement_dutycycle4():
    global dutycycle4
    if(dutycycle4>2):
        dutycycle4 -= 0.5
        # p4.ChangeDutyCycle(float(dutycycle4))
        # sleep(1)
        # p4.ChangeDutyCycle(0)
    return jsonify({'dutycycle4': dutycycle4})

@app.route('/release', methods=['POST'])
def release():
    global dutycycle5
    if(dutycycle5>7):
        dutycycle5 -= 5
        # p5.ChangeDutyCycle(float(dutycycle5))
        # sleep(1)
        # p5.ChangeDutyCycle(0)
    return jsonify({'dutycycle5': dutycycle5})

if __name__ == '__main__':
    app.run()