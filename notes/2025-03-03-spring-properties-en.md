---
audio: false
lang: en
layout: post
title: Property File Selection in Spring Boot
translated: false
generated: true
---

In a Spring Boot Maven project, you have two properties files, `appProperties.properties` and `appProperties-hk.properties`, located under `src/main/resources`. To control which properties file is used, particularly to specify the use of the `-hk` properties, you can leverage Spring Boot's configuration mechanisms. Here's how you can do it:

### Solution

1. **Create an `application.properties` File**
   - By default, Spring Boot looks for `application.properties` or `application.yml` in `src/main/resources` to load configuration settings.
   - To use your custom properties files (`appProperties.properties` and `appProperties-hk.properties`), you need to inform Spring Boot to look for files with the base name `appProperties` instead of the default `application`.
   - Add the following line to a new `application.properties` file in `src/main/resources`:

     ```properties
     spring.config.name=appProperties
     ```

   - This setting tells Spring Boot to load `appProperties.properties` as the base configuration file, and it will also automatically look for profile-specific variants like `appProperties-{profile}.properties` when a profile is active.

2. **Use Spring Profiles to Specify the `-hk` Properties**
   - Spring Boot supports profiles, which allow you to load additional or overriding properties files based on the active profile.
   - Since your file is named `appProperties-hk.properties`, it follows the pattern `appProperties-{profile}.properties`. Here, "hk" can be treated as a profile name.
   - To use `appProperties-hk.properties`, activate the "hk" profile when running your application. Spring Boot will then load both `appProperties.properties` and `appProperties-hk.properties`, with properties in `appProperties-hk.properties` overriding any matching properties in `appProperties.properties`.

3. **How to Activate the "hk" Profile**
   - **Via Command Line**: When running your Spring Boot application, specify the active profile using the `--spring.profiles.active` argument. For example:
     ```bash
     java -jar target/myapp.jar --spring.profiles.active=hk
     ```
     Replace `myapp.jar` with the name of your application's JAR file generated by Maven.

   - **Via Maven**: If you're running the application using the `spring-boot:run` goal, configure the profile in your `pom.xml`:
     ```xml
     <plugin>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-maven-plugin</artifactId>
         <configuration>
             <profiles>
                 <profile>hk</profile>
             </profiles>
         </configuration>
     </plugin>
     ```
     Then run:
     ```bash
     mvn spring-boot:run
     ```

   - **Via System Property**: Set the profile as a JVM argument:
     ```bash
     java -Dspring.profiles.active=hk -jar target/myapp.jar
     ```

   - **Via Environment Variable**: Export the profile in your environment (e.g., in a Unix-like system):
     ```bash
     export SPRING_PROFILES_ACTIVE=hk
     java -jar target/myapp.jar
     ```

### How It Works
- With `spring.config.name=appProperties` set in `application.properties`, Spring Boot uses `appProperties` as the base name for configuration files.
- When no profile is active, only `appProperties.properties` is loaded.
- When the "hk" profile is activated (e.g., via `--spring.profiles.active=hk`), Spring Boot loads both `appProperties.properties` and `appProperties-hk.properties`. Properties defined in `appProperties-hk.properties` take precedence over those in `appProperties.properties` if there are any duplicates.

### Final Steps
- Ensure both `appProperties.properties` and `appProperties-hk.properties` are in `src/main/resources`.
- Add `application.properties` with `spring.config.name=appProperties` to `src/main/resources`.
- Run your application with the "hk" profile activated to use the `-hk` properties.

This approach aligns with Spring Boot conventions, making it a typical and straightforward way to control which properties file is used in your project. To specifically use the `-hk` properties, simply activate the "hk" profile as described above.