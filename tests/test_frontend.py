from tests.mock import ServerTest


class FrontendTestCase(ServerTest):

    def test_home(self):
        response = self.app.get("/")

        self.assertIn("Sistem pendukung keputusan", response.data)