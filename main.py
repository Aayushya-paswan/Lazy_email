from flask import Flask, render_template, request
from email_logic import gmail_compose_url
from AI_model import give_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
      pass
   return render_template('home.html')

if __name__ == '__main__':
   app.run(debug=True)
