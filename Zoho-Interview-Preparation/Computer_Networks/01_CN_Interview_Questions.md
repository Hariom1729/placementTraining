# Computer Networks (CN)

## 1. The OSI Model
**1. What are the 7 layers of the OSI model? (Please Do Not Throw Sausage Pizza Away)**
1. **Physical:** Transmission of raw bit stream over a physical medium (Hubs, Cables).
2. **Data Link:** Node-to-node data transfer, error detection (MAC Addresses, Switches).
3. **Network:** Routing packets across multiple networks (IP Addresses, Routers).
4. **Transport:** End-to-end communication, reliability (TCP, UDP, Port numbers).
5. **Session:** Establishing, managing, and terminating sessions.
6. **Presentation:** Data formatting, encryption, compression.
7. **Application:** Network applications (HTTP, FTP, SMTP).

## 2. TCP/IP and Protocols
**2. TCP vs UDP?**
- **TCP (Transmission Control Protocol):** Connection-oriented, reliable, guarantees delivery (acknowledgments), ordered packets, slower. Used in Web browsing (HTTP), Emails (SMTP), File transfer (FTP).
- **UDP (User Datagram Protocol):** Connectionless, unreliable, no guarantee of delivery or order, very fast. Used in Video streaming, VoIP, Online Gaming, DNS.

**3. What is the TCP 3-Way Handshake?**
Used to establish a reliable connection.
1. **SYN:** Client sends SYN (synchronize) packet to server.
2. **SYN-ACK:** Server receives SYN, replies with SYN and ACK (acknowledgment).
3. **ACK:** Client receives SYN-ACK, replies with ACK. Connection established.

**4. What is DNS (Domain Name System)?**
The phonebook of the internet. Translates human-readable domain names (www.google.com) into machine-readable IP addresses (142.250.190.46). Uses UDP port 53.

## 3. Web Technologies
**5. HTTP vs HTTPS?**
- **HTTP:** HyperText Transfer Protocol. Sends data as plain text. Port 80.
- **HTTPS:** HTTP Secure. Encrypts data using TLS/SSL before transmission. Port 443. Protects against Man-In-The-Middle (MITM) attacks.

**6. HTTP Methods?**
- `GET`: Retrieve data. Data appended to URL. Idempotent.
- `POST`: Submit data. Data in body. Not idempotent.
- `PUT`: Update existing data completely.
- `DELETE`: Remove data.

**7. What are Sockets?**
An endpoint for sending or receiving data across a computer network. Defined by an IP Address and a Port Number (e.g., `192.168.1.5:8080`).

## 4. Networking Devices & Concepts
**8. MAC Address vs IP Address?**
- **MAC Address:** Physical address burned into the Network Interface Card (NIC). Operates at Data Link Layer. Flat addressing space.
- **IP Address:** Logical address assigned by ISP or router. Operates at Network Layer. Hierarchical addressing space.

**9. What is ARP (Address Resolution Protocol)?**
Resolves an IP address to a MAC address. (Broadcasting a message: "Who has IP 192.168.1.10? Tell 192.168.1.5", and getting a unicast reply with the MAC).

**10. NAT (Network Address Translation)?**
A method routers use to map multiple private, local IP addresses to a single public IP address before sending data to the internet. Saves IPv4 addresses.

## 5. Network Security
**11. What is a Firewall?**
A network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules.

**12. Symmetric vs Asymmetric Encryption?**
- **Symmetric:** Uses the same key for both encryption and decryption (Faster, e.g., AES).
- **Asymmetric:** Uses a Public Key for encryption and a Private Key for decryption (Slower but highly secure, e.g., RSA). HTTPS uses Asymmetric encryption to securely exchange a Symmetric key, which is then used for the session.
