from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f')
@app.route('/f/<celsius>')
def celsius_to_fahrenheit(celsius=""):
    """Convert celsius to fahrenheit"""
    return '{} degrees celsius is {} degrees in fahrenheit.'.format(celsius, float(celsius) * 9.0 / 5 + 32)


if __name__ == '__main__':
    app.run()
