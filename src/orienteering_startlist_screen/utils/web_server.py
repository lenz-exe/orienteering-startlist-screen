from datetime import datetime
from typing import Dict, List
from flask import Flask, jsonify, render_template
from werkzeug.serving import make_server
import threading
import time
import logging


logging.getLogger("werkzeug").setLevel(logging.WARNING)

def create_app(start_list: Dict[datetime, List], slot_seconds: int = 60, start_name: str = "") -> Flask:
    app = Flask(__name__)
    event_name = "Test-Event"

    @app.get("/api/now")
    def api_now():
        now_ms = int(time.time() * 1000)
        return jsonify({"now_ms": now_ms})

    @app.get("/")
    def index():
        slots_view = [
            {"start_dt": dt, "participants": plist}
            for dt, plist in sorted(start_list.items(), key=lambda kv: kv[0])
        ]
        return render_template(
            "index.html",
            event_name=event_name,
            slots=slots_view,
            slot_seconds=slot_seconds,
            start_name=start_name,
        )

    return app


class WebServerThread:
    def __init__(self, app: Flask, host: str = "127.0.0.1", port: int = 5000):
        self.server = make_server(host, port, app)
        self.ctx = app.app_context()
        self.ctx.push()
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)

    def start(self):
        self.thread.start()

    def shutdown(self):
        self.server.shutdown()
        self.thread.join(timeout=3)
