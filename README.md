Hotel Search App with Django and Vue.js
This is a simple hotel search application built using Django on the backend and Vue.js on the frontend. The application allows users to search for hotels based on various criteria such as amenities, sorting options, and price range.

Description
The Hotel Search App is designed to provide users with a convenient way to search for hotels based on their preferences. Users can filter hotels by selecting amenities, sorting options, and setting a price range. The application fetches hotel data from the backend server and displays it dynamically on the frontend using Vue.js.

Features
Search for hotels based on amenities
Sort hotels by price in ascending or descending order
Filter hotels by price range using a slider
Display hotel details including name, description, and price
Technologies Used
Django: A high-level Python web framework for backend development.
Vue.js: A progressive JavaScript framework for building user interfaces.
Bootstrap: A front-end framework for building responsive and mobile-first websites.
Installation
Clone the repository:


git clone <repository_url>
Navigate to the project directory:


cd hotel-search-app
Install dependencies:


pip install -r requirements.txt
Run migrations:


python manage.py migrate
Start the Django development server:


python manage.py runserver
Navigate to http://localhost:8000 in your web browser to access the application.

Usage
Select amenities from the dropdown menu.
Choose a sorting option from the dropdown menu.
Adjust the price range using the slider.
View the list of hotels matching the selected criteria.
Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/improvement).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/improvement).
Create a new Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Special thanks to the developers of Django and Vue.js for providing powerful tools to build web applications.
