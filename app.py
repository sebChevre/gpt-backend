import os
from flask import Flask, request
from dotenv import load_dotenv
from healthcheck import HealthCheck, EnvironmentDump
from service.prompt_processor import ask

import logging

# TODO pour load env via script
load_dotenv()
# Logging
file_handler = logging.FileHandler(filename=os.getenv('LOG_FILE'))
handler = logging.StreamHandler()

logging.basicConfig(level=logging.DEBUG, handlers=[file_handler, handler])
app = Flask(__name__)


# Healthcheck
def app_available():
    if app is not None:
        return True, "app ok"


health = HealthCheck()
health.add_check(app_available)
envdump = EnvironmentDump()

# Add a flask route to expose information
app.add_url_rule("/environment", "environment", view_func=lambda: envdump.run())
app.add_url_rule("/health", "healthcheck", view_func=lambda: health.run())


@app.route('/chat', methods=['POST'])
def chat():  # put application's code here
    body = request.json
    prompt = body['prompt']
    response = ask(prompt)
    return response


# Pour lancement via script, hors serveur flask
if __name__ == '__main__':
    logging.debug("From main...")
    load_dotenv()
    app.run()
