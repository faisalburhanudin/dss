from dss.models import Administrator, db
from tests.mock import ServerTest


class AdminTestCase(ServerTest):

    def setUp(self):
        self.db_migrate()

    def tearDown(self):
        self.db_drop()

    def test_home_admin(self):
        response = self.app.get("/admin")

        self.assertIn("Administrator page", response.data.decode("utf-8"))

    def test_admin_add_user_form(self):
        response = self.app.get("/admin/user/add").data.decode("utf-8")

        self.assertIn("Add user", response)
        self.assertIn('action="/admin/user/add"', response)
        self.assertIn('name="username"', response)
        self.assertIn('name="status"', response)
        self.assertIn('name="password"', response)

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

    def test_admin_update_form(self):
        # add one user
        user = Administrator("foo", 1, "bar")
        db.session.add(user)
        db.session.commit()

        response = self.app.get("/admin/user/update/" + str(user.id)).data.decode("utf-8")

        self.assertIn("Update user", response)
        self.assertIn('action="/admin/user/update/{}"'.format(user.id), response)
        self.assertIn('name="username" value="{}"'.format(user.username), response)
        self.assertIn('value="1" selected', response)
        self.assertIn('name="password" value="{}"'.format(user.password), response)
