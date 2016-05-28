from dss.models import Computer, db
from tests.mock import ServerTest


class AdminUserTestCase(ServerTest):

    def setUp(self):
        self.db_migrate()

    def tearDown(self):
        self.db_drop()

    def test_add_computer_form(self):
        response = self.app.get("/admin/computer/add").data.decode("utf-8")

        self.assertIn("Add computer", response)
        self.assertIn('action="/admin/computer/add"', response)
        self.assertIn('name="type"', response)
        self.assertIn('name="price"', response)
        self.assertIn('name="cpu_id"', response)
        self.assertIn('name="gpu_id"', response)
        self.assertIn('name="ram"', response)
        self.assertIn('name="harddisk"', response)
        self.assertIn('name="monitor"', response)

    def test_add_computer_post(self):
        response = self.app.post("/admin/computer/add", data={
            "type":"xya123",
            "price": 2000,
            "cpu_id": 1,
            "gpu_id": 2,
            "ram": 2,
            "harddisk": 200,
            "monitor": 21
        }).data.decode("utf-8")

        self.assertIn("Computer berhasil ditambahkan", response)

        computer = Computer.query.filter_by(type="xya123").first()
        self.assertEqual(2000, computer.price)
        self.assertEqual("1", computer.cpu_id)
        self.assertEqual("2", computer.gpu_id)
        self.assertEqual(2, computer.ram)
        self.assertEqual(200, computer.harddisk)
        self.assertEqual(21, computer.monitor)

    def test_update_computer_form(self):
        # add computer
        computer = Computer("uyg123", 2000, 1, 2, 2, 200, 21)
        db.session.add(computer)
        db.session.commit()

        response = self.app.get("/admin/computer/update/{}".format(computer.type))\
            .data.decode("utf-8")

        self.assertIn("Update computer", response)
        self.assertIn('action="/admin/computer/update/{}"'.format(computer.type), response)
        self.assertIn('name="type" value="{}" disabled'.format(computer.type), response)
        self.assertIn('name="price" value="{}"'.format(computer.price), response)
        self.assertIn('name="cpu_id" value="{}"'.format(computer.cpu_id), response)
        self.assertIn('name="gpu_id" value="{}"'.format(computer.gpu_id), response)
        self.assertIn('name="ram" value="{}"'.format(computer.ram), response)
        self.assertIn('name="harddisk" value="{}"'.format(computer.harddisk), response)
        self.assertIn('name="monitor" value="{}"'.format(computer.monitor), response)

    def test_update_computer_action(self):
        # add computer
        computer = Computer("uyg123", 2000, 1, 2, 2, 200, 21)
        db.session.add(computer)
        db.session.commit()

        response = self.app.post("admin/computer/update/{}".format(computer.type), data={
            "price": 3000,
            "cpu_id": 3,
            "gpu_id": 4,
            "ram": 1,
            "harddisk": 300,
            "monitor": 14
        }).data.decode("utf-8")

        self.assertIn("Computer berhasil di update", response)

        computer = Computer.query.filter_by(type="uyg123").first()
        self.assertEqual(3000, computer.price)
        self.assertEqual("3", computer.cpu_id)
        self.assertEqual("4", computer.gpu_id)
        self.assertEqual(1, computer.ram)
        self.assertEqual(300, computer.harddisk)
        self.assertEqual(14, computer.monitor)
