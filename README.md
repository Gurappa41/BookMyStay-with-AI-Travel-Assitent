BookMyStay – Hotel Booking Web Application
BookMyStay is a full-stack hotel booking web application developed using Python, Django, MySQL, HTML, CSS, JavaScript, and Bootstrap.
The application is designed to provide a simple platform where customers can discover hotels, send booking requests, and interact with an intelligent AI Travel Concierge, while hotel providers can manage their properties and respond to customer requests.
The project focuses on implementing a complete real-world workflow, including authentication, hotel management, booking requests, image handling, database operations, email communication, and GenAI tool calling.
🚀 Key Features
👤 Customer Features

Customer registration and login

Search hotels based on location

Browse available hotels

View complete hotel details

View hotel images, descriptions, pricing, address, and ratings

Submit hotel booking requests

Receive booking responses through email

View booking information and history

Interactive chat with an AI Travel Concierge
🏨 Hotel Provider Features

Provider registration and login

Add new hotel properties

Edit and update hotel information

Manage pricing, address, descriptions, and other details

Upload multiple hotel images

Delete individual hotel images

View customer booking requests

Accept booking requests with room allotment

Decline booking requests with automated email notification

Manage booking and acceptance history
🤖 AI Travel Concierge Features

AI-powered travel assistant using Gemini 3.6 Flash

Database tool calling with search_hotels function to fetch live hotel data

Destination recommendations based on travel preferences and budgets

Trip planning and custom itinerary generation

Basic non-diagnostic travel health tips and packing advice

Emergency helpline integration for Indian traveler support (112, 1363, 108, 1091)

Domain guardrails restricting out-of-scope queries
📩 Booking & Email System

Customer booking request workflow

Provider-side request management

Booking acceptance process

Booking decline notifications

Automated email notifications

Email confirmation/response to customers

Booking status and history management
🔎 Hotel Discovery

Location-based hotel search

Dynamic hotel listings

Hotel cards with important information

Dedicated hotel details pages

Star-based hotel classification

Responsive hotel image display
🛠️ Technology Stack
Backend

Python

Django

Django ORM
AI & LLM

Google GenAI SDK

Gemini 3.6 Flash

Function Calling / Tool Calling
Frontend

HTML5

CSS3

JavaScript

Bootstrap

Bootstrap Icons
Database

MySQL
Other

Django Templates

Email Integration

Media/Image Handling
🔄 How It Works
Customer Flow
Customer
↓
Register / Login
↓
Search Hotels / Ask AI Concierge
↓
View Hotel Details
↓
Send Booking Request
↓
Hotel Provider Receives Request & Email
↓
Provider Accepts Request (or Declines)
↓
Customer Receives Email
↓
Booking History Updated

AI Concierge Flow
Customer Sends Chat Message
↓
Gemini 3.6 Flash Analyzes Query
↓
Tool Call Triggered: search_hotels(city)
↓
Django ORM Queries MySQL Database
↓
Hotel Details Returned to Gemini
↓
AI Generates Structured Response to Customer

⚙️ Installation & Setup

Clone the Repository
[git clone https://github.com/Gurappa41/BookMyStay-with-AI-Travel-Assitent.git]
cd BookMyStay

Create a Virtual Environment
python -m venv venv

Activate it on Windows:
venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

Configure MySQL and Settings
Create a MySQL database and update the database credentials in Django's settings.py
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'bookmystay',
'USER': 'root',
'PASSWORD': 'your_password',
'HOST': 'localhost',
'PORT': '3306',
}
}

Configure Email Settings in settings.py:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'

Set Gemini API Key
Set your Gemini API key in your environment variables:
set GEMINI_API_KEY="your_gemini_api_key"

Run Migrations
python manage.py makemigrations
python manage.py migrate

Start the Server
python manage.py runserver

📚 What I Learned
Developing BookMyStay gave me practical experience in building a complete web application using Django.
Through this project, I worked with Django models, views, forms, URL routing, templates, ORM, MySQL, CRUD operations, authentication, sessions, image uploads, and email integration.
I also gained hands-on experience integrating Generative AI using the Google GenAI SDK (Gemini 3.6 Flash) and implementing function calling (tool calling) to connect an LLM directly to live database queries.
One of the main learning experiences was implementing the interaction between customers and hotel providers. The application handles the complete flow from hotel discovery and booking requests to provider approval, email communication, and booking history.
This project also helped me understand how frontend, backend, AI models, and database components work together to create a functional and responsive web application.
🔮 Future Enhancements
Some features that can be added in future versions include:

💳 Online payment integration

🛏️ Room availability management

⭐ Customer reviews and ratings

🔍 Advanced hotel filters

❌ Booking cancellation

🗺️ Map and location integration

🔐 OTP and password reset

🔗 REST API using Django REST Framework

☁️ Cloud deployment
👨‍💻 Developer
Gurappa B.Tech – Computer Science & Engineering (AI & ML)
Skills: Python | Django | MySQL | LLMs & GenAI | HTML | CSS | JavaScript | Bootstrap
⭐ Project Highlights

Full-stack Django web application

Customer and hotel provider workflows

AI Travel Concierge with real-time database tool calling

MySQL database integration

Hotel and image management

Booking request and approval system

Automated email communication

Responsive Bootstrap interface

Real-world CRUD and database operations
