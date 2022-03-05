import csv

#CLEANS UP STRING INPUT

def line_clean_up(x):
    x = x.split("\n")
    non_empty_lines = [line for line in x if line.strip() != ""]
    new_list = []
    for line in non_empty_lines:
        line = line.strip()
        new_list.append(line)
    return new_list

#BREAKS STRING INTO LISTS AND DEFINES DIC KEY/VALUE PAIRS
def interface_default(list):
    int_default = {}
    for line in list:
        data = line.split(":", 1)
        key = data[0].strip()
        value = data[1].strip()
        if len(value) == 0:
            value = "NULL"
        else:
            value = value
        int_default[key] = value
    return int_default

#FORTIOS DEFAULT INTEFACE "SHOW SYSTEM INTERFACE" OUTPUT
string = """
name                : 
vdom                : 
vrf                 : 0
cli-conn-status     : 0
mode                : static 
dhcp-relay-interface-select-method: auto 
dhcp-relay-service  : disable 
ip                  : 0.0.0.0 0.0.0.0
allowaccess         : 
fail-detect         : disable 
pptp-client         : disable 
arpforward          : enable 
broadcast-forward   : disable 
bfd                 : global 
l2forward           : disable 
icmp-send-redirect  : enable 
icmp-accept-redirect: enable 
vlanforward         : disable 
stpforward          : disable 
ips-sniffer-mode    : disable 
ident-accept        : disable 
ipmac               : disable 
subst               : disable 
substitute-dst-mac  : 00:00:00:00:00:00
status              : up 
netbios-forward     : disable 
wins-ip             : 0.0.0.0
type                : vlan
netflow-sampler     : disable 
sflow-sampler       : disable 
src-check           : enable 
sample-rate         : 2000
polling-interval    : 20
sample-direction    : both 
explicit-web-proxy  : disable 
explicit-ftp-proxy  : disable 
proxy-captive-portal: disable 
tcp-mss             : 0
inbandwidth         : 0
outbandwidth        : 0
egress-shaping-profile: 
ingress-shaping-profile: 
weight              : 0
external            : disable 
vlan-protocol       : 8021q 
trunk               : disable 
devindex            : 0
description         : 
alias               : 
l2tp-client         : disable 
security-mode       : none 
device-identification: enable 
device-user-identification: enable 
estimated-upstream-bandwidth: 0
estimated-downstream-bandwidth: 0
measured-upstream-bandwidth: 0
measured-downstream-bandwidth: 0
bandwidth-measure-time: 
monitor-bandwidth   : disable 
vrrp-virtual-mac    : disable 
vrrp:
role                : lan 
snmp-index          : 59
secondary-IP        : disable 
preserve-session-route: disable 
auto-auth-extension-device: disable 
ap-discover         : enable 
ip-managed-by-fortiipam: disable 
switch-controller-igmp-snooping-proxy: disable 
switch-controller-igmp-snooping-fast-leave: disable 
switch-controller-feature: none 
swc-vlan            : 0
color               : 0
tagging:
ipv6:
    ip6-mode            : static 
    nd-mode             : basic 
    ip6-address         : ::/0
    ip6-allowaccess     : 
    icmp6-send-redirect : enable 
    ra-send-mtu         : enable 
    ip6-reachable-time  : 0
    ip6-retrans-time    : 0
    ip6-hop-limit       : 0
    dhcp6-prefix-delegation: disable
delegated-DNS1      : ::
delegated-DNS2      : ::
delegated-domain          : 
    dhcp6-information-request: disable 
    cli-conn6-status    : 0
    vrrp-virtual-mac6   : disable 
    vrip6_link_local    : ::
    ip6-send-adv        : disable 
    autoconf            : disable
prefix      : ::/0
preferred-life-time         : 0
valid-life-time     : 0
    dhcp6-relay-service : disable 
client-options:
priority            : 0
dhcp-relay-request-all-server: disable 
dhcp-client-identifier: 
dhcp-renew-time     : 0
idle-timeout        : 0
detected-peer-mtu   : 0
disc-retry-timeout  : 1
padt-retry-timeout  : 1
dns-server-override : enable
Acquired DNS1       : 0.0.0.0
Acquired DNS2       : 0.0.0.0
mtu-override        : disable 
wccp                : disable 
drop-overlapped-fragment: disable 
drop-fragment       : disable 
interface           : 
vlanid              : 0
"""

#CLEANS TEXT
default = line_clean_up(string)

#DICT LOOP TO CSV - CHANGE NAME IF REQUIRED
with open('default_interface.csv', 'w') as f:
    for key in interface_default(default).keys():
        f.write("%s,%s\n"%(key,interface_default(default)[key]))
