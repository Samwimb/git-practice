from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    #! TODO: implement home page SAM
    s = validation(s)
    return "hello world"

def validation(s):
    """validate input

    Args:
        s (str): the input str
    """
    # ! TODO implement validation FELIPE
    return s

if __name__ == "__main__":
    app.run()