from db.mongo import reviews_collection, hotels_collection

def get_owner_dashboard_data(hotel_id):
    hotel = hotels_collection.find_one({"_id": hotel_id}, {"name": 1, "city": 1, "province": 1})

    summary_pipeline = [
        {"$match": {"hotelId": hotel_id}},
        {
            "$group": {
                "_id": "$hotelId",
                "averageRating": {"$avg": "$rating"},
                "totalReviews": {"$sum": 1}
            }
        }
    ]

    rating_distribution_pipeline = [
        {"$match": {"hotelId": hotel_id}},
        {
            "$group": {
                "_id": "$rating",
                "count": {"$sum": 1}
            }
        },
        {"$sort": {"_id": 1}}
    ]

    low_reviews = list(
        reviews_collection.find(
            {"hotelId": hotel_id, "rating": {"$lte": 2}},
            {"title": 1, "text": 1, "rating": 1, "reviewDate": 1}
        ).sort("reviewDate", -1).limit(10)
    )

    summary_result = list(reviews_collection.aggregate(summary_pipeline))
    rating_distribution = list(reviews_collection.aggregate(rating_distribution_pipeline))

    summary = {
        "averageRating": 0,
        "totalReviews": 0
    }

    if summary_result:
        summary["averageRating"] = round(summary_result[0]["averageRating"], 2)
        summary["totalReviews"] = summary_result[0]["totalReviews"]

    return {
        "hotel": hotel,
        "summary": summary,
        "ratingDistribution": rating_distribution,
        "lowRatedReviews": low_reviews
    }