Instructions for running the API paths to test the applications in the review process:

PREPARATIONS

First, make sure that, in the project's outer folder (with a Pipfile), you've executed the following commands before you proceed with the test steps:
			
			pipenv install
			pipenv shell

TESTS

Test the available unit tests from the terminal using:

	python manage.py test restaurant.tests.test_models
	python manage.py test restaurant.tests.test_views

To confirm that this web app serves static HTML content:

	python manage.py runserver
	Then, visit: /restaurant/

Djoser endpoints...

To confirm user registration, you can make a POST request to create a new user:

	/auth/users/

To login an user and get its authentication token:
	
	/auth/token/login/

# In the next endpoints, if asked for authentication, you can login using the credentials:

			username: eduardo
			password: xJr,r%eB7ot.a

Menu endpoints...

To see all menu items:

	/restaurant/menu/

To see any given menu item by id (initially 1, 2 or 4):
	
	/restaurant/menu/{menu_item_id}

Table booking...

Make a POST request to book a table at:

	/restaurant/booking/tables/

To see any given booking by id (initially 1 or 2):

	/restaurant/booking/tables/{booking_id}

To confirm that the Django application connects to a MySQL database:
	
	Check DATABASES in the project's settings.py file.


