from flask import Flask, render_template_string, request   # Importing the Flask modules required for this project
import RPi.GPIO as GPIO     # Importing the GPIO library to control GPIO pins of Raspberry Pi
from time import sleep      # Import sleep module from time library to add delays
 
# Pins where we have connected servos
servo_pin = 26          
servo_pin1 = 19
 
GPIO.setmode(GPIO.BCM)      # We are using the BCM pin numbering
# Declaring Servo Pins as output pins
GPIO.setup(servo_pin, GPIO.OUT)     
GPIO.setup(servo_pin1, GPIO.OUT)
 
# Created PWM channels at 50Hz frequency
p = GPIO.PWM(servo_pin, 50)
p1 = GPIO.PWM(servo_pin1, 50)
 
# Initial duty cycle
p.start(0)
p1.start(0)
 
# Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)
# Enable debug mode
app.config['DEBUG'] = True
 
# which URL should call the associated function.
@app.route("/")
def home():
    return render_template_string('index.html')
 
@app.route("/test", methods=["GET", "POST"])
def test():
    data = request.get_json()
    dutycycle = data['dutycycle']
    if request.method == 'POST':
        if request.form.get('action1') == 'UP':
            p.ChangeDutyCycle(float(dutycycle))
        elif request.form.get('action2') == 'DOWN':
            p.ChangeDutyCycle(float(dutycycle))
    # Give servo some time to move
    sleep(1)
    # Pause the servo
    p.ChangeDutyCycle(0)
    
    return render_template_string('index.html')
 
# Run the app on the local development server
if __name__ == "__main__":
    app.run()