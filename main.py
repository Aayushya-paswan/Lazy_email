from flask import Flask, render_template, request
from email_logic import gmail_compose_url
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('home.html')

if __name__ == '__main__':
   app.run(debug=True)
