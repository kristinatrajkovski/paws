from datetime import datetime

from flask import url_for

missing1 = {
    "Age":"2",
    "Breed":"Alaskan Malamute",
    "Name": "Freddie",
    "Contact": "trajkovskikristina@gmail.com",
    "Location": "Istanbul Teknik Universitesi",
    "DateTime": datetime (2021, 8, 7, 19, 38, 00), 
    "Picture": "freddie.jpg"
}
missing2 = {
    "Age":"5",
    "Breed":"Golden Retriever",
    "Name": "Charlie",
    "Contact": "johndoe@gmail.com",
    "Location": "Central Park",
    "DateTime": datetime (2021, 5, 7, 8, 38, 00), 
    "Picture": "charlie.jpg"
}

found1 = {
    "Age":"4",
    "Breed":"Goldendoodle",
    "Contact": "johndoe@gmail.com",
    "Location": "Central Park",
    "DateTime": datetime (2021, 5, 27, 8, 38, 00), 
    "Picture": "melba.jpg"
}

adoption1 = {
    "Age":"2",
    "Breed":"Alaskan Malamute",
    "Name": "Freddie",
    "Contact": "trajkovskikristina@gmail.com",
    "Location": "Istanbul, Turkey",
    "Picture": "freddie.jpg"
}

kristinatrajkovski = {
    "Name": "Kristina Trajkovski",
    "Username": "kristina8822",
    "Email": "trajkovskikristina@gmail.com",
    "Location": "Istanbul, Turkey",
    "PhoneNumber":"+90 544 927 72 78",
    "Missing":[missing1, missing2],
    "Found":[],
    "Adoption":[adoption1]
}
johndoe = {
    "Name": "John Doe",
    "Username": "johndoe",
    "Email": "johndoe@gmail.com",
    "Location": "New York, New York",
    "PhoneNumber":"+1 840 123 45 67",
    "Missing":[],
    "Found":[found1],
    "Adoption":[]
}
landoncampbell = {
    "Name": "Landon Campbell",
    "User": "RedFox",
    "Email": "redfoxmma@gmail.com",
}

users = {
    "1": kristinatrajkovski,
    "2": johndoe,
    "3": landoncampbell
}

alaskan_husky1 = {
    "Name": "Chocolate",
}
golden_retriever1 = {
    "Name": "Buddy",
}

missing_pets = {
    "Alaskan Husky": alaskan_husky1,
    "Golden Retriever": golden_retriever1
}


found_pets = {

}

adoptable_pets = {

}

messages = {
    "Text": "Hello, I'd like to purchase your animal!",
    "Sender": users["3"],
    "Recipient": users["1"]
}
