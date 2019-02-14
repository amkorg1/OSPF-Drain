<H1># OSPF-Drain</H1>
<strong>Synopsis : </strong>
In a production environment we may require draining traffic away from a particular device to undertake maintenance on that device and undrain traffic to return to before.
In OSPF network - For maintenance, we can divert traffic by automating drainage of a router and then resume traffic after completion
This can be implemented in GNS as done here or on real routers in network, in the same way.

<strong>Here I have implemented the same idea in an OSPF network.</strong>

<strong>Links : </strong>
Host C1 – Switch     -f2/0   -R1
			  – f2/0       -R2
			  – f2/0       -R3
			  – f2/0       -R4

<strong> IP-Addresses : </strong>
<p>R1 – 'ip':'198.51.100.21'</p>
<p>R2 – 'ip':'198.51.100.22'</p>
<p>R3 – 'ip':'198.51.100.23'</p>
<p>R4 - 'ip':'198.51.100.24'</p>

For interfaces we have taken 192.161.x.x/24 network 
All interfaces have been advertised in OSPF.
And are reachable.

<strong>USAGE:</strong>
After you run the script you can choose to drain R2 or R3,post-that you must choose undrain to see results before you choose for the second time.

<strong>UNDRAIN</strong>
This resumes the traffic direction as it was before with all the interfaces back to equal cost.
When we undrain traffic on all devices, 
Traceroute to both R1 interfaces from R4 show different paths.
This should probably be chosen as first option to try and see the direction of traffic.

Traceroute to R1-f0/0 interface goes through R2 
Traceroute to R1-f1/0 does through R3

<strong>DRAIN R3</strong>

After we drain R3, 
<p>Traffic will move from R2 </p>
<p>Before - Traceroute to both R1 interfaces from R4 show different hops,</p>
<p>1st traceroute hop at R2 </p>
<p>2nd traceroute hop at R1</p>
<p>After - Traceroute from R4 show to both R1 interfaces, hop at R2 then R1</p>


<strong>DRAIN R2</strong>

<p>After we drain, R2</p>
<p>Traffic will move from R3</p>
<p>Before - Traceroute to both R1 interfaces from R4 show different hops,</p>
<p>1st traceroute hop at R2 </p>
<p>2nd traceroute hop at R1</p>
<p>After - Traceroute to both R1 interfaces from R4 show, hope at R3 then R1.</p>

<strong><p>Assumptions and future improvements –</srong> 
<p>Traceroute will always be done from a host on R4 –.</p>

Currently I have written different scripts for -
<p>Undrain
<p>Drain R3</p>
<p>Drain R2</p>

<p>I created different scripts, have to merge into 1 script which provides options for user to choose.<p>
	<p> Final.py does that job </p>

