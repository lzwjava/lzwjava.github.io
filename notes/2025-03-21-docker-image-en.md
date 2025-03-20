---
title: "Building and Deploying a Docker Image"
lang: en
layout: post
audio: false
translated: false
generated: true
---

Here’s a step-by-step guide to building a Spring Boot application into a Docker image and deploying it on a server:

### Prerequisites
1. **Java** (e.g., JDK 17 or compatible version) installed locally.
2. **Maven** or **Gradle** (depending on your Spring Boot project setup).
3. **Docker** installed on your local machine and the server.
4. **A Spring Boot project** ready to containerize.
5. **Server access** (e.g., via SSH) with Docker installed.

---

### Step 1: Prepare Your Spring Boot Application
Ensure your Spring Boot application is working locally. Test it with:
```bash
mvn spring-boot:run  # If using Maven
# OR
gradle bootRun       # If using Gradle
```

Make sure the application builds successfully:
```bash
mvn clean package    # Maven
# OR
gradle build         # Gradle
```
This generates a `.jar` file (e.g., `target/myapp-1.0.0.jar`).

---

### Step 2: Create a Dockerfile
In your project’s root directory (where the `.jar` file is located), create a file named `Dockerfile` with the following content:

```dockerfile
# Use an official OpenJDK runtime as the base image
FROM openjdk:17-jdk-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Spring Boot JAR file into the container
COPY target/myapp-1.0.0.jar app.jar

# Expose the port your Spring Boot app runs on (default is 8080)
EXPOSE 8080

# Run the JAR file
ENTRYPOINT ["java", "-jar", "app.jar"]
```

**Notes:**
- Replace `myapp-1.0.0.jar` with the actual name of your JAR file.
- Adjust the Java version (`openjdk:17-jdk-slim`) if your app uses a different version.

---

### Step 3: Build the Docker Image
From the directory containing the `Dockerfile`, run:
```bash
docker build -t myapp:latest .
```
- `-t myapp:latest` tags the image as `myapp` with the `latest` version.
- The `.` tells Docker to use the current directory for the build context.

Verify the image was created:
```bash
docker images
```

---

### Step 4: Test the Docker Image Locally
Run the container locally to ensure it works:
```bash
docker run -p 8080:8080 myapp:latest
```
- `-p 8080:8080` maps port 8080 on your machine to port 8080 in the container.
- Open a browser or use `curl` to test (e.g., `curl http://localhost:8080`).

Stop the container with `Ctrl+C` or find its ID with `docker ps` and stop it:
```bash
docker stop <container-id>
```

---

### Step 5: Push the Image to a Docker Registry (Optional)
To deploy to a server, you’ll need to push the image to a registry like Docker Hub (or a private registry). If you skip this, you’ll transfer the image manually.

1. Log in to Docker Hub:
   ```bash
   docker login
   ```
2. Tag your image:
   ```bash
   docker tag myapp:latest yourusername/myapp:latest
   ```
3. Push the image:
   ```bash
   docker push yourusername/myapp:latest
   ```

---

### Step 6: Deploy to the Server
#### Option 1: Using a Registry
1. SSH into your server:
   ```bash
   ssh user@server-ip
   ```
2. Pull the image:
   ```bash
   docker pull yourusername/myapp:latest
   ```
3. Run the container:
   ```bash
   docker run -d -p 8080:8080 yourusername/myapp:latest
   ```
   - `-d` runs the container in detached mode (background).

#### Option 2: Manual Transfer
If you didn’t use a registry:
1. Save the image locally as a `.tar` file:
   ```bash
   docker save -o myapp.tar myapp:latest
   ```
2. Transfer it to the server (e.g., via SCP):
   ```bash
   scp myapp.tar user@server-ip:/path/to/destination
   ```
3. SSH into the server:
   ```bash
   ssh user@server-ip
   ```
4. Load the image:
   ```bash
   docker load -i myapp.tar
   ```
5. Run the container:
   ```bash
   docker run -d -p 8080:8080 myapp:latest
   ```

---

### Step 7: Verify Deployment
Check if the container is running:
```bash
docker ps
```

Test the app from the server or externally:
- If on the server: `curl http://localhost:8080`
- If external: Use the server’s IP (e.g., `http://server-ip:8080`), ensuring the port is open in the server’s firewall.

---

### Optional: Enhancements
- **Environment Variables**: Pass configs to your app:
  ```bash
  docker run -d -p 8080:8080 -e "SPRING_PROFILES_ACTIVE=prod" myapp:latest
  ```
- **Docker Compose**: For multi-container setups, use a `docker-compose.yml` file.
- **Restart Policy**: Add `--restart unless-stopped` to ensure the container restarts on server reboot.

Let me know if you need help with any specific part!