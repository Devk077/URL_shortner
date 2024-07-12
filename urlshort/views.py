from django.shortcuts import render, HttpResponse, redirect
from .models import URL, QRCode
import uuid
import requests
import json
from django.conf import settings
from django.core.files.storage import default_storage
import os
from django.http import JsonResponse
from django.shortcuts import render
import qrcode
# Create your views here.
def index(request):
    return render(request, "index.html")

def create_qrcode(request):
    if request.method == "POST":
        link = request.POST.get("link")
        clientkey = request.POST.get('g-recaptcha-response')

        # Validate reCAPTCHA
        if not clientkey:
            return HttpResponse("reCAPTCHA validation failed", status=400)

        secretkey = settings.RECAPTCHA_PRIVATE_KEY  # Replace with your secret key
        captcha_data = {
            "secret": secretkey,
            "response": clientkey,
        }
        verify_response = requests.post("https://www.google.com/recaptcha/api/siteverify", data=captcha_data)
        response_data = json.loads(verify_response.text)

        if response_data['success']:
            # reCAPTCHA verification passed, continue with QR code generation
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(link)
            qr.make(fit=True)
            qr_img = qr.make_image(fill_color="black", back_color="white")

            # Save QR code image to a file
            img_filename = f'qrcode_{uuid.uuid4()}.png'
            img_path = os.path.join(settings.MEDIA_ROOT, 'qrcodes', img_filename)
            qr_img.save(img_path)

            # Save QR code data to the database
            qr_code = QRCode(
                uuid=img_filename.split('.')[0],
                img=f'qrcodes/{img_filename}',
                url=link
            )
            qr_code.save()

            # Construct the image URL
            img_url = os.path.join(settings.MEDIA_URL, 'qrcodes', img_filename)
            return JsonResponse({'img_url': img_url, 'uuid': qr_code.uuid})
        else:
            # reCAPTCHA verification failed
            return HttpResponse("Invalid reCAPTCHA. Please try again.", status=400)

    return HttpResponse("Method not allowed", status=405)

def create_url(request):
    if request.method == "POST":
        link = request.POST.get("link")
        custom_name = request.POST.get("name")
        print(custom_name)
        clientkey = request.POST.get('g-recaptcha-response')

        # Validate reCAPTCHA
        if not clientkey:
            return HttpResponse("reCAPTCHA validation failed", status=400)

        secretkey = settings.RECAPTCHA_PRIVATE_KEY  # Replace with your secret key
        captcha_data = {
            "secret": secretkey,
            "response": clientkey,
        }
        verify_response = requests.post("https://www.google.com/recaptcha/api/siteverify", data=captcha_data)
        response_data = json.loads(verify_response.text)

        if response_data['success']:
            # reCAPTCHA verification passed, continue with URL shortening logic
            if custom_name:
                if len(custom_name) > 10:
                    return HttpResponse("Custom Name too long. Please keep it under 10 characters.", status=400)
                else:
                    new_url = URL(url=link, uuid=custom_name)
                    new_url.save()
                    return HttpResponse(new_url.uuid)
            else:
                uid = str(uuid.uuid4())[:5]
                new_url = URL(url=link, uuid=uid)
                new_url.save()
                return HttpResponse(uid)
        else:
            # reCAPTCHA verification failed
            return HttpResponse("Invalid reCAPTCHA. Please try again.", status=400)

    return HttpResponse("Method not allowed", status=405)

def go(request, pk):
    try:
        url_details = URL.objects.get(uuid=pk)
        if not url_details.url.startswith("http"):
            return redirect("http://" + url_details.url)
        elif not url_details.url.startswith("https"):
            return redirect("https://" + url_details.url)
        else:
            return redirect(url_details.url)
    except URL.DoesNotExist:
        return HttpResponse("URL not found", status=404)  # Return a 404 status code for better clarity
