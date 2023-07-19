# Interactive User Guides Template Based on Django

<div align="center">
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" target="_blank" /></div>
</br>
This project is a web-based interactive user guide template built using the Django web framework. It provides a flexible and customizable platform for creating user guides that can be used to educate and onboard new users or to provide assistance and support for existing users.
</br>
</br>
The user guide template includes a variety of features, such as interactive walkthroughs, step-by-step instructions, and tooltips, designed to help users learn and navigate your application or website. The user guide is also fully responsive, meaning it can be accessed from any device, including desktops, tablets, and smartphones.
</br>
</br>
The project includes a predefined template that can be customized to match your application's branding and style. The template is designed to be easy to use and can be adapted to suit a wide range of use cases.
</br>
</br>
In addition to the user guide templates, the project also includes a set of tools for managing and updating your user guides. These tools include a web-based editor for creating and modifying your user guides.
</br>
</br>
Overall, this project provides a powerful and flexible platform for creating interactive user guides that can help improve the user experience of your device or web application.
</br>
</br>
Whether you are looking to educate new users or provide ongoing support and assistance, this user guide template based on Django can help you achieve your goals.
</br>
</br>

## How to Run

This Django project is designed to be easy to set up and run. Here are the steps you need to follow to get started:

### Prerequisites
Before you can run this Django project, you need to have the following software installed:

Python 3.6 or later
Django 3.0 or later

### Installation

To install this Django project, follow these steps:

1- Clone the project repository to your local machine using the command:
```sh
git clone https://github.com/yourusername/yourproject.git
```
2- Navigate to the project directory using the command:
```sh
cd yourproject
```
3- Create a virtual environment and activate it using the following commands:
```sh
python3 -m venv env
source env/bin/activate
```
4- Install the project dependencies using the command:
```sh
pip install -r requirements.txt
```

### Create user to create and edit data 

create a superuser by writing the following command:
```sh
python manage.py createsuperuser
```
We then write the following credentials step by step. We can fill these credentials according to our preferences:

```sh
Username: testAdminUser
Email address: test@gmail.com
Password: ********
Password (again): ********
```
Note: After filling a row, press “Enter” to fill the other information.

Now the superuser will be created if we have entered all fields correctly.

### Running the Project

Once you have installed and configured the Django project, you can run it using the following command:
```sh
python manage.py runserver
```

This command will start the Django development server, and you should be able to access the project by navigating to ```http://127.0.0.1:8000/``` in your web browser.

That's it! You should now have this Django project up and running on your local machine.

## License
MIT

**Free Software!**

