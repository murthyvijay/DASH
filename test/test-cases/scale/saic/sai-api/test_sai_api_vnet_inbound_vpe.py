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


class TestSaiVnetInbound:

    def test_vnet_inbound_simple_create(self, dpu):

        commands = [
            {
                "name": "vpe",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_VIP_ENTRY",
                "key": {
                    "switch_id": "$SWITCH_ID",
                    "vip": "1.1.1.1"
                },
                "attributes": [
                    "SAI_VIP_ENTRY_ATTR_ACTION", "SAI_VIP_ENTRY_ACTION_ACCEPT"
                ]
            }
        ]
        result = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values create =======")
        pprint(result)

    def test_vnet_inbound_simple_get1(self, dpu):

        commands = [
            {
                "name": "$vpe",
                "op": "get",
                "type": "SAI_OBJECT_TYPE_VIP_ENTRY",
                "attribute": "SAI_VIP_ENTRY_ATTR_ACTION"
            }
        ]
        result = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values get =======")
        pprint(result)

        assert (result[0].value(), "SAI_VIP_ENTRY_ACTION_ACCEPT")

    def test_vnet_inbound_simple_set(self, dpu):

        commands = [
            {
                "name": "$vpe",
                "op": "set",
                "type": "SAI_OBJECT_TYPE_VIP_ENTRY",
                "key": {
                    "switch_id": "$SWITCH_ID",
                    "vip": "2.2.2.2"
                },
                "attributes": [
                    "SAI_VIP_ENTRY_ATTR_ACTION", "SAI_VIP_ENTRY_ACTION_REJECT"
                ]
            }
        ]
        result = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values set =======")
        pprint(result)

    def test_vnet_inbound_simple_get2(self, dpu):

        commands = [
            {
                "name": "$vpe",
                "op": "get",
                "type": "SAI_OBJECT_TYPE_VIP_ENTRY",
                "attribute": "SAI_VIP_ENTRY_ATTR_ACTION"
            }
        ]
        result = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values get =======")
        pprint(result)

        assert (result[0].value(), "SAI_VIP_ENTRY_ACTION_REJECT")

    def test_vnet_inbound_simple_remove(self, dpu):

        commands = [
            {
                "name": "vpe",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_VIP_ENTRY",
                "key": {
                    "switch_id": "$SWITCH_ID",
                    "vip": "2.2.2.2"
                },
                "attributes": [
                    "SAI_VIP_ENTRY_ATTR_ACTION", "SAI_VIP_ENTRY_ACTION_ACCEPT"
                ]
            }
        ]

        result = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values remove =======")
        pprint(result)
