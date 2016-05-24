from dss.models import Administrator
from tests.mock import ServerTest


class AdminTestCase(ServerTest):

    def setUp(self):
        self.db_migrate()

    def tearDown(self):
        self.db_drop()

    def test_home_admin(self):
        response = self.app.get("/admin")

        self.assertIn("Administrator page", response.data.decode("utf-8"))

    def test_admin_add_user_get(self):
        response = self.app.get("/admin/user/add")

        self.assertIn("Add user", response.data.decode("utf-8"))
        self.assertIn('action="/admin/user/add"', response.data.decode("utf-8"))
        self.assertIn('name="username"', response.data.decode("utf-8"))
        self.assertIn('name="status"', response.data.decode("utf-8"))
        self.assertIn('name="password"', response.data.decode("utf-8"))

    def test_addmin_add_user_post(self):
        response = self.app.post("/admin/user/add", data={
            "username": "faisal",
            "status": "2",
            "password": "123"
        })

        self.assertIn("User berhasil ditambahkan", response.data.decode("utf-8"))

        administrator = Administrator.query.filter_by(username="faisal").first()
        self.assertEqual(2, administrator.status)
        self.assertEqual('123', administrator.password)
