# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from django.contrib import messages
# import base64
# from datetime import date
# from django.core.mail import send_mail
# from django.conf import settings
# from .models import HotelProviders, HotelImages, CustomerDetails, requestData, history_data
# def home(request):
#     return render(request, 'indexLogin.html')
# def Customerstorage(request):
#     if request.method == "POST":
#         name = request.POST.get('Name')
#         phone = request.POST.get('Mobile')
#         email = request.POST.get('Email')
#         password = request.POST.get('Password1')
#         cpassword = request.POST.get('Password2')
#         if password != cpassword:
#             messages.error(request, "Passwords didn't match.")
#             return redirect('/')
#         if CustomerDetails.objects.filter(email=email).exists():
#             messages.error(request, "Registration Failed: Email already exists.")
#             return redirect('/')
#         storage = CustomerDetails.objects.create(name=name, phone=phone, email=email, password=password)
#         storage.save()
#         messages.success(request, "Customer Registration Successful! You can now login.")
#         return redirect('/')
# def Providerstorage(request):
#     if request.method == "POST":
#         name = request.POST.get('Name')
#         email = request.POST.get('Email')
#         mobile = request.POST.get('Mobile')
#         HotelName = request.POST.get('HotelName')
#         password1 = request.POST.get('Password1')
#         password2 = request.POST.get('Password2')
#         city = request.POST.get('City')
#         Type = request.POST.get('Type')
#         Price = request.POST.get('Price')
#         address = request.POST.get('Address')
#         desc = request.POST.get('Msg')
#         if password1 != password2:
#             messages.error(request, "Passwords didn't match.")
#             return redirect('/')
#         if HotelProviders.objects.filter(email=email).exists():
#             messages.error(request, "Provider Registration Failed: Email already exists.")
#             return redirect('/')
#         storage = HotelProviders.objects.create(
#             name=name, email=email, phone=mobile, HotelName=HotelName,
#             password=password1, city=city, address=address, msg=desc,
#             HotelType=Type, Price=Price
#         )
#         storage.save()
#         images = request.FILES.getlist('hotel_images')
#         for image in images:
#             image_binary = image.read()
#             HotelImages.objects.create(
#                 hotel=storage,
#                 image=image_binary
#             )
#         messages.success(request, "Provider Registration Successful! You can now login.")
#         return redirect('/')
# def login(request):
#     if request.method == "POST":
#         Email = request.POST.get('Email')
#         Password = request.POST.get('Password')
#         Type = request.POST.get('Type')
#         if Type == 'Pro':
#             if HotelProviders.objects.filter(email=Email, password=Password).exists():
#                 data = HotelProviders.objects.get(email=Email, password=Password)
#                 images = HotelImages.objects.filter(hotel=data)
#                 for img in images:
#                     img.base64 = base64.b64encode(img.image).decode("utf-8")
#                 res = requestData.objects.filter(hotel_id=data.id)
#                 return render(
#                     request,
#                     "U_provider_dash_board.html",
#                     {"provider": data, "images": images, "respon": res}
#                 )
#             else:
#                 messages.error(request, "Provider login failed. Please check your credentials.")
#                 return redirect('/')
#         elif Type == 'Cust':
#             if CustomerDetails.objects.filter(email=Email, password=Password).exists():
#                 data = HotelProviders.objects.all()
#                 return render(request, "Customer_dashboard.html", context={'hotels': data})
#             else:
#                 messages.error(request, "Customer login failed. Please check your credentials.")
#                 return redirect('/')
#     return redirect('/')
# def locationsearch(request):
#     data=HotelProviders.objects.filter(city=request.GET.get('search'))
#     return render(request, "Customer_dashboard.html", context={'hotels': data})
# def all(request):
#     data = HotelProviders.objects.all()
#     return render(request, "Customer_dashboard.html", context={'hotels': data})
# def hotel_details(request,id):
#     data = HotelProviders.objects.get(id=id)
#     images=HotelImages.objects.filter(hotel_id=id)
#     for img in images:
#         img.base64 = base64.b64encode(img.image).decode("utf-8")
#     return render(request, "Hotel_Temp.html", context={'hotel': data,'images':images})
# def requestdata(request,id):
#     name=request.POST.get('Name')
#     email=request.POST.get('Email')
#     mobile=request.POST.get('Mobile')
#     checkin=request.POST.get('Checkin')
#     checkout=request.POST.get('Checkout')
#     storage=requestData.objects.create(name=name,email=email,phone=mobile,checkin=checkin,checkout=checkout,hotel_id=id)
#     storage.save()
#     mail=HotelProviders.objects.get(id=id).email
#     provider=HotelProviders.objects.get(id=id).name
#     send_mail(
#         subject="New Customer Booking Request – Action Required",
#         message=f"""
# Dear {provider},
# Greetings from BookMyStay!
# You have received a new booking request from a customer who is interested in staying at your hotel.
# Customer Details:
# Customer Name: {name}
# phone number: {mobile}
# email: {email}
# Please log in to your BookMyStay dashboard to view the complete booking details, including the customer's request and stay information.
# Kindly review the request and take the necessary action at your earliest convenience. If you are able to accommodate the customer, please accept the request and allot a suitable room. If there is no availability, you may decline the request.
# We appreciate your prompt response and cooperation in providing our customers with a smooth and pleasant booking experience.
# Thank you for being a valued partner of BookMyStay.
# Best regards,
# BookMyStay Team
# """
#         ,
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[mail]
#     )
#     messages.success(request, "Booking successful! You will get a response from the owner in your mail.")
#     return redirect('hotel_details', id=id)
# def accept_request(request, id, email, u_id):
#     hotel_details = HotelProviders.objects.get(id=id)
#     provider = hotel_details.name
#     hotel_name = hotel_details.HotelName
#     hotel_address = hotel_details.address
#     phone_number = hotel_details.phone
#     req_data = requestData.objects.get(id=u_id)
#     if request.method == "POST":
#         room_number = request.POST.get('roomnumber')
#         try:
#             rooms_int = int(room_number)
#         except ValueError:
#             rooms_int = 0
#         history = history_data.objects.create(
#             hotelId=hotel_details.id,
#             cName=req_data.name,
#             phone=req_data.phone,
#             email=req_data.email,
#             checkin=req_data.checkin,
#             checkout=req_data.checkout,
#             alloted_rooms=rooms_int,
#             accepted_date=date.today()
#         )
#         history.save()
#         send_mail(
#             subject="Hotel Booking Confirmed – We Look Forward to Welcoming You!",
#             message=f"""Dear Customer,
# Warm greetings from {hotel_name}!
# We are delighted to confirm your booking with us. Thank you for choosing {hotel_name} for your stay. It is our pleasure to welcome you, and we look forward to providing you with a comfortable, relaxing, and memorable experience.
# Reservation Details:
# Hotel Name: {hotel_name}
# Hotel Address: {hotel_address}
# Allotted Room Number: {room_number}
# We hope your upcoming stay will be filled with comfort, happiness, and wonderful moments. Our team is committed to making your visit enjoyable and ensuring that you feel right at home throughout your stay.
# We wish you a safe and pleasant journey to the hotel. May you have a wonderful time with us and create many happy memories during your stay.
# Should you need any assistance before or during your visit, please do not hesitate to contact our front desk team. We will be happy to assist you with any questions or special requests.
# Phone: {phone_number}
# Email: {settings.EMAIL_HOST_USER}
# Thank you once again for choosing {hotel_name}. We sincerely appreciate your trust and look forward to welcoming you.
# Wishing you a safe journey, a pleasant stay, and a wonderful experience with us!
# Warm regards,
# {provider}
# {hotel_name}
#         """,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[email]
#         )
#         req_data.delete()
#     elif request.method == "GET":
#         send_mail(
#             subject="Hotel Booking Request – Not Accepted",
#             message=f"""Dear Customer,
# Thank you for choosing our hotel and for submitting your booking request.
# We regret to inform you that your booking request could not be accepted, and a room has not been allotted to you for the requested stay.
# We apologize for any inconvenience this may cause and appreciate your understanding.
# If you have any questions or would like to check for alternative availability, please feel free to contact our front desk team.
# {hotel_name}
# {hotel_address}
# Phone: {phone_number}
# Email: {settings.EMAIL_HOST_USER}
# We hope to have the opportunity to serve you in the future.
# Warm regards,
# {provider}
# {hotel_name}
# """,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[email]
#         )
#         req_data.delete()
#     images = HotelImages.objects.filter(hotel=hotel_details)
#     for img in images:
#         img.base64 = base64.b64encode(img.image).decode("utf-8")
#     res = requestData.objects.filter(hotel_id=hotel_details.id)
#     return render(
#         request,
#         "U_provider_dash_board.html",
#         {
#             "provider": hotel_details,
#             "images": images,
#             "respon": res
#         }
#     )
# def provider_history(request, id):
#     provider = HotelProviders.objects.get(id=id)
#     past_bookings = history_data.objects.filter(hotelId=id).order_by('-accepted_date')
#     return render(
#         request,
#         "Provider_History.html",
#         {
#             "provider": provider,
#             "bookings": past_bookings
#         }
#     )
# def edit_hotel(request, id):
#     hotel = HotelProviders.objects.get(id=id)
#     if request.method == "POST":
#         hotel.HotelName = request.POST.get('HotelName')
#         hotel.city = request.POST.get('City')
#         hotel.address = request.POST.get('Address')
#         hotel.msg = request.POST.get('Msg')
#         hotel.phone = request.POST.get('Mobile')
#         hotel.save()
#         if request.FILES.getlist('hotel_images'):
#             images = request.FILES.getlist('hotel_images')
#             for image in images:
#                 image_binary = image.read()
#                 HotelImages.objects.create(
#                     hotel=hotel,
#                     image=image_binary
#                 )
#         messages.success(request, "Hotel details updated successfully!")
#         images = HotelImages.objects.filter(hotel=hotel)
#         for img in images:
#             img.base64 = base64.b64encode(img.image).decode("utf-8")
#         res = requestData.objects.filter(hotel_id=hotel.id)
#         return render(
#             request,
#             "U_provider_dash_board.html",
#             {
#                 "provider": hotel,
#                 "images": images,
#                 "respon": res
#             }
#         )
#     images = HotelImages.objects.filter(hotel=hotel)
#     for img in images:
#         img.base64 = base64.b64encode(img.image).decode("utf-8")
#     return render(request, "edit_hotel.html", {"provider": hotel, "images": images})
# def delete_image(request, img_id):
#     try:
#         img = HotelImages.objects.get(id=img_id)
#         hotel_id = img.hotel.id
#         img.delete()
#         messages.success(request, "Image deleted successfully.")
#     except HotelImages.DoesNotExist:
#         messages.error(request, "Image not found.")
#         hotel_id = None
#     return redirect('edit_hotel', id=hotel_id)
# def logout_user(request):
#     request.session.flush()
#     return redirect('/')
# def accept_history(request,id):
#     bookings=history_data.objects.filter(hotelId=id)
#     return render(request, "accepted_history.html",context={"bookings":bookings})

import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
import base64
from datetime import date
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from google import genai
from google.genai import types
from .models import HotelProviders, HotelImages, CustomerDetails, requestData, history_data


def home(request):
    return render(request, 'indexLogin.html')


def Customerstorage(request):
    if request.method == "POST":
        name = request.POST.get('Name')
        phone = request.POST.get('Mobile')
        email = request.POST.get('Email')
        password = request.POST.get('Password1')
        cpassword = request.POST.get('Password2')
        if password != cpassword:
            messages.error(request, "Passwords didn't match.")
            return redirect('/')
        if CustomerDetails.objects.filter(email=email).exists():
            messages.error(request, "Registration Failed: Email already exists.")
            return redirect('/')
        storage = CustomerDetails.objects.create(name=name, phone=phone, email=email, password=password)
        storage.save()
        messages.success(request, "Customer Registration Successful! You can now login.")
        return redirect('/')


def Providerstorage(request):
    if request.method == "POST":
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        mobile = request.POST.get('Mobile')
        HotelName = request.POST.get('HotelName')
        password1 = request.POST.get('Password1')
        password2 = request.POST.get('Password2')
        city = request.POST.get('City')
        Type = request.POST.get('Type')
        Price = request.POST.get('Price')
        address = request.POST.get('Address')
        desc = request.POST.get('Msg')
        if password1 != password2:
            messages.error(request, "Passwords didn't match.")
            return redirect('/')
        if HotelProviders.objects.filter(email=email).exists():
            messages.error(request, "Provider Registration Failed: Email already exists.")
            return redirect('/')
        storage = HotelProviders.objects.create(
            name=name, email=email, phone=mobile, HotelName=HotelName,
            password=password1, city=city, address=address, msg=desc,
            HotelType=Type, Price=Price
        )
        storage.save()
        images = request.FILES.getlist('hotel_images')
        for image in images:
            image_binary = image.read()
            HotelImages.objects.create(
                hotel=storage,
                image=image_binary
            )
        messages.success(request, "Provider Registration Successful! You can now login.")
        return redirect('/')


def login(request):
    if request.method == "POST":
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        Type = request.POST.get('Type')
        if Type == 'Pro':
            if HotelProviders.objects.filter(email=Email, password=Password).exists():
                data = HotelProviders.objects.get(email=Email, password=Password)
                images = HotelImages.objects.filter(hotel=data)
                for img in images:
                    img.base64 = base64.b64encode(img.image).decode("utf-8")
                res = requestData.objects.filter(hotel_id=data.id)
                return render(
                    request,
                    "U_provider_dash_board.html",
                    {"provider": data, "images": images, "respon": res}
                )
            else:
                messages.error(request, "Provider login failed. Please check your credentials.")
                return redirect('/')
        elif Type == 'Cust':
            if CustomerDetails.objects.filter(email=Email, password=Password).exists():
                data = HotelProviders.objects.all()
                return render(request, "Customer_dashboard.html", context={'hotels': data})
            else:
                messages.error(request, "Customer login failed. Please check your credentials.")
                return redirect('/')
    return redirect('/')


def locationsearch(request):
    data = HotelProviders.objects.filter(city=request.GET.get('search'))
    return render(request, "Customer_dashboard.html", context={'hotels': data})


def all(request):
    data = HotelProviders.objects.all()
    return render(request, "Customer_dashboard.html", context={'hotels': data})


def hotel_details(request, id):
    data = HotelProviders.objects.get(id=id)
    images = HotelImages.objects.filter(hotel_id=id)
    for img in images:
        img.base64 = base64.b64encode(img.image).decode("utf-8")
    return render(request, "Hotel_Temp.html", context={'hotel': data, 'images': images})


def requestdata(request, id):
    name = request.POST.get('Name')
    email = request.POST.get('Email')
    mobile = request.POST.get('Mobile')
    checkin = request.POST.get('Checkin')
    checkout = request.POST.get('Checkout')
    storage = requestData.objects.create(name=name, email=email, phone=mobile, checkin=checkin, checkout=checkout,
                                         hotel_id=id)
    storage.save()
    mail = HotelProviders.objects.get(id=id).email
    provider = HotelProviders.objects.get(id=id).name
    send_mail(
        subject="New Customer Booking Request – Action Required",
        message=f"""
Dear {provider},
Greetings from BookMyStay!
You have received a new booking request from a customer who is interested in staying at your hotel.
Customer Details:
Customer Name: {name}
phone number: {mobile}
email: {email}
Please log in to your BookMyStay dashboard to view the complete booking details, including the customer's request and stay information.
Kindly review the request and take the necessary action at your earliest convenience. If you are able to accommodate the customer, please accept the request and allot a suitable room. If there is no availability, you may decline the request.
We appreciate your prompt response and cooperation in providing our customers with a smooth and pleasant booking experience.
Thank you for being a valued partner of BookMyStay.
Best regards,
BookMyStay Team
"""
        ,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[mail]
    )
    messages.success(request, "Booking successful! You will get a response from the owner in your mail.")
    return redirect('hotel_details', id=id)


def accept_request(request, id, email, u_id):
    hotel_details = HotelProviders.objects.get(id=id)
    provider = hotel_details.name
    hotel_name = hotel_details.HotelName
    hotel_address = hotel_details.address
    phone_number = hotel_details.phone
    req_data = requestData.objects.get(id=u_id)
    if request.method == "POST":
        room_number = request.POST.get('roomnumber')
        try:
            rooms_int = int(room_number)
        except ValueError:
            rooms_int = 0
        history = history_data.objects.create(
            hotelId=hotel_details.id,
            cName=req_data.name,
            phone=req_data.phone,
            email=req_data.email,
            checkin=req_data.checkin,
            checkout=req_data.checkout,
            alloted_rooms=rooms_int,
            accepted_date=date.today()
        )
        history.save()
        send_mail(
            subject="Hotel Booking Confirmed – We Look Forward to Welcoming You!",
            message=f"""Dear Customer,
Warm greetings from {hotel_name}!
We are delighted to confirm your booking with us. Thank you for choosing {hotel_name} for your stay. It is our pleasure to welcome you, and we look forward to providing you with a comfortable, relaxing, and memorable experience.
Reservation Details:
Hotel Name: {hotel_name}
Hotel Address: {hotel_address}
Allotted Room Number: {room_number}
We hope your upcoming stay will be filled with comfort, happiness, and wonderful moments. Our team is committed to making your visit enjoyable and ensuring that you feel right at home throughout your stay.
We wish you a safe and pleasant journey to the hotel. May you have a wonderful time with us and create many happy memories during your stay.
Should you need any assistance before or during your visit, please do not hesitate to contact our front desk team. We will be happy to assist you with any questions or special requests.
Phone: {phone_number}
Email: {settings.EMAIL_HOST_USER}
Thank you once again for choosing {hotel_name}. We sincerely appreciate your trust and look forward to welcoming you.
Wishing you a safe journey, a pleasant stay, and a wonderful experience with us!
Warm regards,
{provider}
{hotel_name}
        """,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
        req_data.delete()
    elif request.method == "GET":
        send_mail(
            subject="Hotel Booking Request – Not Accepted",
            message=f"""Dear Customer,
Thank you for choosing our hotel and for submitting your booking request.
We regret to inform you that your booking request could not be accepted, and a room has not been allotted to you for the requested stay.
We apologize for any inconvenience this may cause and appreciate your understanding.
If you have any questions or would like to check for alternative availability, please feel free to contact our front desk team.
{hotel_name}
{hotel_address}
Phone: {phone_number}
Email: {settings.EMAIL_HOST_USER}
We hope to have the opportunity to serve you in the future.
Warm regards,
{provider}
{hotel_name}
""",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
        req_data.delete()
    images = HotelImages.objects.filter(hotel=hotel_details)
    for img in images:
        img.base64 = base64.b64encode(img.image).decode("utf-8")
    res = requestData.objects.filter(hotel_id=hotel_details.id)
    return render(
        request,
        "U_provider_dash_board.html",
        {
            "provider": hotel_details,
            "images": images,
            "respon": res
        }
    )


def provider_history(request, id):
    provider = HotelProviders.objects.get(id=id)
    past_bookings = history_data.objects.filter(hotelId=id).order_by('-accepted_date')
    return render(
        request,
        "Provider_History.html",
        {
            "provider": provider,
            "bookings": past_bookings
        }
    )


def edit_hotel(request, id):
    hotel = HotelProviders.objects.get(id=id)
    if request.method == "POST":
        hotel.HotelName = request.POST.get('HotelName')
        hotel.city = request.POST.get('City')
        hotel.address = request.POST.get('Address')
        hotel.msg = request.POST.get('Msg')
        hotel.phone = request.POST.get('Mobile')
        hotel.save()
        if request.FILES.getlist('hotel_images'):
            images = request.FILES.getlist('hotel_images')
            for image in images:
                image_binary = image.read()
                HotelImages.objects.create(
                    hotel=hotel,
                    image=image_binary
                )
        messages.success(request, "Hotel details updated successfully!")
        images = HotelImages.objects.filter(hotel=hotel)
        for img in images:
            img.base64 = base64.b64encode(img.image).decode("utf-8")
        res = requestData.objects.filter(hotel_id=hotel.id)
        return render(
            request,
            "U_provider_dash_board.html",
            {
                "provider": hotel,
                "images": images,
                "respon": res
            }
        )
    images = HotelImages.objects.filter(hotel=hotel)
    for img in images:
        img.base64 = base64.b64encode(img.image).decode("utf-8")
    return render(request, "edit_hotel.html", {"provider": hotel, "images": images})


def delete_image(request, img_id):
    try:
        img = HotelImages.objects.get(id=img_id)
        hotel_id = img.hotel.id
        img.delete()
        messages.success(request, "Image deleted successfully.")
    except HotelImages.DoesNotExist:
        messages.error(request, "Image not found.")
        hotel_id = None
    return redirect('edit_hotel', id=hotel_id)


def logout_user(request):
    request.session.flush()
    return redirect('/')


def accept_history(request, id):
    bookings = history_data.objects.filter(hotelId=id)
    return render(request, "accepted_history.html", context={"bookings": bookings})

def search_hotels(city: str) -> str:
    """Searches the database for hotels in a specific city."""
    hotels = HotelProviders.objects.filter(city__icontains=city)
    if not hotels.exists():
        return f"No hotels currently registered in {city} on BookMyStay."

    results = []
    for h in hotels:
        results.append(
            f"Hotel: {h.HotelName} | Rating: {h.HotelType} Stars | Price: ₹{h.Price}/night | Location: {h.address} ({h.city})"
        )
    return "\n".join(results)


@csrf_exempt
def hotel_chat(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message")

            client = genai.Client(api_key="")
            travel_concierge_instruction = (
                "You are an authentic, knowledgeable, and helpful AI Travel Concierge for 'BookMyStay'.\n\n"
                "Your responsibilities are strictly limited to the following categories:\n\n"
                "1. Destination Guidance (Confusion on where to visit):\n"
                "   - If a user is unsure where to go, ask clarifying questions about their preferences (e.g., beaches, mountains, budget, family vs. solo).\n"
                "   - Recommend ideal cities or states based on their criteria.\n\n"
                "2. Trip Planning & Itineraries:\n"
                "   - When asked to plan a trip, provide a brief, well-structured travel guide (best time to visit, top attractions, brief itinerary).\n\n"
                "3. Hotel Availability & Booking:\n"
                "   - Whenever a specific city or destination is mentioned for a stay, ALWAYS use the `search_hotels(city)` tool.\n"
                "   - Showcase the retrieved hotels seamlessly. If none are found, mention that BookMyStay is currently onboarding stays in that region.\n"
                "   - For direct hotel searches (e.g., 'hotels in goa'), ONLY display the hotel results concisely without a full itinerary.\n\n"
                "4. Basic Medical Assistance & Travel Health:\n"
                "   - Provide general, non-diagnostic travel health tips (e.g., handling motion sickness, altitude sickness precautions, hydration, basic first-aid packing list).\n"
                "   - Always advise users to seek professional medical help for severe issues.\n\n"
                "5. Emergency Helplines (India):\n"
                "   - If asked for emergency help, provide the official Indian national helplines:\n"
                "     * 112: National Emergency (Police, Fire, Ambulance)\n"
                "     * 1363 or 1800-11-1363: 24x7 Multi-lingual Tourist Helpline\n"
                "     * 108: Emergency Disaster/Ambulance\n"
                "     * 1091: Women's Helpline\n\n"
                "6. Out-of-Scope Queries (CRITICAL):\n"
                "   - If the user asks about coding, math, general knowledge, or anything unrelated to travel, vacations, hotels, or travel safety, you MUST politely decline and state: 'I am made to clear vacation related issues.'\n\n"
                "Maintain a warm, professional, and helpful tone using clean formatting."
            )

            chat = client.chats.create(
                model="gemini-3.6-flash",
                config=types.GenerateContentConfig(
                    system_instruction=travel_concierge_instruction,
                    tools=[search_hotels]
                )
            )

            response = chat.send_message(user_message)
            return JsonResponse({"response": response.text})

        except Exception as e:
            return JsonResponse({"response": f"Sorry, I encountered an error: {str(e)}"})

    return JsonResponse({"error": "Invalid request"}, status=400)



