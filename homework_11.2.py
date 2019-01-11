from draw_network_graph import draw_topology
from homework_11_1 import parse_cdp_neighbors

draw_topology(parse_cdp_neighbors('SW1>show cdp neighborsCapability Codes: R - Router, T - Trans Bridge, B - Source Route BridgeS - Switch, H - Host, I - IGMP, r - Repeater, P - PhoneDevice ID    Local Intrfce   Holdtme     Capability       Platform    Port IDR1           Eth 0/1         122           R S I           2811       Eth 0/0R2           Eth 0/2         143           R S I           2811       Eth 0/0R3           Eth 0/3         151           R S I           2811       Eth 0/0'))
