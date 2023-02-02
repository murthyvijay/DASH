import json
import time
from pathlib import Path
from pprint import pprint

import pytest


class TestSaiPort:

    def test_port_create(self, dpu):

        commands = [
            {
                "name": "port",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_PORT",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values create =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_PORT Create error"

    def test_port_remove(self, dpu):

        commands = [
            {
                "name": "port",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_PORT",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values remove =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_PORT Remove error"