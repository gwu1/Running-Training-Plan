from flask import Flask, request, render_template_string

app = Flask(__name__)

# Constants
SPORTS_GROUND_TOTAL = 7.2  # Option 1: SCTC -> Sha Tin Sports Ground -> Lek Yuen Bridge -> SCTC
MA_ON_SHAN_TOTAL = 10.3  # Option 2: SCTC -> Ma On Shan Promenade -> SCTC
SCIENCE_PARK_TOTAL = 10.9  # Option 3: SCTC -> Ma Bridge -> HK Science Park -> SCTC
DRILL_SETS = 5  # Option 1 only
DRILL_REPS = 2.5  # Option 1 only
DRILL_TIME_PER_SET = 0.5  # min (Option 1 only)
SPRINT_DISTANCE = 0.1  # km (Option 1 only)
SPRINT_SPEED = 20 / 60  # 20 sec per 100m (min, Option 1 only)
SPRINT_REST = 1.5  # min (Option 1 only)
SPRINT_SETS_DEFAULT = 4  # Default sprint sets (Option 1 only)
OPTION_1_MAP_LINK = "https://maps.app.goo.gl/cyK1zG1BgUSYvQnTA"  # Option 1 map
OPTION_2_MAP_LINK = "https://maps.app.goo.gl/PJUPhhiZeCjRpKh69"  # Option 2 map
OPTION_3_MAP_LINK = "https://maps.app.goo.gl/u3Xoe1FsuoGPUYek7"  # Option 3 map
OPTION_1_DRILL_VIDEO_1 = "https://youtu.be/6H8WLfyavWk?si=MmN68RnCtHBKkWSo"  # Drill video 1
OPTION_1_DRILL_VIDEO_2 = "https://youtube.com/shorts/mUD2u-YVn7A?si=XbALHTDWobAVhwYh"  # Drill video 2

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
            max-width: 400px;
        }
        .result b { color: #0066cc; }
        .result a { color: #0066cc; text-decoration: underline; }
        form { background: rgba(255, 255, 255, 0.8); padding: 15px; border-radius: 5px; }
        select { margin-right: 5px; }
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
               onchange="toggleSprintSets()"> 7.2 km (SCTC -> Sha Tin Sports Ground -> Lek Yuen Bridge -> SCTC,
                                              includes drills and sprints)<br>
        <input type="radio" name="route" value="2" {{ 'checked' if selected_route == 2 else '' }}
               onchange="toggleSprintSets()"> 10.3 km (SCTC -> Ma On Shan Promenade -> SCTC)<br>
        <input type="radio" name="route" value="3" {{ 'checked' if selected_route == 3 else '' }}
               onchange="toggleSprintSets()"> 10.9 km (SCTC -> Ma Bridge -> HK Science Park -> SCTC)<br><br>
        <label>Running Pace (min/km, default 6:00):</label><br>
        <select name="pace_minutes" required>
            {% for min in range(4, 11) %}
                <option value="{{ min }}" {{ 'selected' if min == 6 else '' }}>{{ min }}</option>
            {% endfor %}
        </select> min
        <select name="pace_seconds" required>
            {% for sec in range(0, 60, 5) %}
                <option value="{{ sec }}" {{ 'selected' if sec == 0 else '' }}>{{ '%02d' % sec }}</option>
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
    selected_route = 1  # Default route

    if request.method == 'POST':
        # Get form inputs
        route = int(request.form['route'])
        pace_minutes = int(request.form['pace_minutes'])
        pace_seconds = int(request.form['pace_seconds'])
        pace = pace_minutes + (pace_seconds / 60)  # Convert to decimal minutes
        selected_route = route

        # Set distance, route, and links
        if route == 1:
            total_distance = SPORTS_GROUND_TOTAL
            route_name = "SCTC -> Sha Tin Sports Ground -> Lek Yuen Bridge -> SCTC"
            sprint_sets = int(request.form.get('sprint_sets', SPRINT_SETS_DEFAULT))
            drill_time = DRILL_SETS * DRILL_REPS * DRILL_TIME_PER_SET
            sprint_time = sprint_sets * (SPRINT_SPEED + SPRINT_REST)
            total_time = total_distance * pace + drill_time + sprint_time
            extra_links = (
                f'<br><b>Route Map:</b> <a href="{OPTION_1_MAP_LINK}" target="_blank">Google Maps</a><br>'
                f'<b>Drill Videos:</b> <a href="{OPTION_1_DRILL_VIDEO_1}" target="_blank">Video 1</a> | '
                f'<a href="{OPTION_1_DRILL_VIDEO_2}" target="_blank">Video 2</a>'
            )
            sprint_summary = f"<b>Sprints:</b> {sprint_sets} x 100m (~{int(sprint_time)} min, includes rest)<br>"
            drill_summary = f"<b>Drills:</b> {int(DRILL_SETS * DRILL_REPS)} reps (~{int(drill_time)} min)<br>"
        elif route == 2:
            total_distance = MA_ON_SHAN_TOTAL
            route_name = "SCTC -> Ma On Shan Promenade -> SCTC"
            total_time = total_distance * pace  # No drills or sprints
            extra_links = f'<br><b>Route Map:</b> <a href="{OPTION_2_MAP_LINK}" target="_blank">Google Maps</a>'
            sprint_summary = ""
            drill_summary = ""
        else:  # Option 3
            total_distance = SCIENCE_PARK_TOTAL
            route_name = "SCTC -> Ma Bridge -> HK Science Park -> SCTC"
            total_time = total_distance * pace  # No drills or sprints
            extra_links = f'<br><b>Route Map:</b> <a href="{OPTION_3_MAP_LINK}" target="_blank">Google Maps</a>'
            sprint_summary = ""
            drill_summary = ""

        # Calculations
        run_time = total_distance * pace
        hours = int(total_time // 60)
        minutes = int(total_time % 60)

        # Formatted result
        result = (
            f"<b>Run:</b> {total_distance} km ({route_name})<br>"
            f"<b>Run Time:</b> {int(run_time)} min<br>"
            f"{drill_summary}"
            f"{sprint_summary}"
            f"<b>Total Time:</b> {hours} hr {minutes} min"
            f"{extra_links}<br>"
            f"<i>Power up your training in Sha Tin!</i>"
        )

    return render_template_string(TEMPLATE, result=result, selected_route=selected_route)


if __name__ == '__main__':
    app.run(debug=True)
