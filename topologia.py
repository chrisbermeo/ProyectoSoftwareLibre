#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
from mininet.util import dumpNodeConnections


def topologia():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='212.18.0.0/24')

    info( '*** Agregar controladores\n' )
    info( '*** Agregar switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch, failMode='standalone')
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch, failMode='standalone')
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch, failMode='standalone')
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch, failMode='standalone')
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch, failMode='standalone')
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch, failMode='standalone')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch, failMode='standalone')

    info( '*** Agregar hosts\n')
    h3 = net.addHost('h3', cls=Host, ip='212.18.0.3', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='212.18.0.6', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='212.18.0.5', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='212.18.0.8', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='212.18.0.2', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='212.18.0.4', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='212.18.0.7', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='212.18.0.1', defaultRoute=None)

