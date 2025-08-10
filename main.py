from flask import Flask, render_template, request, redirect
from email_logic import gmail_compose_url
from AI_model import give_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
        recipients = request.form.get('Recipients')
        prompts = request.form.get('Prompts')
        subject = give_response("""Write a short, impactful, and attention-grabbing email subject line based on the following prompt.
The subject should match the tone and purpose of the email, be concise (ideally under 10 words), and encourage the recipient to open it.
If key details are missing, fill them in logically to make the subject line relevant and compelling.
Do not include any part of the email body, greeting, closing, or extra explanation — return only the subject line.

here id the Email context: """ + prompts)
        body = give_response("""Write only the main body text for an email based on the following prompt.
Do not include a subject line, greeting, closing, signature, or any extra explanation.
Use a tone (formal, semi-formal, or informal) that fits the context, but do not mention the tone in your response.
If details are missing, fill them in logically to make the email clear and coherent.
Keep the length appropriate for the situation — concise for quick updates, more detailed for explanations or invitations.
Respond with only the email body text, nothing else.

Here is the Email context:  """+prompts)
       # print(f"subject:- {subject}")
       # print(f"{body}")
        url = gmail_compose_url(recipients, str(subject), str(body))
        return redirect(url)

   return render_template('home.html')

if __name__ == '__main__':
   app.run(debug=True)
