# Operating Systems: Top Interview Questions

Here are the most frequently asked Operating Systems questions in technical interviews.

---

## Question 1: What is the difference between a Process and a Thread?
**Answer:**
- A **Process** is a program in execution. It is a heavy-weight operation. Each process has its own isolated memory space (code, data, heap, and stack). Inter-process communication (IPC) is slow and complex. If one process crashes, it generally does not affect others.
- A **Thread** is a sequence of execution within a process. It is a light-weight operation. All threads within a single process share the same memory space (code, data, heap) but have their own separate stacks and registers. Thread communication is very fast, but if one thread crashes, it can take down the entire process.

## Question 2: What is a Deadlock? What are its necessary conditions?
**Answer:**
A deadlock is a situation where two or more processes are unable to proceed because each is waiting for a resource that the other holds, creating an infinite circular wait.
Four conditions must hold simultaneously for a deadlock (Coffman Conditions):
1. **Mutual Exclusion:** Resources cannot be shared.
2. **Hold and Wait:** A process is holding a resource while waiting for another.
3. **No Preemption:** Resources cannot be forcibly taken from a process.
4. **Circular Wait:** A closed chain of processes exists, where each process is waiting for a resource held by the next process in the chain.

## Question 3: What is Paging? What problem does it solve?
**Answer:**
Paging is a memory management technique where the OS divides physical memory into fixed-size blocks called **frames**, and logical memory (the program) into blocks of the same size called **pages**.
The OS maps pages to frames using a Page Table. Because any page can be placed in any available frame, the program does not need to be loaded into a single contiguous block of physical RAM.
**Problem solved:** It completely eliminates **External Fragmentation** (wasted free space between allocated blocks of memory).

## Question 4: What is a Page Fault?
**Answer:**
A page fault occurs when a program attempts to access a block of memory (a page) that is mapped into its virtual address space, but is NOT currently loaded into physical RAM.
When this happens, the CPU triggers an interrupt, and the OS must fetch the required page from the hard drive (swap space/page file) and load it into an empty frame in RAM before the program can continue.

## Question 5: What is Virtual Memory?
**Answer:**
Virtual memory is a memory management capability that creates an illusion for users that they have a very large, contiguous physical memory. In reality, the OS allocates virtual addresses to processes and keeps only the currently actively used parts of the program in physical RAM, while the rest sits on the hard disk. When needed, the OS swaps data in and out of RAM automatically. This allows programs larger than the physical RAM to execute.

## Question 6: What is a Mutex vs a Semaphore?
**Answer:**
Both are synchronization tools to prevent race conditions.
- **Mutex (Mutual Exclusion Object):** A locking mechanism used to protect a critical section. Only ONE thread can acquire the lock, and strictly the *same thread* that acquired it must release it. (Concept: A key to a bathroom).
- **Semaphore:** A signaling mechanism that uses an integer counter. It allows a specific number of threads (N) to access a resource simultaneously. A binary semaphore (N=1) acts like a mutex, but with one major difference: a semaphore can be released by a *different* thread than the one that acquired it. (Concept: Bouncers letting X people into a club).

## Question 7: Explain the Banker's Algorithm.
**Answer:**
The Banker's Algorithm is a **Deadlock Avoidance** algorithm.
Whenever a process requests a resource, the OS runs this algorithm. It simulates the allocation of the requested resource and then checks if the resulting system state is "Safe". A safe state means there is at least one sequence of execution for all processes to finish without deadlocking. If the state is safe, the resource is granted. If not, the process must wait.

## Question 8: What is Thrashing?
**Answer:**
Thrashing occurs when a computer's virtual memory subsystem is in a constant state of paging. The system spends more time swapping pages in and out of the hard disk than it does executing actual application code. This results in severe performance degradation and usually happens when there are too many processes running or too little physical RAM.
