dataset: https://www.kaggle.com/datasets/datafiniti/hotel-reviews?resource=download&select=Datafiniti_Hotel_Reviews_Jun19.csv

To create customized collection
hotels:
[
  {
    $group: {
      _id: "$id",
      name: { $first: "$name" },
      address: { $first: "$address" },
      city: { $first: "$city" },
      province: { $first: "$province" },
      country: { $first: "$country" },
      postalCode: { $first: "$postalCode" },
      categories: { $first: "$categories" },
      primaryCategories: { $first: "$primaryCategories" },
      latitude: { $first: { $toDouble: "$latitude" } },
      longitude: { $first: { $toDouble: "$longitude" } }
    }
  },
  {
    $project: {
      _id: 1,
      name: 1,
      address: 1,
      city: 1,
      province: 1,
      country: 1,
      postalCode: 1,
      primaryCategories: 1,
      categories: {
        $split: ["$categories", ","]
      },
      location: {
        type: "Point",
        coordinates: ["$longitude", "$latitude"]
      }
    }
  },
  {
    $out: "hotels"
  }
]


Reviews:
[
  {
    $project: {
      hotelId: "$id",

      reviewDate: {
        $cond: [
          { $eq: [{ $type: "$reviews.date" }, "date"] },
          "$reviews.date",
          {
            $cond: [
              { $ifNull: ["$reviews.date", false] },
              { $dateFromString: { dateString: "$reviews.date" } },
              null
            ]
          }
        ]
      },

      rating: {
        $cond: [
          { $ifNull: ["$reviews.rating", false] },
          { $toInt: "$reviews.rating" },
          null
        ]
      },

      text: "$reviews.text",
      title: "$reviews.title",
      username: "$reviews.username",
      userCity: "$reviews.userCity",
      userProvince: "$reviews.userProvince"
    }
  },
  {
    $out: "reviews"
  }
]

