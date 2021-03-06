from flask import Flask
from apps.user import app_user
from apps.auth import app_auth
from apps.trans import app_trans

app = Flask(__name__)
app.register_blueprint(app_user)
app.register_blueprint(app_auth)
app.register_blueprint(app_trans)
if __name__ == "__main__":
    app.run(debug=True,host= "0.0.0.0", port=3000)
