from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
  return render_template('templates/hello.html')

if __name__ == '__main__':
  app.run(debug=True)
