# Learning Log - Personal Learning Journal with Django

**Learning Log** is a web application that helps users keep track of the subjects they are studying and record what they learn. Users can create learning topics and add notes or annotations to each topic, building a personal learning journal over time.

The project was developed with **Python and Django**, applying Django's **MVT (Model-View-Template)** architecture, authentication features, and ORM for database management.

------------------------------------------------------------------------

## 🚀 Features

### 🔐 Authentication and User Access

-   **User Registration:** Create an account using Django's built-in user creation form.
-   **Login and Logout:** Authenticate securely through Django's authentication system.
-   **Restricted Access:** Topics and annotations are available only to authenticated users.
-   **User Data Privacy:** Users can access only the topics they own and the notes associated with those topics.

### 📚 Learning Topic Management

-   **Create Topics:** Add subjects or topics you are currently studying.
-   **Topic Listing:** View and organize your personal learning topics.
-   **Topic Details:** Open a topic to view its associated annotations.
-   **Ownership:** Each topic is linked to its creator.

### 📝 Annotation Management

-   **Add Notes:** Record knowledge, ideas, and summaries within a learning topic.
-   **View Annotations:** Browse notes associated with a topic, ordered by their most recent creation date.
-   **Edit Notes:** Update existing annotations as your understanding evolves.
-   **Timestamps:** Topics and annotations store their creation date and time.

### 🎨 Interface and Administration

-   **Django Templates:** Render the application's pages on the server.
-   **Bootstrap:** Use Bootstrap styling through the `django-bootstrap3` package.
-   **Django Admin:** Manage application data through Django's built-in administration interface.

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   **Back-end:** Python 3, Django 6
-   **Front-end:** Django Templates, HTML, Bootstrap 3 integration (`django-bootstrap3`)
-   **Database:** SQLite
-   **Authentication:** Django's built-in authentication system
-   **ORM:** Django Object-Relational Mapper (ORM)

------------------------------------------------------------------------

## 📦 How to Run the Project Locally

Follow these steps to set up and run the application on your machine.

### 1. Clone the Repository

``` bash
git clone https://github.com/Moises-Jorge/Learning_Log.git
cd Learning_Log
```

### 2. Create and Activate a Virtual Environment

**Linux/macOS:**

``` bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**

``` bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

``` bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

``` bash
python manage.py migrate
```

### 5. Create a Superuser (Optional - Django Admin)

``` bash
python manage.py createsuperuser
```

Follow the terminal prompts to create the administrator account.

### 6. Run the Development Server

``` bash
python manage.py runserver
```

Open the application in your browser:

-   **Application:** http://127.0.0.1:8000/
-   **Admin Panel:** http://127.0.0.1:8000/admin/

------------------------------------------------------------------------

## ⚙️ Data Model Structure (Django ORM)

The application uses two main models:

### `TopicModel`

-   `title`: `CharField` --- topic title, with a maximum of 200 characters.
-   `date_added`: `DateTimeField` --- automatically records when the topic is created.
-   `owner`: `ForeignKey` --- links the topic to Django's built-in `User` model. Topics are deleted when their owner is deleted.

### `AnnotationModel`

-   `topic_id`: `ForeignKey` --- links an annotation to its learning topic. Annotations are deleted when the related topic is deleted.
-   `text`: `TextField` --- content of the learning note.
-   `date_added`: `DateTimeField` --- automatically records when the annotation is created.

Relationship overview:

-   One user can own multiple topics.
-   One topic can contain multiple annotations.
-   Each annotation belongs to one topic.

------------------------------------------------------------------------

## 🎯 Project Objective

Learning Log was developed as an academic and practical project to strengthen skills in Django web development, including user authentication, class-based views, forms, database relationships, ORM operations, and template-based interfaces.
