import json
import time
from pathlib import Path
from pprint import pprint

import pytest


class TestSaiNextHop:

    def test_next_hop_create(self, dpu):

        commands = [
            {
                "name": "host_interface",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_NEXT_HOP",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values create =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_NEXT_HOP Create error"

    def test_next_hop_remove(self, dpu):

        commands = [
            {
                "name": "host_interface",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_NEXT_HOP",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values remove =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_NEXT_HOP Remove error"
