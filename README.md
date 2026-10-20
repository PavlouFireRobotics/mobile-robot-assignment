# Mobile Robot Take-Home Assignment

This take-home assignment consists of two independent ROS 2 applications:

1. [Perception: person detection and 3D location estimation](src/perception/README.md)
2. [Navigation: Turtlesim navigation action server](src/navigation/README.md)

Your submission must contain working solutions to **both parts**. Read the dedicated README for each part before starting; those documents define the detailed functional requirements and expected deliverables.

## Development environment

- ROS 2 Humble
- A Docker image based on Ubuntu 22.04 with ROS 2 Humble
- C++ for the navigation task
- Python or C++ for the perception task, unless a dedicated requirement states otherwise

## Repository and workspace structure

This repository is a single ROS 2 workspace. Place all ROS 2 packages below the relevant task directory:

```text
mobile-robot-assignment/
├── Dockerfile
├── README.md
├── src/
│   ├── navigation/
│   │   ├── README.md
│   │   └── <navigation ROS 2 packages>/
│   └── perception/
│       ├── README.md
│       ├── front_camera_info/
│       └── <additional perception ROS 2 packages>/
└── <optional supporting files>
```

The `navigation` and `perception` directories group related packages; they are not themselves ROS 2 packages or separate workspaces. Do not add another `src` directory beneath either one. The complete workspace must be buildable from the repository root with a single `colcon` command.

For example, new packages can be created with:

```bash
ros2 pkg create --destination-directory src/navigation <package_name>
ros2 pkg create --destination-directory src/perception <package_name>
```

Package names and package boundaries are yours to choose unless they are specified in a task README.

## Docker requirements

Provide one `Dockerfile` that produces a single image containing:

- ROS 2 Humble;
- the dependencies required by both tasks;
- everything needed to build and run the submitted ROS 2 packages.

You may run the image as one container or as multiple containers. A single container is likely sufficient, but choose the arrangement that best supports your solution. If multiple containers are required, provide a `compose.yaml` or `docker-compose.yml` that starts and connects them correctly. All containers must use the submitted image, although they may run different commands.

Do not copy the perception dataset into the image. Mount it at runtime, as described in the perception task. Generated results that should remain available after a container exits must also be written to a bind mount or Docker volume.

If a component needs access to a graphical display, host networking, hardware acceleration, or another host resource, document the required Docker options and any platform assumptions.

## Build and launch requirements

The documented Docker workflow must allow an evaluator to build the image and then, inside the provided environment, build the complete workspace using commands equivalent to:

```bash
colcon build --symlink-install
source install/setup.bash
```

Provide a separate ROS 2 launch file for each part of the assignment:

- the perception launch file must start the nodes needed for the complete perception pipeline;
- the navigation launch file must start the nodes needed for the complete navigation application.

The two applications do not need to run simultaneously. Each must be independently launchable and testable. Supporting commands such as starting Turtlesim or playing the supplied ROS bag may be included in the launch system or documented as separate steps.

## Submission documentation

Add a clearly marked `Candidate solution` section to this README, or provide a root-level `SOLUTION.md`, with exact commands that allow an evaluator to:

1. build the Docker image;
2. start the required container or containers;
3. mount or otherwise provide the perception dataset;
4. build the ROS 2 workspace;
5. launch the perception solution;
6. launch the navigation solution;
7. reproduce the required demonstrations and tests for both tasks;
8. locate generated results and test output.

Also document:

- your package and node architecture;
- important design decisions and trade-offs;
- assumptions and known limitations;
- the operating system and ROS 2 distribution used for development and testing;
- any incomplete requirements and how you would approach them with more time.

Commands should work from a clean clone and must not depend on undeclared software installed on the evaluator's machine other than Docker and the host facilities explicitly documented by you.

Do not remove or rewrite the assignment requirements in the root or task-specific READMEs when adding your solution documentation.

## General expectations

- Keep generated `build/`, `install/`, and `log/` directories out of version control.
- Do not commit the supplied dataset, downloaded neural-network weights, credentials, or other unnecessarily large generated files.
- Declare package dependencies in the appropriate `package.xml`, `CMakeLists.txt`, `setup.py`, or dependency files.
- Include configuration, launch, interface, test, and helper files needed to reproduce your solution.
- Prefer a clear, reliable implementation that you can explain and modify during the follow-up interview.

Internet access and AI assistance are allowed and expected, but you remain responsible for understanding all submitted code and design decisions.

## Submission

Submit your completed solution as a private GitHub repository and grant access to:

- `DimitriosGkegkas`
- `RoboKon9`
