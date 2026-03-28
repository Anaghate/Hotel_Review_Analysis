from flask import Blueprint, render_template
from flask import jsonify
from services.analytics_service import (
    get_owner_dashboard_data,
    get_rating_trends,
    get_loyal_customers,
    get_customer_segments,
    get_review_insights
)

owner_bp = Blueprint("owner", __name__)

@owner_bp.route("/owner/<hotel_id>")
def owner_dashboard(hotel_id):
    dashboard = get_owner_dashboard_data(hotel_id)
    return render_template("owner_dashboard.html", dashboard=dashboard)

@owner_bp.route("/api/owner/<hotel_id>/trends")
def api_trends(hotel_id):
    return jsonify(get_rating_trends(hotel_id))

@owner_bp.route("/api/owner/<hotel_id>/loyalty")
def api_loyalty(hotel_id):
    return jsonify(get_loyal_customers(hotel_id))

@owner_bp.route("/api/owner/<hotel_id>/segments")
def api_segments(hotel_id):
    return jsonify(get_customer_segments(hotel_id))

@owner_bp.route("/api/owner/<hotel_id>/insights")
def api_insights(hotel_id):
    return jsonify(get_review_insights(hotel_id))