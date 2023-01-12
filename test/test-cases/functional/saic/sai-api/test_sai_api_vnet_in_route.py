import json
import time
from pathlib import Path
from pprint import pprint

import pytest

# Constants
SWITCH_ID = 5


class TestSaiVnetInboundRoutingEntry:

    @pytest.mark.dependency(depends=['test_sai_api_vnet_eni.py::test_vnet_eni_create'], scope='session')
    def test_vnet_inbound_routing_entry_create(self, dpu):

        commands = [
            {
                "name": "inbound_routing_entry",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY",
                "key": {
                    "switch_id": "$SWITCH_ID",
                    "eni_id": "1",
                    "vni": "1000",
                    "sip": "10.10.2.0",
                    "sip_mask": "255.255.255.0",
                    "priority": 0
                },
                "attributes": [
                    "SAI_INBOUND_ROUTING_ENTRY_ATTR_ACTION",
                    "SAI_INBOUND_ROUTING_ENTRY_ACTION_VXLAN_DECAP_PA_VALIDATE",
                    "SAI_INBOUND_ROUTING_ENTRY_ATTR_SRC_VNET_ID",
                    "$vnet_1"
                ]
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values create =======")
        pprint(results)

        assert all( [result == 0 for result in results]), "SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY Create error"

    @pytest.mark.skip(reason="get and set not implemented, yet")
    def test_vnet_inbound_routing_entry_get1(self, dpu):

        commands = [
            {
                "name": "inbound_routing_entry",
                "op": "get",
                "type": "SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY",
                "attribute": "SAI_INBOUND_ROUTING_ENTRY_ATTR_ACTION"
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values get =======")
        pprint(results)

        assert all( [result == 0 for result in results]), "SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY Get error"

    @pytest.mark.skip(reason="get and set not implemented, yet")
    def test_vnet_inbound_routing_entry_set(self, dpu):

        commands = [
            {
                "name": "inbound_routing_entry",
                "op": "set",
                "type": "SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY",
                "key": {
                    "switch_id": "$SWITCH_ID",
                    "eni_id": "$eni_id",
                    "vni": "2000",
                    "sip": "10.10.10.0",
                    "sip_mask": "255.255.255.0",
                    "priority": 0
                },
                "attribute": [
                    "SAI_INBOUND_ROUTING_ENTRY_ATTR_ACTION",
                    "SAI_INBOUND_ROUTING_ENTRY_ACTION_VXLAN_DECAP_CA_VALIDATE",
                ]
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values set =======")
        pprint(results)

        assert all( [result == 0 for result in results]), "SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY Set error"

    @pytest.mark.skip(reason="get and set not implemented, yet")
    def test_vnet_inbound_routing_entry_get2(self, dpu):

        commands = [
            {
                "name": "$vnet",
                "op": "get",
                "type": "SAI_OBJECT_TYPE_VNET",
                "attribute": "SAI_INBOUND_ROUTING_ENTRY_ATTR_ACTION"
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values get =======")
        pprint(results)

        assert all( [result == 0 for result in results]), "SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY Get error"

    @pytest.mark.dependency(depends=['test_vnet_inbound_routing_entry_create'], scope='session')
    def test_vnet_inbound_routing_entry_remove(self, dpu):

        commands = [
            {
                "name": "inbound_routing_entry",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY",
                "key": {
                    "switch_id": "$SWITCH_ID",
                    "eni_id": "1",
                    "vni": "1000",
                    "sip": "10.10.10.0",
                    "sip_mask": "255.255.255.0",
                    "priority": 0
                },
                "attributes": [
                    "SAI_INBOUND_ROUTING_ENTRY_ATTR_ACTION",
                    "SAI_INBOUND_ROUTING_ENTRY_ACTION_VXLAN_DECAP_PA_VALIDATE",
                    "SAI_INBOUND_ROUTING_ENTRY_ATTR_SRC_VNET_ID",
                    "$vnet_1"
                ]
            },
        ]

        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values remove =======")
        pprint(results)

        assert all( [result == 0 for result in results]), "SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY Remove error"
