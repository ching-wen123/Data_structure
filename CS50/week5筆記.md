## Stack
- A special region of computer's memory.
  - Stores temporary variables created by each function.
- The stack is a "LIFO" data structure.
- Stack is managed and optimized by the CPU.
- When a function declares a new variable, it is "pushed" onto the stack. 
- When a function exits, all of the variables are freed.
  - It is to say, they are deleted.
- Once variables are deleted, that region of memory becomes available.

## Heap
- A region of computer's memory 
  - But that is not managed automatically for you.
- It's not as tightly managed by the CPU. 
- A more free-floating region of memory.
- To allocate memory, you must use "malloc()" or "calloc()", which are built-in C functions. 
- Once you have allocated memory on the heap, you need using "free()" to de-allocate that memory .
- If you fail to deallocate, your program will have a memory leak.
  - That is, memory on the heap won't be available to other processes. 
  - There is a tool called "valgrind" that can help you detect memory leaks.

## Stack vs Heap Pros and Cons

### Stack
very fast access

don't have to de-allocate variables

space is managed efficiently by CPU

limit on stack size (OS-dependent)

variables cannot be resized

### Heap
variables can be accessed globally

no limit on memory size

(relatively) slower access

no guaranteed efficient use of space

you must in charge of allocating and freeing variables)

variables can be resized using realloc()


參考資料：https://gribblelab.org/CBootCamp/7_Memory_Stack_vs_Heap.html
