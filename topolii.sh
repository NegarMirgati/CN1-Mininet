ip netns add h1
ip netns add h2
ip netns add h3
ip netns add h4

ovs-vsctl add-br s1
ovs-vsctl add-br s2
ovs-vsctl add-br s3

ip link add h1-eth0 type veth peer name s1-eth1
ip link add h2-eth0 type veth peer name s1-eth2
ip link add s1-eth3 type veth peer name s2-eth1
ip link add h3-eth0 type veth peer name s3-eth1
ip link add h4-eth0 type veth peer name s3-eth2
ip link add s3-eth3 type veth peer name s2-eth2

ip link set h1-eth0 netns h1
ip link set h2-eth0 netns h2
ip link set h3-eth0 netns h3
ip link set h4-eth0 netns h4

ovs-vsctl add-port s1 s1-eth1
ovs-vsctl add-port s1 s1-eth2
ovs-vsctl add-port s1 s1-eth3
ovs-vsctl add-port s2 s2-eth1
ovs-vsctl add-port s2 s2-eth2
ovs-vsctl add-port s3 s3-eth1
ovs-vsctl add-port s3 s3-eth2
ovs-vsctl add-port s3 se-eth3


ovs-vsctl set-controller s1 tcp:127.0.0.1
ovs-vsctl set-controller s2 tcp:127.0.0.1
ovs-vsctl set-controller s3 tcp:127.0.0.1

ip netns exec h1 ifconfig h1-eth0 10.0.0.1
ip netns exec h1 ifconfig lo up
ip netns exec h2 ifconfig h2-eth0 10.0.0.2
ip netns exec h2 ifconfig lo up
ip netns exec h3 ifconfig h3-eth0 10.0.0.3
ip netns exec h3 ifconfig lo up
ip netns exec h4 ifconfig h4-eth0 10.0.0.4
ip netns exec h4 ifconfig lo up

ifconfig s1-eth1 up
ifconfig s1-eth2 up
ifconfig s1-eth3 up
ifconfig s2-eth1 up
ifconfig s2-eth2 up
ifconfig s3-eth1 up
ifconfig s3-eth2 up
ifconfig s3-eth3 up

ip netns exec h1 ping -c1 10.0.0.3




