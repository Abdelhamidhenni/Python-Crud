from flask import Flask
from apps.hello import app_hello
from apps.user import app_user
from apps.auth import app_auth

app = Flask(__name__)
app.register_blueprint(app_hello)
app.register_blueprint(app_user)
app.register_blueprint(app_auth)


if __name__ == "__main__":
    app.run(debug=True,host= "0.0.0.0", port=3000)
