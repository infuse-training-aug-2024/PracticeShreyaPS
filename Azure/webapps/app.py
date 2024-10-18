import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Access the environment variable
    my_variable = os.getenv('my_variable')
    return f"Value of MY_VARIABLE is: {my_variable}"

if __name__ == "__main__":
    app.run()
