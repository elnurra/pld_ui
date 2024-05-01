from flask import Flask, render_template, request

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
     return render_template('home.html')

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
@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html', companies=companies_awaiting_approval)

@app.route('/approve_company', methods=['PUT'])
def approve_company():
    company_id = int(request.form['company_id'])
    for company in companies_awaiting_approval:
        if company['id'] == company_id:
            company['approved'] = True
            break
    return 'Company Approved Successfully'
if __name__ == '__main__':
    app.run(debug=True)
