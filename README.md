# clammy-ng
The next generation ansible-managed linux router framework using all the trendy new things

## intro

Current device target is a nanopi-r5s running Armbian using a WAN port for internet, and then LAN1 and LAN2 aggregated in a [Router on a stick](https://en.wikipedia.org/wiki/Router_on_a_stick) pattern for east-west traffic.

Desire is to have a robust router config with zone firewall leveraging the following underlying components

*  netplan
*  firewalld
*  dnsmasq
*  frrouting
*  wireguard

## getting started

This repo is meant to be the ansible project directory.. or close to it plus documentation..  Trying to leverage off-the-shelf roles when possible.  Other roles will via the [clammy collection](https://github.com/lanefu/ansible-collection-clammy)

### environment setup

there are better ways, but this way for now...  `.gitignore` has been preconfigured to use namedspace ansible home `~/.clammy-ng-ansible/` and `venv` used in the example.

#### requirements

assume you have python3 and python3-venv installed

```
python3 venv venv
source activate venv/bin/activate
python3 -m pip install requirements.txt
ansible-galaxy install -r requirements.yml
ansible-galaxy install -r requirements-clammy-ng.yml 
```

## order of operations

Naturally there's some sequencing challenges with a router.. especially out of the box.  For now `full.yml` is the POC full sequence of operations.
in reality, this stuff will proably want to be decoupled...  

I think there's going to be a generally need to decouple WAN interface-oriented operations from LAN, including firewall management.

guesses so far:

1. sysctl_base config # interface specific stuff might move this
1. configure wan interface
1. configure lan interfaces
1. configure vpn interfaces
1. configure wan firewall ingress and port forwards
1. configure lan/vpn zones
1. configure wan/vpn zone policies
1. configure DHCP / DNS (dnsmasq)  # what happens if vpn needs DNS to work?
