import json
import time
from pathlib import Path
from pprint import pprint

import pytest
import saichallenger.dataplane.snappi.snappi_traffic_utils as stu
from saichallenger.dataplane.ptf_testutils import (send_packet,
                                                   simple_udp_packet,
                                                   simple_vxlan_packet,
                                                   verify_no_other_packets,
                                                   verify_packet)

import dash_helper.vnet2vnet_helper as dh

current_file_dir = Path(__file__).parent

# Constants
SWITCH_ID = 5



class TestSaiDirectionLookup:

    def test_direction_lookup_create(self, dpu):

        commands = [
            {   
            "name": "direction_lookup_entry",
            "op": "create",
            "type": "SAI_OBJECT_TYPE_DIRECTION_LOOKUP_ENTRY",
            "key": {
            "switch_id": "$SWITCH_ID",
            "vni": "2000"
            },
	    "attributes": [
	      "SAI_DIRECTION_LOOKUP_ENTRY_ATTR_ACTION",
	      "SAI_DIRECTION_LOOKUP_ENTRY_ACTION_SET_OUTBOUND_DIRECTION"
	    ]
	    },
        ]
        result = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values create =======")
        pprint(result)

    def test_direction_lookup_get1(self, dpu):

        commands = [
            {
                "name": "$vpe",
                "op": "get",
                "type": "SAI_OBJECT_TYPE_DIRECTION_LOOKUP_ENTRY"
            }
        ]
        result = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values get =======")
        pprint(result)

        # TODO:add value get assert
        # Assert if result[value1]  == "2000"

    def test_direction_lookup_set(self, dpu):

        commands = [
            {
                "name": "$vpe",
                "op": "set",
                "type": "SAI_OBJECT_TYPE_DIRECTION_LOOKUP_ENTRY",
                "key": {
                "switch_id": "$SWITCH_ID",
                "vni": "4000"
            },
            "attributes": [
              "SAI_DIRECTION_LOOKUP_ENTRY_ATTR_ACTION",
              "SAI_DIRECTION_LOOKUP_ENTRY_ACTION_SET_OUTBOUND_DIRECTION"
            ]
          },
        ]

        result = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values set =======")
        pprint(result)

    def test_direction_lookup_get2(self, dpu):

        commands = [
            {
                "name": "$vpe",
                "op": "get",
                "type": "SAI_OBJECT_TYPE_VIP_ENTRY"
            }
        ]
        result = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values get =======")
        pprint(result)

        # TODO:add value get assert
        # Assert if result.value1 == "4000"

    def test_direction_lookup_remove(self, dpu):

        commands = [
            {   
            "name": "direction_lookup_entry",
            "op": "remove",
            "type": "SAI_OBJECT_TYPE_DIRECTION_LOOKUP_ENTRY",
            "key": {
            "switch_id": "$SWITCH_ID",
            "vni": "2000"
            },
            "attributes": [
            "SAI_DIRECTION_LOOKUP_ENTRY_ATTR_ACTION",
            "SAI_DIRECTION_LOOKUP_ENTRY_ACTION_SET_OUTBOUND_DIRECTION"
            ]
	    },
        ]

        result = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values remove =======")
        pprint(result)
