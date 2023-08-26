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

This repo is meant to be the ansible project directory.. or close to it plus documentation..  Trying to leverage off-the-shelf roles when possible.  Other roles will via the clammy collection

### environment setup

there are better ways, but this way for now...  `.gitignore` has been preconfigured to hide the `.ansible` home directory and `venv` used in the example.

#### requirements

assume you have python3 and python3-venv installed

```
python3 venv venv
source activate venv/bin/activate
python3 -m pip install requirements.txt
ansible-galaxy install -r requirements.yml
```
