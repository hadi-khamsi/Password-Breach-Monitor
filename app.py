from flask import Flask, render_template, request, redirect, url_for
from main import check_breach

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form['password']
        breach_status = check_breach(password)
        return redirect('/result/' + str(breach_status))  # Redirect to the 'display_result' route
    return render_template('index.html')

@app.route('/result/<breach_status>')
def display_result(breach_status):
    return render_template('result.html', breach_status=breach_status)

if __name__ == '__main__':
    app.run()