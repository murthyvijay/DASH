import json
import time
from pathlib import Path
from pprint import pprint

import pytest


class TestSaiSwitch:

    def test_switch_create(self, dpu):

        commands = [
            {
                "name": "switch",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_SWITCH",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values create =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_SWITCH Create error"

    def test_switch_remove(self, dpu):

        commands = [
            {
                "name": "switch",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_SWITCH",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values remove =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_SWITCH Remove error"
