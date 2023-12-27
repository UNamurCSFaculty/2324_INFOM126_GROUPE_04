
# Setup Guide for Guestbook Project

Welcome to the Guestbook project! This document will guide you through the setup process to get your development environment ready.

## Docker

If you rather use a docker solution to test your changes, this can be done. But, be sure that docker is installed on your workstation. 

You first had to build the docker image using the Dockerfile. Be sure to be in the right directory.

```bash
docker build -t guestbook-django . 
```

Then, you are able to run the docker.

```bash
docker run -dp 127.0.0.1:8000:8000 guestbook-django
```

Now, open the following link in your favorite browser: http://127.0.0.1:8000

## Manually

### Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.10 or above
- pip (Python package installer)
- Virtual environment (optional but recommended)
- Git
- Database (SQLite)

### Getting the Code

First, you'll need to clone the repository:

```bash
git clone https://github.com/yourusername/guestbook.git
cd guestbook
```

### Setting Up a Virtual Environment

It's recommended to create a virtual environment to keep dependencies required by different projects separate by creating isolated python virtual environments for them. Here's how you can do that:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Installing Dependencies

Once your virtual environment is activated, you can install the project dependencies:

```bash
pip install -r requirements.txt
```

### Configuring the Database

By default, Django uses SQLite, so there's minimal configuration required. However, if you're using a different database, you'll need to configure it in your `settings.py` file.

### Running Migrations

Before you can run the application, you need to apply the migrations to set up your database schema:

```bash
python manage.py migrate
```

### Running the Development Server

To run the development server and access the application in your browser, execute:

```bash
python manage.py runserver
```

Now, you should be able to open http://127.0.0.1:8000/ in your browser and see the project running.

## Next Steps

- Explore the application and its features.
- Consult the `README.md` for more information on the project structure and guidelines.
- Check out the `CONTRIBUTING.md` file to see how you can contribute to the project.

Congratulations, you've successfully set up the Guestbook project on your local machine!
