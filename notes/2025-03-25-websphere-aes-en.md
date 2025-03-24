---
title: Websphere AES Password
lang: en
layout: post
audio: false
translated: false
generated: true
---

In WebSphere Application Server, passwords in configuration files like `server.xml` (for Liberty) or other XML configuration files (e.g., `resources.xml`, `security.xml` in traditional WebSphere) are often encrypted using AES (Advanced Encryption Standard) when security utilities are employed. If the password in your `server.xml` file for an Oracle JDBC datasource is in AES-encrypted format, it typically appears with an `{aes}` prefix, such as `{aes}YSPuwMQqjeo/DlSNYnUZ3E6z6WLVmEaAtDmMaFg6JCY=`. To decode this password, you need to use WebSphere's built-in tools or APIs, as the encryption is tied to a specific encryption key managed by the server.

Here’s how you can decode an AES-encrypted password from a WebSphere `server.xml` file:

### Steps to Decode the Password

1. **Understand the Encryption Context**  
   WebSphere Liberty (and traditional WebSphere) uses an encryption key stored in the server's configuration to encrypt and decrypt sensitive data like passwords. In Liberty, this key is typically managed via the `securityUtility` tool or embedded in the server's configuration. The AES-encrypted password cannot be decrypted without access to this key, which is unique to the WebSphere instance.

2. **Locate the Encrypted Password**  
   In your `server.xml` file, find the Oracle JDBC datasource configuration. It might look something like this:
   ```xml
   <dataSource id="oracleDS" jndiName="jdbc/oracleDS">
       <jdbcDriver libraryRef="OracleLib"/>
       <properties.oracle url="jdbc:oracle:thin:@//localhost:1521/ORCL" 
                       user="myuser" 
                       password="{aes}YSPuwMQqjeo/DlSNYnUZ3E6z6WLVmEaAtDmMaFg6JCY="/>
   </dataSource>
   ```
   The `password` attribute contains the AES-encrypted value.

3. **Use WebSphere Liberty’s `securityUtility` Tool**  
   WebSphere Liberty provides the `securityUtility` command-line tool to encode and decode passwords. To decode an AES-encrypted password:
   - Navigate to your WebSphere Liberty installation directory (e.g., `/opt/ibm/wlp`).
   - Run the `securityUtility` command with the `decode` option:
     ```bash
     bin/securityUtility decode --encoding=aes "YSPuwMQqjeo/DlSNYnUZ3E6z6WLVmEaAtDmMaFg6JCY="
     ```
   - **Important Note**: You must run this command from the specific Liberty server instance where the password was originally encrypted, as it relies on the server’s encryption key (stored in files like `bootstrap.properties` or `server.xml` under the `keyStore` configuration). If the key has been customized, you may need to specify the `--key` parameter with the encryption key value.

   If successful, the tool will output the decrypted password.

4. **Alternative: Use a Java Program with WebSphere APIs**  
   If you’re working with a traditional WebSphere Application Server or need programmatic access, you can use the `com.ibm.websphere.crypto.PasswordUtil` class to decode the password. Here’s an example:
   ```java
   import com.ibm.websphere.crypto.PasswordUtil;

   public class DecodePassword {
       public static void main(String[] args) {
           String encodedPassword = "{aes}YSPuwMQqjeo/DlSNYnUZ3E6z6WLVmEaAtDmMaFg6JCY=";
           try {
               String decodedPassword = PasswordUtil.decode(encodedPassword);
               System.out.println("Decoded Password: " + decodedPassword);
           } catch (Exception e) {
               System.err.println("Error decoding password: " + e.getMessage());
           }
       }
   }
   ```
   - **Requirements**: 
     - This must be run in an environment with WebSphere libraries (e.g., `ws_runtime.jar`) in the classpath.
     - The program must execute within the WebSphere server context or have access to the encryption key used by the server.
     - For traditional WebSphere, you can find the required JARs in `<WAS_HOME>/AppServer/plugins/`.

5. **Handling Key Management**  
   - In Liberty, the default AES key is derived from the server’s configuration. If a custom key was used (e.g., specified in `server.xml` via `<variable name="wlp.password.encryption.key" value="yourCustomKey"/>`), you’ll need to provide it to the `securityUtility` tool or your Java code.
   - In traditional WebSphere, the encryption key is tied to the `SerializedSystemIni` service, and decoding must occur within the server’s runtime environment.

6. **Verify the Decoded Password**  
   Once decoded, test the password by connecting to the Oracle database using a tool like SQL*Plus or a simple JDBC test program to ensure it works:
   ```java
   import java.sql.Connection;
   import java.sql.DriverManager;

   public class TestJDBC {
       public static void main(String[] args) throws Exception {
           String url = "jdbc:oracle:thin:@//localhost:1521/ORCL";
           String user = "myuser";
           String password = "decoded_password_here";
           Connection conn = DriverManager.getConnection(url, user, password);
           System.out.println("Connection successful!");
           conn.close();
       }
   }
   ```

### Key Considerations
- **Security**: Decoding passwords exposes sensitive information, so perform this operation in a secure environment and avoid logging or storing the plaintext password unnecessarily.
- **Server-Specific Encryption**: The AES encryption is tied to the specific WebSphere instance. You cannot decode the password on a different server unless you replicate the encryption key and configuration.
- **Liberty vs. Traditional WebSphere**: The process differs slightly between Liberty and traditional WebSphere. Liberty relies on `securityUtility`, while traditional WebSphere often uses the `PasswordDecoder` class or similar utilities.

If you’re unable to decode the password (e.g., due to missing keys or incorrect server context), you may need to re-encrypt a new password using the same WebSphere instance and update the `server.xml` file accordingly. Let me know if you need further assistance with your specific setup!