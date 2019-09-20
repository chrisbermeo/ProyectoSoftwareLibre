# ProyectoSoftwareLibre
Creación de topología en Mininet con script en Python

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
//ESTOS SON LOS IMPORTS QUE SE USARON PARA EL DESARROLLO DEL SCRIPT

def topologia(): //CREACION DEL ENCABEZADO CON EL NOMBRE DE LA FUNCIÓN *topologia()* PARA LA CREACIÓN DE LOS HOST, LOS SWITCH Y SUS CONEXIONES 
net = Mininet( topo=None, 
               build=False,
               ipBase='212.18.0.0/24') //USANDO LA IP BASE QUE SE ASIGNARA A LOS HOST
               
    info( '*** Agregar controladores\n' ) //TEXTO INFORMATIVO DE LA AGREGACION DE LOS CONTROLADORES 
    info( '*** Agregar switches\n') //TEXTO INFORMATIVO DE LA AGREGACION DE LOS SWITCHES
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch, failMode='standalone') //*s1* VARIABLE CON LA CUAL SE CREA EL PRIMER SWITCH DE LA TOPOLOGIA
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch, failMode='standalone')
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch, failMode='standalone')
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch, failMode='standalone')
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch, failMode='standalone')
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch, failMode='standalone')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch, failMode='standalone')

    info( '*** Agregar hosts\n')  //TEXTO INFORMATIVO DE LA AGREGACION DE LOS HOST
    h3 = net.addHost('h3', cls=Host, ip='212.18.0.3', defaultRoute=None) //AGREGA UN HOST A LA TOPOLOGIA CON SU DIRECCION IP Y SIN NINGUNA RUTA POR DEFAULT
    h6 = net.addHost('h6', cls=Host, ip='212.18.0.6', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='212.18.0.5', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='212.18.0.8', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='212.18.0.2', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='212.18.0.4', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='212.18.0.7', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='212.18.0.1', defaultRoute=None)
    
    info( '* Agregar conexiones\n')
    bd = {'bw':10,'delay':'5'} //VARIABLE QUE CONTIENE EL VALOR DEL ANCHO DE BANDA Y EL RETARDO DE LOS ENLACES
    net.addLink(h7, s4, cls=TCLink, **bd) //CREACION DE LA CONEXION ENTRE EL HOST 7 *h7* Y EL SWITCH 4 *s4* CON EL VALOR DEL ANCHO DE BANDA Y EL RETARDO
    net.addLink(h8, s4, cls=TCLink, **bd)
    net.addLink(h1, s1, cls=TCLink, **bd)
    net.addLink(h2, s1, cls=TCLink, **bd)
    net.addLink(h3, s2, cls=TCLink, **bd)
    net.addLink(h4, s2, cls=TCLink, **bd)
    net.addLink(s1, s7, cls=TCLink, **bd)
    net.addLink(s2, s7, cls=TCLink, **bd)
    net.addLink(s5, s7, cls=TCLink, **bd)
    net.addLink(s6, s7, cls=TCLink, **bd)
    net.addLink(s3, s5, cls=TCLink, **bd)
    net.addLink(s4, s6, cls=TCLink, **bd)
    net.addLink(h5, s3, cls=TCLink, **bd)
    net.addLink(h6, s3, cls=TCLink, **bd)

    info( '* Iniciando la red\n')
    net.build() //INICIANDO EL FUNCIONAMIENTO DE LA RED 
    info( '* Iniciando los controladores\n')
    for controller in net.controllers:
        controller.start() //INICIANDO EL CONTROLADOR 
        
    info( '* Iniciando los switches\n')
    net.get('s1').start([]) //INICIANDO EL FUNCIONAMIENTO DE LOS SWITCHES
    net.get('s3').start([])
    net.get('s6').start([])
    net.get('s7').start([])
    net.get('s4').start([])
    net.get('s5').start([])
    net.get('s2').start([])

    info( '* Switches y hosts configurados\n')
    dumpNodeConnections( net.hosts ) //FUNCION QUE PERMITE VER LAS CONEXIONES DE LOS HOST
    dumpNodeConnections( net.switches ) //FUNCION QUE PERMITE VER LAS CONEXIONES DE LOS SWITCHES
    net.pingAll() //FUNCION QUE REALIZA PING ENTRE TODOS LOS HOST 
    net.stop() //FUNCION QUE DETIENE LA EJECUCION DE LA TOPOLOGIA 

if _name_ == '_main_':
    setLogLevel( 'info' )
    topologia() 


