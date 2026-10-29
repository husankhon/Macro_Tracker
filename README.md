# MacroTracker 🔥

A sleek, modern macronutrient and daily calorie tracking web application built with **Django** and a high-performance **Frontend Dashboard** (Vanilla CSS, JavaScript, and Chart.js).

---

## ✨ Features

- 🎯 **Interactive Daily Calorie Target**:
  - Quick goal presets: `1,800`, `2,000`, `2,200`, `2,500` kcal, plus custom target input.
  - Persisted client-side via `localStorage` so your daily target is remembered across sessions.
  - Live metric counters for **Daily Goal**, **Calories Consumed**, and **Remaining / Over Budget**.

- 📊 **Animated Calorie Progress Bar**:
  - Real-time animated progress fill with light beam shimmer effects.
  - Milestone indicators at `25%`, `50%`, `75%`, and `100%`.
  - Dynamic color transitions:
    - 🟢 **In Budget** (< 95%): Warm orange gradient glow.
    - 🎯 **Goal Reached** (95% - 100%): Emerald green gradient glow.
    - ⚠️ **Over Budget** (> 100%): Crimson alert gradient with `+X kcal over target` indicator.

- 📈 **Dual-Mode Calorie Breakdown Chart**:
  - Interactive Doughnut chart with center stat readout.
  - **Macro Energy Split**: Visualizes calories from Protein (4 kcal/g), Carbs (4 kcal/g), Fat (9 kcal/g), and remaining calories to reach your goal.
  - **By Food View**: Dynamically parses logged food items from the DOM and visualizes each food's share of calories.
  - Powered by Chart.js with an automatic native HTML5 Canvas fallback for offline reliability.

- ⚡ **Live Macro & Calorie Serving Preview**:
  - Instant client-side macro calculations when selecting a food catalog item and adjusting serving quantities.

- 👤 **Multi-User Logging**:
  - Assign food entries to specific user accounts with styled badges in the food log table.

- 🗑️ **Confirmation Deletion Page**:
  - Dedicated [delete.html](myapp/templates/myapp/delete.html) confirmation screen displaying full macro details of the item prior to deletion.

- 🌙 **Modern Dark-Mode Aesthetic**:
  - Glassmorphism card surfaces, custom typography (Inter font), smooth micro-animations, and full mobile responsiveness.

---

## 🛠️ Tech Stack

- **Backend**: Python 3, Django
- **Database**: SQLite (default, easily switchable to PostgreSQL)
- **Frontend**: HTML5, Vanilla CSS3 (Custom design system), JavaScript (ES6+)
- **Charting**: Chart.js (with pure HTML5 Canvas fallback)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/husankhon/Macro_Tracker.git
cd Macro_Tracker
```

### 2. Set Up Virtual Environment

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

Open your browser and navigate to:
```text
http://127.0.0.1:8000/
```

Access the Django Admin panel to manage the food catalog:
```text
http://127.0.0.1:8000/admin/
```

---

## 📁 Project Structure

```text
mysite/
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── myapp/
    ├── admin.py
    ├── apps.py
    ├── models.py          # Food & FoodLog models
    ├── urls.py
    ├── views.py           # Dashboard & delete views
    └── templates/
        └── myapp/
            ├── index.html  # Main dashboard with progress bar & charts
            └── delete.html # Delete confirmation page
```

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
