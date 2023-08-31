from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from collections import defaultdict
from collections.abc import Mapping

from ansible.errors import AnsibleFilterTypeError
from ansible.plugins.filter.core import dict_to_list_of_dict_key_value_elements


def interfaces_by_zone(data):
    if not isinstance(data, Mapping):
        raise AnsibleFilterTypeError(f"interfaces_by_zone requires a dictionry, got {type(data)} instead")

    result = defaultdict(list)
    for interface, spec in data.items():
        if zone := spec.get("zone"):
            try:
                result[zone].append(interface)
            except TypeError as exc:
                raise AnsibleFilterTypeError(exc)

    return dict_to_list_of_dict_key_value_elements(result, key_name="zone", value_name="interfaces")


class FilterModule(object):
    def filters(self):
        return {
            'interfaces_by_zone': interfaces_by_zone,
        }
