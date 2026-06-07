# System Design - Extended TCS NQT Interview Questions (Part 2)

Further system design concepts focusing on APIs, microservices, and high availability.

---

## 9. What are Microservices? How do they differ from a Monolithic Architecture?
**Answer:**
- **Monolith:** The entire application (UI, business logic, data access) is built and deployed as a single, indivisible unit. Simple to develop initially, but scales poorly and becomes a nightmare to maintain as it grows.
- **Microservices:** The application is broken down into small, independent services based on business capabilities (e.g., User Service, Payment Service, Inventory Service). They communicate via APIs. They can be scaled independently, written in different languages, and deployed without affecting the whole system.

## 10. What is a REST API? Explain its core principles.
**Answer:**
REST (Representational State Transfer) is an architectural style for designing networked applications. APIs that follow these principles are RESTful.
**Core Principles:**
1. **Client-Server Separation:** The client handles UI; the server handles data storage.
2. **Statelessness:** Each request from client to server must contain all information needed to understand the request. The server does not store client state between requests.
3. **Cacheability:** Responses must define themselves as cacheable or not to improve performance.
4. **Uniform Interface:** Standard HTTP methods (GET, POST, PUT, DELETE) are used on standardized endpoints (e.g., `GET /users/123`).

## 11. What is Rate Limiting? Why is it necessary?
**Answer:**
Rate limiting restricts the number of requests a client can make to an API within a specified time window (e.g., 100 requests per minute).
**Necessity:**
- Prevents Denial of Service (DoS) attacks and brute-force password cracking.
- Prevents abuse by scrapers or rogue scripts.
- Ensures fair usage and high availability for all users.
- Controls infrastructure costs.

## 12. Explain the difference between Long Polling, WebSockets, and Server-Sent Events (SSE).
**Answer:**
These are techniques for real-time communication.
- **Long Polling:** The client requests data. The server holds the connection open until it has new data, sends it, and the connection closes. The client immediately opens a new one. (Heavy overhead).
- **WebSockets:** Establishes a persistent, full-duplex (two-way) connection. Both the client and server can send messages to each other at any time instantly. Best for chat apps or multiplayer games.
- **SSE:** A persistent connection where only the server can push updates to the client (one-way). Best for live stock tickers or news feeds.

## 13. What is a Reverse Proxy?
**Answer:**
While a standard proxy sits in front of *clients* to hide them from the internet, a **Reverse Proxy** sits in front of *web servers* to hide them from clients. It intercepts incoming requests and forwards them to the appropriate backend server.
Benefits: Load balancing, SSL termination, caching static content, and hiding internal server IP addresses for security (e.g., NGINX).

## 14. What is the difference between SQL and NoSQL Scaling?
**Answer:**
- **SQL Scaling:** Typically designed to scale **vertically** (adding a bigger CPU/RAM to a single machine). Horizontal scaling (sharding) is possible but highly complex because maintaining ACID properties and handling joins across multiple machines is difficult.
- **NoSQL Scaling:** Designed from the ground up to scale **horizontally**. Data is easily partitioned across hundreds of cheap commodity servers. They achieve this by sacrificing strict consistency for eventual consistency (CAP Theorem).

## 15. What does "Eventual Consistency" mean?
**Answer:**
In distributed systems, eventual consistency means that if no new updates are made to a given piece of data, eventually all accesses to that item will return the last updated value.
For example, if you update your Facebook profile picture, the server in the US updates instantly. The server in India might show the old picture for a few seconds before the data replicates. It sacrifices immediate consistency for high availability.
