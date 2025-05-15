---
title: Using Control-M Client 9
lang: en
layout: post
audio: false
translated: false
generated: true
---

Using Control-M Client 9 involves interacting with the Control-M/Enterprise Manager (EM) to manage, schedule, and monitor batch workflows. Below is a concise guide to help you get started, based on available information and general usage patterns for Control-M Client 9.0.21. Note that specific steps may vary depending on your organization's setup, permissions, and configuration.

---

### **1. Prerequisites for Using Control-M Client 9**
Before using the Control-M Client, ensure the following:
- **System Requirements**: Verify your Windows system meets the minimum requirements (e.g., compatible OS, Java 1.8 64-bit or higher in the Path Environment Variable). Check the Control-M 9.0.21 Release Notes for details.[](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/Control-M_Client_Installation.htm)
- **Installation**: The client should be installed via Client Distribution (recommended) or manually. For manual installation, log in with Administrator permissions, copy installation files to the home directory, and run the setup.[](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/Control-M_Client_Installation.htm)
- **Java Configuration**: Ensure Java is accessible, either locally or on a network path defined in `<EM_HOME>/Client_Updates/conf/client_deploy_java.properties`.[](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/Control-M_Client_Installation.htm)
- **Access**: Obtain login credentials and connection details (e.g., Control-M/EM host and port) from your Control-M administrator.

---

### **2. Accessing the Control-M Client**
1. **Launch the Client**:
   - On Windows, locate the Control-M Client application (e.g., via Start Menu or desktop shortcut).
   - If using Client Distribution, updates may prompt during login. Follow on-screen instructions to install updates.[](https://documents.bmc.com/supportu/9.0.21.200/en-US/Documentation/Control-M_Client_Distribution.htm)
2. **Log In**:
   - Enter your user ID and password (provided by your administrator).
   - Specify the Control-M/EM server host and port. By default, the client uses HTTP; for security, configure HTTPS as recommended.[](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/Control-M_Client_Installation.htm)
   - If using Single Sign-On (SSO) or LDAP, ensure compatibility mode is configured correctly.[](https://docs.bmc.com/docs/controlm/9019/control-m-compatibility-for-version-9-0-19-200-871978014.html)

---

### **3. Key Features and Navigation**
Control-M Client 9 provides a desktop interface for managing workflows, though many functions are transitioning to the Control-M Web interface. Key areas include:

- **Planning Domain**:
  - Define and manage job definitions, folders, and scheduling criteria.
  - Use the Planning domain to create SMART folders, set dependencies, and configure cyclic scheduling.[](https://docs.bmc.com/docs/controlm/9018/what-s-new-in-control-m-9-0-18-830144775.html)
  - Import/export Site Standards in JSON format for consistency.[](https://www.dbi-services.com/blog/introducing-control-m-9-0-21/)

- **Monitoring Domain**:
  - Monitor job execution, track statuses, and view logs.
  - Access viewpoints to visualize up to 20,000 jobs (optimized for 1920x1080 resolution).[](https://docs.bmc.com/docs/controlm/90201/control-m-compatibility-for-version-9-0-21-200-1238266382.html)
  - Use proactive SLA management tools to ensure service-level agreements are met.[](https://apps.apple.com/us/app/control-m/id441450712)

- **Tools Domain**:
  - Customize Site Standards and User Views to tailor the interface to organizational needs.[](https://docs.bmc.com/docs/controlm/9019/what-s-new-in-control-m-9-0-19-797339045.html)
  - Use Application Integrator to create custom job types for AWS, Azure, or other services.[](https://docs.bmc.com/docs/controlm/9019/what-s-new-in-control-m-9-0-19-797339045.html)

- **Workflow Insights (Add-On)**:
  - Access dashboards to track workflow metrics (requires an Elasticsearch cluster).[](https://docs.bmc.com/docs/controlm/90201/what-s-new-in-control-m-9-0-21-1044383595.html)

- **Reports**:
  - Generate and share reports based on job execution data. New access controls apply in 9.0.21.[](https://docs.bmc.com/docs/controlm/90201/what-s-new-in-control-m-9-0-21-1044383595.html)

---

### **4. Common Tasks**
Here’s how to perform typical tasks in Control-M Client 9:

- **Create a Job**:
  1. In the Planning domain, create a new SMART folder or job.
  2. Define job attributes (e.g., name, type, schedule, dependencies, and "Run As" user).
  3. Use Application Integrator for custom job types (e.g., AWS Lambda, Azure Logic Apps).[](https://docs.bmc.com/docs/controlm/9019/what-s-new-in-control-m-9-0-19-797339045.html)
  4. Save and deploy the job to the Control-M/Server.

- **Monitor Jobs**:
  1. In the Monitoring domain, open a viewpoint to see active jobs.
  2. Check job statuses (e.g., Executing, Completed, Failed).
  3. View logs or z/OS job output via the Monitoring domain.[](https://docs.bmc.com/docs/controlm/9019/what-s-new-in-control-m-9-0-19-797339045.html)
  4. Take actions like rerunning or holding jobs.

- **Manage Users and Roles**:
  - Note: User and role management has moved to Control-M Web in 9.0.21. Assign users to roles (e.g., Administrator, Team Leader, Viewer) for access control.[](https://www.dbi-services.com/blog/introducing-control-m-9-0-21/)
  - Contact your administrator to configure roles if you lack permissions.

- **Automate File Transfers**:
  - Use the Managed File Transfer (MFT) plug-in to transfer files to/from Azure Blob Storage, Google Cloud Storage, etc.
  - Configure MFT settings via the Control-M Web interface (e.g., allowed/blocked users, TLS 1.3 security).[](https://www.dbi-services.com/blog/introducing-control-m-9-0-21/)

---

### **5. Using Control-M Web Interface**
Control-M 9.0.21 emphasizes the Web interface for most operations, reducing reliance on the desktop client:
- Access via a supported browser (Google Chrome 78+, Microsoft Edge 80+).[](https://docs.bmc.com/docs/controlm/9020/control-m-compatibility-for-version-9-0-20-900847337.html)
- Log in using the URL: `<Control-M/EM_Host>:<port>/Welcome/`.
- Perform tasks like job management, monitoring, and LDAP configuration in the Web interface.[](https://www.dbi-services.com/blog/introducing-control-m-9-0-21/)
- The Web interface offers welcome pages with how-to videos and use-case examples.[](https://docs.bmc.com/docs/controlm/9020/what-s-new-in-control-m-9-0-20-900847340.html)

---

### **6. Troubleshooting Tips**
- **Login Issues**: Ensure compatibility mode is off for new features and verify EM/Server versions match (e.g., both 9.0.21).[](https://docs.bmc.com/docs/controlm/9018/what-s-new-in-control-m-9-0-18-830144775.html)
- **Java Errors**: Confirm Java 1.8 (64-bit) or higher is in the Path Environment Variable. Avoid 32-bit Java.[](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/Control-M_Client_Installation.htm)
- **Performance**: For large viewpoints (20,000+ jobs), ensure sufficient system resources and a compatible browser.[](https://docs.bmc.com/docs/controlm/90201/control-m-compatibility-for-version-9-0-21-200-1238266382.html)
- **Support**: Contact BMC Support or leverage the AMIGO program for upgrade/compatibility issues.[](https://docs.bmc.com/docs/ctm/control-m-workload-automation-documentation-471556599.html)

---

### **7. Additional Resources**
- **Mobile Access**: Use the Control-M mobile app (iOS/Android) for monitoring workflows on the go. Version 9.0.21.300 is available.[](https://apps.apple.com/us/app/control-m/id441450712)
- **Documentation**: Access user guides, installation manuals, and API references at [BMC Documentation](https://docs.bmc.com).[](https://docs.bmc.com/docs/controlm/90201/what-s-new-in-control-m-9-0-21-1044383595.html)
- **Training**: Check BMC Communities or your organization’s Control-M administrator for training resources.[](https://community.bmc.com/s/article/How-to-download-and-install-the-Control-M-Enterprise-Manager-9-Client)

---

### **Notes**
- **Version Compatibility**: Ensure Control-M/EM, Server, and Agent versions are compatible (e.g., 9.0.21.200). Older Application Packs (9.0.20.200 or earlier) may not work with Agent 9.0.21.[](https://docs.bmc.com/docs/controlm/90201/control-m-compatibility-for-version-9-0-21-1044383593.html)
- **Transition to Web**: BMC is phasing out desktop client features in favor of the Web interface. Familiarize yourself with Control-M Web for future-proofing.[](https://docs.bmc.com/docs/controlm/9020/what-s-new-in-control-m-9-0-20-900847340.html)
- **Critical Thinking**: Always verify configuration settings with your administrator, as documentation may not reflect custom setups or recent patches.

If you need specific steps for a task (e.g., creating a job, configuring MFT, or using the API), let me know, and I can provide a more detailed walkthrough!