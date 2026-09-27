🏨 BookMyStay with AI Travel Assistant

A modern full-stack hotel booking web application built with Python, Django, MySQL, HTML, CSS, JavaScript, and Bootstrap, enhanced with an AI-powered Travel Assistant using Google Gemini.

BookMyStay allows customers to search hotels, send booking requests, receive booking confirmations, while hotel providers manage their hotels, bookings, and customer interactions. The integrated AI assistant helps users discover destinations, plan trips, search hotels, and answer travel-related questions.

🚀 Features
👤 Customer
Customer Registration & Login
Browse Hotels
Search Hotels by City
Hotel Details Page
View Multiple Hotel Images
Hotel Ratings
Send Booking Requests
Booking Confirmation via Email
Booking History
🏨 Hotel Provider
Provider Registration & Login
Add New Hotels
Update Hotel Details
Upload Multiple Images
Delete Hotel Images
View Customer Booking Requests
Accept / Reject Requests
Booking History Management
📧 Email Notifications
Customer Booking Request Email
Booking Acceptance Email
Booking Rejection Email
Automated Email Communication
🤖 AI Travel Assistant (Google Gemini)

The latest version introduces an intelligent AI Travel Assistant capable of:

🌍 Destination Recommendations
🧳 Personalized Trip Planning
🏨 Hotel Search from BookMyStay Database
📍 Travel Guidance
🩺 Basic Travel Health Tips
🚨 Emergency Helpline Information
💬 Natural Language Conversations

Unlike a normal chatbot, the assistant can search hotels directly from the BookMyStay database and recommend suitable stays.

🔍 Hotel Discovery
Search Hotels by Location
Hotel Cards
Detailed Hotel Information
Hotel Images Gallery
Star Rating
Hotel Pricing
Responsive Design
💻 Technology Stack
Backend
Python
Django
Django ORM
Frontend
HTML5
CSS3
JavaScript
Bootstrap 5
Bootstrap Icons
Database
MySQL
AI
Google Gemini API
Other
Django Templates
Email Integration
Image Upload
CRUD Operations
🔄 Application Workflow
Customer
      │
      ▼
Register / Login
      │
      ▼
Browse Hotels
      │
      ▼
Search Hotels
      │
      ▼
View Hotel Details
      │
      ▼
Send Booking Request
      │
      ▼
Provider Receives Request
      │
      ▼
Accept / Reject Booking
      │
      ▼
Customer Receives Email
      │
      ▼
Booking History Updated
🤖 AI Assistant Workflow
User
   │
   ▼
Ask AI Assistant
   │
   ▼
Google Gemini
   │
   ▼
Travel Suggestions
Trip Planning
Hotel Search
Health Tips
Emergency Help
📂 Project Structure
BookMyStay/
│
├── Templates/
├── Static/
├── database/
├── media/
├── manage.py
├── requirements.txt
├── README.md
└── db.sqlite3 / MySQL
⚙️ Installation
Clone Repository
git clone https://github.com/Gurappa41/BookMyStay-with-AI-Travel-Assistant-.git
cd BookMyStay-with-AI-Travel-Assistant-
Create Virtual Environment
python -m venv venv

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Configure Database

Update your MySQL credentials inside settings.py.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "bookmystay",
        "USER": "root",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
Configure Environment Variables

Store sensitive credentials as environment variables instead of hardcoding them.

EMAIL_HOST_USER=your_email
EMAIL_HOST_PASSWORD=your_password
GEMINI_API_KEY=your_api_key
Run Migrations
python manage.py makemigrations
python manage.py migrate
Run Server
python manage.py runserver

Visit

http://127.0.0.1:8000/
📸 Screenshots

Add screenshots here.

Home Page

Customer Dashboard

Hotel Details

Provider Dashboard

Booking Request

AI Travel Assistant
📚 Learning Outcomes

This project helped me gain practical experience in:

Django MVC Architecture
Django ORM
CRUD Operations
Authentication
Sessions
MySQL Integration
Image Upload & Management
Email Automation
RESTful Design Principles
Google Gemini API Integration
AI Prompt Engineering
Responsive Web Design
Debugging & Problem Solving
🔮 Future Enhancements
💳 Online Payments
📱 SMS Notifications
⭐ Reviews & Ratings
❤️ Wishlist
📅 Room Availability Calendar
🔐 OTP Authentication
🔄 Password Reset
📍 Google Maps Integration
🌦️ Weather Information
🎤 Voice-based AI Assistant
📱 Mobile Responsive PWA
☁️ Cloud Deployment (AWS / Render)
👨‍💻 Developer

Gurappa

B.Tech – Computer Science & Engineering (AI & ML)

Skills

Python
Django
MySQL
HTML
CSS
JavaScript
Bootstrap
Google Gemini API
Git & GitHub
⭐ Highlights
✅ Full Stack Django Project
✅ AI-Powered Travel Assistant
✅ Google Gemini Integration
✅ Hotel Booking Workflow
✅ Provider Dashboard
✅ Email Notifications
✅ MySQL Database
✅ Responsive UI
✅ Real-world CRUD Operations
✅ Production-ready Architecture
