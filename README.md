
# Flask Application

This application was created during classes at the School of Artistic Crafts in Jelenia Góra, in the field of IT Technician, as part of the Application Programming course. The project includes basic functionalities of a web application, such as data management through ORM, routing, and HTML templates for the user interface.

## Functionalities

- Data management using Flask-SQLAlchemy (data models for products, categories, and brands)
- Displaying data in the browser (HTML templates)
- Generating sample data for application testing

## Installation

To install the required dependencies, clone the repository and run:

```
pip install -r requirements.txt
```

Then, to configure the database, execute the following commands:

```
flask db init
flask db migrate
flask db upgrade
```

## Running the application

The application can be launched using the command:

```
python app.py
```

## Directory Structure

- `app/` - main application files (models, routes, initialization)
- `app/templates` - HTML templates
- `scripts/` - auxiliary scripts, e.g., for generating data
- `app.py` - application startup file
- `config.py` - application configuration

## Copyright

The project was created as part of the Application Programming classes in the 4IR class by Bartosz Bryniarski. You are free to use the code.
