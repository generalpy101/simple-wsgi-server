import pytest
import multiprocessing
import requests
from src import ThreadedServer

class TestRoutes:
    @pytest.fixture(autouse = True, scope="session")
    def start_server(self):
        server = ThreadedServer('0.0.0.0',8080)
        p = multiprocessing.Process(target=server.listen)
        p.start()
        yield 
        p.terminate()
    
    def test_home(self):
        req = requests.get("localhost:5000")
        assert req.status_code == 200
        assert b"Hello from /" in req.content