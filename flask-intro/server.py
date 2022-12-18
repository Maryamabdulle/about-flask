"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = [
  'stupid', 'ugly', 'mean', 'slow'
]

@app.route('/')
def start_here():
    """Home page."""

    return """
      <!doctype html>
        <html>
          <p>Hi! This is the home page.</p>
          <a href="/hello">Hello</a>
        </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""
      
    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
        </form>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <div>
                <label for="compliment_choice">Choose your compliment:</label>
                <select name="compliment" id="compliment_choice">
                    <option value="awesome">awesome</option>
                    <option value="terrific">terrific</option>
                    <option value="neato">neato</option>
                    <option value="fantabulous">fantabulous</option>
                    <option value="wowza">wowza</option>
                    <option value="oh-so-not-meh">oh-so-not-meh</option>
                    <option value="brilliant">brilliant</option>
                    <option value="ducky">ducky</option>
                    <option value="coolio">coolio</option>
                    <option value="incredible">incredible</option>
                    <option value="wonderful">wonderful</option>
                    <option value="smashing">smashing</option>
                    <option value="lovely">lovely</option>
                </select>
            </div>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """
@app.route('/diss')    
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    insult = choice(INSULTS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}!
      </body>
    </html>
    """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")