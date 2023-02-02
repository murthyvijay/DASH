import json
import time
from pathlib import Path
from pprint import pprint

import pytest


class TestSaiRouteEntry:

    def test_route_entry_create(self, dpu):

        commands = [
            {
                "name": "route_entry",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_ROUTE_ENTRY",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values create =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_ROUTE_ENTRY Create error"

    def test_route_entry_remove(self, dpu):

        commands = [
            {
                "name": "route_entry",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_ROUTE_ENTRY",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values remove =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_ROUTE_ENTRY Remove error"
