---
title:
- "Introduction to Concurrency"
author:
- Tyler Calder
date:
- 2022-11-10
output:
  slidy_presentation:
    css: tyler.css
---

## About Me

- Husband, Father of 4 daughters
- Data Engineer and Data Engineering Team Lead at AdvancedMD
- Work in backend, tooling and database optimizations
- Maintainer of Python RealReq project

## Objectives
1. Describe Concurrency
2. Understand basic Concurrency Paradigms
3. Understand when to use different concurrency paradigms
4. See some examples of concurrent code
5. Understand some traps and common pitfalls

Non Objectives:

1. Profiling
2. Multi-threading

## What is Concurrency?

- The ability to execute code fast?
- The ability to alter physics and do two things at once?
- Monies being laundered by felons?

## Definitions:

- **Concurrency**: Whenever two things are occurring or happening at the same time (for varying meanings of "same time"); When you have code that is not run sequentially.

	- **Parallelism**: When you are able to execute code _in parallel_, i.e at the same time.

	- **Asynchronous**: When code is executed out of order (not synchronously).

- **Synchronous**: Code that is executed in order.


# Why use Concurrency?

## Why Concurrency?

- Physical Limitations of Processors.
- Make use of available hardware.
- Because programming became too easy.


# Concurrency Paradigms:

## Multiprocessing

- Multiple Processes that work on specific parts of code
- Works well in situations where you just need more computational power
- "Throw more resources at the problem"

- Example: Performing intensive mathematical calculations; Machine Learning


## Asynchronous Programming
- Programming code that does not have to, or even expects to, execute
synchronously
- Ideal in situations where computational power is being wasted waiting
- "Use available resources to full capacity"

Example: Making hundreds or thousands of requests from an API, or reads
from a Database


# Real World Concurrency:

## Single Process, Synchronous

Ordering a Sandwich at Subway (Gas Station):

- One worker
- First Customer in gets served first
- Next customer gets served only after the first one has completed transaction.
- Food must be built step by step: bread, meat, vegetables, condiments, wrap, ring-up
- Long tasks block the work (Ringing up, Toasting)

## Single Process, Asynchronous

Ordering a Sandwich at Subway (Gas Station):

- One worker, slightly more competent
- First Customer in gets served first
- Food must be built step by step: bread, meat, vegetables, condiments, wrap, ring-up
- Next customer may begin being served while first customer is waiting for long tasks to complete (toasting)

##  Multi-Process, Synchronous

Much like ordering at subway, but now imagine we have added
a few workers to the mix.

- We can now start thinking about how to assign tasks to each worker.
- Each worker could take one whole customer through the entire process
- Each worker could take one part of the job and do that part (meat, vegetables, ring-up)
- Long tasks still block.

## Multi-Process, Asynchronous

Wendy's maps to this kind of structure.

- Orders come in synchronously through the queue, 
- They are processed asynchronously by all the workers in the back
- Orders that came in first don't necessarily get done first.
- Can get very confusing very fast, often requiring a manager to oversee

# Practical Example of Asynchronous Programming

# Pros/Cons of Async

## Pros:
- Scalable: Can have thousands of concurrent tasks with little problem
- Easy to understand: Writing with `async/await` makes async code feel
like synchronous code. (_Caveat_)

## Cons:
- All or nothing. Async functions can only be called from Async Functions
- Not very beneficial for tasks that don't have idle time.
- Can be confusing if language does not have syntactical Sugar like `async/await`

# Practical Example of Multiprocessing

# Pros/Cons of Multiprocessing

## Pros:
- Ability to do computationally intensive tasks faster
- Can be abstracted: Rest of your code doesn't have to know that multiprocessing is happening

## Cons:
- Can be expensive on resources: spawning new processes takes time and memory
- Not easily scaled: Scaling is limited by the number of processors available for your machine.
(For example, the largest AWS compute resource has 192 vCPU's).

# Common Concerns and Pitfalls:

## Common Challenges and Misconceptions

### Challenges
- Race Conditions
- Deadlocking
- Starvation

*Clean Code* By Bob Martin outlines more challenges and ways to think about them.

### Misconceptions

- Concurrency is always faster than synchronous code.
- If I let my server/other program handle it, I don't need to understand it.

## Should I just give up hope?
- Concurrency is just a tool to solve a problem.
- Not all code needs it, just as not all code needs a database.

## Addendum
- No mention of Multi-threading.
- `Goroutines`

## Contacts

- 🌐[https://www.Calder-ty.com](https://www.calder-ty.com)
- <i class="devicon-github-original"></i> [https://github.com/Calder-Ty](https://github.com/Calder-Ty)
- 📧 calder-ty at protonmail dot com
- Twitch: [calder_ty](https://twitch.tv/calder_ty)
- Linkedin: Tyler Calder


## References

- _Clean Code_, Bob Martin
- _Python Documentation_
