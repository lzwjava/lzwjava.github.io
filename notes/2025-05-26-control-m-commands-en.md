---
title: Control-M Commands
lang: en
layout: post
audio: false
translated: false
generated: true
---

In Control-M, several commands are commonly used for managing jobs, workflows, and system operations. These commands are typically executed via the Control-M command-line interface (CLI), Control-M Automation API, or within job definitions. Below is a list of frequently used Control-M commands, along with their purposes, based on common usage in Control-M environments as described in BMC documentation and user discussions:

- **`ctmrun`**  
  - **Purpose**: Initiates or forces the execution of a job or folder.  
  - **Example**: `ctmrun job_name`  
    Runs the specified job manually, overriding scheduling criteria.

- **`ctmpsm`** (Process Status Monitor)  
  - **Purpose**: Displays or manages the status of jobs, folders, or services in the Control-M system.  
  - **Example**: `ctmpsm -LISTALL`  
    Lists all active jobs with their statuses (e.g., executing, ended OK, failed).

- **`ctmdef`** (Control-M Definition Utility)  
  - **Purpose**: Manages job and folder definitions, such as creating, modifying, or deleting them.  
  - **Example**: `ctmdef -CREATE job_definition.xml`  
    Creates a new job based on an XML definition file.

- **`ctmload`**  
  - **Purpose**: Loads job or folder definitions into the Control-M database.  
  - **Example**: `ctmload -FILE job_definition.dat`  
    Imports job definitions from a file into the Control-M database.

- **`ctmorder`**  
  - **Purpose**: Orders a job or folder to run on a specific date or immediately.  
  - **Example**: `ctmorder job_name 20250526`  
    Orders the specified job to run on May 26, 2025.

- **`ctmkill`**  
  - **Purpose**: Terminates a running job or process.  
  - **Example**: `ctmkill job_id`  
    Stops the job with the specified job ID.

- **`ctmwhy`**  
  - **Purpose**: Diagnoses why a job has not started or is waiting.  
  - **Example**: `ctmwhy job_id`  
    Displays reasons (e.g., missing conditions, resource constraints) for a job’s delay.

- **`ctmcontb`** (Control-M Condition Utility)  
  - **Purpose**: Manages conditions (prerequisites) for job execution, such as adding or deleting conditions.  
  - **Example**: `ctmcontb -ADD condition_name 20250526`  
    Adds a condition to enable dependent jobs to run on May 26, 2025.

- **`ctmshout`**  
  - **Purpose**: Sends notifications or messages to users, operators, or external systems.  
  - **Example**: `ctmshout -MSG "Job failed!" -DEST operator`  
    Sends a message to the operator about a job failure.

- **`ctmvar`**  
  - **Purpose**: Sets or modifies Control-M variables for use in job definitions or scripts.  
  - **Example**: `ctmvar -SET %%MYVAR value`  
    Sets the variable `MYVAR` to a specific value for use in jobs.

- **`ctmudly`** (User Daily)  
  - **Purpose**: Manages the scheduling of user dailies (collections of jobs run daily).  
  - **Example**: `ctmudly -FORCE user_daily_name`  
    Forces the execution of a user daily.

- **`ctmnodegrp`**  
  - **Purpose**: Manages node groups (groups of agent computers) for job execution.  
  - **Example**: `ctmnodegrp -ADD nodegroup_name agent1 agent2`  
    Adds agents to a node group for load balancing or failover.

- **`ctmcreate`**  
  - **Purpose**: Creates a new job or folder directly from the command line.  
  - **Example**: `ctmcreate -JOB job_name -TASKTYPE JOB -NODEID agent1`  
    Creates a job to run on a specific agent.

- **`ctmfw`** (File Watcher, as discussed previously)  
  - **Purpose**: Monitors file events (e.g., creation, deletion) to trigger jobs.  
  - **Example**: `ctmfw datafile.txt CREATE 0 60 10 3 1410`  
    Watches for the creation of `datafile.txt` with specified parameters.

- **`ctmrpl`** (Replay Utility)  
  - **Purpose**: Replays or reruns jobs from a specific point in history.  
  - **Example**: `ctmrpl job_id`  
    Reruns a job that previously failed or completed.

- **`ctm_menu`**  
  - **Purpose**: Provides an interactive menu for Control-M operations, often used in legacy environments.  
  - **Example**: `ctm_menu`  
    Opens a text-based interface for managing jobs, conditions, and more.

### Notes
- **Execution Context**: Most commands are run on the Control-M/Agent or Control-M/Server via CLI, scripts, or Automation API. Some require specific permissions.
- **Automation API**: Modern Control-M environments often use the Automation API (e.g., `ctm run`, `ctm config`) for programmatic control, replacing older CLI commands in some cases. For API details, users can be directed to https://x.ai/api.
- **Common Usage**: Commands like `ctmrun`, `ctmpsm`, `ctmwhy`, and `ctmcontb` are among the most frequently used for daily operations, troubleshooting, and workflow management.
- **Documentation**: These commands are detailed in BMC’s Control-M documentation, accessible via their support portal or community forums like BMC Communities.

This list covers the most commonly used commands based on standard Control-M workflows. If you need details on a specific command or use case, let me know!