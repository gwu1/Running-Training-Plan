import unittest
from flask_app import app  # Adjust to running_training_planning if renamed


class TestRunningTrainingPlanning(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_get(self):
        # Test GET request to home page
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Running / Training Planning', response.data)
        self.assertIn(b'Choose Route:', response.data)

    def test_option_1_post(self):
        # Test POST for Option 1 (7.5 km with drills and sprints)
        response = self.app.post('/', data={
            'route': '1',
            'pace_minutes': '6',
            'pace_seconds': '0',
            'sprint_sets': '4'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Workout Summary', response.data)
        self.assertIn(b'7.5 km (SCTC -> Sha Tin Sports Ground -> Twin Bridge -> SCTC)', response.data)
        self.assertIn(b'45 min', response.data)
        self.assertIn(b'12 reps (~6 min)', response.data)
        self.assertIn(b'4 x 100m (~7 min, includes rest)', response.data)
        self.assertIn(b'0 hr 58 min', response.data)

    def test_option_2_post(self):
        # Test POST for Option 2 (10.3 km, run only)
        response = self.app.post('/', data={
            'route': '2',
            'pace_minutes': '6',
            'pace_seconds': '0'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Workout Summary', response.data)
        self.assertIn(b'10.3 km (SCTC -> Ma On Shan Promenade -> SCTC)', response.data)
        self.assertIn(b'61 min', response.data)
        self.assertIn(b'1 hr 1 min', response.data)
        self.assertNotIn(b'Drills:', response.data)
        self.assertNotIn(b'Sprints:', response.data)

    def test_option_3_post(self):
        # Test POST for Option 3 (13.5 km, run only)
        response = self.app.post('/', data={
            'route': '3',
            'pace_minutes': '6',
            'pace_seconds': '0'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Workout Summary', response.data)
        self.assertIn(b'13.5 km (SCTC -> Twin Bridge -> HK Science Park -> SCTC)', response.data)
        self.assertIn(b'81 min', response.data)
        self.assertIn(b'1 hr 21 min', response.data)
        self.assertNotIn(b'Drills:', response.data)
        self.assertNotIn(b'Sprints:', response.data)


if __name__ == '__main__':
    unittest.main()
