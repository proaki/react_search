import os
import sys
sys.path.insert(0, os.getcwd())
import json
import datetime
import unittest
from fastapi.testclient import TestClient
from src.main import app
from src.database.migrate import DBMigrator

client = TestClient(app)


class TestTasksEndpoint(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestTasksEndpoint, self).__init__(*args, **kwargs)
        self.DBM = DBMigrator()
        self.client = TestClient(app)
        # Test organization data
        self.test_organization = {"id": "2d6bb3c2-c168-457b-851d-78d29ded089e",
                                  "name": "test organization"}
        # Test annotator data
        self.test_annotator = {"id": "2d6bb3c2-c168-457b-851d-78d29ded089e",
                               "name": "test annotator",
                               "age": 28,
                               "gender": "male",
                               "organization_id": "2d6bb3c2-c168-457b-851d-78d29ded089e"}
        # Test annotation type data
        self.test_annotation_type = {"id": "2d6bb3c2-c168-457b-851d-78d29ded089e",
                                     "objective_name": "gr",
                                     "label_name": "genre",
                                     "value_type": "str"}

        # Test audio_format type data
        self.test_audio_format_type = {"id": "2d6bb3c2-c168-457b-851d-78d29ded089e",
                                       "precision": 16,
                                       "sample_rate": 44100,
                                       "channels": 2}

        # Test audio data
        self.test_audio = {"md5": "2d6bb3c2-c168-457b-851d-78d29ded089e",
                           "file_name": "audio.wav",
                           "audio_format_id": "2d6bb3c2-c168-457b-851d-78d29ded089e",
                           "duration": "00:30:01.020",
                           "custom_property": json.dumps({"external_id": "external ID"}),
                           "organization_id": "2d6bb3c2-c168-457b-851d-78d29ded089e"}

        # Test audio_annotation data
        self.test_audio_annotation = {"id": "2d6bb3c2-c168-457b-851d-78d29ded089e",
                                      "annotation_type_id": "2d6bb3c2-c168-457b-851d-78d29ded089e",
                                      "annotator_id": "2d6bb3c2-c168-457b-851d-78d29ded089e",
                                      "task_id": "2d6bb3c2-c168-457b-851d-78d29ded089e",
                                      "value": "Rock",
                                      "start_time": json.dumps((datetime.datetime.min + datetime.timedelta(seconds=0 / 1000.0)).time(), default=str),
                                      "stop_time": json.dumps((datetime.datetime.min + datetime.timedelta(seconds=209280 / 1000.0)).time(), default=str),
                                      "md5": "2d6bb3c2-c168-457b-851d-78d29ded089e",
                                      "version": 1}
        # Test task data
        self.test_task = {"id": "2d6bb3c2-c168-457b-851d-78d29ded089e",
                             "name": "genre_classification",
                             "type": "classification",
                             "description": "Music Genre Classification"}
        # Test Updated task
        self.updated_test_task = {"id": "2d6bb3c2-c168-457b-851d-78d29ded089e",
                                     "name": "key_classification"}
        # Test wrong param task
        self.test_wrong_task = {"id": "1206a713-129e-445d-9532-8d682d911be9",
                                   "name": "key_detection"}

    def setUp(self):
        # Clean table
        self.DBM.drop_table_contents()

    def tearDown(self):
        # Clean table
        self.DBM.drop_table_contents()

    def test_01_post_task(self):
        # Create organization
        response = client.post("/organizations", json.dumps(self.test_organization))
        assert response.status_code == 200

        # Create annotator
        response = client.post("/annotators", json.dumps(self.test_annotator))
        assert response.status_code == 200

        # Create audio_format type
        response = client.post("/audio_format", json.dumps(self.test_audio_format_type))
        assert response.status_code == 200

        # Create audio
        response = client.post("/audio", json.dumps(self.test_audio))
        assert response.status_code == 200

        # Create annotation type
        response = client.post("/annotation_types", json.dumps(self.test_annotation_type))
        assert response.status_code == 200

        # Create task
        response = client.post("/tasks", json.dumps(self.test_task))
        assert response.status_code == 200

        # Create audio annotation
        response = client.post("/audio_annotations", json.dumps(self.test_audio_annotation))
        assert response.status_code == 200

    def test_02_post_task_with_wrong_parameter(self):
        # Create organization
        response = client.post("/organizations", json.dumps(self.test_organization))
        assert response.status_code == 200

        # Create annotator
        response = client.post("/annotators", json.dumps(self.test_annotator))
        assert response.status_code == 200

        # Create audio_format type
        response = client.post("/audio_format", json.dumps(self.test_audio_format_type))
        assert response.status_code == 200

        # Create audio
        response = client.post("/audio", json.dumps(self.test_audio))
        assert response.status_code == 200

        # Create annotation type
        response = client.post("/annotation_types", json.dumps(self.test_annotation_type))
        assert response.status_code == 200

        # Create task
        response = client.post("/tasks", json.dumps(self.test_wrong_task))
        assert response.status_code == 422

    def test_03_get_task_all(self):
        # Create organization
        response = client.post("/organizations", json.dumps(self.test_organization))
        assert response.status_code == 200

        # Create annotator
        response = client.post("/annotators", json.dumps(self.test_annotator))
        assert response.status_code == 200

        # Create audio_format type
        response = client.post("/audio_format", json.dumps(self.test_audio_format_type))
        assert response.status_code == 200

        # Create audio
        response = client.post("/audio", json.dumps(self.test_audio))
        assert response.status_code == 200

        # Create annotation type
        response = client.post("/annotation_types", json.dumps(self.test_annotation_type))
        assert response.status_code == 200

        # Create task
        response = client.post("/tasks", json.dumps(self.test_task))
        assert response.status_code == 200

        # Get all tasks
        response = client.get("/tasks")
        assert response.status_code == 200

    def test_04_get_task_by_name(self):
        # Create organization
        response = client.post("/organizations", json.dumps(self.test_organization))
        assert response.status_code == 200

        # Create annotator
        response = client.post("/annotators", json.dumps(self.test_annotator))
        assert response.status_code == 200

        # Create audio_format type
        response = client.post("/audio_format", json.dumps(self.test_audio_format_type))
        assert response.status_code == 200

        # Create audio
        response = client.post("/audio", json.dumps(self.test_audio))
        assert response.status_code == 200

        # Create annotation type
        response = client.post("/annotation_types", json.dumps(self.test_annotation_type))
        assert response.status_code == 200

        # Create task
        response = client.post("/tasks", json.dumps(self.test_task))
        assert response.status_code == 200

        # Get annotator by name
        response = client.get(f"/tasks/name/{self.test_task['name']}")
        assert response.status_code == 200

    def test_05_get_task_by_wrong_name(self):
        # Create organization
        response = client.post("/organizations", json.dumps(self.test_organization))
        assert response.status_code == 200

        # Create annotator
        response = client.post("/annotators", json.dumps(self.test_annotator))
        assert response.status_code == 200

        # Create audio_format type
        response = client.post("/audio_format", json.dumps(self.test_audio_format_type))
        assert response.status_code == 200

        # Create audio
        response = client.post("/audio", json.dumps(self.test_audio))
        assert response.status_code == 200

        # Create annotation type
        response = client.post("/annotation_types", json.dumps(self.test_annotation_type))
        assert response.status_code == 200

        # Create task
        response = client.post("/tasks", json.dumps(self.test_task))
        assert response.status_code == 200

        # Get task by name
        response = client.get(f"/tasks/name/{self.test_wrong_task['name']}")
        assert response.status_code == 400
        assert json.loads(response.content)['detail'] == f"{self.test_wrong_task['name']} does not exist"

    def test_06_get_task_by_id(self):
        # Create organization
        response = client.post("/organizations", json.dumps(self.test_organization))
        assert response.status_code == 200

        # Create annotator
        response = client.post("/annotators", json.dumps(self.test_annotator))
        assert response.status_code == 200

        # Create audio_format type
        response = client.post("/audio_format", json.dumps(self.test_audio_format_type))
        assert response.status_code == 200

        # Create audio
        response = client.post("/audio", json.dumps(self.test_audio))
        assert response.status_code == 200

        # Create annotation type
        response = client.post("/annotation_types", json.dumps(self.test_annotation_type))
        assert response.status_code == 200

        # Create task
        response = client.post("/tasks", json.dumps(self.test_task))
        assert response.status_code == 200

        # Get task by ID
        response = client.get(f"/tasks/id/{self.test_task['id']}")
        assert response.status_code == 200

    def test_07_get_task_by_wrong_id(self):
        # Create organization
        response = client.post("/organizations", json.dumps(self.test_organization))
        assert response.status_code == 200

        # Create annotator
        response = client.post("/annotators", json.dumps(self.test_annotator))
        assert response.status_code == 200

        # Create audio_format type
        response = client.post("/audio_format", json.dumps(self.test_audio_format_type))
        assert response.status_code == 200

        # Create audio
        response = client.post("/audio", json.dumps(self.test_audio))
        assert response.status_code == 200

        # Create annotation type
        response = client.post("/annotation_types", json.dumps(self.test_annotation_type))
        assert response.status_code == 200

        # Create task
        response = client.post("/tasks", json.dumps(self.test_task))
        assert response.status_code == 200

        # Get task by ID
        response = client.get(f"/tasks/id/{self.test_wrong_task['id']}")
        assert response.status_code == 400
        assert json.loads(response.content)['detail'] == f"{self.test_wrong_task['id']} does not exist"

    def test_08_update_task(self):
        # Create organization
        response = client.post("/organizations", json.dumps(self.test_organization))
        assert response.status_code == 200

        # Create annotator
        response = client.post("/annotators", json.dumps(self.test_annotator))
        assert response.status_code == 200

        # Create audio_format type
        response = client.post("/audio_format", json.dumps(self.test_audio_format_type))
        assert response.status_code == 200

        # Create audio
        response = client.post("/audio", json.dumps(self.test_audio))
        assert response.status_code == 200

        # Create annotation type
        response = client.post("/annotation_types", json.dumps(self.test_annotation_type))
        assert response.status_code == 200

        # Create task
        response = client.post("/tasks", json.dumps(self.test_task))
        assert response.status_code == 200

        # Put annotator
        response = client.put("/tasks", json.dumps(self.updated_test_task))
        assert response.status_code == 200

        # Get task by updated name
        response = client.get(f"/tasks/id/{self.updated_test_task['id']}")
        assert response.status_code == 200
        assert json.loads(response.content)['name'] == self.updated_test_task['name']

    def test_09_update_task_wrong_name(self):
        # Create organization
        response = client.post("/organizations", json.dumps(self.test_organization))
        assert response.status_code == 200

        # Create annotator
        response = client.post("/annotators", json.dumps(self.test_annotator))
        assert response.status_code == 200

        # Create audio_format type
        response = client.post("/audio_format", json.dumps(self.test_audio_format_type))
        assert response.status_code == 200

        # Create audio
        response = client.post("/audio", json.dumps(self.test_audio))
        assert response.status_code == 200

        # Create annotation type
        response = client.post("/annotation_types", json.dumps(self.test_annotation_type))
        assert response.status_code == 200

        # Create task
        response = client.post("/tasks", json.dumps(self.test_task))
        assert response.status_code == 200

        # Put task
        response = client.put("/tasks", json.dumps(self.test_wrong_task))
        assert response.status_code == 400
        assert json.loads(response.content)['detail'] == f"{self.test_wrong_task['id']} does not exist"

    def test_10_delete_task_by_id(self):
        # Create organization
        response = client.post("/organizations", json.dumps(self.test_organization))
        assert response.status_code == 200

        # Create annotator
        response = client.post("/annotators", json.dumps(self.test_annotator))
        assert response.status_code == 200

        # Create audio_format type
        response = client.post("/audio_format", json.dumps(self.test_audio_format_type))
        assert response.status_code == 200

        # Create audio
        response = client.post("/audio", json.dumps(self.test_audio))
        assert response.status_code == 200

        # Create annotation type
        response = client.post("/annotation_types", json.dumps(self.test_annotation_type))
        assert response.status_code == 200

        # Create task
        response = client.post("/tasks", json.dumps(self.test_task))
        assert response.status_code == 200

        # Delete task by ID
        response = client.delete(f"/tasks/id/{self.test_task['id']}")
        assert response.status_code == 200

    def test_11_delete_task_wrong_id(self):
        # Create organization
        response = client.post("/organizations", json.dumps(self.test_organization))
        assert response.status_code == 200

        # Create annotator
        response = client.post("/annotators", json.dumps(self.test_annotator))
        assert response.status_code == 200

        # Create audio_format type
        response = client.post("/audio_format", json.dumps(self.test_audio_format_type))
        assert response.status_code == 200

        # Create audio
        response = client.post("/audio", json.dumps(self.test_audio))
        assert response.status_code == 200

        # Create annotation type
        response = client.post("/annotation_types", json.dumps(self.test_annotation_type))
        assert response.status_code == 200

        # Create task
        response = client.post("/tasks", json.dumps(self.test_task))
        assert response.status_code == 200

        # Delete task by ID
        response = client.delete(f"/tasks/id/{self.test_wrong_task['id']}")
        assert response.status_code == 400
