import unittest
import identidock


class TestIdentify(unittest.TestCase):

    def setUp(self): 
        identidock.app.config["TESTING"] = True
        self.app = identidock.app.test_client()
    

    def test_get_mainpage(self):
        page = self.app.get( "/")
        assert page.status_code == 200
        assert 'Hello' in str( page.data )
        assert 'Alice Chang' in str( page.data )   
        
if __name__ == '__main__':
    unittest.main()