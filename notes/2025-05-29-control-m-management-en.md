---
title: Control-M Workload Management Overview
lang: en
layout: post
audio: false
translated: false
generated: true
---

Control-M is a workload automation tool by BMC Software used to manage, schedule, and monitor batch jobs and workflows. Below, I’ll address your queries about **Control-M order**, **customized filters**, **folder**, **sub-application**, **application**, **freeing a job**, **running a job**, **job output**, and **advanced usage**, based on the provided context and general knowledge of Control-M.

---

### **1. What is "Order" in Control-M?**
In Control-M, **ordering** a job or folder refers to scheduling or submitting it to the **Active Jobs Database** for execution, either manually or based on predefined scheduling criteria. Ordering determines when a job or folder is processed by the Control-M/Server, which monitors and submits jobs to Control-M/Agents when their dependencies (e.g., prerequisites, events, or resources) are met.

- **How it works**: 
  - Jobs or folders are ordered into the Active Jobs Database, typically during the "New Day Procedure" (a daily process that schedules jobs based on their definitions) or manually via utilities like `ctmudly` or the Control-M GUI.
  - Example: The `ctmudly` utility allows ordering a folder at a specific time/date using a syntax like `ctmudly -DAILY_NAME <USER_DAILY_NAME>` (limited to 10 characters for the daily name).[](https://www.dbi-services.com/blog/control-m-em-order-jobs-with-a-specific-user-daily/)
  - You can specify an **OrderMethod** (e.g., "Manual" for manual ordering) at the folder level.[](https://docs.bmc.com/docs/automation-api/9191/folder-869560598.html)
  - **Ad hoc ordering**: Ordering an ad hoc job may lead to issues in some versions (e.g., Control-M 9.0.21), where a different job from the same folder might be ordered if the folder contains more than 10 jobs.[](https://docs.bmc.com/docs/controlm/90201/control-m-enterprise-manager-job-order-1147442151.html)

- **Key Points**:
  - Ordering respects scheduling criteria (e.g., calendars, weekdays, or specific dates) and dependencies (e.g., events or resources).
  - Use the **Control-M/EM** or **Automation API** to order jobs programmatically or via the GUI.

---

### **2. Customized Filter for All Jobs, Folder, Sub-Application, Application**
Control-M allows **customized filters** to search, view, or manage jobs, folders, sub-applications, and applications in the **Monitoring domain** or through utilities like `ctmpsm`. Filters help refine the view of jobs or folders based on specific attributes.

- **How to Create Customized Filters**:
  - **In the Monitoring Domain**:
    - From the Monitoring domain, use the **Find** or **Advanced Find** feature to filter jobs by attributes like job name, filename, run ID, application, sub-application, or status (e.g., OK, NOTOK).[](https://documents.bmc.com/supportu/controlm-saas/en-US/Documentation/Job_management.htm)
    - Example: In the **Quick Find** toolbar, type a job attribute (e.g., `Application:Billing`) or use the **Advanced Find** dialog box to specify multiple criteria (e.g., `Application = Billing AND SubApplication = Payable`).[](https://documents.bmc.com/supportu/controlm-saas/en-US/Documentation/Job_management.htm)
    - Filters can include **pattern matching** (e.g., using `*` for wildcards, like `Job*` to match all jobs starting with "Job").[](https://docs.itrsgroup.com/docs/geneos/5.3.0/Netprobe/control-m/control-m-plug-in-tr.html)
  - **Using Control-M Plug-in**:
    - The Control-M plug-in (for versions 9.0.18+) supports custom dataviews to filter jobs by parameters like application, sub-application, or status. You can configure these in the plug-in’s settings.[](https://docs.itrsgroup.com/docs/geneos/5.3.0/Netprobe/control-m/control-m-plug-in-tr.html)
  - **Using Control-M Reports**:
    - The Control-M reporting tool allows filtering jobs by fields like application, sub-application, or host. You can save filter templates for reuse and share them with other users.[](https://www.dbi-services.com/blog/control-m-em-generate-a-job-report-in-few-clicks/)
    - Example: Filter jobs with `Application = HR` and `SubApplication = Payroll` to generate a report.[](https://www.dbi-services.com/blog/control-m-em-generate-a-job-report-in-few-clicks/)

- **Key Attributes for Filtering**:
  - **Application**: A logical grouping of jobs related to a specific business process (e.g., "Billing"). Used to organize jobs at a high level.[](https://docs.bmc.com/docs/automation-api/9191/folder-869560598.html)
  - **Sub-Application**: A subset of an application for finer categorization (e.g., "Payable" under "Billing").[](https://docs.bmc.com/docs/automation-api/9191/folder-869560598.html)
  - **Folder**: A container for jobs or subfolders, with scheduling criteria or dependencies applied at the folder level. Folders can be **Regular**, **SMART** (with advanced scheduling and dependency logic), or **Simple** (basic container without folder-level configurations).[](https://docs.bmc.com/docs/automation-api/9191/folder-869560598.html)
  - **Job Attributes**: Includes job name, status, host, run ID, or custom fields like `BusinessFields` (e.g., `Department:HR`).[](https://docs.bmc.com/docs/automation-api/9191/folder-869560598.html)

- **Example Filter**:
  - To view all jobs in the "Billing" application with sub-application "Payable":
    ```json
    {
      "Application": "Billing",
      "SubApplication": "Payable"
    }
    ```
  - In the GUI, select **Advanced Find**, set `Application = Billing`, `SubApplication = Payable`, and press Enter to display matching jobs.[](https://documents.bmc.com/supportu/controlm-saas/en-US/Documentation/Job_management.htm)

---

### **3. Free a Job**
**Freeing a job** in Control-M releases a job that is in a **Held** state, allowing it to proceed to execution if its dependencies are met.

- **How to Free a Job**:
  - **Using the Monitoring Domain**:
    - In the Monitoring domain, right-click a held job and select **Free** from the context menu. This releases the job to continue processing.[](https://controlm.wisconsin.gov/help/CTMHelp/en-US/Documentation/Utilities/ctmpsm.htm)
  - **Using the `ctmpsm` Utility**:
    - Run the `ctmpsm` utility and select the **F (Free)** option from the Active Jobs Database menu to release a held job.[](https://controlm.wisconsin.gov/help/CTMHelp/en-US/Documentation/Utilities/ctmpsm.htm)[](https://documents.bmc.com/supportu/controlm-saas/en-US/Documentation/Utilities/ctmpsm.htm)
    - Example command: `ctmpsm -FREE <job_id>`
  - **Using Automation API**:
    - Use the REST API or CLI to issue a `free` command for a specific job. For example:
      ```bash
      ctm run job:free <job_id>
      ```

- **When to Free a Job**:
  - A job may be held due to manual intervention (e.g., using the **Hold** action) or unmet dependencies (e.g., waiting for a resource or event). Freeing it allows the job to proceed once conditions are satisfied.[](https://controlm.wisconsin.gov/help/CTMHelp/en-US/Documentation/Utilities/ctmpsm.htm)

---

### **4. Run a Job**
**Running a job** in Control-M executes it immediately, overriding its scheduling criteria or prerequisites.

- **How to Run a Job**:
  - **Using the Monitoring Domain**:
    - In the Monitoring domain, right-click the job and select **Run** to execute it immediately, bypassing any unmet scheduling criteria or dependencies.[](https://documents.bmc.com/supportu/controlm-saas/en-US/Documentation/Job_management.htm)
  - **Using the `ctmpsm` Utility**:
    - Select the **R (Rerun)** option to rerun a job or use the **Run Now (Force)** option to execute it immediately. Note that **Rerun** affects only jobs, not SMART folders.[](https://controlm.wisconsin.gov/help/CTMHelp/en-US/Documentation/Utilities/ctmpsm.htm)[](https://documents.bmc.com/supportu/controlm-saas/en-US/Documentation/Utilities/ctmpsm.htm)
    - Example command: `ctmpsm -RERUN <job_id>`
  - **Using Automation API**:
    - Use the REST API or CLI to run a job:
      ```bash
      ctm run job:run <job_id>
      ```
    - Example JSON to run a job:
      ```json
      {
        "JobName": "MyJob",
        "Type": "Job:Command",
        "Command": "echo hello",
        "RunAs": "user1"
      }
      ```[](https://docs.bmc.com/xwiki/bin/view/Control-M-Orchestration/Control-M/Control-M-Automation-API/ctmapi9202/)

- **Key Points**:
  - Running a job manually is useful for testing or urgent executions.
  - Ensure the job’s dependencies (e.g., resources or events) are available, or use **Force** to bypass them.

---

### **5. Job Output**
**Job output** in Control-M refers to the logs, system output (sysout), or results generated by a job’s execution.

- **How to View Job Output**:
  - **In the Monitoring Domain**:
    - Right-click a job and select **View Output** to display the job’s sysout or execution log.[](https://controlm.wisconsin.gov/help/CTMHelp/en-US/Documentation/Utilities/ctmpsm.htm)[](https://docs.bmc.com/docs/controlm/9020/control-m-web-supported-capabilities-922475916.html)
    - For database jobs, you can configure output formats (e.g., XML) using parameters like `OutputSQLOutput` or `SQLOutputFormat`.[](https://docs.bmc.com/docs/automation-api/920/job-types-887941124.html)
  - **Using the `ctmpsm` Utility**:
    - Select the **J (Output)** option in the Active Jobs Database menu to view the job’s output.[](https://controlm.wisconsin.gov/help/CTMHelp/en-US/Documentation/Utilities/ctmpsm.htm)[](https://documents.bmc.com/supportu/controlm-saas/en-US/Documentation/Utilities/ctmpsm.htm)
    - Example command: `ctmpsm -OUTPUT <job_id>`
  - **Using Automation API**:
    - Retrieve job output via the REST API:
      ```bash
      ctm run job:output::get <job_id>
      ```
  - **Control-M Reports**:
    - Generate reports to include job output details, filtered by criteria like job status or application.[](https://www.dbi-services.com/blog/control-m-em-generate-a-job-report-in-few-clicks/)

- **Sysout Archiving**:
  - Control-M can archive job output using sysout archive allocation parameters (e.g., `UNIT=arcunit`, `SPACE=(arcspct,(arcpri#,arcsec#),RLSE)`). The **DO SYSOUT** command triggers archiving.[](https://documents.bmc.com/supportu/INC/9.0.21/en-US/INCONTROL/Customizing/Customizing_Control-M.htm)

- **Example**:
  - For a job defined as:
    ```json
    {
      "Type": "Job:Database:EmbeddedQuery",
      "Query": "SELECT * FROM DUMMY",
      "OutputSQLOutput": "Y",
      "SQLOutputFormat": "XML"
    }
    ```
    The output will be in XML format and can be viewed in the Monitoring domain or via API.[](https://docs.bmc.com/docs/automation-api/920/job-types-887941124.html)

---

### **6. Advanced Usage in Control-M**
**Advanced usage** in Control-M refers to leveraging its more sophisticated features for complex workflow automation, dependency management, and integration with modern DevOps practices. Below are key aspects:

- **Advanced Scheduling**:
  - **Rule-Based Calendars**: Define specific days for job execution using calendars and advanced rules (e.g., `MonthDays` or `WeekDays` with parameters like `+2`, `-3`, `>4`). Example:
    ```json
    "When": {
      "MonthDaysCalendar": "Summer2017",
      "MonthDays": ["1", "+2", "-3", ">4", "<5", "D6", "L7"]
    }
    ```[](https://docs.bmc.com/docs/automation-api/9191/job-properties-869560601.html)[](https://docs.bmc.com/docs/automation-api/9192/job-properties-917140771.html)
  - **Cyclic Jobs**: Jobs that rerun at specified intervals (e.g., every 2 hours). Configure using `Cyclic` parameters.[](https://manualzz.com/doc/6971388/control-m-workload-automation-user-guide-8.0.00.700)[](https://manualzz.com/doc/o/aviq3/control-m-workload-automation-user-guide-8.0.00.700-planning)
  - **Date/Time Constraints**: Specify ranges when jobs can or cannot run (e.g., `FromDate` and `ToDate`).[](https://docs.bmc.com/docs/automation-api/9191/job-properties-869560601.html)[](https://docs.bmc.com/docs/automation-api/9192/job-properties-917140771.html)

- **Event Management**:
  - Jobs can wait for, add, or delete events using `WaitForEvents`, `AddEvents`, or `DeleteEvents`. Example:
    ```json
    "Wait1": {
      "Type": "WaitForEvents",
      "Events": [
        {"Event": "e1"},
        {"Event": "e2"},
        {"Event": "e3", "OrderDate": "AnyDate"}
      ]
    }
    ```
    Logical operators (AND/OR) can define relationships between events.[](https://docs.bmc.com/docs/automation-api/9191/job-properties-869560601.html)[](https://docs.bmc.com/docs/automation-api/9192/job-properties-917140771.html)

- **Control-M Automation API**:
  - Manage job workflows as code using JSON, integrated with source control systems like Git. Example:
    ```json
    {
      "FolderSample": {
        "Type": "Folder",
        "Job1": {
          "Type": "Job:Command",
          "Command": "echo I am a Job",
          "RunAs": "controlm"
        }
      }
    }
    ```
    Deploy and test job flows using the **Control-M Workbench** or CLI.[](https://docs.bmc.com/xwiki/bin/view/Control-M-Orchestration/Control-M/Control-M-Automation-API/ctmapi9202/)[](https://www.dbi-services.com/blog/control-m-em-control-m-automation-api-overview-and-installation/)
  - Supports provisioning agents, configuring host groups, and automating deployments.[](https://docs.bmc.com/xwiki/bin/view/Control-M-Orchestration/Control-M/Control-M-Automation-API/ctmapi9202/)

- **Reference Sub-Folders**:
  - Create sub-folders that reference existing SMART folders or jobs to reuse workflows without duplication. Example:
    ```json
    {
      "Clothing_Department": {
        "Type": "SubFolder",
        "Reference": true,
        "ReferencePath": "Billing/Invoice"
      }
    }
    ```
    Useful for organizations with shared workflows across departments.[](https://documents.bmc.com/supportu/controlm-saas/en-US/Documentation/Creating_a_Sub-folder.htm)

- **Job Dependencies and Flows**:
  - Define job sequences using **Flow** objects to enforce order dependencies:
    ```json
    {
      "Flow1": {
        "Type": "Flow",
        "Sequence": ["Job1", "Job3"]
      }
    }
    ```
    Supports cross-folder and sub-folder dependencies.[](https://docs.bmc.com/docs/automation-api/9191/folder-869560598.html)

- **Resource Management**:
  - Use **Mutex** (mutual exclusion) resources or **Resource Pools** to control job concurrency or resource allocation. Example:
    ```json
    "mut1": {
      "Type": "Resource:Mutex",
      "MutexType": "Exclusive"
    }
    ```[](https://docs.bmc.com/docs/automation-api/9191/folder-869560598.html)
  - Manage lock resources or prerequisites via the `ctmpsm` utility.[](https://controlm.wisconsin.gov/help/CTMHelp/en-US/Documentation/Utilities/ctmpsm.htm)[](https://documents.bmc.com/supportu/controlm-saas/en-US/Documentation/Utilities/ctmpsm.htm)

- **Custom Notifications**:
  - Configure notifications for job execution time or status (e.g., `Notify:ExecutionTime` for jobs running less than expected). Example:
    ```json
    "Notify1": {
      "Type": "Notify:ExecutionTime",
      "Criteria": "LessThan",
      "Value": "3",
      "Message": "Less than expected"
    }
    ```[](https://docs.bmc.com/docs/automation-api/9191/folder-869560598.html)

- **Environment-Specific Configurations**:
  - Reuse jobs across environments (e.g., UAT, Prod) by defining environment-specific variables in files like `UAT.txt` or `PROD.txt`. Example:
    ```
    /home/controlm/cntrlm_server/UAT.txt:
    %%CM_ORA_SERVR=UAT
    %%CM_ORA_DBASE=UA01
    %%CM_ORA_SCRPT=/opt/oracle/local/custom/bin
    ```
    Reference these in the **SubApplication** field to dynamically resolve variables.[](https://stackoverflow.com/questions/77113182/how-to-reuse-control-m-jobs-and-workspace-for-different-environments)

- **Mass Updates**:
  - Use **Control-M OS to Application Jobs** to update entire job flows (e.g., replacing OS jobs with file transfer jobs).[](https://controlm.wisconsin.gov/help/CTMHelp/en-US/Documentation/Conversion/Control-M_OS_to_Application_Jobs.htm)

- **JCL Verification**:
  - Verify JCL code for z/OS jobs before execution, defining custom parameters and filters to catch errors.[](https://documents.bmc.com/supportu/controlm-saas/en-US/Documentation/Job_management.htm)

- **Integration with Third-Party Applications**:
  - Support for jobs like **Hadoop:Oozie**, **Azure:BatchAccount**, or **Database:EmbeddedQuery** for advanced integrations. Example:
    ```json
    "OozieJob": {
      "Type": "Job:Hadoop:Oozie",
      "Host": "edgenode",
      "ConnectionProfile": "DEV_CLUSTER"
    }
    ```[](https://docs.bmc.com/docs/automation-api/920/job-types-887941124.html)

---

### **Summary**
- **Order**: Submits jobs or folders to the Active Jobs Database for execution, manually or via scheduling.
- **Customized Filters**: Use Monitoring domain, `ctmpsm`, or reports to filter jobs by application, sub-application, folder, or other attributes.
- **Folder, Sub-Application, Application**: Organize jobs hierarchically; folders contain jobs/subfolders, applications group related jobs, and sub-applications provide finer categorization.
- **Free a Job**: Releases a held job using GUI, `ctmpsm`, or API.
- **Run a Job**: Executes a job immediately, overriding criteria, via GUI, `ctmpsm`, or API.
- **Job Output**: View logs/sysout via Monitoring domain, `ctmpsm`, or API; configure formats for database jobs.
- **Advanced Usage**: Includes rule-based calendars, event management, Automation API, reference sub-folders, flows, resource management, notifications, and integrations.

For further details, refer to the official BMC Documentation (https://docs.bmc.com) or the Control-M Automation API guide (https://x.ai/api). If you have specific scenarios or need examples, let me know!