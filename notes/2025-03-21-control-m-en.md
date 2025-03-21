---
title: Control-M
lang: en
layout: post
audio: false
translated: false
generated: true
---

Control-M is a workload automation tool developed by BMC Software, designed to manage, schedule, and monitor batch jobs and workflows across various platforms and applications. If you're wondering **how to use Control-M**, here’s a general guide to get you started:

### Steps to Use Control-M
1. **Install and Configure Control-M**  
   Begin by setting up Control-M in your environment. This typically involves installing the Control-M server, deploying agents on the machines where jobs will run, and configuring a client interface (such as Control-M/Enterprise Manager or the web-based interface) to interact with the system.

2. **Define Jobs**  
   Create the jobs you want to automate. A job could be a script, a command, or an application process. You’ll specify details like the job type, the script or command to execute, parameters, and the target host where it should run.

3. **Schedule Jobs**  
   Set up schedules to determine when and how often jobs should execute. Control-M supports flexible scheduling options, including:
   - **Time-based**: Run daily at a specific time (e.g., 2 AM).
   - **Event-based**: Trigger based on external events.
   - **Dependency-based**: Run after another job completes.

4. **Set Up Dependencies**  
   If jobs need to run in a specific order (e.g., Job B starts only after Job A finishes), define these dependencies to ensure proper sequencing and smooth workflow execution.

5. **Monitor and Manage Jobs**  
   Use the Control-M interface to track job statuses, view logs, and address issues. You can intervene manually if needed—such as rerunning a failed job or adjusting schedules.

6. **Analyze and Optimize Workflows**  
   Leverage Control-M’s reporting tools to review job performance, identify inefficiencies, and optimize your automation processes over time.

### Getting Started Practically
To use Control-M effectively, you’ll interact with its interface to perform these tasks. For example, to create a simple job that runs a script daily:
- Log in to the Control-M client.
- Navigate to the job definition area.
- Create a new job, specifying the script path and scheduling it for a specific time (e.g., every day at 2 AM).
- Save and activate the job.

### Where to Learn More
Since Control-M’s features and interface may vary by version, consult these resources for detailed, hands-on guidance:
- **Official BMC Documentation**: Provides comprehensive instructions and version-specific details.
- **Training Courses**: BMC offers formal training to master Control-M.
- **Online Tutorials**: Look for community resources or videos for practical examples.

By following these steps and exploring available resources, you’ll be well-equipped to use Control-M to automate and manage your workflows efficiently!

---

Control-M, developed by BMC Software, is **not free**. It is a commercial enterprise-grade workload automation tool designed for managing complex job scheduling and workflows across various systems. BMC Software licenses Control-M, and its pricing typically depends on factors such as the number of jobs, agents, or the scale of your deployment.

### Licensing and Costs
- **Paid License**: Control-M requires a purchased license, which can be tailored to your organization’s needs (e.g., based on job volume or features like advanced reporting).
- **Subscription or Perpetual Models**: BMC may offer subscription-based pricing or a one-time perpetual license with annual maintenance fees.
- **Enterprise Focus**: It’s aimed at businesses with robust automation needs, so costs reflect its scalability and support offerings.

### Free Alternatives?
There isn’t a free version of Control-M, but BMC occasionally provides **trial versions** or limited-time access for evaluation. You’d need to contact BMC directly or check their website for current trial options.

If you’re looking for **free alternatives** to Control-M, consider open-source workload automation tools like:
- **Apache Airflow**: Great for data workflows, though it’s more developer-oriented.
- **Cron**: Basic scheduling on Unix systems, but lacks advanced features.
- **Rundeck**: An open-source job scheduler with a community edition.

For exact pricing or to explore a trial, I recommend visiting the official BMC Software website or reaching out to their sales team, as costs vary by use case and aren’t publicly listed. Let me know if you’d like more details on alternatives!

---

Using the Control-M client on Windows involves interacting with the Control-M/Enterprise Manager (EM) GUI or the newer web-based interface to define, schedule, and monitor jobs. Below is a step-by-step guide to help you get started with the Control-M client on a Windows system:

### Prerequisites
1. **Control-M Installation**: Ensure the Control-M server and agents are installed and configured by your system administrator. The client component (Control-M/EM GUI or web interface) should also be available.
2. **Access Credentials**: Obtain login credentials (username and password) from your Control-M administrator.
3. **Windows Compatibility**: Confirm your Windows version (e.g., Windows 10 or 11) is supported by the Control-M client version you’re using.

### Steps to Use the Control-M Client on Windows
#### Option 1: Using the Control-M/Enterprise Manager GUI
1. **Launch the Client**  
   - Locate the Control-M/EM shortcut on your desktop or in the Start menu. It’s typically installed as part of the client setup.
   - Double-click to open the application. If it’s not installed, download and install it from the BMC-provided installer (requires admin rights).

2. **Log In**  
   - Enter your username and password in the login window.
   - Specify the Control-M/EM server hostname or IP address if prompted.

3. **Navigate the Interface**  
   - **Planning**: Define jobs and workflows here.
     - Click “New Job” to create a job (e.g., run a script like `C:\scripts\backup.bat`).
     - Set properties: job type (e.g., OS job), execution details, and schedule (e.g., daily at 3 AM).
   - **Monitoring**: View active jobs, check statuses (e.g., “Completed OK” or “Failed”), and review logs.
   - **Tools**: Access utilities like calendars or reports.

4. **Define a Sample Job**  
   - Go to the Planning tab.
   - Create a job: Select “OS” job type, input `C:\path\to\your\script.bat`, and set a schedule.
   - Save and load the job into the active environment.

5. **Monitor and Manage**  
   - Switch to the Monitoring tab.
   - Watch job execution in real-time, right-click to rerun or troubleshoot failed jobs, and view logs for details.

#### Option 2: Using the Web-Based Interface
1. **Access the Web Client**  
   - Open a supported browser (e.g., Chrome, Edge) on Windows.
   - Enter the URL provided by your admin (e.g., `https://controlm-server:port`).

2. **Log In**  
   - Use your credentials to access the web interface.

3. **Perform Tasks**  
   - **Job Definition**: Similar to the GUI, create jobs via a streamlined interface.
   - **Scheduling**: Set run times or dependencies using a visual editor.
   - **Monitoring**: Track job progress with dashboards and alerts.

4. **Example Workflow**  
   - Define a job to execute a Windows command (`dir > output.txt`).
   - Schedule it and monitor its status from the dashboard.

### Tips for Windows Users
- **File Paths**: Use Windows-style paths (e.g., `C:\folder\file.bat`) when defining jobs.
- **Permissions**: Ensure the Control-M agent on the Windows machine has permissions to execute scripts or commands.
- **Logs**: Check job logs in the client if something fails—look for errors like “file not found” or “access denied.”

### Learning More
- **Documentation**: Access the BMC Control-M user guide via the client’s Help menu or BMC’s website.
- **Tutorials**: Look for BMC-provided videos or ask your admin for training materials.

This should give you a solid start with the Control-M client on Windows! Let me know if you need help with a specific task, like troubleshooting a job.

