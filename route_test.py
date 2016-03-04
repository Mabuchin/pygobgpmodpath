#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import route_originater

##Define Target Host IP
HOST_PEER = "172.16.55.86"

##Define BGPCommunity
#route-type community
PEER = "64540:7"
#Control's community
BLACKHOLE = "64540:666"

#gobgp2
def peer_routeoriginate():
	modpaths = []
	NEXTHOP = "10.10.10.1"
	NEXTHOP6 = "fd00:260:10::1"

	modpaths.append({
		"route":"192.168.1.0/24" ,
		"next_hop": NEXTHOP,
		"community":[]
	})

	modpaths.append({
		"route":"0.0.0.0/0" ,
		"next_hop":NEXTHOP ,
		"community":[]
	})

	modpaths.append({
		"route":"172.16.1.0/24" ,
		"next_hop":NEXTHOP ,
		"community":[]
	})

	modpaths.append({
		"route":"192.168.1.100/32" ,
		"next_hop":NEXTHOP ,
		"community":[]
	})

	modpaths.append({
		"route":"192.168.5.0/24" ,
		"next_hop":NEXTHOP ,
		"community":[]
	})

	modpaths.append({
		"route":"192.168.107.0/24" ,
		"next_hop":NEXTHOP ,
		"community":[]
	})

	modpaths.append({
		"route":"192.168.101.0/24" ,
		"next_hop":NEXTHOP ,
		"community":[]
	})

	modpaths.append({
		"route":"fd00:192:1::/48" ,
		"next_hop":NEXTHOP6 ,
		"community":[]
	})

	modpaths.append({
		"route":"::/0" ,
		"next_hop":NEXTHOP6 ,
		"community":[]
	})

	modpaths.append({
		"route":"fd00:192:5::/48" ,
		"next_hop":NEXTHOP6 ,
		"community":[]
	})

	modpaths.append({
		"route":"fd00:192:1::100/128" ,
		"next_hop":NEXTHOP6 ,
		"community":[]
	})

	modpaths.append({
		"route":"fd00:192:101::/48" ,
		"next_hop":NEXTHOP6 ,
		"community":[]
	})
	routemod = route_originater.RouteOrinate()
	routemod.modpath(HOST,modpaths)

if __name__ == '__main__':
	peer_routeoriginate()
