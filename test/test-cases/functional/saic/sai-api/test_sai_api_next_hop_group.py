import json
import time
from pathlib import Path
from pprint import pprint

import pytest


class TestSaiNextHopGroup:

    def test_next_hop_group_create(self, dpu):

        commands = [
            {
                "name": "next_hop_group",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_NEXT_HOP_GROUP",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values create =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_NEXT_HOP_GROUP Create error"

    def test_next_hop_group_remove(self, dpu):

        commands = [
            {
                "name": "next_hop_group",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_NEXT_HOP_GROUP",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values remove =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_NEXT_HOP_GROUP Remove error"
