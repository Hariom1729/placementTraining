# Operating Systems (OS)

## 1. Process Management
**1. What is an Operating System?**
It is system software that acts as an interface between the user/applications and the computer hardware. It manages memory, processes, storage, and I/O.

**2. Process vs Thread?**
- **Process:** An executing instance of a program. Heavyweight, has its own isolated memory space (Heap, Data, Code segments). Context switching is slow.
- **Thread:** A unit of execution within a process. Lightweight, shares the Heap and Data segments with other threads of the same process but has its own Stack and Registers. Context switching is fast.

**3. What is a PCB (Process Control Block)?**
A data structure maintained by the OS for every process. It contains Process State, Program Counter, CPU registers, CPU scheduling info, and Memory management info.

## 2. CPU Scheduling
**4. What is Context Switching?**
The process of storing the state (registers, PC) of the currently running process/thread and restoring the state of the next process/thread to be executed.

**5. Scheduling Algorithms:**
- **FCFS:** First Come First Serve (Non-preemptive, suffers from Convoy Effect).
- **SJF:** Shortest Job First (Can be preemptive/non-preemptive, suffers from Starvation).
- **Round Robin:** Time quantum based. Preemptive. Good for time-sharing systems.
- **Priority Scheduling:** Highest priority executed first. (Solution to starvation: Aging).

## 3. Concurrency and Synchronization
**6. What is a Critical Section?**
A code segment where shared variables are accessed. Only one process/thread should be allowed inside the critical section at a time.

**7. Mutex vs Semaphore?**
- **Mutex (Mutual Exclusion):** A locking mechanism. Only the thread that acquired the mutex can release it. Binary state (0 or 1).
- **Semaphore:** A signaling mechanism. Uses an integer counter (`wait()` and `signal()` operations). Can be Binary or Counting. Any thread can release a semaphore.

## 4. Deadlocks
**8. What is a Deadlock?**
A situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.

**9. Four necessary conditions for Deadlock (Coffman Conditions):**
1. **Mutual Exclusion:** Resources cannot be shared.
2. **Hold and Wait:** A process holding a resource is waiting for another.
3. **No Preemption:** Resources cannot be forcefully taken away.
4. **Circular Wait:** Process A waits for B, B waits for C, C waits for A.

**10. Banker's Algorithm?**
A deadlock avoidance algorithm. It simulates the allocation of maximum possible amounts of all resources and checks for a "safe state" before officially allocating.

## 5. Memory Management
**11. Paging vs Segmentation?**
- **Paging:** Divides logical memory into fixed-size blocks (Pages) and physical memory into fixed-size blocks (Frames). Solves External Fragmentation. Causes Internal Fragmentation.
- **Segmentation:** Divides memory into variable-sized logical blocks (Segments) based on program structure (functions, objects). Causes External Fragmentation.

**12. What is Virtual Memory?**
A technique that creates an illusion that the computer has more RAM than it actually does by using a portion of the hard drive (Swap space) to store inactive pages.

**13. Page Fault?**
Occurs when a program tries to access a page that is mapped in the address space but not currently loaded in physical RAM. The OS must fetch it from the disk.

**14. Thrashing?**
A condition where the OS spends more time swapping pages in and out of memory than executing actual instructions, severely degrading performance. Occurs when physical memory is too small for active processes.
