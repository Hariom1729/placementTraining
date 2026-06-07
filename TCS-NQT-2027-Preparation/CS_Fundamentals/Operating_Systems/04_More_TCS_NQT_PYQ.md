# Operating Systems - Extended TCS NQT Interview Questions (Part 2)

More frequently asked OS questions focusing on memory, processes, and Linux concepts.

---

## 11. What is a Thread Control Block (TCB) vs Process Control Block (PCB)?
**Answer:**
- **PCB:** Contains information about a process, such as Process State, Program Counter, CPU registers, CPU scheduling information, Memory-management information, and I/O status.
- **TCB:** Contains information specific to a single thread within a process, such as Thread ID, Thread State, CPU registers for that thread, and the thread's Stack Pointer. Since threads share memory, the TCB is much smaller than the PCB.

## 12. Explain the concept of Cache Memory.
**Answer:**
Cache memory is a small, extremely fast memory located close to the CPU (often on the CPU chip itself). It acts as a buffer between the CPU and the main memory (RAM). It stores frequently used data and instructions so the CPU doesn't have to wait for the slower RAM. It utilizes the principle of **Locality of Reference** (Temporal and Spatial).

## 13. What is the difference between Preemptive and Non-Preemptive Scheduling?
**Answer:**
- **Preemptive Scheduling:** The OS can forcibly interrupt a currently running process and move it back to the Ready queue to allocate the CPU to another process (e.g., a higher priority process or because the time quantum expired). Examples: Round Robin, Shortest Remaining Time First.
- **Non-Preemptive Scheduling:** Once a process gets the CPU, it keeps it until it voluntarily releases it by terminating or waiting for I/O. The OS cannot interrupt it. Examples: FCFS, basic SJF.

## 14. What is Swap Space?
**Answer:**
Swap space is a designated portion of the hard disk drive (or SSD) that the OS uses as an extension of RAM. When the physical RAM is full, the OS moves inactive pages of memory from RAM to the swap space (Swapping Out) to free up space for active processes. When those pages are needed again, they are moved back to RAM (Swapping In).

## 15. What is the concept of "Starvation" in OS? How is it resolved?
**Answer:**
Starvation occurs when a low-priority process is perpetually denied access to the CPU because there is always a steady stream of higher-priority processes being executed.
**Resolution:** It is solved using **Aging**. The OS gradually increases the priority of a process the longer it waits in the Ready queue, ensuring that it eventually becomes the highest priority and gets executed.

## 16. What is the Critical Section Problem? What are the requirements for its solution?
**Answer:**
The critical section is a segment of code where a process accesses shared resources. If multiple processes execute their critical sections concurrently, race conditions occur.
A valid solution must satisfy three requirements:
1. **Mutual Exclusion:** Only one process can be in its critical section at a time.
2. **Progress:** If no process is in its critical section, processes waiting to enter cannot be postponed indefinitely.
3. **Bounded Waiting:** There must be a limit on the number of times other processes can enter their critical sections after a process has requested to enter its own.

## 17. Explain the differences between a Microkernel and a Monolithic Kernel.
**Answer:**
- **Monolithic Kernel:** All OS services (memory management, file system, device drivers) run in the kernel space. It is highly efficient and fast, but if one service crashes (like a driver), the whole system crashes. Examples: Linux, Windows.
- **Microkernel:** Only essential services (IPC, basic scheduling, memory management) run in kernel space. Other services (file systems, drivers) run in user space. It is slower due to heavy IPC overhead, but highly stable and secure because a crashed driver doesn't crash the kernel. Example: QNX.

## 18. What is an Interrupt?
**Answer:**
An interrupt is a signal sent to the CPU by hardware or software indicating an event that needs immediate attention. When an interrupt occurs, the CPU stops its current execution, saves its state, and executes an Interrupt Handler (or ISR - Interrupt Service Routine) to process the event, before resuming the previous task.

## 19. What is the concept of a Semaphore? Difference between Binary and Counting Semaphore.
**Answer:**
A semaphore is an integer variable used for synchronization among processes. It is manipulated using two atomic operations: `wait()` (decrements) and `signal()` (increments).
- **Binary Semaphore:** The integer value can only be 0 or 1. Used to achieve mutual exclusion (similar to a Mutex).
- **Counting Semaphore:** The integer value can range over an unrestricted domain. Used to control access to a resource that has multiple identical instances (e.g., 5 available printers).

## 20. What is a System Call?
**Answer:**
A system call is the programmatic way in which a computer program requests a service from the kernel of the OS. Since user applications run in restricted User Mode, they cannot directly access hardware or memory. They must make a system call, which triggers a context switch into Kernel Mode, allowing the OS to perform the privileged operation on behalf of the application.
