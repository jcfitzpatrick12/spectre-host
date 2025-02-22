# SPDX-FileCopyrightText: © 2024 Jimmy Fitzpatrick <jcfitzpatrick12@gmail.com>
# This file is part of SPECTRE
# SPDX-License-Identifier: GPL-3.0-or-later


from flask import Blueprint, request

from spectre_server.services import logs
from spectre_server.routes._format_responses import jsendify_response


logs_blueprint = Blueprint("logs", __name__)


@logs_blueprint.route("", methods=["GET"])
@jsendify_response
def get_logs(
) -> list[str]:
    process_type = request.args.get("process-type", type = str)
    year         = request.args.get("year", type = int)
    month        = request.args.get("month", type = int)
    day          = request.args.get("day", type = int)
    return logs.get_logs(process_type, 
                         year,
                         month,
                         day)


@logs_blueprint.route("", methods=["DELETE"])
@jsendify_response
def delete_logs(
) -> list[str]:
    process_type = request.args.get("process-type", type = str)
    year         = request.args.get("year", type = int)
    month        = request.args.get("month", type = int)
    day          = request.args.get("day", type = int)
    return logs.delete_logs(process_type, 
                            year,
                            month,
                            day)

@logs_blueprint.route("/<string:pid>", methods=["GET"])
@jsendify_response
def get_log(pid: str
) -> str:
    return logs.get_log(pid=pid)