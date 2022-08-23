import pytest
from flask import session
import requests, json, os
from dotenv import load_dotenv, find_dotenv
from todo_app import app

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = app.create_app()

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client



class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data
        self.status_code = 200
    def json(self):
        return self.fake_response_data



def stub(url, headers={}):
    trellobid = os.environ.get('TrelloBID')
    lk=os.environ.get('URL')
    apikey = os.getenv('APIKEY') 
    apitoken = os.getenv('APIToken')

    if url == lk+"1/boards/"+trellobid+"/lists?cards=open&key="+apikey+"&token="+apitoken:
        # Response data of this call is a list of dictionaries. Each dict is per status type - and has a list of cards in dict plus other things.
        fake_response_data = [
                                {
	                                "id":"62d90941864f2a4bff844d47",
	                                "name":"To Do",
                                    "idBoard":"62d90941864f2a4bff844d40",
	                                "cards":
	                                [
		                                {"id":"62d909554037ac170a69361c","idBoard":"62d90941864f2a4bff844d40","name":"W2 exercise"}, 
		                                {"id":"62d98a268e2cbd2aa27c9cb9","idBoard":"62d90941864f2a4bff844d40","name":"cd111"},
		                                {"id":"62d911f4a134af2aae043f6a","idBoard":"62d90941864f2a4bff844d40","name":"W2 trello items"}
	                                ]
                                },
                                {
	                                "id":"62d90941864f2a4bff844d36",
	                                "name":"Done",
                                    "idBoard":"62d90941864f2a4bff844d41",
	                                "cards":
	                                [
		                                {"id":"62d909554037ac170a69360c","idBoard":"62d90941864f2a4bff844d41","name":"W3 exercise"}, 
		                                {"id":"62d98a268e2cbd2aa27c9cb8","idBoard":"62d90941864f2a4bff844d41","name":"cd211"},
		                                {"id":"62d911f4a134af2aae043f5a","idBoard":"62d90941864f2a4bff844d41","name":"W3 trello items"}
	                                ]
                                }
                            ]
        return StubResponse(fake_response_data)

    raise Exception(f'Integration test did not expect URL "{url}"')


def test_indexpage(monkeypatch, client):
    # This replaces any call to requests.get with our own function
    monkeypatch.setattr(requests, 'get', stub)
    response = client.get('/')
    assert "W2 exercise" in response.data.decode()
    assert "cd111" in response.data.decode()
    assert "cd211" in response.data.decode()
    assert "W3 trello items" in response.data.decode()