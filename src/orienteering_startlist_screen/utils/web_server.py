import os
from datetime import datetime
from typing import Dict, List
from pathlib import Path
import sys
from flask import Flask, jsonify, render_template
from werkzeug.serving import make_server
import threading
import time
import logging

logging.getLogger("werkzeug").setLevel(logging.WARNING)

def resource_path(*parts: str) -> str:
    """Get the correct path in development environment and in binary environment."""
    base = getattr(sys, "_MEIPASS", Path(__file__).resolve().parent)
    return str(Path(base, *parts))

def create_app(start_list: Dict[datetime, List], slot_seconds: int = 60, start_name: str = "") -> Flask:
    template_dir = resource_path("templates")
    static_dir = resource_path("static")
    app = Flask(
        __name__,
        template_folder=template_dir,
        static_folder=static_dir,
        static_url_path="/static"
    )

    @app.get("/api/now")
    def api_now():
        now_ms = int(time.time() * 1000)
        return jsonify({"now_ms": now_ms})

    @app.get("/")
    def index():
        try:
            slots_view = [
                {"start_dt": dt, "participants": plist}
                for dt, plist in sorted(start_list.items(), key=lambda kv: kv[0])
            ]
            return render_template(
                "index.html",
                slots=slots_view,
                slot_seconds=slot_seconds,
                start_name=start_name,
            )
        except Exception as e:
            raise Exception(e)

    return app

class WebServerThread:
    def __init__(self, app: Flask, host: str = "127.0.0.1", port: int = 5000):
        self.server = make_server(host, port, app)
        self.ctx = app.app_context()
        self.ctx.push()
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)

    def start(self):
        try:
            self.thread.start()
        except Exception as e:
            raise Exception(e)

    def shutdown(self):
        self.server.shutdown()
        self.thread.join(timeout=3)
