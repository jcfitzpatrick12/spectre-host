from flask import Flask
from spectre_core.logging import configure_root_logger

from spectre_server.routes.start import start_blueprint
from spectre_server.routes.create import create_blueprint
from spectre_server.routes.delete import delete_blueprint
from spectre_server.routes.get import get_blueprint
from spectre_server.routes.test import test_blueprint
from spectre_server.routes.update import update_blueprint
from spectre_server.routes.web_fetch import web_fetch_blueprint

app = Flask(__name__)

# Register blueprints for modularity 
app.register_blueprint(start_blueprint, url_prefix="/start")
app.register_blueprint(create_blueprint, url_prefix="/create")
app.register_blueprint(delete_blueprint, url_prefix="/delete")
app.register_blueprint(get_blueprint, url_prefix="/get")
app.register_blueprint(test_blueprint, url_prefix="/test")
app.register_blueprint(update_blueprint, url_prefix="/update")
app.register_blueprint(web_fetch_blueprint, url_prefix="/web-fetch")


if __name__ == "__main__":
    configure_root_logger("USER")
    app.run(host="0.0.0.0", 
            port=5000, 
            debug=True)
