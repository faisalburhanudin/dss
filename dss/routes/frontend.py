import copy
from flask import Blueprint, render_template, jsonify, request
from dss.models import Computer

bp = Blueprint(__name__, 'frontend')


@bp.route("/")
def home():
    return render_template("index.html")


@bp.route("/json/saw")
def saw():
    price_priority = request.form.get("price", 0)
    ram_priority = request.form.get("ram", 0)
    harddisk_priority = request.form.get("harddisk", 0)
    monitor_priority = request.form.get("monitor", 0)
    cpu_priority = request.form.get("cpu", 0)
    gpu_priority = request.form.get("gpu", 0)

    weight = [
        price_priority,
        ram_priority,
        harddisk_priority,
        monitor_priority,
        cpu_priority,
        gpu_priority]

    # load array kandidat
    computers = [
        [com,
         com.price,
         com.cpu,
         com.gpu,
         com.ram,
         com.harddisk,
         com.monitor] for com in Computer.query.all()]

    # criteria
    # get max min per matrix
    c1 = min([p[1] for p in computers])
    c2 = max([p[2] for p in computers])
    c3 = max([p[3] for p in computers])
    c4 = max([p[4] for p in computers])
    c5 = max([p[5] for p in computers])
    c6 = max([p[6] for p in computers])

    # copy ori for normalitation
    normalisation = copy.deepcopy(computers)

    # normalitation
    for idx, i in enumerate(normalisation):
        normalisation[idx][1] = c1 / i[1]
        normalisation[idx][2] = i[2] / c2
        normalisation[idx][3] = i[3] / c3
        normalisation[idx][4] = i[4] / c4
        normalisation[idx][5] = i[5] / c5
        normalisation[idx][6] = i[6] / c6

    # rank
    for idx, i in enumerate(normalisation):
        rank = (weight[0] * normalisation[idx][1]) + \
               (weight[1] * normalisation[idx][2]) + \
               (weight[2] * normalisation[idx][3]) + \
               (weight[3] * normalisation[idx][4]) + \
               (weight[4] * normalisation[idx][5]) + \
               (weight[5] * normalisation[idx][6])

        # and to last matrix
        normalisation[idx].append(rank)

    # sort by high score
    final = sorted(normalisation, key=lambda l: l[7], reverse=True)

    result = []
    for f in final:
        result.append({
            "type": f[0].type,
            "score": f[7]
        })

    response = {
        "result": result
    }
    return jsonify(response)
