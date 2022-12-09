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


class TestSaiVnetVni:

    def test_vnet_eni_ether_address_create(self, dpu):

        commands = [
            {
                "name": "eni_ether_address_map_entry",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_ENI_ETHER_ADDRESS_MAP_ENTRY",
                "key": {
                    "switch_id": "$SWITCH_ID",
                    "address": "00:AA:AA:AA:AA:00"
                },
                "attributes": [
                    "SAI_ENI_ETHER_ADDRESS_MAP_ENTRY_ATTR_ENI_ID",
                    "$eni_id"
                ]
            },
        ]
        result = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values create =======")
        pprint(result)

    def test_vnet_eni_ether_address_get1(self, dpu):

        commands = [
            {
                "name": "$eni_ether_address_map_entry",
                "op": "get",
                "type": "SAI_OBJECT_TYPE_ENI_ETHER_ADDRESS_MAP_ENTRY"
            }
        ]
        result = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values get =======")
        pprint(result)

        assert (result[0].value(), TODO: figure out $eni_id)

    def test_vnet_eni_ether_address_set(self, dpu):

        commands = [
            {
                "name": "eni_ether_address_map_entry",
                "op": "set",
                "type": "SAI_OBJECT_TYPE_ENI_ETHER_ADDRESS_MAP_ENTRY",
                "key": {
                    "switch_id": "$SWITCH_ID",
                    "address": "00:AA:AA:AA:BB:00"
                },
                "attributes": [
                    "SAI_ENI_ETHER_ADDRESS_MAP_ENTRY_ATTR_ENI_ID",
                    "$eni_id"
                ]
            },
        ]
        result = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values set =======")
        pprint(result)

    def test_vnet_eni_ether_address_get2(self, dpu):

        commands = [
            {
                "name": "$vnet",
                "op": "get",
                "type": "SAI_OBJECT_TYPE_VNET"
            }
        ]
        result = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values get =======")
        pprint(result)

        assert (result[0].value(), TODO: figure out $eni_id)

    def test_vnet_eni_ether_address_remove(self, dpu):

        commands = [
            {
                "name": "eni_ether_address_map_entry",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_ENI_ETHER_ADDRESS_MAP_ENTRY",
                "key": {
                    "switch_id": "$SWITCH_ID",
                    "address": "00:AA:AA:AA:BB:00"
                },
                "attributes": [
                    "SAI_ENI_ETHER_ADDRESS_MAP_ENTRY_ATTR_ENI_ID",
                    "$eni_id"
                ]
            },
        ]

        result = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values remove =======")
        pprint(result)
