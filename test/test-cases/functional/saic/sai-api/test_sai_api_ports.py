import json
import time
from pathlib import Path
from pprint import pprint

import pytest


class TestSaiPorts:

    def test_ports_create(self, dpu):

        commands = [
            {
                "name": "ports",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_PORTS",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values create =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_PORTS Create error"

    def test_ports_remove(self, dpu):

        commands = [
            {
                "name": "ports",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_PORTS",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values remove =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_PORTS Remove error"