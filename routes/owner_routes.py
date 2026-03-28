from flask import Blueprint, render_template
from services.analytics_service import get_owner_dashboard_data

owner_bp = Blueprint("owner", __name__)

@owner_bp.route("/owner/<hotel_id>")
def owner_dashboard(hotel_id):
    dashboard = get_owner_dashboard_data(hotel_id)
    return render_template("owner_dashboard.html", dashboard=dashboard)