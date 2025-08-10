import urllib.parse

def gmail_compose_url(to, subject, body):
    base_url = "https://mail.google.com/mail/?view=cm&fs=1"
    params = {
        "to": to,
        "su": subject,
        "body": body
    }
    return base_url + "&" + urllib.parse.urlencode(params)

if __name__ == "__main__":
    to_email = "test@example.com"
    subject = "Hello from Lazy Email"
    body = "This is a pre-filled email body."
    url = gmail_compose_url(to_email, subject, body)
    print("Open this URL:", url)
