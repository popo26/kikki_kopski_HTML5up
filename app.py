from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/pieces")
# def pieces():
#     return render_template("work.html")

if __name__ == "__main__":
    app.run(debug=True)
