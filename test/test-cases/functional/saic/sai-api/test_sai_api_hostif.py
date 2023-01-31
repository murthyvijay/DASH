import json
import time
from pathlib import Path
from pprint import pprint

import pytest

HOSTIF_OBJID = 1


class TestSaiHostIf:

    def test_host_interface_create(self, dpu):

        commands = [
            {
                "name": "host_interface",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_HOSTIF",
                "attributes": [
                    "SAI_HOSTIF_ATTR_NAME",
                    "sai_hostif",   
                ]
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values create =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_HOSTIF Create error"
        
    def test_host_interface_remove(self, dpu):

        commands = [
            {
                "name": "host_interface",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_HOSTIF",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values remove =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_HOSTIF Remove error"