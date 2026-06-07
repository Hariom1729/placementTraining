# Computer Networks - Extended TCS NQT Interview Questions (Part 2)

Deep dive into advanced networking concepts frequently tested.

---

## 11. What is the difference between IPv4 and IPv6?
**Answer:**
- **IPv4:** Uses 32-bit addresses, allowing for approximately 4.3 billion unique IP addresses. Written in decimal format separated by dots (e.g., `192.168.1.1`).
- **IPv6:** Developed because IPv4 addresses were running out. Uses 128-bit addresses, allowing for a practically infinite number of unique IPs ($3.4 \times 10^{38}$). Written in hexadecimal format separated by colons (e.g., `2001:0db8:85a3:0000:0000:8a2e:0370:7334`).

## 12. What is a Default Gateway?
**Answer:**
A default gateway is the node (usually a router) on a computer network that serves as the forwarding host to other networks when no other route specification matches the destination IP address. If a computer wants to send data to an IP outside its local subnet, it sends the data to the default gateway, which then routes it to the internet.

## 13. What is NAT (Network Address Translation)?
**Answer:**
NAT is a process used by routers to translate private IP addresses (used within a local network) to a single public IP address (used on the internet), and vice versa. It allows multiple devices on a local network to share a single public IP address, conserving the limited pool of IPv4 addresses and adding a layer of security.

## 14. Explain the difference between HTTP GET and POST methods.
**Answer:**
- **GET:** Requests data from a specified resource. Parameters are appended to the URL. Should not be used when dealing with sensitive data. Can be cached and bookmarked. Limited length.
- **POST:** Submits data to be processed to a specified resource. Data is included in the body of the HTTP request, not the URL. More secure for sensitive data (like passwords). Cannot be cached or bookmarked. No length limit.

## 15. What is a Firewall?
**Answer:**
A firewall is a network security device (hardware or software) that monitors and filters incoming and outgoing network traffic based on an organization's previously established security policies. It essentially acts as a barrier between a trusted internal network and untrusted external networks (like the internet).

## 16. What is the purpose of the Transport Layer?
**Answer:**
The Transport Layer (Layer 4) is responsible for end-to-end communication over a network. It provides logical communication between application processes running on different hosts. Its key duties include:
- Multiplexing/Demultiplexing (using Port Numbers).
- Segmentation and Reassembly of data.
- Connection Control (TCP vs UDP).
- Flow Control (preventing a fast sender from overwhelming a slow receiver).
- Error Control (detecting and retransmitting lost packets).

## 17. What is a Ping and how does it work?
**Answer:**
Ping is a command-line utility used to test the reachability of a host on an IP network and to measure the round-trip time for messages. It works by sending ICMP (Internet Control Message Protocol) Echo Request packets to the target host and waiting for an ICMP Echo Reply.

## 18. What is the difference between Static Routing and Dynamic Routing?
**Answer:**
- **Static Routing:** Routes are manually configured by a network administrator. It is simple and secure but doesn't adapt to network changes or failures automatically. Good for small networks.
- **Dynamic Routing:** Routers use routing protocols (like OSPF, BGP) to automatically discover the network topology and calculate the best paths. If a link goes down, the routers automatically find a new path. Essential for large networks like the internet.

## 19. What is a Proxy Server?
**Answer:**
A proxy server is an intermediary server that sits between a client and the internet. When a client requests a resource, the request goes to the proxy server first. The proxy evaluates the request, fetches the resource on behalf of the client, and returns it. It is used for anonymity, security, caching, and bypassing geo-restrictions.

## 20. What is a VPN (Virtual Private Network)?
**Answer:**
A VPN establishes a secure, encrypted connection (a "tunnel") over a less secure network (the internet). It encrypts all data traffic and masks the user's IP address, providing privacy and allowing remote users to securely access internal corporate networks as if they were directly connected.
