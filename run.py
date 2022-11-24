import os   # Stardard python library, built-in variable 
from flask import Flask     # Importing the Flask Class

# Create an instance of this class and store it in the app variable
app = Flask(__name__)


# Route decorator to tell Flask what URL should trigger the function
@app.route("/")
def index():
    return "Hello, World"


# Using the os module to get the 'IP' environment variable if it exists
# but set a default value if it's not found
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
