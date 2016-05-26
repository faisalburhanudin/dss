from tests.mock import ServerTest


class AdminTestCase(ServerTest):

    def setUp(self):
        self.db_migrate()

    def tearDown(self):
        self.db_drop()

    def test_home_admin(self):
        response = self.app.get("/admin")

        self.assertIn("Administrator page", response.data.decode("utf-8"))
