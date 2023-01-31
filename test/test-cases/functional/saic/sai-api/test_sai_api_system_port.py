import json
import time
from pathlib import Path
from pprint import pprint

import pytest

HOSTIF_OBJID = 1


class TestSaiSystemPort:

    def test_system_port_create(self, dpu):

        commands = [
            {
                "name": "host_interface",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_SYSTEM_PORT",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values create =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_SYSTEM_PORT Create error"

    def test_system_port_remove(self, dpu):

        commands = [
            {
                "name": "host_interface",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_SYSTEM_PORT",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values remove =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_SYSTEM_PORT Remove error"
