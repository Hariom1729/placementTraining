# Computer Networks - TCS NQT Last 5 Years PYQs

These are the top repeated CN questions in TCS technical interviews.

---

## 1. What is the OSI Model? Explain the functions of the Data Link Layer and Network Layer.
**Answer:**
The OSI model is a 7-layer conceptual framework for network communication.
- **Data Link Layer (Layer 2):** Responsible for node-to-node delivery of data on the same network. It handles physical addressing (MAC addresses), error detection (using Checksums), and flow control. Uses Switches. Data unit is a Frame.
- **Network Layer (Layer 3):** Responsible for routing packets across different networks from source to destination. It handles logical addressing (IP addresses). Uses Routers. Data unit is a Packet.

## 2. What happens exactly when you type a URL in the browser?
**Answer:** *(Very frequent question)*
1. **DNS Resolution:** The browser resolves the domain name (google.com) to an IP address using caches (browser, OS, router) or by querying DNS servers.
2. **TCP Connection:** The browser establishes a connection with the server via the TCP 3-way handshake (SYN, SYN-ACK, ACK).
3. **SSL/TLS Handshake:** If using HTTPS, encryption keys are exchanged.
4. **HTTP Request:** The browser sends a GET request.
5. **Server Response:** The server responds with the HTML content.
6. **Rendering:** The browser parses the HTML and renders the DOM.

## 3. Differentiate between TCP and UDP. Which one does Video Streaming use and why?
**Answer:**
- **TCP (Transmission Control Protocol):** Connection-oriented, reliable, guarantees order, performs error checking and retransmission. Slower. (HTTP, Emails).
- **UDP (User Datagram Protocol):** Connectionless, unreliable, no order guarantee, no retransmission. Very fast.
- **Video Streaming** uses **UDP**. In live video, speed is critical. If a few frames drop (data loss), the video might glitch for a millisecond, which is acceptable. Waiting for TCP to retransmit lost packets would cause the video to constantly pause and buffer.

## 4. What is a MAC address and how is it different from an IP address?
**Answer:**
- **MAC Address:** A 48-bit physical address burned into the Network Interface Card (NIC). It is permanent. It operates at Layer 2 and is used to find devices on the *local* network. Example: `00-B0-D0-63-C2-26`.
- **IP Address:** A 32-bit (IPv4) or 128-bit (IPv6) logical address assigned by the router/ISP. It changes based on the network you join. Operates at Layer 3 and is used to route traffic across the *internet*. Example: `192.168.1.5`.

## 5. What are the common Port Numbers you should know?
**Answer:**
- FTP (File Transfer): 20, 21
- SSH (Secure Shell): 22
- SMTP (Email sending): 25
- DNS (Domain Name System): 53
- HTTP (Web): 80
- HTTPS (Secure Web): 443

## 6. What is DNS?
**Answer:**
DNS (Domain Name System) is the "phonebook" of the internet. Humans remember website names like `amazon.com`, but computers communicate using numbers (IP addresses). DNS translates the human-readable domain names into IP addresses so browsers can load internet resources.

## 7. What is the difference between a Router and a Switch?
**Answer:**
- **Switch:** Operates at Layer 2 (Data Link). Connects devices within the *same* local area network (LAN). It uses MAC addresses to forward data only to the specific intended device.
- **Router:** Operates at Layer 3 (Network). Connects *different* networks together (e.g., your home LAN to the internet). It uses IP addresses to determine the best path to route packets.

## 8. What is DHCP?
**Answer:**
DHCP (Dynamic Host Configuration Protocol) is a network management protocol used to automatically assign an IP address and other network configuration parameters to a device when it joins a network, so the user doesn't have to configure IP addresses manually.

## 9. Explain the concept of Subnetting.
**Answer:**
Subnetting is the practice of dividing a single large network into multiple smaller, manageable, and secure logical sub-networks (subnets). It improves network performance by reducing broadcast traffic and provides better security by isolating network segments.

## 10. What is ARP?
**Answer:**
ARP (Address Resolution Protocol) is used to map a known logical IP address to an unknown physical MAC address on a local network. When a device knows the IP of the destination but not the MAC, it broadcasts an ARP request saying "Who has this IP?" The device with that IP replies with its MAC address.
