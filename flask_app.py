from flask import Flask, request, render_template_string
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Constants
SPORTS_GROUND_TOTAL = 7.5
MA_ON_SHAN_TOTAL = 10.3
SCIENCE_PARK_TOTAL = 13.5
MUI_TSZ_LAM_TOTAL = 12.3
MEI_TIN_TOTAL = 11.4
TSUEN_WAN_TOTAL = 22.4
SHAM_TSENG_TOTAL = 11.7  # Option 7
DRILL_SETS = 5
DRILL_REPS = 2.5
DRILL_TIME_PER_SET = 0.5
SPRINT_DISTANCE = 0.1
SPRINT_SPEED = 20 / 60
SPRINT_REST = 1.5
SPRINT_SETS_DEFAULT = 4
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

# Route Embed URLs (Directions mode)
OPTION_1_MAP = (
    f"https://www.google.com/maps/embed/v1/directions?key={API_KEY}"
    "&origin=HKJC Sha Tin Communications and Technology Centre"
    "&destination=HKJC Sha Tin Communications and Technology Centre"
    "&waypoints=Hong Kong Sports Institute, 25 Yuen Wo Rd, Sha Tin, Hong Kong|Sha Tin Sports Ground|Sha Tin Twin Bridge, Sha Tin, Hong Kong|Hong Kong Sports Institute, 25 Yuen Wo Rd, Sha Tin, Hong Kong"
    "&mode=walking"
)
OPTION_2_MAP = (
    f"https://www.google.com/maps/embed/v1/directions?key={API_KEY}"
    "&origin=HKJC Sha Tin Communications and Technology Centre"
    "&destination=HKJC Sha Tin Communications and Technology Centre"
    "&waypoints=Hong Kong Sports Institute, 25 Yuen Wo Rd, Sha Tin, Hong Kong|Sha Tin Twin Bridge, Sha Tin, Hong Kong|Oceanaire|Sha Tin Twin Bridge, Sha Tin, Hong Kong|Hong Kong Sports Institute, 25 Yuen Wo Rd, Sha Tin, Hong Kong"
    "&mode=walking"
)
OPTION_3_MAP = (
    f"https://www.google.com/maps/embed/v1/directions?key={API_KEY}"
    "&origin=HKJC Sha Tin Communications and Technology Centre"
    "&destination=HKJC Sha Tin Communications and Technology Centre"
    "&waypoints=Hong Kong Sports Institute, 25 Yuen Wo Rd, Sha Tin, Hong Kong|Sha Tin Twin Bridge|Hong Kong Science Park|Sha Tin Twin Bridge|Hong Kong Sports Institute, 25 Yuen Wo Rd, Sha Tin, Hong Kong"
    "&mode=walking"
)
OPTION_4_MAP = (
    f"https://www.google.com/maps/embed/v1/directions?key={API_KEY}"
    "&origin=HKJC Sha Tin Communications and Technology Centre"
    "&destination=HKJC Sha Tin Communications and Technology Centre"
    "&waypoints=Hong Kong Sports Institute, 25 Yuen Wo Rd, Sha Tin, Hong Kong|22.39309, 114.2334|Hong Kong Sports Institute, 25 Yuen Wo Rd, Sha Tin, Hong Kong"
    "&mode=walking"
)
OPTION_5_MAP = (
    f"https://www.google.com/maps/embed/v1/directions?key={API_KEY}"
    "&origin=HKJC Sha Tin Communications and Technology Centre"
    "&destination=HKJC Sha Tin Communications and Technology Centre"
    "&waypoints=Hong Kong Sports Institute, 25 Yuen Wo Rd, Sha Tin, Hong Kong|22.375855, 114.168843|22.383320, 114.196178"
    "&mode=walking"
)
OPTION_6_MAP = (
    f"https://www.google.com/maps/embed/v1/directions?key={API_KEY}"
    "&origin=Tsuen Wan West Station, Hong Kong"
    "&destination=Tsuen Wan West Station, Hong Kong"
    "&waypoints=Tuen Mun Road Bus-Bus Interchange, Hong Kong"
    "&mode=walking"
)
OPTION_7_MAP = (
    f"https://www.google.com/maps/embed/v1/directions?key={API_KEY}"
    "&origin=Hoi Hing Road Public Toilet, Tsuen Wan"
    "&destination=Hoi Hing Road Public Toilet, Tsuen Wan"
    "&waypoints=22.364648, 114.064399"
    "&mode=walking"
)
OPTION_1_DRILL_VIDEO_1 = "https://youtu.be/6H8WLfyavWk?si=MmN68RnCtHBKkWSo"
OPTION_1_DRILL_VIDEO_2 = "https://youtube.com/shorts/mUD2u-YVn7A?si=XbALHTDWobAVhwYh"

# HTML template
TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Running / Training Planning</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-image: url('/static/background.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            min-height: 100vh;
        }
        h1 { color: #333; }
        h2 {
            color: white;
            background: rgba(0, 0, 0, 0.5);
            display: inline-block;
            padding: 5px 10px;
            border-radius: 3px;
        }
        .result {
            background: rgba(249, 249, 249, 0.9);
            padding: 15px;
            border-radius: 5px;
            max-width: 600px;
        }
        .result b { color: #0066cc; }
        .result a { color: #0066cc; text-decoration: underline; }
        form { background: rgba(255, 255, 255, 0.8); padding: 15px; border-radius: 5px; }
        select { margin-right: 5px; }
        iframe { border: 0; width: 100%; height: 400px; margin-top: 10px; }
    </style>
    <script>
        function toggleSprintSets() {
            var route = document.querySelector('input[name="route"]:checked').value;
            var sprintSetsDiv = document.getElementById('sprint_sets_div');
            sprintSetsDiv.style.display = (route === '1') ? 'block' : 'none';
        }
    </script>
</head>
<body onload="toggleSprintSets()">
    <h1>Running / Training Planning</h1>
    <form method="POST">
        <label>Choose Route:</label><br>
        <input type="radio" name="route" value="1" {{ 'checked' if selected_route == 1 else '' }}
               onchange="toggleSprintSets()"> 7.5 km (SCTC -> Sha Tin Sports Ground -> Twin Bridge -> SCTC,
                                              includes drills and sprints)<br>
        <input type="radio" name="route" value="2" {{ 'checked' if selected_route == 2 else '' }}
               onchange="toggleSprintSets()"> 10.3 km (SCTC -> Ma On Shan Promenade -> SCTC)<br>
        <input type="radio" name="route" value="3" {{ 'checked' if selected_route == 3 else '' }}
               onchange="toggleSprintSets()"> 13.5 km (SCTC -> Twin Bridge -> HK Science Park -> SCTC)<br>
        <input type="radio" name="route" value="4" {{ 'checked' if selected_route == 4 else '' }}
               onchange="toggleSprintSets()"> 12.3 km (SCTC -> Mui Tsz Lam -> SCTC)<br>
        <input type="radio" name="route" value="5" {{ 'checked' if selected_route == 5 else '' }}
               onchange="toggleSprintSets()"> 11.4 km (SCTC -> Mei Tin Estate, Tai Wai -> SCTC)<br>
        <input type="radio" name="route" value="6" {{ 'checked' if selected_route == 6 else '' }}
               onchange="toggleSprintSets()"> 22.4 km (Tsuen Wan West Station -> Tuen Mun Road Bus-Bus Interchange -> Tsuen Wan West Station)<br>
        <input type="radio" name="route" value="7" {{ 'checked' if selected_route == 7 else '' }}
               onchange="toggleSprintSets()"> 11.7 km (Tsuen Wan West -> The Garden, Sham Tseng -> Tsuen Wan West)<br><br>
        <label>Running Pace (min/km, default 6:00):</label><br>
        <select name="pace_minutes" required>
            {% for min in range(4, 11) %}
                <option value="{{ min }}" {{ 'selected' if min == pace_minutes else '' }}>{{ min }}</option>
            {% endfor %}
        </select> min
        <select name="pace_seconds" required>
            {% for sec in range(0, 60, 5) %}
                <option value="{{ sec }}" {{ 'selected' if sec == pace_seconds else '' }}>{{ '%02d' % sec }}</option>
            {% endfor %}
        </select> sec<br><br>
        <div id="sprint_sets_div">
            <label>Sprint Sets (4 or 5, default 4, Option 1 only):</label>
            <input type="number" name="sprint_sets" min="4" max="5" value="4"><br><br>
        </div>
        <input type="submit" value="Calculate">
    </form>
    {% if result %}
        <h2>Workout Summary</h2>
        <div class="result">{{ result|safe }}</div>
    {% endif %}
</body>
</html>
'''


@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    selected_route = 1
    pace_minutes = 6  # Default pace minutes
    pace_seconds = 0  # Default pace seconds

    if request.method == 'POST':
        route = int(request.form['route'])
        pace_minutes = int(request.form['pace_minutes'])
        pace_seconds = int(request.form['pace_seconds'])
        pace = pace_minutes + (pace_seconds / 60)
        selected_route = route

        if route == 1:
            total_distance = SPORTS_GROUND_TOTAL
            route_name = "SCTC -> Sha Tin Sports Ground -> Twin Bridge -> SCTC"
            sprint_sets = int(request.form.get('sprint_sets', SPRINT_SETS_DEFAULT))
            drill_time = DRILL_SETS * DRILL_REPS * DRILL_TIME_PER_SET
            sprint_time = sprint_sets * (SPRINT_SPEED + SPRINT_REST)
            total_time = total_distance * pace + drill_time + sprint_time
            extra_links = (
                f'<br><b>Drill Videos:</b> <a href="{OPTION_1_DRILL_VIDEO_1}" target="_blank">Video 1</a> | '
                f'<a href="{OPTION_1_DRILL_VIDEO_2}" target="_blank">Video 2</a>'
            )
            sprint_summary = f"<b>Sprints:</b> {sprint_sets} x 100m (~{int(sprint_time)} min, includes rest)<br>"
            drill_summary = f"<b>Drills:</b> {int(DRILL_SETS * DRILL_REPS)} reps (~{int(drill_time)} min)<br>"
            map_embed = f'<iframe src="{OPTION_1_MAP}" allowfullscreen></iframe>'
            message = "Power up your training in Sha Tin!"
        elif route == 2:
            total_distance = MA_ON_SHAN_TOTAL
            route_name = "SCTC -> Ma On Shan Promenade -> SCTC"
            total_time = total_distance * pace
            extra_links = ""
            sprint_summary = ""
            drill_summary = ""
            map_embed = f'<iframe src="{OPTION_2_MAP}" allowfullscreen></iframe>'
            message = "Power up your training in Sha Tin!"
        elif route == 3:
            total_distance = SCIENCE_PARK_TOTAL
            route_name = "SCTC -> Twin Bridge -> HK Science Park -> SCTC"
            total_time = total_distance * pace
            extra_links = ""
            sprint_summary = ""
            drill_summary = ""
            map_embed = f'<iframe src="{OPTION_3_MAP}" allowfullscreen></iframe>'
            message = "Power up your training in Sha Tin!"
        elif route == 4:
            total_distance = MUI_TSZ_LAM_TOTAL
            route_name = "SCTC -> Mui Tsz Lam -> SCTC"
            total_time = total_distance * pace
            extra_links = ""
            sprint_summary = ""
            drill_summary = ""
            map_embed = f'<iframe src="{OPTION_4_MAP}" allowfullscreen></iframe>'
            message = "Power up your training in Sha Tin!"
        elif route == 5:
            total_distance = MEI_TIN_TOTAL
            route_name = "SCTC -> Mei Tin Estate, Tai Wai -> SCTC"
            total_time = total_distance * pace
            extra_links = ""
            sprint_summary = ""
            drill_summary = ""
            map_embed = f'<iframe src="{OPTION_5_MAP}" allowfullscreen></iframe>'
            message = "Power up your training in Sha Tin!"
        elif route == 6:
            total_distance = TSUEN_WAN_TOTAL
            route_name = "Tsuen Wan West Station -> Tuen Mun Road Bus-Bus Interchange -> Tsuen Wan West Station"
            total_time = total_distance * pace
            extra_links = ""
            sprint_summary = ""
            drill_summary = ""
            map_embed = f'<iframe src="{OPTION_6_MAP}" allowfullscreen></iframe>'
            message = "Power up your training in Tsuen Wan!"
        else:  # Option 7
            total_distance = SHAM_TSENG_TOTAL
            route_name = "Tsuen Wan West -> The Garden, Sham Tseng -> Tsuen Wan West"
            total_time = total_distance * pace
            extra_links = ""
            sprint_summary = ""
            drill_summary = ""
            map_embed = f'<iframe src="{OPTION_7_MAP}" allowfullscreen></iframe>'
            message = "Power up your training in Tsuen Wan!"

        run_time = total_distance * pace
        hours = int(total_time // 60)
        minutes = int(total_time % 60)
        pace_display = f"{pace_minutes}:{pace_seconds:02d}"  # Format pace as MM:SS

        result = (
            f"<b>Run:</b> {total_distance} km ({route_name})<br>"
            f"<b>Pace:</b> {pace_display} min/km<br>"
            f"<b>Run Time:</b> {int(run_time)} min<br>"
            f"{drill_summary}"
            f"{sprint_summary}"
            f"<b>Total Time:</b> {hours} hr {minutes} min"
            f"{extra_links}<br>"
            f"<i>{message}</i><br>"
            f"{map_embed}"
        )

    return render_template_string(TEMPLATE, result=result, selected_route=selected_route, 
                                 pace_minutes=pace_minutes, pace_seconds=pace_seconds)


if __name__ == '__main__':
    app.run(debug=True)
