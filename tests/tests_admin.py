from tests.mock import ServerTest


class AdminTestCase(ServerTest):

    def test_home_admin(self):
        response = self.app.get("/admin")

        self.assertIn("Administrator page", response.data.decode("utf-8"))

    def test_admin_add_user_get(self):
        response = self.app.get("/admin/user/add")

        self.assertIn("Add user", response.data.decode("utf-8"))
