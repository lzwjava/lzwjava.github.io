---
title: Passing File Results in Control-M Jobs
lang: en
layout: post
audio: false
translated: false
generated: true
---

In Control-M, passing a file result from one job to the next and understanding **In** and **Out** conditions are critical for managing job dependencies and workflows. Below, I’ll explain how to pass file results between jobs and clarify the concept of **In** and **Out** conditions, including their usage, based on Control-M’s scheduling and dependency mechanisms.

---

### **1. Passing File Results to the Next Job in Control-M**

To pass the result of a file (e.g., output file, data, or status) from one job to another in Control-M, you can use a combination of **File Watcher jobs**, **AutoEdit variables**, **conditions**, or **file transfer jobs**. Here are the primary methods:

#### **Method 1: Using a File Watcher Job**
A **File Watcher job** can detect the creation, deletion, or modification of a file and trigger the next job in the workflow. This is useful when the first job generates a file that the next job depends on.

- **Steps**:
  1. **Create a File Watcher Job**:
     - Define a **File Watcher: Create** job to monitor the output file of the first job (e.g., `C:/path/output.txt`).
     - Set parameters like `Path`, `SearchInterval`, `TimeLimit`, and `MinimumSize` to ensure the file meets specific criteria (e.g., minimum size to confirm it’s complete). Example JSON for Automation API:
       ```json
       "FWJobCreate": {
         "Type": "Job:FileWatcher:Create",
         "RunAs": "controlm",
         "Path": "C:/path/output.txt",
         "SearchInterval": "45",
         "TimeLimit": "22",
         "MinimumSize": "10B"
       }
       ```
      [](https://docs.bmc.com/xwiki/bin/view/Control-M-Orchestration/Control-M/Control-M-Automation-API/ctmapi9202/Code-Reference/Job-types/)
  2. **Set an Out Condition**:
     - In the File Watcher job, define an **Out Condition** (e.g., `FILE-CREATED-OK`) to signal that the file was detected.
     - Example: In the job’s **Actions** tab, add an **Out Condition** like `FILE-CREATED-OK` with `ODATE` (original date) or a specific date.
  3. **Link to the Next Job**:
     - In the dependent job, add an **In Condition** matching the File Watcher’s **Out Condition** (e.g., `FILE-CREATED-OK`).
     - The dependent job will only run once the file is detected and the condition is satisfied.
  4. **Pass the File Path**:
     - Use an **AutoEdit variable** to pass the file path to the next job. For example, set a variable like `%%FILE_PATH=C:/path/output.txt` in the File Watcher job’s **Actions** tab (under **Set Variable**).
     - In the next job, reference the file path using the AutoEdit variable (e.g., `%%FILE_PATH`) in the script or command.

#### **Method 2: Using AutoEdit Variables for File Content or Path**
If the first job generates a file and you need to pass its content or metadata (e.g., file path) to the next job, **AutoEdit variables** are ideal.

- **Steps**:
  1. **Generate the File in the First Job**:
     - Ensure the first job creates the file in a known location (e.g., `/home/user/output.txt`).
  2. **Set an AutoEdit Variable**:
     - In the first job’s **Actions** tab, use a **Set Variable** action to define an AutoEdit variable, such as `%%OUTPUT_FILE=/home/user/output.txt`.
     - Alternatively, if the job’s output contains dynamic data, you can capture it using a script and set it as an AutoEdit variable.
  3. **Pass to the Next Job**:
     - In the dependent job, reference the AutoEdit variable (e.g., `%%OUTPUT_FILE`) in the script or command line to access the file path or content.
     - Example: If the next job is a script job, use `%%OUTPUT_FILE` in the script to read or process the file.
     - For example, a script might include:
       ```bash
       cat %%OUTPUT_FILE
       ```
  4. **Ensure Dependency**:
     - Use **In** and **Out** conditions to ensure the second job only runs after the first job completes successfully. For example:
       - First job **Out Condition**: `JOB1-COMPLETE-OK`
       - Second job **In Condition**: `JOB1-COMPLETE-OK`

#### **Method 3: Using Control-M Managed File Transfer (MFT)**
If the file needs to be transferred between systems or locations before being used by the next job, use a **Control-M MFT job**.

- **Steps**:
  1. **Configure an MFT Job**:
     - Create a **Job:FileTransfer** to move the file from the source (where the first job creates it) to a destination accessible by the next job.
     - Example JSON for Automation API:
       ```json
       "FileTransferJob": {
         "Type": "Job:FileTransfer:FTP",
         "ConnectionProfile": "FTP_CONNECTION_PROFILE",
         "Source": "C:/path/output.txt",
         "Destination": "/home/user/destination/output.txt"
       }
       ```
      [](https://docs.bmc.com/docs/automation-api/9181/code-reference-784100975.html)
  2. **Set Conditions**:
     - Add an **Out Condition** in the MFT job (e.g., `FILE-TRANSFERRED-OK`) to signal successful transfer.
     - Add a matching **In Condition** in the next job to ensure it waits for the file transfer to complete.
  3. **Access the File**:
     - The next job can access the file at the destination path (e.g., `/home/user/destination/output.txt`) using a script or command.

#### **Method 4: Using Shared Storage or Scripts**
If both jobs run on the same system or have access to shared storage, the first job can write the file to a shared location, and the second job can directly access it.

- **Steps**:
  1. **Write to Shared Location**:
     - The first job writes the file to a shared directory (e.g., `/shared/output.txt`).
  2. **Pass File Path**:
     - Use an **AutoEdit variable** or hardcode the file path in the second job’s script.
  3. **Ensure Dependency**:
     - Use **In** and **Out** conditions to ensure the second job waits for the first job to complete and create the file.

#### **Example Workflow**:
- **Job 1 (Script Job)**: Creates `output.txt` and sets an **Out Condition** `JOB1-DONE` and an AutoEdit variable `%%OUTPUT_FILE=/path/output.txt`.
- **Job 2 (File Watcher Job)**: Monitors `%%OUTPUT_FILE` and sets an **Out Condition** `FILE-DETECTED`.
- **Job 3 (Processing Job)**: Uses `%%OUTPUT_FILE` in its script and has an **In Condition** `FILE-DETECTED`.

---

### **2. Understanding In and Out Conditions in Control-M**

**In** and **Out** conditions in Control-M are used to manage dependencies between jobs, ensuring that jobs execute in the correct order based on events or statuses.

#### **What Are Conditions?**
- **Conditions** are logical flags used to control the flow of jobs in Control-M. They act as signals that indicate whether a job can start (In Conditions) or has completed (Out Conditions).
- There are two types of conditions:
  - **Prerequisite Conditions**: Local to a specific Control-M server or datacenter.
  - **Global Conditions**: Used for dependencies across different datacenters or servers.[](http://www.ctmguru.com/p/faq.html)

#### **In Conditions**
- **Definition**: An **In Condition** is a prerequisite that a job requires to start. The job will not execute until all its **In Conditions** are satisfied (i.e., added to the Active Jobs File, or AJF).
- **Example**:
  - Job B has an **In Condition** `JOB-A-OK`.
  - Job B will only start when the condition `JOB-A-OK` is present in the AJF, typically added by Job A upon successful completion.
- **Usage**:
  - Defined in the **Prerequisites** tab of a job in the Control-M GUI or via JSON in the Automation API.
  - Example JSON:
    ```json
    "JobB": {
      "Type": "Job:Command",
      "Command": "echo Hello",
      "InConditions": [
        {"Name": "JOB-A-OK", "ODATE": "ODAT"}
      ]
    }
    ```
- **Maybe Conditions**: A special type of **In Condition** that allows a job to run even if the predecessor job is not in the AJF. For example, if Job B depends on `JOB-A-OK` but Job A is not scheduled, Job B can still run if the condition is marked as a "Maybe Condition" (e.g., `#-JOB-A-OK`).[](https://www.wisdomjobs.com/e-university/control-m-interview-questions.html)

#### **Out Conditions**
- **Definition**: An **Out Condition** is a signal that a job adds to the AJF upon completion (or another specified event, like failure). It is used to trigger dependent jobs.
- **Example**:
  - Job A adds an **Out Condition** `JOB-A-OK` when it completes successfully.
  - This condition can be used as an **In Condition** for Job B.
- **Usage**:
  - Defined in the **Actions** tab of a job under **On/Do** actions in the GUI or via JSON in the Automation API.
  - Example JSON:
    ```json
    "JobA": {
      "Type": "Job:Command",
      "Command": "create_file.sh",
      "OutConditions": [
        {"Name": "JOB-A-OK", "ODATE": "ODAT"}
      ]
    }
    ```
- **On/Do Actions**:
  - You can configure **Out Conditions** based on job status (e.g., `OK`, `NOTOK`, or `ANY`) using the **On/Do** tab.
  - Example: In Control-M V7, to delete a condition when a job ends (regardless of status), you might use:
    ```xml
    <ON STMT="*" CODE="COMPSTAT=0"> <DOCOND NAME="MY_CONDITION" ODATE="ODAT" SIGN="DEL" />
    <ON STMT="*" CODE="COMPSTAT!=0"> <DOCOND NAME="MY_CONDITION" ODATE="ODAT" SIGN="DEL" />
    ```
   [](https://stackoverflow.com/questions/48152235/control-m-on-do-condition-when-job-ended)

#### **Key Points About Conditions**:
- **Naming Convention**: Conditions typically follow a format like `JOB-NAME-EVENT` (e.g., `JOB-A-OK`) for clarity, but you can use any unique name.
- **ODATE**: The **Original Date** (`ODATE`) ties the condition to a specific scheduling date. Use `ODAT` for the current scheduling date or specify a fixed date.
- **Adding/Removing Conditions**:
  - **Add**: A job adds a condition to the AJF using an **Out Condition** (e.g., `SIGN="ADD"`).
  - **Delete**: A job can remove a condition using an **On/Do** action (e.g., `SIGN="DEL"`) to clean up dependencies.[](https://stackoverflow.com/questions/48152235/control-m-on-do-condition-when-job-ended)
- **Global Conditions**: Used for cross-datacenter dependencies, defined via the **Tools > Global Conditions** option in the Control-M GUI.[](https://www.wisdomjobs.com/e-university/control-m-interview-questions.html)
- **Dynamic Conditions**: Conditions can be added or removed dynamically using scripts or the Control-M Automation API.

#### **Example of In and Out Conditions**:
- **Scenario**: Job A creates a file, and Job B processes it.
  - **Job A**:
    - **Out Condition**: `FILE-CREATED-OK` (added when Job A completes successfully).
    - Script: Creates `output.txt` and sets `%%OUTPUT_FILE=/path/output.txt`.
  - **Job B**:
    - **In Condition**: `FILE-CREATED-OK` (waits for Job A to add this condition).
    - Script: Uses `%%OUTPUT_FILE` to read `/path/output.txt`.

#### **Tips for Managing Conditions**:
- **Use Descriptive Names**: Clear condition names (e.g., `JOB-A-FILE-CREATED`) make workflows easier to understand.
- **Clean Up Conditions**: Remove unnecessary conditions using **On/Do** actions to avoid clutter in the AJF.
- **Monitor Conditions**: Use the Control-M GUI’s **Viewpoint** or **Monitoring** domain to check condition statuses.
- **Automation API**: For programmatic control, use the Control-M Automation API to manage conditions dynamically. Example:
  ```json
  ctm run condition::add "JOB-A-OK" "ODAT"
  ctm run condition::delete "JOB-A-OK" "ODAT"
  ```
  [](https://www.dbi-services.com/blog/control-m-em-control-m-automation-api-overview-and-installation/)

---

### **Practical Example**
**Scenario**: Job 1 generates a report file (`report.csv`), and Job 2 processes it only if the file exists.

1. **Job 1 (Report Generation)**:
   - Type: `Job:Script`
   - Script: Creates `/shared/report.csv`.
   - **Out Condition**: `REPORT-GENERATED-OK`
   - **AutoEdit Variable**: `%%REPORT_FILE=/shared/report.csv`

2. **Job 2 (File Watcher)**:
   - Type: `Job:FileWatcher:Create`
   - Path: `%%REPORT_FILE`
   - **In Condition**: `REPORT-GENERATED-OK`
   - **Out Condition**: `FILE-DETECTED-OK`

3. **Job 3 (Processing)**:
   - Type: `Job:Script`
   - Script: Processes `%%REPORT_FILE`
   - **In Condition**: `FILE-DETECTED-OK`

**Workflow**:
- Job 1 runs, creates `report.csv`, sets `%%REPORT_FILE`, and adds `REPORT-GENERATED-OK`.
- Job 2 waits for `REPORT-GENERATED-OK`, detects `report.csv`, and adds `FILE-DETECTED-OK`.
- Job 3 waits for `FILE-DETECTED-OK` and processes `report.csv` using `%%REPORT_FILE`.

---

### **Additional Notes**
- **New Day Processing (NDP)**: Jobs with **In Conditions** that are not met are cleared during NDP unless **Keep Active** is set to a value greater than 0. For example, if `Keep Active = 1`, the job remains in the AJF for one additional day.[](https://stackoverflow.com/questions/63931524/how-long-does-a-control-m-job-stays-in-waiting-state-for-the-pre-requisites-to-b)
- **Debugging**:
  - Check the job’s **Output** or **Log** in the Control-M Monitoring domain to troubleshoot file or condition issues.[](https://documents.bmc.com/supportu/controlm-saas/en-US/Documentation/Job_management.htm)
  - Use the **Find** or **Advanced Search** in the Control-M GUI to locate jobs and their conditions.[](https://documents.bmc.com/supportu/controlm-saas/en-US/Documentation/Job_management.htm)
- **Automation API**: For dynamic workflows, use the Control-M Automation API to create and run jobs on demand, passing file paths or conditions programmatically.[](https://stackoverflow.com/questions/76792277/dynamic-job-definitions-using-control-m-rest-api-version-9-0-19)
- **Performance**: Avoid excessive conditions or cyclic jobs, as they can impact performance, especially with large workflows (e.g., 35,000 jobs/day).[](https://bmcapps.my.site.com/casemgmt/sc_KnowledgeArticle?sfdcid=kA33n000000Y7kTCAS&type=FAQ)

---

### **Sources**
-: BMC Documentation on Job Management[](https://documents.bmc.com/supportu/controlm-saas/en-US/Documentation/Job_management.htm)
-: Control-M Automation API Overview[](https://www.dbi-services.com/blog/control-m-em-control-m-automation-api-overview-and-installation/)
-: Stack Overflow on Control-M On/Do Conditions[](https://stackoverflow.com/questions/48152235/control-m-on-do-condition-when-job-ended)
-: Stack Overflow on Job Waiting States[](https://stackoverflow.com/questions/63931524/how-long-does-a-control-m-job-stays-in-waiting-state-for-the-pre-requisites-to-b)
-: FAQ on Control-M Conditions[](http://www.ctmguru.com/p/faq.html)
-: Wisdom Jobs on Control-M Conditions[](https://www.wisdomjobs.com/e-university/control-m-interview-questions.html)
-: BMC Documentation on Job Types[](https://docs.bmc.com/xwiki/bin/view/Control-M-Orchestration/Control-M/Control-M-Automation-API/ctmapi9202/Code-Reference/Job-types/)
-: BMC Documentation on Job Properties[](https://docs.bmc.com/docs/automation-api/9191/job-properties-869560601.html)
-: Stack Overflow on Dynamic Job Definitions[](https://stackoverflow.com/questions/76792277/dynamic-job-definitions-using-control-m-rest-api-version-9-0-19)
-: BMC Documentation on Code Reference[](https://docs.bmc.com/docs/automation-api/9181/code-reference-784100975.html)

If you need further clarification or a specific example tailored to your environment, please provide more details (e.g., job types, file format, or Control-M version)!