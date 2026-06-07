# Computer Networks: Crash Course

Computer Networks is a core CS subject that deals with how computers communicate with each other over a network. For TCS NQT and technical interviews, you must be very comfortable with the OSI Model, TCP/IP, and various protocols.

---

## 1. The OSI Model (Open Systems Interconnection)

The OSI model is a conceptual framework used to understand and standardize how different network protocols interact. It consists of 7 layers. A great mnemonic to remember from top to bottom is: **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing.

### Layer 7: Application Layer
- The interface between the user application and the network.
- **Protocols:** HTTP, HTTPS, FTP, SMTP, DNS, POP3.
- **Data Unit:** Data / Message.

### Layer 6: Presentation Layer
- Formats, encrypts, and compresses data so the application layer can accept it.
- **Protocols:** SSL/TLS, JPEG, ASCII.
- **Data Unit:** Data.

### Layer 5: Session Layer
- Establishes, manages, and terminates connections (sessions) between applications.
- **Protocols:** NetBIOS, PPTP.
- **Data Unit:** Data.

### Layer 4: Transport Layer
- Ensures complete and reliable delivery of data. Handles flow control and error recovery.
- **Protocols:** TCP (Transmission Control Protocol), UDP (User Datagram Protocol).
- **Data Unit:** Segment (TCP) / Datagram (UDP).
- **Hardware:** Load Balancers, Firewalls.

### Layer 3: Network Layer
- Determines the best physical path for the data to travel (Routing) and handles logical addressing (IP addresses).
- **Protocols:** IPv4, IPv6, ICMP (used by Ping), ARP.
- **Data Unit:** Packet.
- **Hardware:** Routers.

### Layer 2: Data Link Layer
- Provides node-to-node data transfer and handles physical addressing (MAC addresses). Also does error detection (using Checksums/CRC).
- **Protocols:** Ethernet, Wi-Fi (802.11), PPP.
- **Data Unit:** Frame.
- **Hardware:** Switches, Bridges.

### Layer 1: Physical Layer
- The physical cable or wireless connection between network nodes. Transmits raw bit streams.
- **Protocols:** USB, Bluetooth, Ethernet physical layer.
- **Data Unit:** Bit.
- **Hardware:** Cables, Hubs, Repeaters.

---

## 2. TCP vs. UDP

The Transport layer is primarily governed by these two protocols.

| Feature | TCP (Transmission Control Protocol) | UDP (User Datagram Protocol) |
| :--- | :--- | :--- |
| **Connection** | Connection-oriented (requires 3-way handshake) | Connectionless (just sends data) |
| **Reliability** | Highly reliable. Guarantees delivery. | Unreliable. No guarantee. |
| **Speed** | Slower (due to error checking & overhead) | Very Fast |
| **Order** | Packets are delivered in a specific order | Packets arrive in any order |
| **Use Cases** | Web Browsing (HTTP), Email (SMTP), File Transfer (FTP) | Video Streaming, Online Gaming, VoIP, DNS |

### The TCP 3-Way Handshake
Before sending data, TCP establishes a connection:
1. **SYN:** Client sends a SYN (synchronize) packet to the server.
2. **SYN-ACK:** Server receives it and replies with a SYN-ACK (synchronize-acknowledge).
3. **ACK:** Client receives the SYN-ACK and replies with an ACK (acknowledge). Connection is established.

---

## 3. Important Network Protocols & Ports

You should memorize these common default ports:
- **HTTP:** 80 (Unencrypted Web)
- **HTTPS:** 443 (Encrypted Web)
- **FTP:** 20/21 (File Transfer)
- **SSH:** 22 (Secure Shell)
- **SMTP:** 25 (Sending Emails)
- **DNS:** 53 (Domain Name System)

---

## 4. IP Addresses & MAC Addresses

- **IP Address (Logical Address):** Assigned by the network. Can change. Identifies the connection of a device to the internet. (e.g., IPv4 `192.168.1.5` is 32-bit; IPv6 is 128-bit).
- **MAC Address (Physical Address):** Hardcoded into the Network Interface Card (NIC) by the manufacturer. Never changes. Used within a local network (Layer 2). It is a 48-bit address (e.g., `00:1A:2B:3C:4D:5E`).

---

## 5. DNS (Domain Name System)
DNS is the phonebook of the internet. Humans access information online through domain names, like `google.com`. Web browsers interact through IP addresses. DNS translates domain names to IP addresses so browsers can load internet resources.
