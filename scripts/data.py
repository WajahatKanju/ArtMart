from .independant_models import (
    category1,
    category2,
    category3,
    brands,
    video_provider1,
    video_provider2,
    attribute_values,
)

products_data = [
    {
        "name": "Disney and Pixar WALL-E Robot Toy, Remote\
            Control Hello WALL-E Robot Figure, Gifts for Kids (Amazon Exclusive)",
        "category": category1,
        "brand": brands[-1],
        "min_purchase_qty": 1,
        "refundable": True,
        "base_price": 52.99,
        "description": "A Nice Product for kids to play with",
        "images": [
            {
                "is_thumbnail": True,
                "image_path": "./scripts/images/yellow_rover_with_eyes.jpg",
                "description": "WALL-E",
            },
            {
                "is_thumbnail": False,
                "image_path": "./scripts/images/sizes yellow rovers.jpg",
                "description": "WALL-E",
            },
            {
                "is_thumbnail": False,
                "image_path": "./scripts/images/yello_rover_with_kids.jpg",
                "description": "bot Toy",
            },
        ],
        "video_data": {
            "video_provider": video_provider1,
            "video_link": "https://www.youtube.com/watch?v=7oVSaUWeKt0",
        },
        "variation": {
            "stock_quantity": 45,
            "attributes": [
                attribute_values[2],
                attribute_values[6],
                attribute_values[13],
            ],
        },
    },
    {
        "name": "Skullcandy Crusher Evo Wireless Over-Ear Headphones",
        "category": category1,
        "brand": brands[0],
        "min_purchase_qty": 1,
        "refundable": True,
        "base_price": 149.99,
        "description": "Premium wireless headphones with adjustable bass",
        "images": [
            {
                "is_thumbnail": True,
                "image_path": "./scripts/images/skullcandy_headphones.jpg",
                "description": "Skullcandy Crusher Evo",
            },
            {
                "is_thumbnail": False,
                "image_path": "./scripts/images/skullcandy_headphones_case.jpg",
                "description": "Carrying Case",
            },
        ],
        "video_data": {
            "video_provider": video_provider1,
            "video_link": "https://www.youtube.com/watch?v=1234567890",
        },
        "variation": {
            "stock_quantity": 30,
            "attributes": [
                attribute_values[0],
                attribute_values[1],
                attribute_values[9],
            ],
        },
    },
    {
        "name": "P&G Tide Laundry Detergent, Original Scent",
        "category": category3,
        "brand": brands[2],
        "min_purchase_qty": 1,
        "refundable": True,
        "base_price": 9.99,
        "description": "Effective laundry detergent for everyday use",
        "images": [
            {
                "is_thumbnail": True,
                "image_path": "./scripts/images/tide_detergent.jpg",
                "description": "Tide Laundry Detergent",
            },
        ],
        "video_data": {
            "video_provider": video_provider2,
            "video_link": "https://www.dailymotion.com/video/abcdefghijk",
        },
        "variation": {
            "stock_quantity": 100,
            "attributes": [
                attribute_values[0],
                attribute_values[3],
            ],
        },
    },
    {
        "name": "Granier Leather Wallet",
        "category": category2,
        "brand": brands[3],
        "min_purchase_qty": 1,
        "refundable": True,
        "base_price": 29.99,
        "description": "High-quality leather wallet with multiple compartments",
        "images": [
            {
                "is_thumbnail": True,
                "image_path": "./scripts/images/leather_wallet.jpg",
                "description": "Granier Leather Wallet",
            },
        ],
        "video_data": {
            "video_provider": video_provider1,
            "video_link": "https://www.youtube.com/watch?v=mnopqrstuv",
        },
        "variation": {
            "stock_quantity": 50,
            "attributes": [
                attribute_values[1],
                attribute_values[2],
                attribute_values[11],
            ],
        },
    },
    {
        "name": "Unilever Dove Beauty Bar Soap",
        "category": category2,
        "brand": brands[4],
        "min_purchase_qty": 1,
        "refundable": True,
        "base_price": 3.99,
        "description": "Gentle cleansing beauty bar for soft and smooth skin",
        "images": [
            {
                "is_thumbnail": True,
                "image_path": "./scripts/images/dove_beauty_bar.jpg",
                "description": "Dove Beauty Bar",
            },
        ],
        "video_data": {
            "video_provider": video_provider2,
            "video_link": "https://www.dailymotion.com/video/lmnopqrs",
        },
        "variation": {
            "stock_quantity": 200,
            "attributes": [
                attribute_values[0],
                attribute_values[2],
                attribute_values[10],
            ],
        },
    },
    {
        "name": "Nestle Crunch Milk Chocolate Bar",
        "category": category3,
        "brand": brands[5],
        "min_purchase_qty": 1,
        "refundable": True,
        "base_price": 1.49,
        "description": "Delicious milk chocolate bar with crisped rice",
        "images": [
            {
                "is_thumbnail": True,
                "image_path": "./scripts/images/crunch_chocolate_bar.jpg",
                "description": "Nestle Crunch Chocolate Bar",
            },
        ],
        "video_data": {
            "video_provider": video_provider1,
            "video_link": "https://www.youtube.com/watch?v=uvwxyz1234",
        },
        "variation": {
            "stock_quantity": 300,
            "attributes": [
                attribute_values[0],
                attribute_values[3],
            ],
        },
    },
    {
        "name": "Shan Chicken Biryani Mix",
        "category": category3,
        "brand": brands[6],
        "min_purchase_qty": 1,
        "refundable": True,
        "base_price": 2.99,
        "description": "Convenient mix for making delicious chicken biryani",
        "images": [
            {
                "is_thumbnail": True,
                "image_path": "./scripts/images/chicken_biryani_mix.jpg",
                "description": "Shan Chicken Biryani Mix",
            },
        ],
        "video_data": {
            "video_provider": video_provider2,
            "video_link": "https://www.dailymotion.com/video/wxyz5678",
        },
        "variation": {
            "stock_quantity": 150,
            "attributes": [
                attribute_values[0],
                attribute_values[2],
                attribute_values[8],
            ],
        },
    },
    {
        "name": "National Foods Chai Tea Masala",
        "category": category3,
        "brand": brands[7],
        "min_purchase_qty": 1,
        "refundable": True,
        "base_price": 4.49,
        "description": "Spice blend for making aromatic chai tea",
        "images": [
            {
                "is_thumbnail": True,
                "image_path": "./scripts/images/chai_tea_masala.jpg",
                "description": "National Foods Chai Tea Masala",
            },
        ],
        "video_data": {
            "video_provider": video_provider1,
            "video_link": "https://www.youtube.com/watch?v=1234abcd",
        },
        "variation": {
            "stock_quantity": 100,
            "attributes": [
                attribute_values[0],
                attribute_values[2],
                attribute_values[7],
            ],
        },
    },
    {
        "name": "Robotiatoys Robo Pet Dog",
        "category": category1,
        "brand": brands[1],
        "min_purchase_qty": 1,
        "refundable": True,
        "base_price": 69.99,
        "description": "Interactive robotic pet dog with various features",
        "images": [
            {
                "is_thumbnail": True,
                "image_path": "./scripts/images/robo_pet_dog.jpg",
                "description": "Robotiatoys Robo Pet Dog",
            },
        ],
        "video_data": {
            "video_provider": video_provider1,
            "video_link": "https://www.youtube.com/watch?v=efgh5678",
        },
        "variation": {
            "stock_quantity": 25,
            "attributes": [
                attribute_values[0],
                attribute_values[2],
                attribute_values[12],
            ],
        },
    },
    {
        "name": "Disney Princess Dress Up Trunk Deluxe",
        "category": category1,
        "brand": brands[-1],
        "min_purchase_qty": 1,
        "refundable": True,
        "base_price": 49.99,
        "description": "Dress-up trunk set for kids with Disney Princess themes",
        "images": [
            {
                "is_thumbnail": True,
                "image_path": "./scripts/images/princess_dress_up_trunk.jpg",
                "description": "Disney Princess Dress Up Trunk",
            },
        ],
        "video_data": {
            "video_provider": video_provider2,
            "video_link": "https://www.dailymotion.com/video/ijklmnopqr",
        },
        "variation": {
            "stock_quantity": 40,
            "attributes": [
                attribute_values[2],
                attribute_values[6],
                attribute_values[14],
            ],
        },
    },
    {
        "name": "Skullcandy Indy Evo True Wireless In-Ear Earbuds",
        "category": category1,
        "brand": brands[0],
        "min_purchase_qty": 1,
        "refundable": True,
        "base_price": 79.99,
        "description": "Wireless in-ear earbuds with high-quality audio",
        "images": [
            {
                "is_thumbnail": True,
                "image_path": "./scripts/images/skullcandy_earbuds.jpg",
                "description": "Skullcandy Indy Evo",
            },
        ],
        "video_data": {
            "video_provider": video_provider1,
            "video_link": "https://www.youtube.com/watch?v=5678efghij",
        },
        "variation": {
            "stock_quantity": 35,
            "attributes": [
                attribute_values[0],
                attribute_values[1],
                attribute_values[14],
            ],
        },
    },
    {
        "name": "P&G Charmin Ultra Strong Toilet Paper",
        "category": category3,
        "brand": brands[2],
        "min_purchase_qty": 1,
        "refundable": True,
        "base_price": 12.99,
        "description": "Soft and strong toilet paper for everyday use",
        "images": [
            {
                "is_thumbnail": True,
                "image_path": "./scripts/images/charmin_toilet_paper.jpg",
                "description": "Charmin Ultra Strong Toilet Paper",
            },
        ],
        "video_data": {
            "video_provider": video_provider2,
            "video_link": "https://www.dailymotion.com/video/mnopqrstuv",
        },
        "variation": {
            "stock_quantity": 120,
            "attributes": [
                attribute_values[0],
                attribute_values[3],
            ],
        },
    },
    {
        "name": "Granier Leather Belt",
        "category": category2,
        "brand": brands[3],
        "min_purchase_qty": 1,
        "refundable": True,
        "base_price": 19.99,
        "description": "Stylish leather belt for men and women",
        "images": [
            {
                "is_thumbnail": True,
                "image_path": "./scripts/images/leather_belt.jpg",
                "description": "Granier Leather Belt",
            },
        ],
        "video_data": {
            "video_provider": video_provider1,
            "video_link": "https://www.youtube.com/watch?v=qrstuvwxyz12",
        },
        "variation": {
            "stock_quantity": 60,
            "attributes": [
                attribute_values[1],
                attribute_values[2],
                attribute_values[11],
            ],
        },
    },
    {
        "name": "Unilever Axe Body Wash",
        "category": category2,
        "brand": brands[4],
        "min_purchase_qty": 1,
        "refundable": True,
        "base_price": 5.99,
        "description": "Refreshing body wash for a clean and invigorating shower",
        "images": [
            {
                "is_thumbnail": True,
                "image_path": "./scripts/images/axe_body_wash.jpg",
                "description": "Axe Body Wash",
            },
        ],
        "video_data": {
            "video_provider": video_provider2,
            "video_link": "https://www.dailymotion.com/video/uvwxyz12345",
        },
        "variation": {
            "stock_quantity": 150,
            "attributes": [
                attribute_values[0],
                attribute_values[2],
                attribute_values[10],
            ],
        },
    },
    {
        "name": "Nestle Kit Kat Wafer Bars",
        "category": category3,
        "brand": brands[5],
        "min_purchase_qty": 1,
        "refundable": True,
        "base_price": 1.99,
        "description": "Classic wafer bars with smooth milk chocolate",
        "images": [
            {
                "is_thumbnail": True,
                "image_path": "./scripts/images/kit_kat_wafer_bars.jpg",
                "description": "Nestle Kit Kat Wafer Bars",
            },
        ],
        "video_data": {
            "video_provider": video_provider1,
            "video_link": "https://www.youtube.com/watch?v=abcdefg1234",
        },
        "variation": {
            "stock_quantity": 250,
            "attributes": [
                attribute_values[0],
                attribute_values[3],
            ],
        },
    },
    {
        "name": "Shan Korma Masala",
        "category": category3,
        "brand": brands[6],
        "min_purchase_qty": 1,
        "refundable": True,
        "base_price": 2.49,
        "description": "Spice mix for preparing flavorful korma dishes",
        "images": [
            {
                "is_thumbnail": True,
                "image_path": "./scripts/images/korma_masala.jpg",
                "description": "Shan Korma Masala",
            },
        ],
        "video_data": {
            "video_provider": video_provider2,
            "video_link": "https://www.dailymotion.com/video/ijklmnopqrs",
        },
        "variation": {
            "stock_quantity": 180,
            "attributes": [
                attribute_values[0],
                attribute_values[2],
                attribute_values[8],
            ],
        },
    },
    {
        "name": "National Foods Garam Masala",
        "category": category3,
        "brand": brands[7],
        "min_purchase_qty": 1,
        "refundable": True,
        "base_price": 3.49,
        "description": "Spice blend for adding warmth and flavor to dishes",
        "images": [
            {
                "is_thumbnail": True,
                "image_path": "./scripts/images/garam_masala.jpg",
                "description": "National Foods Garam Masala",
            },
        ],
        "video_data": {
            "video_provider": video_provider1,
            "video_link": "https://www.youtube.com/watch?v=mnopqrstuv1",
        },
        "variation": {
            "stock_quantity": 120,
            "attributes": [
                attribute_values[0],
                attribute_values[2],
                attribute_values[7],
            ],
        },
    },
]
