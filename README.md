# Running / Training Planning

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Live Demo](https://img.shields.io/badge/Try%20It%20Now-https://genewu.pythonanywhere.com-brightgreen)](https://genewu.pythonanywhere.com/)

**Plan your next run in Sha Tin, Hong Kong with style!** This Flask app calculates your workout time based on distance, pace, drills, and sprints—now with **interactive Google Maps showing your full route embedded in the page**! Enjoy drill videos and a Sha Tin Racecourse backdrop for that local vibe. 🌟

## ✨ Features
- **Routes:**
  - **7.2 km**: SCTC → Sha Tin Sports Ground → Twin Bridge → SCTC (includes drills & sprints).
  - **10.3 km**: SCTC → Ma On Shan Promenade → SCTC.
  - **13.5 km**: SCTC → Twin Bridge → HK Science Park → SCTC.
- **Customizable:** Set pace (default 6:00 min/km) via dropdowns; adjust sprint sets for Option 1.
- **Output:** Detailed summary with run time, drill/sprint times (if applicable), and total duration.
- **Extras:** Embedded maps and drill tutorial videos.

## 📸 Screenshot
<img width="1414" alt="Screenshot 2025-03-22 at 3 50 37 PM" src="https://github.com/user-attachments/assets/d37a813d-4b65-4039-b47e-ed3cf76798f5" />

## 🚀 Try It Live!
[**Click Here to Run It Now!**](https://genewu.pythonanywhere.com/)  
Hosted on PythonAnywhere—check out your Sha Tin workout plan in action!


## ⚡ Quick Start

1. **Clone the Repo:**
   ```bash
   git clone https://github.com/yourusername/running-training-planning.git
   cd running-training-planning
   ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up API Key:**
- Get a Google Maps API key [here](https://developers.google.com/maps/documentation/embed/get-api-key).
- Create a `.env` file in the project root with:
```bash
GOOGLE_MAPS_API_KEY=your_api_key_here
```

4. **Run the App:**
    ```bash
    python flask_app.py
    ```
    - Visit http://127.0.0.1:5000 in your browser

5. **Run Test:**
    ```bash
    pytest
    ```

# 🔧 Setup Details

## Prerequisites
- Python 3.x
- Git

## Running Locally
- Ensure Background Image: If `static/background.jpg` is missing, download it [here](https://res.hkjc.com/racingnews/wp-content/uploads/sites/3/2022/01/news02_220130_05.jpg) and place it in `static/`.

## Running Unit Tests
- Tests verify route caluclations and page rendering
- Expected output: `Ran 4 tests in 0.XXXs OK`.

## Deploy Your Own
- PythonAnywhere: Live at genewu.pythonanywhere.com. See their docs to host yours!
  - Upload .env via the Files tab or set the env var in the dashboard.
- Render Alternative:
1. Push to GitHub (exclude `.env`).
2. At render.com:
- Build: pip install -r requirements.txt
- Start: gunicorn flask_app:app
- Add GOOGLE_MAPS_API_KEY to Render’s Environment Variables.
3. Get your URL.

## 🎯 Usage
- Pick a route (default: 7.2 km).
- Set pace and sprints (Option 1 only).
- Hit "Calculate" for your plan with a route map!

## 📂 Project Structure
```
running-training-planning/
├── flask_app.py                  # Main app with route maps
├── test_flask_app.py             # Tests
├── static/
│   └── background.jpg            # Sha Tin Racecourse pic
├── requirements.txt              # Dependencies
├── Procfile                      # Render config
├── .gitignore                    # Git exclusions
├── .env                          # API key (not in Git)
└── README.md                     # This file
```

## 🛠️ Dependencies
- `flask`: Web framework.
- `gunicorn`: WSGI server for Render.

## 🙌 Credits
- Background: [Hong Kong Jockey Club](https://res.hkjc.com/racingnews/wp-content/uploads/sites/3/2022/01/news02_220130_05.jpg)
- Drill Videoes: Linked in the app via YouTube.

## 📜 License
MIT License - free to use, modify, and distribute!
