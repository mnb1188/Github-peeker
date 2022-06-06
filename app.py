from flask import Flask
from External_func import *

app = Flask(__name__)

from routes import *


def main():
    app.run(debug=True)
    

if __name__ == "__main__":
    main()