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
eni_id = 1
vnet_1 = 1


class TestSaiVnetVni:

    def test_vnet_pa_validation_entry_create(self, dpu):

        commands = [
            {
                "name": "pa_validation_entry",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_PA_VALIDATION_ENTRY",
                "key": {
                    "switch_id": "$SWITCH_ID",
                    "sip": "10.10.2.10",
                    "vnet_id": "$vnet"
                },
                "attributes": [
                    "SAI_PA_VALIDATION_ENTRY_ATTR_ACTION",
                    "SAI_PA_VALIDATION_ENTRY_ACTION_PERMIT"
                ]
            }
        ]
        result = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values create =======")
        pprint(result)

    def test_vnet_pa_validation_entry_get1(self, dpu):

        commands = [
            {
                "name": "pa_validation_entry",
                "op": "get",
                "type": "SAI_OBJECT_TYPE_PA_VALIDATION_ENTRY",
                "attribute": "SAI_PA_VALIDATION_ENTRY_ATTR_ACTION"
            }
        ]
        result = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values get =======")
        pprint(result)

        assert (result[0].value(), "SAI_PA_VALIDATION_ENTRY_ACTION_PERMIT")

    # TODO: figure out all supported values for set attributes
    def test_vnet_pa_validation_entry_set(self, dpu):

        commands = [
            {
                "name": "pa_validation_entry",
                "op": "set",
                "type": "SAI_OBJECT_TYPE_PA_VALIDATION_ENTRY",
                "key": {
                    "switch_id": "$SWITCH_ID",
                    "sip": "10.10.10.10",
                    "vnet_id": "$vnet"
                },
                "attribute": [
                    "SAI_PA_VALIDATION_ENTRY_ATTR_ACTION",
                    "SAI_PA_VALIDATION_ENTRY_ACTION_DENY"
                ]
            }
        ]
        result = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values set =======")
        pprint(result)

    def test_vnet_pa_validation_entry_get2(self, dpu):

        commands = [
            {
                "name": "pa_validation_entry",
                "op": "get",
                "type": "SAI_OBJECT_TYPE_PA_VALIDATION_ENTRY",
                "attribute": "SAI_PA_VALIDATION_ENTRY_ATTR_ACTION"
            }
        ]
        result = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values get =======")
        pprint(result)

        assert (result[0].value(), "SAI_PA_VALIDATION_ENTRY_ACTION_DENY")

    def test_vnet_pa_validation_entry_remove(self, dpu):

        commands = [
            {
                "name": "pa_validation_entry",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_PA_VALIDATION_ENTRY",
                "key": {
                    "switch_id": "$SWITCH_ID",
                    "sip": "10.10.10.10",
                    "vnet_id": "$vnet"
                },
                "attribute": [
                    "SAI_PA_VALIDATION_ENTRY_ATTR_ACTION",
                    "SAI_PA_VALIDATION_ENTRY_ACTION_PERMIT"
                ]
            }
        ]

        result = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values remove =======")
        pprint(result)
