# System Design: Top Interview Questions

Here are the most frequently asked System Design questions in technical interviews. For freshers/juniors (like TCS NQT), the focus is usually on knowing the components (Load Balancers, Caches, DBs) rather than architecting the whole system perfectly.

---

## Question 1: What is the difference between SQL and NoSQL?
**Answer:**
- **SQL (Relational):** Stores data in tables with predefined schemas. Uses Structured Query Language. Good for complex queries and transactional data where ACID properties are essential (e.g., Banking). Vertically scalable.
- **NoSQL (Non-relational):** Stores data in documents, key-value pairs, or graphs. Dynamic schema. Good for unstructured data, hierarchical data, and rapid agile development. Horizontally scalable (e.g., Social Media feeds).

## Question 2: Explain Horizontal vs. Vertical Scaling.
**Answer:**
- **Vertical Scaling (Scale Up):** Adding more CPU/RAM/Disk to an existing server. It's easy but has a hard physical limit and can cause downtime during upgrades.
- **Horizontal Scaling (Scale Out):** Adding more servers to a cluster. Requires a Load Balancer. It is more resilient (no single point of failure) and theoretically infinitely scalable, but harder to manage and implement.

## Question 3: What is a Load Balancer and how does it work?
**Answer:**
A Load Balancer sits between the clients and the backend servers. It accepts incoming network traffic and distributes it across multiple servers to ensure no single server is overwhelmed. If a server goes down, the load balancer redirects traffic to the remaining online servers. Common algorithms include Round Robin and Least Connections.

## Question 4: What is the CAP Theorem?
**Answer:**
The CAP theorem states that a distributed system can only guarantee two out of three characteristics:
1. **Consistency:** All nodes see the same data at the same time.
2. **Availability:** Every request gets a response (success/failure).
3. **Partition Tolerance:** The system works even if network communication fails between nodes.
Since networks will fail (Partition Tolerance is a given), you must choose between Consistency (e.g., relational DBs) and Availability (e.g., Cassandra).

## Question 5: How does Caching work? What is a Cache Miss?
**Answer:**
Caching stores copies of frequently accessed data in high-speed storage (usually RAM, like Redis) to serve future requests faster. 
- A **Cache Hit** occurs when the requested data is found in the cache.
- A **Cache Miss** occurs when the data is not in the cache, forcing the system to fetch it from the primary, slower database and then load it into the cache for next time.

## Question 6: Design a URL Shortener (like bit.ly)
*(High-Level Concept)*
- **Requirements:** Given a long URL, return a short URL. When hitting the short URL, redirect to the long one.
- **Database:** A simple table with `id`, `short_url`, `long_url`.
- **Encoding:** Convert the auto-incrementing `id` from the DB into a Base62 string (a-z, A-Z, 0-9). For example, ID `1000` becomes `g8`.
- **Scaling:** Use a Load Balancer and Multiple API servers. Cache frequently accessed URLs in Redis to prevent DB hits for viral links.

## Question 7: Explain Database Sharding.
**Answer:**
Sharding is a type of database partitioning that separates very large databases into smaller, faster, more easily managed parts called data shards. Each shard is held on a separate database server. For example, you might put users with IDs 1-10000 on Database A, and users 10001-20000 on Database B. It allows horizontal scaling of databases.

## Question 8: What is a Content Delivery Network (CDN)?
**Answer:**
A CDN is a geographically distributed network of proxy servers and their data centers. The goal is to provide high availability and high performance by distributing the service spatially relative to end-users. They are primarily used to cache static assets like Images, Videos, HTML, CSS, and JS files closer to the user (e.g., Cloudflare, AWS CloudFront).
