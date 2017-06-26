#Jim Vargas

from flask import Flask, request, redirect
import cgi
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <form method= 'POST'>
                <label> Rotate by: 
                    <input name= "rot" type= "text" value= '0' />
                </label>
            
                <label> Text to encrypt:
                    <textarea name= "text" >{0}</textarea>
                </label>
                <input type= "submit" value= "DoTheThing" />
            </form>
        </body>
    </html>
"""

@app.route("/")
def index():
    new = ""
    return form.format(new)


@app.route("/", methods= ['POST'])
def encrypt():
    rot = int(
        cgi.escape(
            request.form['rot']
            )
        )
    text = cgi.escape(
        request.form['text']
    )
    new = rotate_string(text, rot)

    SpitThing = ("<h1>The thing you entered:</h1>" + 
        "<p>" + text + "</p>" +
        "<h1>Your encrypted text:</h1>" + 
        "<p>" + new + "</p>")

    return form.format(new)

app.run()