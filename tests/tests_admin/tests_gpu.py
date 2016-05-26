from tests.mock import ServerTest


class AdminUserTestCase(ServerTest):

    def setUp(self):
        self.db_migrate()

    def tearDown(self):
        self.db_drop()

    def test_add_gpu_form(self):
        response = self.app.get("/admin/gpu/add").data.decode("utf-8")

        self.assertIn("Add gpu", response)
        self.assertIn('action="/admin/gpu/add"', response)
        self.assertIn('name="type"', response)
        self.assertIn('name="memory"', response)
        self.assertIn('name="speed"', response)
