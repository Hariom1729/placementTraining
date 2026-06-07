# System Design: Comprehensive Crash Course

System Design is the process of defining the architecture, components, modules, interfaces, and data for a system to satisfy specified requirements. In interviews, it tests your ability to build scalable, highly available, and performant systems.

---

## 1. Core Concepts of System Design

### 1.1 Scalability
Scalability is the capability of a system to handle a growing amount of work, or its potential to be enlarged to accommodate that growth.
- **Vertical Scaling (Scaling Up):** Adding more power (CPU, RAM) to an existing machine. Limited by the maximum capacity of a single machine.
- **Horizontal Scaling (Scaling Out):** Adding more machines into your pool of resources. This is the preferred method for modern distributed systems.

### 1.2 Availability & Reliability
- **Reliability:** The probability a system will fail in a given period. "Does it work correctly?"
- **Availability:** The percentage of time a system remains operational. "Is it up right now?" (Measured in "Nines" - e.g., 99.999% availability).

### 1.3 Latency & Throughput
- **Latency:** The time required to perform some action or to produce some result (e.g., time taken for a packet to travel from client to server).
- **Throughput:** The number of such actions executed or results produced per unit of time (e.g., requests per second).

---

## 2. Key Components of Distributed Systems

### 2.1 Load Balancers
A Load Balancer distributes incoming network traffic across a group of backend servers. This ensures no single server bears too much demand, improving overall responsiveness and availability.
- **Types:** Hardware vs. Software (e.g., NGINX, HAProxy).
- **Algorithms:** Round Robin, Least Connections, IP Hash.

### 2.2 Caching
Caches take advantage of the locality of reference principle: recently requested data is likely to be requested again. Caching heavily reduces latency and database load.
- **Where to Cache:** Client, CDN (Content Delivery Network), Web Server, Database.
- **Cache Eviction Policies:** LRU (Least Recently Used), LFU (Least Frequently Used), FIFO.
- **Popular Technologies:** Redis, Memcached.

### 2.3 Databases
Choosing the right database is crucial in system design.
- **Relational Databases (SQL):** MySQL, PostgreSQL. Best for structured data, ACID compliance (Atomicity, Consistency, Isolation, Durability), and complex queries.
- **Non-Relational (NoSQL):** MongoDB (Document), Cassandra (Column-Family), Neo4j (Graph). Best for unstructured data, high write throughput, and horizontal scalability.

### 2.4 Database Scaling Strategies
- **Replication:** Master-Slave replication. Master handles writes; Slaves handle reads.
- **Sharding (Data Partitioning):** Distributing a single database across multiple machines based on a shard key (e.g., user ID).
- **Federation:** Splitting up databases by function (e.g., Forum DB, Users DB).

### 2.5 Message Queues
Message queues receive, hold, and deliver messages. They decouple heavy, asynchronous processing from the main application flow.
- **Use Cases:** Sending emails, video processing, background jobs.
- **Technologies:** Kafka, RabbitMQ, Amazon SQS.

---

## 3. The CAP Theorem
The CAP theorem states that it is impossible for a distributed data store to simultaneously provide more than two out of the following three guarantees:
- **Consistency:** Every read receives the most recent write or an error.
- **Availability:** Every request receives a (non-error) response, without the guarantee that it contains the most recent write.
- **Partition Tolerance:** The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes.
*In the real world, network partitions (P) are unavoidable, so you must choose between Consistency (C) and Availability (A) - resulting in CP or AP systems.*

---

## 4. Standard System Design Interview Framework
When asked a system design question, follow these steps:
1. **Requirements Clarification:** Understand the exact scope. (Functional: What it does. Non-Functional: Scale, latency, availability).
2. **Back-of-the-Envelope Estimation:** Estimate traffic (QPS), storage, and bandwidth.
3. **High-Level Design:** Draw the core components (Client -> Load Balancer -> Web Servers -> Database).
4. **Detailed Design:** Deep dive into specific components, database schemas, and APIs.
5. **Identify and Resolve Bottlenecks:** Discuss single points of failure, scalability limits, and how caching/sharding can help.
