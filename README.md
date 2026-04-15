# 🧠 Fake News Detector (Django Project)

A full-stack web application built using Django that detects whether a given news content is **Real or Fake**.

---

## 🌐 Live Demo

👉 https://fake-news-detector-8wwm.onrender.com

---

## 🚀 Features

* 📰 User can enter news content
* 🔍 Detects whether news is Fake or Real
* 💾 Stores results in database (SQLite)
* ⚡ Fast and simple UI
* 🌍 Deployed on Render

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Python (Django Framework)
* **Database:** SQLite
* **Deployment:** Render
* **Server:** Gunicorn

---

## 📁 Project Structure

```
FakeNews_detector/
│
├── manage.py
├── requirements.txt
├── build.sh
├── runtime.txt
│
├── FakeNews_detector/
│   ├── settings.py
│   ├── urls.py
│
├── detector/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── detector/
│           ├── index.html
│           └── result.html
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```
git clone https://github.com/ganeshbavu/Fake-news-detector.git
```

2. Navigate to project folder:

```
cd Fake-news-detector
```

3. Create virtual environment:

```
python -m venv venv
```

4. Activate environment:

```
venv\Scripts\activate
```

5. Install dependencies:

```
pip install -r requirements.txt
```

6. Run migrations:

```
python manage.py migrate
```

7. Start server:

```
python manage.py runserver
```

8. Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🧠 How It Works

* User enters news content
* System checks keywords (basic logic)
* Displays result: **Fake** or **Real**
* Stores input and result in database

---

## 📌 Future Enhancements

* 🤖 Integrate Machine Learning model
* 🔐 Add user authentication (Login/Register)
* 📊 Dashboard for previous results
* 🎨 Improve UI/UX

---

## 👨‍💻 Author

**Ganesh Bavu**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
