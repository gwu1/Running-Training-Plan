from flask import Flask, request, render_template_string

app = Flask(__name__)

# Constants
SPORTS_GROUND_TOTAL = 7.2  # Option 1: SCTC -> Sha Tin Sports Ground -> Lek Yuen Bridge -> SCTC
MA_ON_SHAN_TOTAL = 10.3    # Option 2: SCTC -> Ma On Shan Promenade -> SCTC
DRILL_SETS = 5
DRILL_REPS = 2.5
DRILL_TIME_PER_SET = 0.5  # min
SPRINT_DISTANCE = 0.1  # km
SPRINT_SPEED = 20 / 60  # 20 sec per 100m (min)
SPRINT_REST = 1.5  # min
SPRINT_SETS_DEFAULT = 4  # Default sprint sets
OPTION_1_MAP_LINK = "https://maps.app.goo.gl/cyK1zG1BgUSYvQnTA"  # Option 1 map
OPTION_2_MAP_LINK = "https://maps.app.goo.gl/PJUPhhiZeCjRpKh69"  # Option 2 map
OPTION_1_DRILL_VIDEO_1 = "https://youtu.be/6H8WLfyavWk?si=MmN68RnCtHBKkWSo"  # Drill video 1
OPTION_1_DRILL_VIDEO_2 = "https://youtube.com/shorts/mUD2u-YVn7A?si=XbALHTDWobAVhwYh"  # Drill video 2

# HTML template with updated h2 styling
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
    </style>
</head>
<body>
    <h1>Running / Training Planning</h1>
    <form method="POST">
        <label>Choose Route:</label><br>
        <input type="radio" name="route" value="1" checked> 7.2 km (SCTC -> Sha Tin Sports Ground -> Lek Yuen Bridge -> SCTC)<br>
        <input type="radio" name="route" value="2"> 10.3 km (SCTC -> Ma On Shan Promenade -> SCTC)<br><br>
        <label>Running Pace (min/km, default 6):</label>
        <input type="number" name="pace" step="0.1" value="6" required><br><br>
        <label>Sprint Sets (4 or 5, default 4):</label>
        <input type="number" name="sprint_sets" min="4" max="5" value="4"><br><br>
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
    if request.method == 'POST':
        # Get form inputs
        route = int(request.form['route'])
        pace = float(request.form['pace'])
        sprint_sets = int(request.form.get('sprint_sets', SPRINT_SETS_DEFAULT))

        # Set distance, route, and links
        if route == 1:
            total_distance = SPORTS_GROUND_TOTAL
            route_name = "SCTC -> Sha Tin Sports Ground -> Lek Yuen Bridge -> SCTC"
            extra_links = (f'<br><b>Route Map:</b> <a href="{OPTION_1_MAP_LINK}" target="_blank">Google Maps</a><br>'
                           f'<b>Drill Videos:</b> <a href="{OPTION_1_DRILL_VIDEO_1}" target="_blank">Video 1</a> | '
                           f'<a href="{OPTION_1_DRILL_VIDEO_2}" target="_blank">Video 2</a>')
        else:
            total_distance = MA_ON_SHAN_TOTAL
            route_name = "SCTC -> Ma On Shan Promenade -> SCTC"
            extra_links = f'<br><b>Route Map:</b> <a href="{OPTION_2_MAP_LINK}" target="_blank">Google Maps</a>'

        # Calculations
        run_time = total_distance * pace
        drill_time = DRILL_SETS * DRILL_REPS * DRILL_TIME_PER_SET
        sprint_time = sprint_sets * (SPRINT_SPEED + SPRINT_REST)
        total_time = run_time + drill_time + sprint_time
        hours = int(total_time // 60)
        minutes = int(total_time % 60)

        # Formatted result
        result = (f"<b>Run:</b> {total_distance} km ({route_name})<br>"
                  f"<b>Run Time:</b> {int(run_time)} min<br>"
                  f"<b>Drills:</b> {int(DRILL_SETS * DRILL_REPS)} reps (~{int(drill_time)} min)<br>"
                  f"<b>Sprints:</b> {sprint_sets} x 100m (~{int(sprint_time)} min)<br>"
                  f"<b>Total Time:</b> {hours} hr {minutes} min"
                  f"{extra_links}<br>"
                  f"<i>Power up your training in Sha Tin!</i>")

    return render_template_string(TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
