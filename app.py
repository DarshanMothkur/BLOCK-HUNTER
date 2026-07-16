"""
Block Hunter - Application Entry Point
======================================
IIoT Cybersecurity Platform using Federated Learning, MLP, Blockchain & Flask.

Run:
    python app.py

Then open http://127.0.0.1:5000
"""

from __future__ import annotations

import os
import sys

# Ensure project root is on PYTHONPATH when running as script
ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from flask import Flask, render_template, send_from_directory, session, redirect, url_for
from flask_cors import CORS

from backend.config import Config
from backend.api.auth import auth_bp
from backend.api.devices import devices_bp
from backend.api.threats import threats_bp
from backend.api.federated import fl_bp
from backend.api.blockchain_api import blockchain_bp
from backend.api.alerts import alerts_bp
from backend.api.dashboard import dashboard_bp
from backend.api.reports import reports_bp
from database.init_db import init_database, get_db_path


def create_app(config_class: type = Config) -> Flask:
    """
    Application factory.

    Builds the Flask app, registers blueprints, and wires static/frontend paths
    so the project remains GitHub-ready and easy to extend.
    """
    app = Flask(
        __name__,
        template_folder=os.path.join(ROOT, "frontend"),
        static_folder=os.path.join(ROOT, "frontend", "static"),
        static_url_path="/static",
    )
    app.config.from_object(config_class)
    CORS(app, supports_credentials=True)

    # ---------- REST API blueprints ----------
    app.register_blueprint(auth_bp, url_prefix="/api/v1/auth")
    app.register_blueprint(devices_bp, url_prefix="/api/v1/devices")
    app.register_blueprint(threats_bp, url_prefix="/api/v1/threats")
    app.register_blueprint(fl_bp, url_prefix="/api/v1/fl")
    app.register_blueprint(blockchain_bp, url_prefix="/api/v1/blockchain")
    app.register_blueprint(alerts_bp, url_prefix="/api/v1/alerts")
    app.register_blueprint(dashboard_bp, url_prefix="/api/v1/dashboard")
    app.register_blueprint(reports_bp, url_prefix="/api/v1/reports")

    # ---------- Page routes (serve HTML frontend) ----------
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/login")
    def login_page():
        return render_template("login.html")

    @app.route("/register")
    def register_page():
        return render_template("register.html")

    @app.route("/dashboard")
    def dashboard_page():
        return render_template("dashboard.html")

    @app.route("/devices")
    def devices_page():
        return render_template("devices.html")

    @app.route("/register-device")
    def register_device_page():
        """Dedicated IIoT device registration page."""
        return render_template("register-device.html")

    @app.route("/monitoring")
    def monitoring_page():
        return render_template("monitoring.html")

    @app.route("/threats")
    def threats_page():
        return render_template("threats.html")

    @app.route("/fl-status")
    def fl_status_page():
        return render_template("fl-status.html")

    @app.route("/blockchain")
    def blockchain_page():
        return render_template("blockchain.html")

    @app.route("/alerts")
    def alerts_page():
        return render_template("alerts.html")

    @app.route("/reports")
    def reports_page():
        return render_template("reports.html")

    @app.route("/health")
    def health():
        """Liveness probe for demos and deployment checks."""
        return {"status": "ok", "service": "Block Hunter", "version": "1.0.0"}

    # Ensure DB exists on first boot
    if not os.path.exists(get_db_path()):
        with app.app_context():
            init_database()

    return app


# Module-level app for `flask run` and WSGI servers
app = create_app()


if __name__ == "__main__":
    # Development server — use a production WSGI server (gunicorn/waitress) in prod
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "1") == "1"
    print(
        f"""
    ╔══════════════════════════════════════════════════╗
    ║           BLOCK HUNTER  ·  IIoT Security         ║
    ║   Federated Learning · MLP · Blockchain · Flask  ║
    ╠══════════════════════════════════════════════════╣
    ║  Dashboard → http://127.0.0.1:{port:<5}              ║
    ╚══════════════════════════════════════════════════╝
    """
    )
    app.run(host="0.0.0.0", port=port, debug=debug)
