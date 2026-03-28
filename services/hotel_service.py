from db.mongo import hotels_collection

def search_hotels(city=None, name=None):
    query = {}

    if city:
        query["city"] = {"$regex": city, "$options": "i"}

    if name:
        query["name"] = {"$regex": name, "$options": "i"}

    projection = {
        "_id": 1,
        "name": 1,
        "city": 1,
        "province": 1,
        "address": 1,
        "postalCode": 1,
        "websites": 1
    }

    hotels = list(hotels_collection.find(query, projection).limit(20))
    return hotels

def get_hotel_details(hotel_id):
    pipeline = [
        {"$match": {"_id": hotel_id}},
        {
            "$lookup": {
                "from": "reviews",
                "localField": "_id",
                "foreignField": "hotelId",
                "as": "reviews"
            }
        }
    ]

    result = list(hotels_collection.aggregate(pipeline))

    if not result:
        return None

    hotel = result[0]
    reviews = hotel.get("reviews", [])

    if reviews:
        avg_rating = round(sum(r.get("rating", 0) for r in reviews) / len(reviews), 2)
    else:
        avg_rating = 0

    hotel["average_rating"] = avg_rating
    hotel["review_count"] = len(reviews)

    return hotel