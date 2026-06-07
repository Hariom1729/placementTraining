# Operating Systems: Crash Course

An Operating System (OS) is system software that manages computer hardware, software resources, and provides common services for computer programs.

---

## 1. Process Management

### 1.1 Process vs. Thread
- **Process:** A program in execution. It has its own independent memory space (code, data, heap, stack). Because memory is isolated, processes cannot easily corrupt each other, but communicating between them (IPC) is slow and heavy.
- **Thread:** A "lightweight process". Multiple threads exist within a single process and share the same memory space (code, data, heap) but have their own individual stacks and registers. Context switching between threads is much faster, but one rogue thread can crash the entire process.

### 1.2 Process States
1. **New:** The process is being created.
2. **Ready:** The process is waiting to be assigned to a processor.
3. **Running:** Instructions are being executed.
4. **Waiting (Blocked):** The process is waiting for some event to occur (e.g., I/O completion).
5. **Terminated:** The process has finished execution.

### 1.3 CPU Scheduling Algorithms
The OS decides which process in the "Ready" queue gets the CPU next.
- **FCFS (First Come First Serve):** Simple, but causes the "Convoy Effect" (short processes wait behind a long one).
- **SJF (Shortest Job First):** Optimal for minimizing average wait time, but impossible to know exact execution times in advance.
- **Round Robin (RR):** Each process gets a small unit of CPU time (time quantum). Excellent for interactive/time-sharing systems.

---

## 2. Concurrency & Synchronization

When multiple threads access shared data, it can lead to data inconsistency (Race Conditions). Synchronization mechanisms solve this.

### 2.1 Critical Section
The part of the code where shared resources (variables, files) are accessed. Only one thread should be allowed inside the critical section at a time.

### 2.2 Mutex vs. Semaphore
- **Mutex (Mutual Exclusion):** A locking mechanism. Only the thread that acquired the lock can release it. Think of it as a single key to a bathroom.
- **Semaphore:** A signaling mechanism that maintains a counter. It allows `N` threads to access a resource. A binary semaphore (counter = 1) is similar to a mutex, but it can be released by a different thread than the one that acquired it.

---

## 3. Deadlocks

A Deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.

### 3.1 The Four Necessary Conditions for Deadlock (Coffman Conditions)
For a deadlock to occur, ALL four of these must hold true simultaneously:
1. **Mutual Exclusion:** At least one resource must be non-shareable.
2. **Hold and Wait:** A process is holding at least one resource and waiting to acquire additional resources held by others.
3. **No Preemption:** Resources cannot be forcibly taken away from a process; they must be released voluntarily.
4. **Circular Wait:** There exists a set of waiting processes `{P0, P1, ..., Pn}` such that `P0` is waiting for `P1`, `P1` for `P2`... and `Pn` for `P0`.

### 3.2 Handling Deadlocks
- **Deadlock Prevention:** Ensure at least one of the 4 Coffman conditions cannot hold.
- **Deadlock Avoidance:** The OS checks the resource request to see if granting it will leave the system in a "Safe State". (e.g., Banker's Algorithm).
- **Deadlock Detection and Recovery:** Let it happen, detect it, and kill processes to break the cycle.

---

## 4. Memory Management

### 4.1 Paging
Paging is a memory management scheme that eliminates the need for contiguous allocation of physical memory.
- **Logical Memory (CPU viewpoint):** Divided into fixed-size blocks called **Pages**.
- **Physical Memory (RAM):** Divided into fixed-size blocks called **Frames** (same size as pages).
- The OS maintains a **Page Table** to map logical Pages to physical Frames. This solves external fragmentation.

### 4.2 Virtual Memory
Virtual memory allows the execution of processes that are not completely in memory. It creates an illusion for the user of having a very large contiguous memory.
- **Demand Paging:** Only bring pages into RAM when they are needed.
- **Page Fault:** Occurs when a program tries to access a page that is mapped in the logical address space but is NOT currently loaded in physical RAM.

### 4.3 Page Replacement Algorithms
When RAM is full and a page fault occurs, the OS must evict an existing page to bring the new one in.
- **FIFO (First In First Out):** Evicts the oldest page. Suffers from Belady's Anomaly (increasing RAM can increase page faults).
- **LRU (Least Recently Used):** Evicts the page that has not been used for the longest time. Generally the best performer.
