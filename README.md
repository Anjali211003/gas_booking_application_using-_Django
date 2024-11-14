Gas Booking Application


A Django-based web application for managing and booking gas cylinder services. This project provides a user-friendly platform for customers to book gas services, view booking history, and manage account details.


Features

User Registration and Authentication: Secure login and signup for customers.
Booking Management: Allows users to book gas cylinders easily.
Booking History: Users can view their past bookings.
Admin Dashboard: Admins can manage bookings, view customer details, and handle service requests.
Notifications: Sends email notifications to users on successful bookings.

Technologies Used
Django - The web framework used for building this application.
SQLite - Database for storing user and booking data.
HTML/CSS - Frontend templates.
Bootstrap - For responsive and styled UI components.

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/Anjali211003/gas_booking_application_using-_Django.git
cd gas_booking_application_using-_Django
Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Run the server:

bash
Copy code
python manage.py runserver

Usage
Access the application at http://127.0.0.1:8000/ in your browser.
Register or log in to book a gas cylinder.
Use the admin dashboard for managing bookings and customer information.


Project Structure
gas_booking/ - Main project directory.
app_name/ - Contains application-specific modules (e.g., booking, user management).
templates/ - HTML templates for frontend views.
static/ - Static files like CSS and JavaScript.


Contributing
Contributions are welcome! Please fork the repository and create a pull request.
