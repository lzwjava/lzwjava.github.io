---
title: Hide Errors (Red Lines) in VSCode for Your Project
lang: en
layout: post
audio: false
translated: false
generated: true
---

In Visual Studio Code (VSCode), the red underlines (error indicators) in a Java Spring Framework project using Gradle are typically shown by the **Java Extension Pack** (which includes the Language Support for Java by Red Hat). These errors come from the Java language server analyzing your code. To suppress these errors (red lines) without fixing the underlying issues, you can adjust settings at the project or workspace level. Here’s how to do it:

### Steps to Hide Errors (Red Lines) in VSCode for Your Project

#### Option 1: Disable Java Problem Reporting for the Project
1. **Open VSCode Settings**
   - Go to `File > Preferences > Settings` (or press `Ctrl + ,` on Windows/Linux, `Cmd + ,` on macOS).

2. **Search for Java Problems**
   - In the search bar at the top of the Settings UI, type `java.errors` or `java.diagnostics`.

3. **Modify the Severity**
   - Look for the setting **Java > Errors: Severity** or **Java > Diagnostics: Enable**.
   - Change the severity of errors from `"Error"` to `"Warning"` or `"Info"`. This won’t remove the underlines entirely but will make them less prominent (e.g., yellow instead of red).
   - Alternatively, if there’s an option like **Java: Diagnostics: Enable**, uncheck it to disable diagnostics entirely (this might not be available in all versions).

4. **Apply to Workspace**
   - To apply this only to your current project, click the "Workspace" tab in the Settings UI before making changes. This ensures the setting is saved in `.vscode/settings.json` for the project rather than globally.

#### Option 2: Edit `.vscode/settings.json` Directly
1. **Open Workspace Settings File**
   - In your project root, check if there’s a `.vscode` folder. If not, create one.
   - Inside `.vscode`, open or create a file called `settings.json`.

2. **Add Configuration to Suppress Errors**
   - Add the following lines to `settings.json`:
     ```json
     {
         "java.errors.incompleteClasspath.severity": "ignore",
         "java.completion.enabled": false,
         "java.validate.references": false,
         "java.diagnostics.enable": false
     }
     ```
   - Explanation:
     - `"java.errors.incompleteClasspath.severity": "ignore"`: Ignores errors related to missing dependencies or classpath issues (common in Gradle projects with failed builds).
     - `"java.completion.enabled": false`: Disables code completion, which can reduce error checking.
     - `"java.validate.references": false`: Stops reference validation, reducing "cannot find symbol" errors.
     - `"java.diagnostics.enable": false`: Disables all Java diagnostics (might not work in all versions; test this).

3. **Save and Reload**
   - Save the file and reload VSCode (`Ctrl + R` or `Cmd + R`) to apply the changes.

#### Option 3: Disable the Java Language Server Temporarily
1. **Disable the Java Extension**
   - Go to the Extensions view (`Ctrl + Shift + X` or `Cmd + Shift + X`).
   - Find **Language Support for Java(TM) by Red Hat**.
   - Click the gear icon and select "Disable (Workspace)" to turn it off only for this project.
   - Reload VSCode. This stops all Java-specific features (including error underlines) but keeps the editor functional for basic editing.

2. **Re-enable Later**
   - You can re-enable it when you’re ready to address the errors.

#### Option 4: Ignore Specific Files or Folders
- If the errors are in specific files or folders (e.g., generated code), you can exclude them:
  - In `.vscode/settings.json`, add:
    ```json
    {
        "files.exclude": {
            "**/path/to/problematic/files": true
        },
        "java.project.sourcePaths": [
            "src/main/java" // Adjust to include only valid source paths
        ]
    }
    ```
  - This hides files from the editor and prevents the Java language server from analyzing them.

#### Option 5: Fix Gradle Build (Alternative Suggestion)
- While you asked to hide errors, the "cannot find symbol" errors often mean Gradle didn’t download dependencies or the build failed. Running `gradle build` or `gradle dependencies` in the terminal might resolve some issues, reducing errors naturally. If you’d like help with that, let me know!

### Notes
- These changes might disable useful features like autocompletion or reference navigation alongside the errors.
- If you’re working in a team, avoid committing `.vscode/settings.json` to version control unless everyone agrees to suppress errors.
- To revert, simply delete or edit the `settings.json` file or re-enable the extension.

After applying one of these options, the red lines should disappear or become less intrusive. Let me know if you need further clarification!