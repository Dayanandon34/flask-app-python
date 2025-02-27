from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''Welcome to Cloud Dayanand. Complete Devops practice session,
            This is Python - Flask APP, We have successfully created a CICD PIPELINE'''

@app.route('/health')
def health():
    return 'Server is up and running'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
