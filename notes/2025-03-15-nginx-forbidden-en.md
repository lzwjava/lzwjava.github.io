---
title: "Fixing Nginx 403 Forbidden Error"
lang: en
layout: post
audio: false
translated: false
generated: true
---

To fix the "403 Forbidden" error you're encountering with your Nginx configuration, you need to address two primary issues: an incorrect use of the `root` directive in your `location` block and potential file system permission problems. Below is a step-by-step guide to resolve the issue based on your provided configuration:

```nginx
server {
    listen 80;
    server_name localhost;
    location /movies {
        root /path/to/your/movie/folder;
        autoindex on; # Enables directory listing
    }
}
```

When you visit `http://localhost/movies`, you get a 403 Forbidden error, which typically indicates that Nginx cannot access or serve the intended directory. Here's how to fix it:

---

### 1. Correct the Nginx Configuration
The current `location /movies` block uses `root /path/to/your/movie/folder;`. In Nginx, the `root` directive appends the request URI (e.g., `/movies`) to the specified path, meaning Nginx tries to serve files from `/path/to/your/movie/folder/movies`. If this directory doesn’t exist, Nginx returns a 403 error.

To fix this, you should use the `alias` directive instead of `root`. The `alias` directive maps the `/movies/` URI directly to `/path/to/your/movie/folder/` without appending the URI, which is likely your intended behavior.

Update your configuration as follows:

```nginx
server {
    listen 80;
    server_name localhost;
    location /movies/ {
        alias /path/to/your/movie/folder/;
        autoindex on; # Enables directory listing
    }
}
```

- **Key Changes:**
  - Changed `root` to `alias`.
  - Added trailing slashes to `location /movies/` and `alias /path/to/your/movie/folder/` to ensure proper directory handling with `autoindex`.

- **Apply the Changes:**
  After updating the configuration file (e.g., `/etc/nginx/nginx.conf` or a file in `/etc/nginx/sites-enabled/`), restart Nginx to apply the changes:
  - On Linux: `sudo systemctl restart nginx`
  - On Windows: Stop and start the Nginx service manually.

- **Test the URL:**
  Visit `http://localhost/movies/` (note the trailing slash) to see if the directory listing appears.

---

### 2. Check File System Permissions
If the configuration change alone doesn’t resolve the 403 error, the issue might be related to file system permissions. Nginx needs read access to `/path/to/your/movie/folder/` and its contents, and this access depends on the user under which Nginx is running (commonly `nginx` or `www-data`).

- **Identify the Nginx User:**
  Check your main Nginx configuration file (e.g., `/etc/nginx/nginx.conf`) for the `user` directive. It might look like:
  ```nginx
  user nginx;
  ```
  If not specified, it could default to `www-data` or another user depending on your system.

- **Verify Permissions:**
  Run the following command to inspect the permissions of your movie folder:
  ```bash
  ls -l /path/to/your/movie/folder
  ```
  This will display the owner, group, and permissions (e.g., `drwxr-xr-x`).

- **Adjust Permissions if Needed:**
  Ensure the Nginx user has read (and execute for directories) access. Here are two options:
  - **Option 1: Change Ownership (Recommended):**
    Set the folder’s owner to the Nginx user (e.g., `nginx`):
    ```bash
    sudo chown -R nginx:nginx /path/to/your/movie/folder
    ```
    Replace `nginx` with the actual user if it’s different (e.g., `www-data`).

  - **Option 2: Make Readable by All (Less Secure):**
    If you don’t want to change ownership, make the folder readable by others:
    ```bash
    sudo chmod -R o+r /path/to/your/movie/folder
    ```

- **Ensure Directory Access:**
  The directory itself needs execute permissions (`x`) for Nginx to access its contents:
  ```bash
  sudo chmod o+x /path/to/your/movie/folder
  ```

- **Check Parent Directories:**
  If `/path/to/your/movie/folder` is within a restricted parent directory (e.g., `/home/user/`), ensure all parent directories up to the root have execute permissions for the Nginx user:
  ```bash
  sudo chmod o+x /path /path/to /path/to/your /path/to/your/movie
  ```

---

### 3. Verify and Troubleshoot
After making these changes, test again by visiting `http://localhost/movies/`. If the 403 error persists:

- **Check the Nginx Error Log:**
  Review the error log for specific details (typically located at `/var/log/nginx/error.log`):
  ```bash
  sudo tail -f /var/log/nginx/error.log
  ```
  Look for messages like “permission denied” or “directory index is forbidden” to pinpoint the issue.

- **Additional Considerations:**
  - **SELinux (if applicable):** On systems like CentOS with SELinux enabled, it might block access. Temporarily set SELinux to permissive mode to test:
    ```bash
    sudo setenforce 0
    ```
    If this resolves the issue, you’ll need to adjust SELinux policies (e.g., using `chcon` or `audit2allow`).
  - **Firewall:** Ensure port 80 is open if accessing from another machine (though unlikely if testing locally via `localhost`).

---

### Final Configuration
Here’s the corrected and complete configuration:

```nginx
server {
    listen 80;
    server_name localhost;
    location /movies/ {
        alias /path/to/your/movie/folder/;
        autoindex on; # Enables directory listing
    }
}
```

- Replace `/path/to/your/movie/folder/` with the actual absolute path to your movie directory.
- Restart Nginx: `sudo systemctl restart nginx`.
- Visit `http://localhost/movies/` to confirm the directory listing works.

By correcting the `alias` directive and ensuring proper file permissions, the 403 Forbidden error should be resolved, allowing you to access your movie folder via Nginx successfully.