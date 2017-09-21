from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

encrypted = ''

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                display: block;
                text-align: right;
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
      <form action="/" method="post">
        <label for="rot">Rotate by:</label>
            <input type="text" name="rot" placeholder="0">
        
            <textarea name="text">{0}</textarea>
    <input type="submit" value="Submit Query"/>
    </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    rot = int(rot)
    message = request.form['text']

    encrypted = rotate_string(message, rot)

    return form.format(encrypted)


app.run()
