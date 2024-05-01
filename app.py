from flask import Flask, render_template

app = Flask(__name__)

# Mock data for companies awaiting approval
companies_awaiting_approval = [
    {"name": "Company A"},
    {"name": "Company B"},
    {"name": "Company C"}
]

# Mock data for admins
admins = [
    {"username": "admin1"},
    {"username": "admin2"}
]

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', companies=companies_awaiting_approval)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/wait')
def wait():
    return render_template('wait.html')
if __name__ == '__main__':
    app.run(debug=True)
