# Django DRF Blog API

A RESTful API for a blog built with Django and Django REST Framework (DRF). This API allows users to create, read, update, and delete blog posts, comment on posts.

---

## Features
- **User Authentication**: Register, login, and logout.
- **Blog Posts**: CRUD operations for blog posts.
- **Comments**: Add comments to posts.
- **Search**: Search for posts by title or content.
- **Pagination**: Paginate posts for better performance.
- **Permissions**: Restrict access to certain actions (e.g., only authors can edit their posts).


---

## Getting Started

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-drf-blog-api.git
   cd django-drf-blog-api 
   ``` 
2. **Create a virtual environment**: (optional but recommended):
    ```bash
        python -m venv venv
        venv\Scripts\activate  # On mac: source venv/bin/activate 
    ```     
3. **Install dependencies**:

    ```bash
        pip install -r requirements.txt
    ```
4. **Set up the database**:

  Update the DATABASES configuration in settings.py with your database credentials.

  Run migrations:
    ```bash
        python manage.py migrate
    ```      

