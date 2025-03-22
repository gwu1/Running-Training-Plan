# Running / Training Planning

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight Flask app to plan running workouts in Sha Tin, Hong Kong. Calculate your total time based on distance, pace, drills, and sprints, with Google Maps links and drill videos for select routes. Enjoy a Sha Tin Racecourse backdrop for that local flair!

## Features
- **Routes:**
  - **7.2 km**: SCTC → Sha Tin Sports Ground → Lek Yuen Bridge → SCTC (includes drills & sprints).
  - **10.3 km**: SCTC → Ma On Shan Promenade → SCTC.
  - **10.9 km**: SCTC → Ma Bridge → HK Science Park → SCTC.
- **Customizable:** Set pace (default 6:00 min/km) via dropdowns; adjust sprint sets for Option 1.
- **Output:** Detailed summary with run time, drill/sprint times (if applicable), and total duration.
- **Extras:** Embedded maps and drill tutorial videos.

## Screenshot
<img width="1417" alt="Screenshot" src="https://github.com/user-attachments/assets/f1ff24ab-2cd0-4bc0-92bb-fee74ac244db" />


## Quick Start

1. **Clone the Repo:**
   ```bash
   git clone https://github.com/yourusername/running-training-planning.git
   cd running-training-planning
   ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the App:**
    ```bash
    python flask_app.py
    ```
    - Visit http://127.0.0.1:5000 in your browser

4. **Run Test:**
    ```bash
    pytest
    ```

# Setup Details

## Prerequisites
- Python 3.x
- Git

## Running Locally
- Ensure Background Image: If `static/background.jpg` is missing, download it [here](https://res.hkjc.com/racingnews/wp-content/uploads/sites/3/2022/01/news02_220130_05.jpg) and place it in `static/`.

## Running Unit Tests
- Tests verify route caluclations and page rendering
- Expected output: `Ran 4 tests in 0.XXXs OK`.

## Deploying to Render
1. Push to Github with all files committed.
2. At render.com:
- New Web Service -> Link this repo
- Build: `pip install -r requirements.txt`
- Start: `gunicorn flask_app:app`.
3. Access your app at te provided URL.

## Usage
- Select a route (default: 7.2km).
- Adjust pace and (for Option 1) sprint sets.
- Click "Calculate" for your workout summary.

## Project Structure
```
running-training-planning/
├── flask_app.py                  # Main app (or running_training_planning.py)
├── test_flask_app.py             # Unit tests (or test_running_training_planning.py)
├── static/
│   └── background.jpg            # Sha Tin Racecourse image
├── requirements.txt              # Dependencies
├── Procfile                      # Render config
└── README.md                     # This file
```

## Dependencies
- `flask`: Web framework.
- `gunicorn`: WSGI server for Render.

## Credits
- Background: [Hong Kong Jockey Club](https://res.hkjc.com/racingnews/wp-content/uploads/sites/3/2022/01/news02_220130_05.jpg)
- Drill Videoes: Linked in the app via YouTube.

## License
MIT License - free to use, modify, and distribute!