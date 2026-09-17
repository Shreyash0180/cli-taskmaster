import unittest
import os
import json
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.storage import initialize_storage, TASKS_FILE
from src.tasks import add_task, get_user_tasks, delete_task

class TestTaskModule(unittest.TestCase):
    def setUp(self):
        self.test_username = "testuser"
        initialize_storage()
        with open(TASKS_FILE, 'w') as f:
            json.dump({}, f)

    def test_add_task(self):
        success, msg = add_task(self.test_username, "Test Task", "Desc", "High")
        self.assertTrue(success)
        tasks = get_user_tasks(self.test_username)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['title'], "Test Task")

    def test_delete_task(self):
        add_task(self.test_username, "Task to delete", "Desc", "Low")
        tasks = get_user_tasks(self.test_username)
        task_id = tasks[0]['task_id']
        
        success, msg = delete_task(self.test_username, task_id)
        self.assertTrue(success)
        self.assertEqual(len(get_user_tasks(self.test_username)), 0)

if __name__ == '__main__':
    unittest.main()
