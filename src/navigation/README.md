
**Project:** Turtlesim Navigation Action Server   
**Suggested effort:** ~ 12–16 hours of development  
**Technology:** ROS 2 (Humble), C++, Turtlesim
 
## 1. Objective

**Design and implement a ROS 2 application in C++** that allows a turtle in the Turtlesim simulator to autonomously navigate to a requested 2D position using a custom ROS 2 action server.

The main objective is not to develop an advanced navigation controller, but to demonstrate your understanding of:

- ROS 2 actions and goal lifecycle management
    
- ROS 2 executors, callbacks, and callback groups
    
- Asynchronous execution and concurrency
    
- Cancellation and preemption
    
- Software architecture and separation of responsibilities
    
- Robustness, testing, and engineering decision-making
    

There is no single expected architecture. We are interested in the reasoning behind your implementation and the trade-offs you make.

## 2. System Architecture

The application must contain at least two separate ROS 2 nodes.

### A. Navigation Action Server

This node exposes an action interface through which clients can request navigation to a target position.

It is responsible for managing navigation goals, cancellation requests, preemption, feedback, and action results.

### B. Navigation Controller

This node is responsible for moving the turtle toward the requested target.

It must use the standard Turtlesim interfaces:

- `/turtle1/pose` — obtain the turtle's pose
    
- `/turtle1/cmd_vel` — command linear and angular velocities
    

Only the navigation controller node should publish turtle velocity commands.

**The communication interface between the action server and navigation controller is yours to design.** You may use ROS 2 topics, services, or another justified mechanism.

The controller and action server must remain logically separated.

## 3. Functional Requirements

### 3.1 Navigation

Implement a custom ROS 2 action that accepts a target position `(x, y)` in Turtlesim coordinates.

The turtle must autonomously navigate toward the target and report success when its distance to the target is within a configurable tolerance.

You may choose your controller implementation. A simple proportional controller based on distance and heading error is sufficient.

Advanced path planning, obstacle avoidance, and orientation alignment at the target are not required.

### 3.2 Action Interface

Define a custom action interface that provides at least the following information:

|Section|Required information|
|---|---|
|Goal|Target x and y coordinates|
|Feedback|Current distance to the target|
|Result|Final distance and a descriptive message|

You may extend the interface if additional information is useful for your design.

Expose the action under the name `/navigate_turtle`.

### 3.3 Goal Lifecycle

Your action server must support:

- Accepting valid navigation goals
    
- Rejecting invalid goals
    
- Starting navigation after goal acceptance
    
- Publishing meaningful feedback during navigation
    
- Reporting `SUCCEEDED` when the target is reached
    
- Reporting appropriate unsuccessful terminal states when navigation cannot be completed
    

The action server must remain responsive while navigation is ongoing.

### 3.4 Cancellation

A client must be able to request cancellation of an active navigation goal.

Your implementation must coordinate the cancellation request with the navigation controller and ensure that the turtle is commanded to stop.

The action result and terminal state must accurately represent the outcome of the cancellation procedure.

Consider that accepting a cancellation request and completing the physical stopping procedure are separate events.

### 3.5 Preemption

Implement a **latest-goal-wins preemption policy**.

When a new valid navigation goal is accepted while another goal is executing, the newer goal should replace the previous navigation objective.

Your implementation must ensure that:

- The previous goal is handled according to a clearly documented terminal-state policy.
    
- The turtle does not execute conflicting navigation commands.
    
- Feedback and results are associated with the correct goals.
    
- Rapidly received navigation requests do not leave the system in an inconsistent state.
    

You are free to decide how the goal replacement procedure is coordinated, provided the behavior is consistent and justified.

### 3.6 Concurrency and Responsiveness

Your implementation must correctly support navigation, new goal requests, and cancellation requests without unnecessarily blocking ROS 2 processing.


Choose the architecture that you consider most appropriate and explain why.

### 3.7 Basic Failure Handling

The system should not remain indefinitely in an active goal state when execution has clearly failed.

At minimum, handle invalid navigation targets and failure to initiate navigation through the controller.

More complex failures, such as a controller process disappearing during execution, may be addressed through implementation or through a discussion of your intended handling strategy.

## 4. Testing Scenarios

Your implementation should demonstrate the following scenarios.

|Scenario|Expected behavior|
|---|---|
|Normal navigation|Turtle reaches target, feedback is published, goal succeeds|
|Cancellation|An active goal can be canceled and the turtle is commanded to stop|
|Preemption|Goal B replaces Goal A and both goal lifecycles are handled correctly|
|Rapid requests|Goals A, B, and C arrive in quick succession without conflicting motion commands|
|Invalid goal|Invalid input is rejected or otherwise handled consistently|

We are also interested in how you would handle cancellation arriving at approximately the same time that navigation completes.

You do not need to reproduce every possible race condition experimentally, but you should explain how your architecture prevents inconsistent terminal decisions.

Automated tests are encouraged. Reproducible manual test procedures or a small test client are also acceptable.

## 5. Deliverables

Include the following in the private GitHub repository described in the [root assignment README](../../README.md):

1. ROS 2 source packages and custom action definition
    
2. Build and dependency instructions
    
3. A launch file for starting the complete navigation system
    
4. A README explaining architecture and important design decisions
    
5. Instructions or scripts for reproducing the required test scenarios
    

Please state the ROS 2 distribution and operating environment used.

The project should be reasonably straightforward to build and run on another development machine with the stated dependencies.



## 6. Final Notes

This is an open-ended software engineering exercise.

We do not expect a production-grade navigation stack, advanced control algorithms, or a completely exhaustive implementation.

We are primarily interested in how you reason about concurrent robotic operations and translate that reasoning into a maintainable ROS 2 architecture.

**A simple, well-explained, and reliable solution is preferable to a complex solution with unclear execution semantics.**

Please respect the time limit. If you cannot complete every requirement, submit your best implementation and describe what remains unfinished, how you would approach it, and why.

You may use AI assistance but make sure that you maintain full understanding of your architecture, design and implementation. You should be prepared to discuss your design decisions and trade-offs during a follow-up technical review.
