import time
import os

from flask import Flask


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY").encode()


@app.route("/time/")
def get_time():
    """
    Gets the current time in epoch time.
    """
    return str(int(time.time()))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host="0.0.0.0", port=port)
