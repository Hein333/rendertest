import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    # Prints to the server log console on Render
    print("Hello, World! I like apple")
    # Displays in the web browser when someone visits your Render URL
    return "Hello, World! I like apple"

if __name__ == "__main__":
    # Render assigns a dynamic PORT environment variable
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
