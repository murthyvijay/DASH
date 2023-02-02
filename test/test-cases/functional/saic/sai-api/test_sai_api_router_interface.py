import json
import time
from pathlib import Path
from pprint import pprint

import pytest

HOSTIF_OBJID = 1


class TestSaiRouterInterface:

    def test_router_interface_create(self, dpu):

        commands = [
            {
                "name": "router_interface",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_ROUTER_INTERFACE",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values create =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_ROUTER_INTERFACE Create error"
        
    def test_router_interface_remove(self, dpu):

        commands = [
            {
                "name": "router_interface",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_ROUTER_INTERFACE",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values remove =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_ROUTER_INTERFACE Remove error"