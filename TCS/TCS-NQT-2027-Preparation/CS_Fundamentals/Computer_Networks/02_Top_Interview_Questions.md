# Computer Networks: Top Interview Questions

Here are the most frequently asked Computer Networks questions in technical interviews, especially for TCS NQT.

---

## Question 1: What is the difference between TCP and UDP?
**Answer:**
- **TCP (Transmission Control Protocol)** is a connection-oriented, reliable protocol. It guarantees that packets arrive in the correct order and without errors using acknowledgments and a 3-way handshake. It is slower. Used for HTTP, FTP, and Emails.
- **UDP (User Datagram Protocol)** is a connectionless, unreliable protocol. It just sends packets without checking if they arrived or in what order. It is much faster and has less overhead. Used for live video streaming, voice calls (VoIP), and gaming where occasional data loss is acceptable.

## Question 2: Explain the TCP 3-Way Handshake.
**Answer:**
The 3-way handshake is the process TCP uses to establish a connection before sending data.
1. **Step 1 (SYN):** The client sends a packet with the SYN (Synchronize) flag set to the server to initiate a connection.
2. **Step 2 (SYN-ACK):** The server receives the SYN, allocates resources, and responds with a packet that has both the SYN and ACK (Acknowledge) flags set.
3. **Step 3 (ACK):** The client receives the SYN-ACK, allocates resources, and sends an ACK packet back to the server. The connection is now established.

## Question 3: What happens when you type "google.com" in your browser and press Enter?
**Answer:**
This is a classic interview question. The high-level steps are:
1. **DNS Lookup:** The browser checks its cache for the IP address of google.com. If not found, it asks the OS cache, then the router cache, then the ISP's DNS server until it gets the IP address.
2. **TCP Connection:** The browser initiates a TCP 3-way handshake with the server at that IP address on port 443 (for HTTPS).
3. **SSL/TLS Handshake:** Because it's HTTPS, the browser and server exchange encryption keys to secure the connection.
4. **HTTP Request:** The browser sends an HTTP GET request for the webpage.
5. **Server Response:** The Google server processes the request and sends back an HTTP response containing the HTML content.
6. **Browser Rendering:** The browser parses the HTML, fetches additional assets (CSS, JS, images), and renders the page for the user.

## Question 4: What is the difference between an IP Address and a MAC Address?
**Answer:**
- **MAC Address (Media Access Control):** A physical, hardware address burned into the network card by the manufacturer. It is a 48-bit address (Layer 2). It is used to identify devices on the *same local network*.
- **IP Address (Internet Protocol):** A logical address assigned by the network (router/ISP). It is a 32-bit (IPv4) or 128-bit (IPv6) address (Layer 3). It is used to route data *across different networks* (the internet).

## Question 5: What is the OSI Model? Name its layers.
**Answer:**
The OSI (Open Systems Interconnection) model is a conceptual framework that standardizes the functions of a communication system into 7 distinct categories or layers.
From top to bottom (closest to user to physical wire):
7. **A**pplication Layer (HTTP, FTP)
6. **P**resentation Layer (SSL, Data formatting)
5. **S**ession Layer (Connection management)
4. **T**ransport Layer (TCP, UDP)
3. **N**etwork Layer (IP, Routing)
2. **D**ata Link Layer (MAC addresses, Switches)
1. **P**hysical Layer (Cables, Bits)
*(Mnemonic: All People Seem To Need Data Processing)*

## Question 6: What is a Subnet Mask?
**Answer:**
A subnet mask is a 32-bit number that masks an IP address, dividing the IP address into two parts: the network address and the host address. It helps routers determine whether a destination IP is on the local network or an external network. For example, a common subnet mask is `255.255.255.0`, meaning the first three octets represent the network, and the last octet represents the specific host device.

## Question 7: Differentiate between a Hub, a Switch, and a Router.
**Answer:**
- **Hub (Layer 1):** A dumb device that receives data on one port and broadcasts it blindly to all other ports. Causes a lot of network collisions.
- **Switch (Layer 2):** An intelligent device that learns MAC addresses. It receives data and sends it *only* to the specific port where the destination device is connected.
- **Router (Layer 3):** Connects different networks together (e.g., your home network to the internet). It uses IP addresses to determine the best path to forward packets.

## Question 8: What is HTTP vs HTTPS?
**Answer:**
- **HTTP (HyperText Transfer Protocol):** Transmits data over the internet in plain text. Anyone intercepting the traffic can read it. Uses Port 80.
- **HTTPS (HTTP Secure):** Uses SSL/TLS to encrypt the data before transmitting it. Even if intercepted, the data is unreadable without the decryption key. Uses Port 443.
