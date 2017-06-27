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
                .error {{ color: red }}
            </style>
        </head>
        <body>
            <form method= 'POST'>
                <label> Rotate by: 
                    <input name= "rot" type= "text" value= '0' />
                </label>
                <p class= "error"> {rot_error} </p>
                <label> Text to encrypt:
                    <textarea name= "text" >{new}</textarea>
                </label>
                <input type= "submit" value= "DoTheThing" />
            </form>
        </body>
    </html>
"""

@app.route("/")
def index():
    new = ""
    rot_error = ""
    return form.format(rot_error= rot_error, new= new)


def IsInteger(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


@app.route("/", methods= ['POST'])
def encrypt():
    rot = cgi.escape(
        request.form['rot'])
    text = cgi.escape(
        request.form['text'])

    rot_error = ""

    if not IsInteger(rot):
        rot_error= "Not a valid integer"
        rot = ""
    else:
        rot = int(rot)

    if not rot_error:
        new = rotate_string(text, rot)
        return form.format(rot_error="", new= new)
    else:
        return form.format(rot_error= rot_error, new= text)

app.run()