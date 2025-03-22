# Running / Training Planning

A simple Flask web app to plan your running workouts in Sha Tin, Hong Kong. Calculate total workout time based on distance, pace, drills, and sprints, with embedded Google Maps links and drill tutorial videos for select routes. Features a Sha Tin Racecourse wallpaper for a local vibe.

## Features
- **Three Routes:**
  - **Option 1:** 7.2 km (SCTC -> Sha Tin Sports Ground -> Lek Yuen Bridge -> SCTC) with drills, sprints, map, and drill videos.
  - **Option 2:** 10.3 km (SCTC -> Ma On Shan Promenade -> SCTC) with map.
  - **Option 3:** 10.9 km (SCTC -> Ma Bridge -> HK Science Park -> SCTC) with map.
- **Inputs:** Customizable running pace (default 6:00 min/km) via dropdowns; sprint sets (default 4, Option 1 only).
- **Output:** Workout summary with run time, drill time (Option 1 only), sprint time (Option 1 only), and total duration.

## Screenshot
<img width="1417" alt="Screenshot" src="https://github.com/user-attachments/assets/f1ff24ab-2cd0-4bc0-92bb-fee74ac244db" />


## Prerequisites
- Python 3.x
- Git

## Setup

### Local Installation
1. **Clone the Repo:**
   ```bash
   git clone https://github.com/yourusername/running-training-planning.git
   cd running-training-planning
