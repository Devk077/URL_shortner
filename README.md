# 🌐 URL Shortener & QR Code Generator

Welcome to the **URL Shortener & QR Code Generator** project! This Django-based web application allows users to shorten URLs and generate QR codes effortlessly. The project is designed to be simple, efficient, and user-friendly.

## 🚀 Key Features

- **URL Shortening**: Quickly shorten long URLs with optional custom names.
- **QR Code Generation**: Generate QR codes for any URL.
- **reCAPTCHA Integration**: Enhanced security with Google reCAPTCHA.
- **User-Friendly Interface**: Clean and modern design for an optimal user experience.
- **Responsive Design**: Works seamlessly on all devices.

## 🎨 User Interface

The interface is designed to be intuitive and easy to use, featuring a gradient background and a clean form layout:

![Screenshot](https://github.com/Devk077/URL_shortner/blob/main/media/image.png)

## 🛠️ Installation

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/url-shortener.git
    cd url-shortener
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the Server**:
    ```bash
    python manage.py runserver
    ```

6. **Visit the Application**:
    Open your browser and go to `http://localhost:8000`.

## 📝 Usage

1. **Enter the URL** you want to shorten or generate a QR code for.
2. **Optional**: Enter a custom name for the shortened URL.
3. **Select** whether you want to create a shortened URL or a QR code.
4. **Complete the reCAPTCHA** and click the "Shorten" button.
5. **Copy the shortened URL** or **download the QR code**.

## 📂 Project Structure

```
urlshortener/
├── urlshortener/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── shortener/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── ...
├── manage.py
├── requirements.txt
└── README.md
```

## 🧩 Models

- **URL**:
    - `url`: The original URL to be shortened.
    - `uuid`: The unique identifier for the shortened URL.

- **QRCode**:
    - `uuid`: The unique identifier for the QR code.
    - `img`: The generated QR code image.
    - `url`: The original URL for the QR code.

## 🔒 Security

- Integrated with **Google reCAPTCHA** to prevent spam and abuse.
- Proper validation and error handling for a secure user experience.

## 🛠️ Technologies Used

- **Django**: High-level Python web framework.
- **jQuery**: Simplifies HTML document traversing and AJAX interactions.
- **Bootstrap**: For responsive design and styling.
- **qrcode**: Python library for generating QR codes.
- **reCAPTCHA**: To protect the application from bots and abuse.

---

⭐ If you like this project, give it a star!

For any queries or support, please contact [dev.kapadia10000@gmail.com](mailto:dev.kapadia10000@gmail.com).

Happy URL Shortening! 🎉
