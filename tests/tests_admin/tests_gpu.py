from dss.models import Gpu, db
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

    def test_add_gpu_post(self):
        response = self.app.post("/admin/gpu/add", data={
            "type": "xya123",
            "memory": "2000",
            "speed": "3000"
        }).data.decode("utf-8")

        self.assertIn("GPU berhasil ditambahkan", response)

        gpu = Gpu.query.filter_by(type="xya123").first()
        self.assertEqual(2000, gpu.memory)
        self.assertEqual(3000, gpu.speed)

    def test_update_gpu_form(self):
        # add gpu
        gpu = Gpu("uyg123", 1000, 2000)
        db.session.add(gpu)
        db.session.commit()

        response = self.app.get("/admin/gpu/update/{}".format(gpu.type))\
            .data.decode("utf-8")

        self.assertIn("Update gpu", response)
        self.assertIn('action="/admin/gpu/update/{}"'.format(gpu.type), response)
        self.assertIn('name="memory" value="{}"'.format(gpu.memory), response)
        self.assertIn('name="speed" value="{}"'.format(gpu.speed), response)

    def test_update_gpu_action(self):
        # add gpu
        # add gpu
        gpu = Gpu("uyg123", 1000, 2000)
        db.session.add(gpu)
        db.session.commit()

        response = self.app.post("admin/gpu/update/{}".format(gpu.type), data={
            "memory": 4000,
            "speed": 8000
        }).data.decode("utf-8")

        self.assertIn("GPU berhasil di update", response)

        gpu = Gpu.query.filter_by(type="uyg123").first()
        self.assertEqual(gpu.memory, 4000)
        self.assertEqual(gpu.speed, 8000)
