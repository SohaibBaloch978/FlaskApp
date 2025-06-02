# Flask Students CRUD App (Enhanced & Dockerized)

## Features
- Modern, responsive UI (Bootstrap 5)
- Full CRUD for student data
- Client-side and server-side input validation
- Dockerized for easy deployment

## Quick Start

### 1. Clone the repo
```sh
git clone https://github.com/SohaibBaloch978/FlaskApp
cd Flask_App
```

### 2. Build the Docker image
```sh
docker build -t flaskapp .
```

### 3. Initialize the database
```sh
docker run --rm -v ${PWD}:/app flaskapp python init_db.py
```
*(On Windows PowerShell, use `${PWD}` instead of `$(pwd)`)*

### 4. Run the app
```sh
docker run -p 5000:5000 -v ${PWD}:/app flaskapp
```
Access the app at: [http://localhost:5000](http://localhost:5000)

## Manual Run (without Docker)
1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
2. Initialize DB:
    ```
    python init_db.py
    ```
3. Run the app:
    ```
    python app.py
    ```

## Project Structure
- `app.py` - main Flask app
- `models.py` - SQLAlchemy models
- `forms.py` - Flask-WTF forms
- `templates/` - HTML templates
- `static/` - CSS and assets
- `requirements.txt` - Python dependencies
- `Dockerfile` & `.dockerignore` - for containerization

## Testing Data
- Example students: Alice Smith, Bob Khan, Sara Ali
- Example users: admin@example.com / Admin@123

---

**Enjoy!**
