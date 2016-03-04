#! /usr/bin/env python
# -*- coding: utf-8 -*-
import gobgp_pb2

from netaddr.ip import IPNetwork
from grpc.beta import implementations

from ryu.lib.packet.bgp import IPAddrPrefix
from ryu.lib.packet.bgp import IP6AddrPrefix
from ryu.lib.packet.bgp import BGPPathAttributeNextHop
from ryu.lib.packet.bgp import BGPPathAttributeMpReachNLRI
from ryu.lib.packet.bgp import BGPPathAttributeAs4Path
from ryu.lib.packet.bgp import BGPPathAttributeAsPath
from ryu.lib.packet.bgp import BGPPathAttributeCommunities
from ryu.lib.packet.bgp import BGPPathAttributeOrigin

_TIMEOUT_SECONDS = 10
Resource_GLOBAL  = 0
AFI_IPV6 = 2
SAFI_UNICAST = 1
ORIGIN = 2

class RouteOrinate():
    def modpath(self,gobgpd_addr,originate_path_list):
        channel = implementations.insecure_channel(gobgpd_addr, 50051)
        with gobgp_pb2.beta_create_GobgpApi_stub(channel) as stub:
            paths = []
            for originate_path in originate_path_list:
                pattrs = []
                path = {}
                subnet = IPNetwork(originate_path['route'])
                ver = subnet.version
                addr = subnet.ip
                mask = subnet.prefixlen
                if ver == 4:
                    nlri = IPAddrPrefix(addr=addr, length=mask)
                    nexthop = BGPPathAttributeNextHop(value=originate_path['next_hop'])
                else :
                    nlri = IP6AddrPrefix(addr=addr, length=mask)
                    nexthop = BGPPathAttributeMpReachNLRI(next_hop = originate_path['next_hop'],nlri = [nlri],afi = AFI_IPV6 , safi = SAFI_UNICAST)

                bin_nlri = nlri.serialize()
                bin_nexthop = nexthop.serialize()

                pattrs.append(str(bin_nexthop))

                origin = BGPPathAttributeOrigin(value=ORIGIN)
                bin_origin = origin.serialize()
                pattrs.append(str(bin_origin))

                if originate_path['community'] :
                    community_set = self.community_convert(originate_path['community'])
                    communities = BGPPathAttributeCommunities(communities=community_set)
                    bin_communities = communities.serialize()
                    pattrs.append(str(bin_communities))

                #as_path = BGPPathAttributeAs4Path(value=[[1234,1111]])
                #bin_as_path = as_path.serialize()
                #pattrs.append(str(bin_as_path))

                path['nlri'] = str(bin_nlri)
                path['pattrs'] = pattrs

                paths.append(path)

            args = []
            args.append(gobgp_pb2.ModPathsArguments(resource=Resource_GLOBAL, paths=paths))
            ret = stub.ModPaths(args, _TIMEOUT_SECONDS)

    def community_convert(self,community_list):
        hex_communities = []
        for community in community_list:
            separate_community = community.split(':')
            if separate_community:
                bin_header = int(separate_community[0]) << 16 #左方向に16ビットシフト
                bin_footer = int(separate_community[1])
                hex_community = bin_header | bin_footer #headとfootの論理和を16進数に変換
                hex_communities.append(hex_community)
        return hex_communities