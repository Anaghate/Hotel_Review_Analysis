from flask import Blueprint, render_template, request
from services.hotel_service import search_hotels, get_hotel_details

user_bp = Blueprint("user", __name__)

@user_bp.route("/")
def home():
    return render_template("home.html")

@user_bp.route("/hotels")
def hotels():
    city = request.args.get("city", "").strip()
    name = request.args.get("name", "").strip()

    hotel_results = search_hotels(city=city, name=name)

    return render_template(
        "hotel_list.html",
        hotels=hotel_results,
        city=city,
        name=name
    )

@user_bp.route("/hotel/<hotel_id>")
def hotel_details(hotel_id):
    hotel = get_hotel_details(hotel_id)
    return render_template("hotel_details.html", hotel=hotel)