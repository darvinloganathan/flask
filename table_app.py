from flask import *
app = Flask(__name__)
@app.route('/')
def customer():
    return render_template('client.html')
@app.route('/success', methods=['POST', 'GET'])
def print_data():
    if request.method == 'POST':
        result = request.form
        return render_template("form.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)