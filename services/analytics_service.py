from db.mongo import reviews_collection, hotels_collection

def get_owner_dashboard_data(hotel_id):
    hotel = hotels_collection.find_one(
        {"_id": hotel_id},
        {"name": 1, "city": 1, "province": 1}
    )

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
    trends = get_rating_trends(hotel_id)
    loyal_customers = get_loyal_customers(hotel_id)
    segments = get_customer_segments(hotel_id)
    insights = get_review_insights(hotel_id)

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
        "lowRatedReviews": low_reviews,
        "trends": trends,
        "loyal_customers": loyal_customers,
        "segments": segments,
        "insights": insights
    }

def get_rating_trends(hotel_id):
    pipeline = [
        {"$match": {"hotelId": hotel_id}},
        {
            "$group": {
                "_id": {
                    "year": {"$year": "$reviewDate"},
                    "month": {"$month": "$reviewDate"}
                },
                "avgRating": {"$avg": "$rating"},
                "count": {"$sum": 1}
            }
        },
        {"$sort": {"_id.year": 1, "_id.month": 1}}
    ]

    return list(reviews_collection.aggregate(pipeline))

def get_loyal_customers(hotel_id):
    pipeline = [
        {"$match": {"hotelId": hotel_id}},
        {
            "$group": {
                "_id": "$username",
                "visitCount": {"$sum": 1},
                "avgRating": {"$avg": "$rating"}
            }
        },
        {"$match": {"visitCount": {"$gte": 2}}},
        {"$sort": {"visitCount": -1}}
    ]

    return list(reviews_collection.aggregate(pipeline))

def get_customer_segments(hotel_id):
    pipeline = [
        {"$match": {"hotelId": hotel_id}},
        {
            "$group": {
                "_id": "$username",
                "avgRating": {"$avg": "$rating"},
                "count": {"$sum": 1}
            }
        },
        {"$match": {"_id": {"$ne": None}}},
        {
            "$project": {
                "segment": {
                    "$switch": {
                        "branches": [
                            {"case": {"$gte": ["$avgRating", 4]}, "then": "Promoter"},
                            {"case": {"$gte": ["$avgRating", 3]}, "then": "Neutral"}
                        ],
                        "default": "Detractor"
                    }
                }
            }
        },
        {
            "$group": {
                "_id": "$segment",
                "count": {"$sum": 1}
            }
        }
    ]

    return list(reviews_collection.aggregate(pipeline))

def get_customer_segments(hotel_id):
    pipeline = [
        {"$match": {"hotelId": hotel_id}},
        {
            "$group": {
                "_id": "$username",
                "avgRating": {"$avg": "$rating"},
                "count": {"$sum": 1}
            }
        },
        {"$match": {"_id": {"$ne": None}}},
        {
            "$project": {
                "segment": {
                    "$switch": {
                        "branches": [
                            {"case": {"$gte": ["$avgRating", 4]}, "then": "Promoter"},
                            {"case": {"$gte": ["$avgRating", 3]}, "then": "Neutral"}
                        ],
                        "default": "Detractor"
                    }
                }
            }
        },
        {
            "$group": {
                "_id": "$segment",
                "count": {"$sum": 1}
            }
        }
    ]

    return list(reviews_collection.aggregate(pipeline))


def get_review_insights(hotel_id):
    pipeline = [
        {"$match": {"hotelId": hotel_id}},
        {
            "$project": {
                "text": 1,
                "hasClean": {"$regexMatch": {"input": "$text", "regex": "clean|dirty", "options": "i"}},
                "hasNoise": {"$regexMatch": {"input": "$text", "regex": "noise|loud", "options": "i"}},
                "hasService": {"$regexMatch": {"input": "$text", "regex": "staff|service", "options": "i"}}
            }
        },
        {
            "$group": {
                "_id": None,
                "clean_mentions": {"$sum": {"$cond": ["$hasClean", 1, 0]}},
                "noise_mentions": {"$sum": {"$cond": ["$hasNoise", 1, 0]}},
                "service_mentions": {"$sum": {"$cond": ["$hasService", 1, 0]}}
            }
        }
    ]

    result = list(reviews_collection.aggregate(pipeline))
    return result[0] if result else {}