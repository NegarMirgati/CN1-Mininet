rom mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.node import CPULimitedHost
from time import sleep
net = Mininet(link=TCLink, host=CPULimitedHost) # net is a Mininet() object
h1 = net.addHost( 'h1' ) # h1 is a Host() object
h2 = net.addHost( 'h2' ) # h2 is a Host()
h3 = net.addHost( 'h3' ) # h3 is a Host()
h4 = net.addHost( 'h4' ) # h3 is a Host()
s1 = net.addSwitch( 's1' ) # s1 is a Switch() object
s2 = net.addSwitch( 's2' ) # s1 is a Switch() object
s3 = net.addSwitch( 's3' ) # s1 is a Switch() object
c0 = net.addController( 'c0' ) # c0 is a Controller()
net.addLink( h1, s1, bw=5, delay='5ms' ) # creates a Link() object
net.addLink( h2, s1, bw=5, delay='5ms' )
net.addLink( s1, s2, bw=1, delay='50ms' )
net.addLink( h3, s3, bw=5, delay='5ms' )
net.addLink( h4, s3, bw=5, delay='5ms' )
net.addLink( s3, s2, bw=1, delay='50ms' )
net.start()
h2.cmd( 'python -m SimpleHTTPSERVER 80 &' )
sleep(2)
h1.cmd( 'curl', h2.IP() )
CLI(net)
h2.cmd( 'kill %python' )
net.stop()
