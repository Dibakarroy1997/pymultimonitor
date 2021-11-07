import enum


class DisplayConfigTopology(enum.IntEnum):
    DISPLAYCONFIG_TOPOLOGY_INTERNAL = 1
    DISPLAYCONFIG_TOPOLOGY_CLONE = 2
    DISPLAYCONFIG_TOPOLOGY_EXTEND = 4
    DISPLAYCONFIG_TOPOLOGY_EXTERNAL = 8
    DISPLAYCONFIG_TOPOLOGY_FORCE_UINT32 = -1

    def __str__(self):
        return self.name.lstrip("DISPLAYCONFIG_TOPOLOGY_")
