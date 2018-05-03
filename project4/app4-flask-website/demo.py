from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("demo.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

# First line imports Flask class from flask package
# Instantiate Flask object
# Last two lines mean run the script when youre running the script from your terminal
# If running this script from another script, then __name__ == name of the script


