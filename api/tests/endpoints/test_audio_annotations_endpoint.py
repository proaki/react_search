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


class TestAudioAnnotationsEndpoint(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestAudioAnnotationsEndpoint, self).__init__(*args, **kwargs)
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

        # Test audio_format type data
        self.test_audio_format_type = {"id": "2d6bb3c2-c168-457b-851d-78d29ded089e",
                                       "precision": 16,
                                       "sample_rate": 44100,
                                       "channels": 2}

        # Test audio data
        self.test_audio = {"md5": "2d6bb3c2-c168-457b-851d-78d29ded089e",
                           "file_name": "audio.wav",
                           "audio_format_id": "2d6bb3c2-c168-457b-851d-78d29ded089e",
                           "duration": "00:30:00.020",
                           "custom_property": json.dumps({"external_id": "external ID"}),
                           "organization_id": "2d6bb3c2-c168-457b-851d-78d29ded089e"}

        # Test annotation type data
        self.test_annotation_type = {"id": "2d6bb3c2-c168-457b-851d-78d29ded089e",
                                     "objective_name": "gr",
                                     "label_name": "genre",
                                     "value_type": "str"}
        # Test task data
        self.test_task = {"id": "2d6bb3c2-c168-457b-851d-78d29ded089e",
                             "name": "genre_classification",
                             "type": "classification",
                             "description": "Music Genre Classification"}

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

        # Test Updated audio_annotation
        self.updated_test_audio_annotation = {"id": "2d6bb3c2-c168-457b-851d-78d29ded089e", "version": 2}

        # Test wrong param audio_annotation
        self.test_wrong_audio_annotation = {"id": "1206a713-129e-445d-9532-8d682d911be9", "value": "Pop"}

    def setUp(self):
        # Clean table
        self.DBM.drop_table_contents()

    def tearDown(self):
        # Clean table
        self.DBM.drop_table_contents()

    def test_01_post_audio_annotation(self):
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

        # Create audio_annotation
        response = client.post("/audio_annotations", json.dumps(self.test_audio_annotation))
        assert response.status_code == 200

    def test_02_post_audio_with_wrong_parameter(self):
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

        # Create audio_annotation
        response = client.post("/audio_annotations", json.dumps(self.test_wrong_audio_annotation))
        assert response.status_code == 422

    def test_03_get_audio_annotation_all(self):
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

        # Get all audio_annotation
        response = client.get("/audio_annotations")
        assert response.status_code == 200

    def test_04_get_audio_annotation_by_id(self):
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

        # Create audio_annotation
        response = client.post("/audio_annotations", json.dumps(self.test_audio_annotation))
        assert response.status_code == 200

        # Get audio_annotation by ID
        response = client.get(f"/audio_annotations/id/{self.test_audio_annotation['id']}")
        assert response.status_code == 200

    def test_05_get_audio_annotation_by_wrong_id(self):
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

        # Create audio_annotation
        response = client.post("/audio_annotations", json.dumps(self.test_audio_annotation))
        assert response.status_code == 200

        # Get audio_annotation by ID
        response = client.get(f"/audio_annotations/id/{self.test_wrong_audio_annotation['id']}")
        assert response.status_code == 400
        assert json.loads(response.content)['detail'] == f"{self.test_wrong_audio_annotation['id']} does not exist"

    def test_06_update_audio_annotation(self):
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

        # Create audio_annotation
        response = client.post("/audio_annotations", json.dumps(self.test_audio_annotation))
        assert response.status_code == 200

        # Put audio_annotation
        response = client.put("/audio_annotations", json.dumps(self.updated_test_audio_annotation))
        assert response.status_code == 200

        # Get audio_annotation by updated ID
        response = client.get(f"/audio_annotations/id/{self.test_audio_annotation['id']}")
        assert response.status_code == 200
        assert json.loads(response.content)['id'] == self.updated_test_audio_annotation['id']

    def test_07_update_audio_wrong_id(self):
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

        # Create audio_annotation
        response = client.post("/audio_annotations", json.dumps(self.test_audio_annotation))
        assert response.status_code == 200

        # Put audio_annotation
        response = client.put("/audio_annotations", json.dumps(self.test_wrong_audio_annotation))
        assert response.status_code == 400
        assert json.loads(response.content)['detail'] == f"{self.test_wrong_audio_annotation['id']} does not exist"

    def test_08_delete_annotator_by_id(self):
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

        # Create audio_annotation
        response = client.post("/audio_annotations", json.dumps(self.test_audio_annotation))
        assert response.status_code == 200

        # Delete audio_annotation by ID
        response = client.delete(f"/audio_annotations/id/{self.updated_test_audio_annotation['id']}")
        assert response.status_code == 200

    def test_09_delete_annotator_wrong_id(self):
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

        # Create audio_annotation
        response = client.post("/audio_annotations", json.dumps(self.test_audio_annotation))
        assert response.status_code == 200

        # Delete audio_annotation by ID
        response = client.delete(f"/audio_annotations/id/{self.test_wrong_audio_annotation['id']}")
        assert response.status_code == 400
