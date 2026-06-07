# Operating Systems - TCS NQT Last 5 Years PYQs

These are the most repeated OS questions in TCS technical interviews.

---

## 1. What is the difference between Multiprogramming, Multitasking, and Multiprocessing?
**Answer:**
- **Multiprogramming:** Keeping multiple programs in main memory at the same time to keep the CPU busy. If one program waits for I/O, the CPU switches to another.
- **Multitasking (Time-Sharing):** A logical extension of multiprogramming. The CPU switches between processes so rapidly that it gives users the illusion that multiple programs are executing simultaneously.
- **Multiprocessing:** Using more than one physical CPU (processors) within a single computer system to execute multiple processes truly simultaneously.

## 2. Explain Demand Paging.
**Answer:**
Demand paging is a method of virtual memory management. The OS does not load the entire program into RAM at startup. Instead, it only brings a page into physical memory when the CPU actually demands (accesses) it. If the page is not in RAM, a **Page Fault** occurs, and the OS fetches it from the hard disk.

## 3. What is Belady's Anomaly?
**Answer:**
Normally, increasing the number of physical memory frames (RAM) should decrease the number of page faults. However, Belady's Anomaly is a situation where increasing the number of frames actually *increases* the number of page faults. This phenomenon is specific to the **FIFO (First-In-First-Out)** page replacement algorithm.

## 4. What are the four Coffman Conditions for Deadlock?
**Answer:**
For a deadlock to occur, all four conditions must hold simultaneously:
1. **Mutual Exclusion:** Resources cannot be shared.
2. **Hold and Wait:** A process holds at least one resource and waits for another.
3. **No Preemption:** A resource cannot be forcibly taken from a process.
4. **Circular Wait:** A cycle of processes exists where each is waiting for a resource held by the next process in the cycle.

## 5. Differentiate between Internal and External Fragmentation.
**Answer:**
- **Internal Fragmentation:** Occurs when fixed-sized memory blocks (pages) are allocated to a process, but the process doesn't need the whole block. The remaining space inside the block is wasted.
- **External Fragmentation:** Occurs when free memory is separated into small blocks and is scattered throughout the RAM. There might be enough total free memory to satisfy a request, but because it is not contiguous, the request fails. Solved by **Paging**.

## 6. What is a Context Switch?
**Answer:**
A context switch is the process of storing the state (registers, program counter) of a currently running process or thread, and restoring the state of the next process to be executed. This allows multiple processes to share a single CPU. It is computationally expensive overhead.

## 7. What is a Zombie Process and an Orphan Process?
**Answer:**
- **Zombie Process:** A child process that has completed execution, but still has an entry in the process table because its parent hasn't yet read its exit status (hasn't called `wait()`).
- **Orphan Process:** A child process whose parent process has terminated or crashed before the child finished. The `init` process (PID 1) usually adopts orphans.

## 8. What is the difference between User Mode and Kernel Mode?
**Answer:**
- **User Mode:** The mode where normal applications run. Code has restricted access to hardware and memory. If it crashes, only the application dies.
- **Kernel Mode:** The highly privileged mode where the core OS runs. It has unrestricted access to all hardware and memory. If code in kernel mode crashes, the entire system crashes (e.g., Blue Screen of Death). To do hardware things, user mode must make a **System Call** to switch to kernel mode.

## 9. How does the Banker's Algorithm work?
**Answer:**
It is a Deadlock Avoidance algorithm. It checks resource requests to ensure they keep the system in a "Safe State." A state is safe if there is at least one sequence of execution that allows all processes to finish without causing a deadlock. If granting a resource request leads to an unsafe state, the request is denied and the process must wait.

## 10. What is Spooling?
**Answer:**
SPOOL stands for Simultaneous Peripheral Operations On-Line. It is a process where data is temporarily held to be used and executed by a device, program, or the system. A classic example is Print Spooling: documents are sent to a buffer (spool) on the disk, and the printer pulls them one by one at its own slow speed, freeing up the CPU for other tasks immediately.
