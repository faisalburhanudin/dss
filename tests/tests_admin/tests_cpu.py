from dss.models import Cpu, db
from tests.mock import ServerTest


class AdminUserTestCase(ServerTest):

    def setUp(self):
        self.db_migrate()

    def tearDown(self):
        self.db_drop()

    def test_add_cpu_form(self):
        response = self.app.get("/admin/cpu/add").data.decode("utf-8")

        self.assertIn("Add cpu", response)
        self.assertIn('action="/admin/cpu/add"', response)
        self.assertIn('name="core"', response)
        self.assertIn('name="speed"', response)
        self.assertIn('name="cache"', response)

    def test_add_cpu_post(self):
        response = self.app.post("/admin/cpu/add", data={
            "type":"xya123",
            "core": 2,
            "speed": "2000",
            "cache": "3000"
        }).data.decode("utf-8")

        self.assertIn("CPU berhasil ditambahkan", response)

        cpu = Cpu.query.filter_by(type="xya123").first()
        self.assertEqual(2, cpu.core)
        self.assertEqual(2000, cpu.speed)
        self.assertEqual(3000, cpu.cache)

    def test_update_cpu_form(self):
        # add cpu
        cpu = Cpu("uyg123", 2, 1000, 2000)
        db.session.add(cpu)
        db.session.commit()

        response = self.app.get("/admin/cpu/update/{}".format(cpu.type))\
            .data.decode("utf-8")

        self.assertIn("Update cpu", response)
        self.assertIn('action="/admin/cpu/update/{}"'.format(cpu.type), response)
        self.assertIn('name="core" value="{}"'.format(cpu.core), response)
        self.assertIn('name="speed" value="{}"'.format(cpu.speed), response)
        self.assertIn('name="cache" value="{}"'.format(cpu.cache), response)

    def test_update_cpu_action(self):
        # add cpu
        cpu = Cpu("uyg123", 2, 1000, 2000)
        db.session.add(cpu)
        db.session.commit()

        response = self.app.post("admin/cpu/update/{}".format(cpu.type), data={
            "core": 8,
            "speed": 4000,
            "cache": 8000
        }).data.decode("utf-8")

        self.assertIn("CPU berhasil di update", response)

        cpu = Cpu.query.filter_by(type="uyg123").first()
        self.assertEqual(cpu.core, 8)
        self.assertEqual(cpu.speed, 4000)
        self.assertEqual(cpu.cache, 8000)
