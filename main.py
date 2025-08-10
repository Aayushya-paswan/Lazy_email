from flask import Flask, render_template, request, redirect
from email_logic import gmail_compose_url
from AI_model import give_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
        recipients = request.form.get('Recipients')
        prompts = request.form.get('Prompts')
        subject = give_response("""Generate only a concise subject line for the following email content. 
        Do not include any explanation, greeting, punctuation outside the subject, or quotation marks. 
        Only return the subject text itself.

        Email content:
        """ + prompts)
        body = give_response("""Write a clear, engaging email body based on the following prompt.  
        Determine whether the tone should be formal, semi-formal, or informal depending on the context.  
        If the prompt lacks necessary details, fill them in logically to make the email complete and coherent.  
        Keep the length appropriate for the context — concise for short updates, detailed for explanations or invitations.  
        Avoid writing the subject line, greetings, or closings unless specifically asked.  
        Only return the main body text of the email.

        Prompt:

        """+prompts)
       # print(f"subject:- {subject}")
       # print(f"{body}")
        url = gmail_compose_url(recipients, str(subject), str(body))
        return redirect(url)

   return render_template('home.html')

if __name__ == '__main__':
   app.run(debug=True)
