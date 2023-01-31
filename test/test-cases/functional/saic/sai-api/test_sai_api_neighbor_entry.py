import json
import time
from pathlib import Path
from pprint import pprint

import pytest


class TestSaiNeighborEntry:

    def test_neighbor_entry_create(self, dpu):

        commands = [
            {
                "name": "host_interface",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_NEIGHBOR_ENTRY",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values create =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_NEIGHBOR_ENTRY Create error"

    def test_neighbor_entry_remove(self, dpu):

        commands = [
            {
                "name": "host_interface",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_NEIGHBOR_ENTRY",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values remove =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_NEIGHBOR_ENTRY Remove error"
