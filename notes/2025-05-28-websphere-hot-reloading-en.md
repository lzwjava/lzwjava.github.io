---
title: Hot Reloading in WebSphere Liberty
lang: en
layout: post
audio: false
translated: false
generated: true
---

Hot reloading, or updating applications on a WebSphere Liberty Profile (WLP) server without restarting, is possible under certain conditions. Below, I outline the approaches to achieve this, focusing on the `defaultServer` and avoiding a full server restart using the `server start` command.

### Key Concepts for Hot Reloading in WebSphere Liberty
WebSphere Liberty supports dynamic application updates through mechanisms like the **dropins** directory, the **applicationMonitor** configuration, and tools like WebSphere Developer Tools (WDT). However, the extent of hot reloading depends on the type of application (e.g., WAR, EAR) and the changes made (e.g., code, configuration).

### 1. Using the `dropins` Directory for Hot Deployment
The `dropins` directory is the simplest way to enable hot reloading for applications in Liberty:
- **Location**: By default, the `dropins` directory is located at `wlp/usr/servers/defaultServer/dropins/`.
- **How it Works**: Place a WAR or EAR file in the `dropins` directory, and Liberty automatically detects and deploys it without a server restart. If you update the file (e.g., replace it with a new version), Liberty reloads the application dynamically.
- **Configuration**: Ensure the `applicationMonitor` element is enabled in the `server.xml` file (it is by default). For example:
  ```xml
  <applicationMonitor updateTrigger="mbean" dropins="dropins" pollingRate="5s"/>
  ```
  - `updateTrigger="mbean"`: Allows dynamic updates via MBean notifications.
  - `dropins="dropins"`: Specifies the directory to monitor.
  - `pollingRate="5s"`: Checks for changes every 5 seconds.
- **Limitations**:
  - Works best for simple WAR files or standalone applications.
  - If your application uses shared libraries or complex configurations (e.g., `enterpriseApplication`), the `dropins` directory may not support hot reloading effectively, as noted in a Stack Overflow discussion where shared libraries caused issues with `dropins`.[](https://stackoverflow.com/questions/41310638/simple-refresh-of-liberty-websphere-sphere-application-server-16-with-enterpris)
- **Steps**:
  1. Place your application (e.g., `myapp.war`) in `wlp/usr/servers/defaultServer/dropins/`.
  2. Liberty detects and deploys it automatically.
  3. Update the WAR file in the `dropins` directory to trigger a reload.

### 2. Using the `apps` Directory with `applicationMonitor`
For more control, you can use the `apps` directory with explicit configuration in `server.xml`:
- **Location**: `wlp/usr/servers/defaultServer/apps/`.
- **Configuration**: Add an `<application>` or `<enterpriseApplication>` element in `server.xml`. For example:
  ```xml
  <applicationManager autoExpand="true"/>
  <application id="MyApp" location="myapp.war" name="MyApp"/>
  ```
  - `autoExpand="true"`: Automatically expands WAR/EAR files for deployment.
- **Hot Reloading**:
  - Update the WAR/EAR file in the `apps` directory.
  - The `applicationMonitor` detects changes and reloads the application.
  - Set `updateTrigger="polled"` or `updateTrigger="mbean"` in the `applicationMonitor` element to control how updates are detected. For example:
    ```xml
    <applicationMonitor updateTrigger="polled" pollingRate="5s"/>
    ```
- **Note**: Unlike `dropins`, the `apps` directory supports shared libraries and complex configurations, but you must explicitly define the application in `server.xml`. If changes aren’t detected, ensure the `scanInterval` attribute is set appropriately, as discussed in a Stack Overflow post.[](https://stackoverflow.com/questions/41310638/simple-refresh-of-liberty-websphere-sphere-application-server-16-with-enterpris)

### 3. Using WebSphere Developer Tools (WDT)
For development environments, WDT (an Eclipse plugin) simplifies hot reloading:
- **How it Works**: WDT monitors your project for code or configuration changes and automatically updates the application on the Liberty server.
- **Setup**:
  1. Install WDT from the IBM WebSphere Developer Tools site (https://developer.ibm.com/wasdev/downloads/).[](https://stackoverflow.com/questions/41310638/simple-refresh-of-liberty-websphere-sphere-application-server-16-with-enterpris)
  2. Configure your Liberty server in Eclipse.
  3. Enable "Run in Development Mode" or use the `mvn liberty:dev` command for Maven projects, which starts the server in dev mode and auto-reloads changes.[](https://stackoverflow.com/questions/59218959/is-there-a-way-to-start-a-local-java-ibm-liberty-server-from-terminal)
- **Advantages**:
  - Supports hot reloading of Java classes, JSPs, and configuration files.
  - No manual file copying required.
- **Limitations**: Primarily for development, not production.

### 4. Maven Plugin for Development Mode
The Liberty Maven Plugin (`liberty:dev`) provides a convenient way to hot reload during development:
- **Command**: Run `mvn liberty:dev` in your project directory.
- **Behavior**: Starts the Liberty server in development mode, monitoring for code or configuration changes and automatically redeploying the application.
- **Setup**:
  1. Add the Liberty Maven Plugin to your `pom.xml`:
     ```xml
     <plugin>
         <groupId>io.openliberty.tools</groupId>
         <artifactId>liberty-maven-plugin</artifactId>
         <version>3.10</version>
     </plugin>
     ```
  2. Run `mvn liberty:dev` from the terminal.
- **Note**: This is ideal for local development and testing, as it eliminates the need for manual server restarts.[](https://stackoverflow.com/questions/59218959/is-there-a-way-to-start-a-local-java-ibm-liberty-server-from-terminal)

### 5. Limitations and Considerations
- **Complex Applications**: For `enterpriseApplication` with shared libraries, hot reloading may not work seamlessly in the `dropins` directory. Use the `apps` directory with explicit `server.xml` configuration instead.[](https://stackoverflow.com/questions/41310638/simple-refresh-of-liberty-websphere-sphere-application-server-16-with-enterpris)
- **JSP and Static Files**: Liberty supports hot reloading of JSPs and static resources (e.g., HTML, CSS) by default when using `applicationMonitor`.
- **Class Reloading**: Hot reloading of Java classes is limited. Significant changes (e.g., method signature changes) may require a server restart or advanced tools like JRebel.
- **Production Considerations**: Hot reloading is primarily for development. In production, changes should be thoroughly tested, and a controlled restart may be preferred for stability.
- **Default Server**: Since you mentioned `server start default`, ensure the server name is `defaultServer` (created automatically if no server is specified). Commands like `server start defaultServer` should be run from `wlp/bin/`.[](https://openliberty.io/docs/latest/reference/command/server-start.html)

### Steps to Enable Hot Reloading
1. **Verify Server Configuration**:
   - Ensure `server.xml` includes `<applicationManager autoExpand="true"/>`.
   - Add `<applicationMonitor updateTrigger="polled" pollingRate="5s"/>` for automatic scanning.
2. **Choose Directory**:
   - Use `dropins` for simple WAR files.
   - Use `apps` for EAR files or applications with shared libraries, and define them in `server.xml`.
3. **Update Application**:
   - Replace the WAR/EAR file in the chosen directory.
   - Alternatively, use WDT or `mvn liberty:dev` for development.
4. **Monitor Logs**:
   - Check `wlp/usr/servers/defaultServer/logs/console.log` for deployment updates or errors.[](https://openliberty.io/docs/latest/reference/command/server-start.html)

### Example `server.xml` for Hot Reloading
```xml
<server description="defaultServer">
    <featureManager>
        <feature>jsp-2.3</feature>
        <feature>servlet-4.0</feature>
    </featureManager>
    <httpEndpoint id="defaultHttpEndpoint" httpPort="9080" httpsPort="9443"/>
    <applicationManager autoExpand="true"/>
    <applicationMonitor updateTrigger="polled" pollingRate="5s"/>
    <application id="MyApp" location="myapp.war" name="MyApp"/>
</server>
```
- Place `myapp.war` in `wlp/usr/servers/defaultServer/apps/`.
- Update the WAR file, and Liberty reloads it within 5 seconds.

### Additional Notes
- **Clean Start**: If hot reloading fails due to cached data, you can start the server with the `--clean` option (`server start defaultServer -- --clean`) to clear cached data, but this requires a restart.[](https://stackoverflow.com/questions/40626266/how-to-forcefully-stop-websphere-liberty-server-in-windows-7)
- **Admin Console**: Liberty’s Admin Center (enabled with the `adminCenter-1.0` feature) allows basic application management but doesn’t support WAR deployment directly.[](https://stackoverflow.com/questions/28806073/how-to-start-admin-console-in-websphere-liberty-profile)
- **Debugging**: For development, start the server in debug mode via WDT or `server debug defaultServer` to troubleshoot issues.[](http://www.setgetweb.com/p/WAS85x/xx30.html)

If you need specific guidance (e.g., handling EAR files with shared libraries or integrating with a CI/CD pipeline), please provide more details about your application setup!