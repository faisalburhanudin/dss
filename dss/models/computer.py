from dss.models import db
from dss.models.cpu import Cpu
from dss.models.gpu import Gpu


class Computer(db.Model):

    type = db.Column(db.String(50), primary_key=True)

    price = db.Column(db.Integer)

    cpu_id = db.Column(db.String(50))

    gpu_id = db.Column(db.String(50))

    ram = db.Column(db.Integer)

    harddisk = db.Column(db.Integer)

    monitor = db.Column(db.Integer)

    def __init__(self, typ, price, cpu_id, gpu_id, ram, harddisk, monitor):
        self.type = typ
        self.price = price
        self.cpu_id = cpu_id
        self.gpu_id = gpu_id
        self.ram = ram
        self.harddisk = harddisk
        self.monitor = monitor

    @property
    def cpu_obj(self):
        c = Cpu.query.filter_by(type=self.cpu_id).first()

        return c

    @property
    def gpu_obj(self):
        g = Gpu.query.filter_by(type=self.gpu_id).first()

        return g

    @property
    def cpu(self):
        c = Cpu.query.filter_by(type=self.cpu_id).first()

        return c.core + c.speed + c.cache

    @property
    def gpu(self):
        g = Gpu.query.filter_by(type=self.gpu_id).first()

        return g.memory + g.speed
