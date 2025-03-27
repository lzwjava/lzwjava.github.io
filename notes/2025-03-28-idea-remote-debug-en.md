---
title: IntelliJ IDEA's Built-in Remote Debugging
lang: en
layout: post
audio: false
translated: false
generated: true
---

To connect IntelliJ IDEA to the debug port of a WebSphere Liberty Server that you've started with `server debug default`, without using the WebSphere Liberty plugin, you can leverage IntelliJ IDEA's built-in remote debugging feature. This approach works because WebSphere Liberty, when started in debug mode, exposes a debug port (typically 7777 by default) that any JVM debugger, including IntelliJ IDEA, can attach to. Below are the detailed steps to achieve this:

---

### Step 1: Start the WebSphere Liberty Server in Debug Mode
When you run `server debug default` (assuming "default" is the name of your server; replace it with your actual server name if different), WebSphere Liberty starts with debugging enabled. By default, this command configures the server to listen for debug connections on port **7777**.

- **Command**: 
  ```bash
  server debug default
  ```
- **What it does**: This starts the "default" server in debug mode, automatically enabling JVM debugging options (e.g., `-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=7777`).
- **Verification**: After running the command, check the server console output or logs (e.g., `messages.log`) to confirm that the server is listening on the debug port. Look for a message indicating the debug port (usually 7777 unless it’s overridden or unavailable).

---

### Step 2: Confirm the Debug Port
The default debug port for WebSphere Liberty is **7777**. However, if this port is in use or has been customized:
- Check the console output after starting the server. It might say something like "Listening for debugger connections on port 7777."
- If the port differs (e.g., a random port is assigned due to a conflict), note the actual port number for use in IntelliJ IDEA.

For this guide, we’ll assume the default port **7777** unless your setup indicates otherwise.

---

### Step 3: Configure Remote Debugging in IntelliJ IDEA
IntelliJ IDEA’s remote debugging feature allows you to connect to the server’s JVM without needing a specific WebSphere plugin. Here’s how to set it up:

1. **Open Run/Debug Configurations**:
   - In IntelliJ IDEA, go to the top menu and select **Run > Edit Configurations**.

2. **Add a New Remote Debug Configuration**:
   - Click the **+** button (or "Add New Configuration") in the top-left corner.
   - From the list, select **Remote JVM Debug** (it might just say "Remote" depending on your IntelliJ version).

3. **Set Configuration Details**:
   - **Name**: Give it a meaningful name, e.g., "WebSphere Liberty Debug."
   - **Host**: Set to `localhost` (assuming the server runs on the same machine as IntelliJ IDEA; use the server’s IP address if it’s remote).
   - **Port**: Set to `7777` (or the actual debug port if different).
   - **Transport**: Ensure it’s set to **Socket**.
   - **Debugger Mode**: Select **Attach** (this tells IntelliJ to connect to an already-running JVM).
   - Leave other settings (like "Command line arguments for remote JVM") as default unless you need specific JVM options.

4. **Save the Configuration**:
   - Click **Apply** and then **OK** to save.

---

### Step 4: Start Debugging
With the server running in debug mode and the configuration set up:
- Go to **Run > Debug** (or click the bug icon) and select your new configuration (e.g., "WebSphere Liberty Debug").
- IntelliJ IDEA will attempt to attach to the server’s JVM on the specified host and port.
- If successful, you’ll see a message in the Debug window like "Connected to the target VM, address: 'localhost:7777'."

---

### Step 5: Debug Your Application
- **Set Breakpoints**: In your source code, click in the gutter next to the line numbers to add breakpoints where you want execution to pause.
- **Trigger Execution**: Interact with your application (e.g., send a request to the server) to hit the breakpoints.
- **Debug**: Once a breakpoint is hit, use IntelliJ’s debugging tools (step over, step into, resume, etc.) to inspect variables and control execution.

---

### Additional Notes
- **Local vs. Remote Server**: If WebSphere Liberty is running on a different machine, replace `localhost` with the server’s IP address in the remote debug configuration. Ensure the debug port (e.g., 7777) is open and not blocked by a firewall.
- **Port Conflicts**: If port 7777 is unavailable when the server starts, WebSphere Liberty might pick a random port. Check the server output to confirm the port and update the IntelliJ configuration accordingly.
- **No Plugin Needed**: This method uses IntelliJ IDEA’s standard remote debugging feature, so no WebSphere Liberty plugin is required.

---

### Summary
By starting your WebSphere Liberty Server with `server debug default` (which enables debugging on port 7777 by default) and configuring a remote debug setup in IntelliJ IDEA, you can connect to the server’s debug port without the WebSphere Liberty plugin. This gives you full debugging capabilities—breakpoints, variable inspection, and step-through execution—directly within IntelliJ IDEA.