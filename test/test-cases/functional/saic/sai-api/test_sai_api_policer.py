import json
import time
from pathlib import Path
from pprint import pprint

import pytest


class TestSaiPolicer:

    def test_policer_create(self, dpu):

        commands = [
            {
                "name": "host_interface",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_POLICER",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values create =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_POLICER Create error"

    def test_policer_remove(self, dpu):

        commands = [
            {
                "name": "host_interface",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_POLICER",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values remove =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_POLICER Remove error"
