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

---

You’re correct—WebSphere Liberty’s `securityUtility` tool does not provide a `decode` option. The `securityUtility` command is designed primarily for encoding passwords (e.g., `securityUtility encode`) and creating security-related artifacts like SSL certificates or LTPA keys, but it lacks a direct `decode` function for AES-encrypted passwords. This is intentional, as decoding sensitive data like passwords outside the server’s runtime environment could pose a security risk, and WebSphere expects the server itself to handle decryption internally when using the encrypted password.

However, you can still decode an AES-encrypted password like `{aes}YSPuwMQqjeo/DlSNYnUZ3E6z6WLVmEaAtDmMaFg6JCY=` from your `server.xml` file by leveraging WebSphere’s APIs programmatically within the Liberty runtime or by resetting the password if decoding isn’t feasible. Here’s how you can address this:

---

### Why `decode` Isn’t Available
- The `securityUtility` tool supports `encode` with options like `--encoding=aes` to encrypt passwords, but decoding is restricted because the AES encryption key is tied to the Liberty server instance (either a default key or a custom one defined via `wlp.password.encryption.key`). Allowing arbitrary decoding via a command-line tool could expose sensitive data if the key were compromised.
- Liberty handles decryption automatically when it uses the password (e.g., in a datasource configuration), so manual decoding isn’t typically necessary for server operation.

---

### Options to Decode the Password

#### 1. **Use a Java Program with `PasswordUtil` in Liberty**
Since `securityUtility` doesn’t offer a `decode` option, you can write a small Java program using the `com.ibm.websphere.crypto.PasswordUtil` class, which Liberty provides for encoding and decoding passwords. This must run within the Liberty server’s runtime environment to access the correct encryption key.

Here’s an example:

```java
import com.ibm.websphere.crypto.PasswordUtil;

public class DecodeAesPassword {
    public static void main(String[] args) {
        String encryptedPassword = "{aes}YSPuwMQqjeo/DlSNYnUZ3E6z6WLVmEaAtDmMaFg6JCY=";
        try {
            String decryptedPassword = PasswordUtil.decode(encryptedPassword);
            System.out.println("Decrypted Password: " + decryptedPassword);
        } catch (Exception e) {
            System.err.println("Error decoding password: " + e.getMessage());
        }
    }
}
```

- **Steps**:
  1. Compile this code with Liberty’s runtime libraries in the classpath (e.g., `wlp/lib/ws_runtime.jar`).
  2. Deploy and run it as a simple application on the same Liberty server where the password was encrypted. This ensures it uses the correct encryption key (default or custom).
  3. Check the output for the plaintext password.

- **Requirements**:
  - Access to the Liberty server’s runtime environment.
  - If a custom key was used (e.g., `<variable name="wlp.password.encryption.key" value="yourCustomKey"/>` in `server.xml`), ensure the program runs in that server context.

#### 2. **Check Logs or Debugging Output**
If you don’t need to decode programmatically but just want to verify the password:
- Temporarily enable trace logging in Liberty to see if the decrypted password is logged during datasource initialization.
- Update `server.xml` with:
  ```xml
  <logging traceSpecification="com.ibm.ws.jdbc.*=all"/>
  ```
- Restart the server and check logs (e.g., `messages.log` or `trace.log`) for JDBC connection attempts. Be cautious, as this might expose sensitive data in logs.

#### 3. **Reset the Password (If Decoding Isn’t Possible)**
If you can’t run a program in the Liberty environment (e.g., no development access), reset the Oracle user’s password and re-encrypt it:
- Connect to the Oracle database as a privileged user (e.g., `SYS` or `SYSTEM`):
  ```sql
  ALTER USER myuser IDENTIFIED BY newpassword123;
  ```
- Encode the new password with `securityUtility`:
  ```bash
  bin/securityUtility encode --encoding=aes "newpassword123"
  ```
  Output might be: `{aes}NewEncryptedValueHere`
- Update `server.xml` with the new encrypted value:
  ```xml
  <properties.oracle url="jdbc:oracle:thin:@//localhost:1521/ORCL" 
                  user="myuser" 
                  password="{aes}NewEncryptedValueHere"/>
  ```
- Restart Liberty and test the connection.

---

### Verifying the Current Password
If you suspect the encrypted password matches a known plaintext value, you can encode the suspected plaintext and compare:
```bash
bin/securityUtility encode --encoding=aes "suspectedpassword"
```
- If the output matches `{aes}YSPuwMQqjeo/DlSNYnUZ3E6z6WLVmEaAtDmMaFg6JCY=`, then `suspectedpassword` is the correct plaintext.

---

### Key Notes
- **Custom Key**: If a custom `wlp.password.encryption.key` was used when the password was encrypted, decoding outside the server context is impossible without that key. Check `server.xml` or `bootstrap.properties` for:
  ```xml
  <variable name="wlp.password.encryption.key" value="yourCustomKey"/>
  ```
  You’d need to replicate the environment or use the Java approach above.
- **Default Key**: If no custom key was set, Liberty uses a default key, but this is still only accessible within the server runtime, not via `securityUtility`.

Since `securityUtility decode` isn’t an option, the Java program is your best bet if you need the original password. If that’s not feasible, resetting it is the simplest workaround. Let me know which approach you’d like to pursue or if you need help with the setup!

---

In WebSphere Liberty, when a custom key is specified with `<variable name="wlp.password.encryption.key" value="yourCustomKey"/>` in `server.xml`, it refers to a user-defined **plaintext encryption key** (a string), not a keystore file (like a `.keystore` or `.p12` file) or a cryptographic key from a `server.properties` file. This custom key is used by Liberty’s AES encryption mechanism to encrypt and decrypt sensitive data, such as passwords in `server.xml`. It’s distinct from SSL/TLS keystores or other key management systems like JKS or PKCS12 files, which are typically used for securing network communication rather than password encryption.

Let me clarify what this "custom key" means and how it relates to your question:

---

### What is the Custom Key (`wlp.password.encryption.key`)?
- **Definition**: The `wlp.password.encryption.key` is a variable that specifies a custom string (e.g., `yourCustomKey`) used as the encryption key for AES password encryption in Liberty. This overrides the default encryption key that Liberty generates internally.
- **Purpose**: It allows administrators to control the encryption key explicitly, ensuring that encrypted values (like `{aes}YSPuwMQqjeo/DlSNYnUZ3E6z6WLVmEaAtDmMaFg6JCY=`) are portable across servers or reproducible, provided the same custom key is used.
- **Format**: It’s a plaintext string, not a file reference or a cryptographic key in a keystore. For example:
  ```xml
  <variable name="wlp.password.encryption.key" value="mySecretKey123"/>
  ```
- **Usage**: When you run `securityUtility encode --encoding=aes "myPassword"` with a custom key defined, Liberty uses that key instead of its default key to generate the encrypted output.

---

### Is It Related to `server.properties`, `.keystore`, or `.p12` Files?
- **No, it’s not a keystore or `.p12` file**: Keystores (e.g., JKS or PKCS12 `.p12` files) are used in Liberty for SSL/TLS configurations (e.g., `<keyStore id="defaultKeyStore" .../>` in `server.xml`) to store certificates and private keys for secure communication. The `wlp.password.encryption.key` is unrelated to these; it’s specifically for encrypting configuration data like passwords.
- **No direct relation to `server.properties`**: There’s no standard `server.properties` file in Liberty. You might be thinking of `bootstrap.properties` or `jvm.options`, which are optional configuration files:
  - **Bootstrap.properties**: You *could* define the custom key here instead of `server.xml`, like this:
    ```
    wlp.password.encryption.key=mySecretKey123
    ```
    Liberty would then use this value for AES encryption/decryption.
  - However, `wlp.password.encryption.key` is typically set in `server.xml` as a `<variable>` element, not tied to a keystore or properties file unless explicitly configured that way.

---

### How the Custom Key Works in Context
- **Default Behavior**: If `wlp.password.encryption.key` is not specified, Liberty generates an internal default key unique to the server instance. This key isn’t exposed and is managed internally, making encrypted passwords non-portable across servers.
- **Custom Key**: When you define `wlp.password.encryption.key`, Liberty uses that string as the AES encryption key. For example:
  ```xml
  <variable name="wlp.password.encryption.key" value="mySecretKey123"/>
  ```
  Then, running:
  ```bash
  bin/securityUtility encode --encoding=aes "myPassword"
  ```
  produces an AES-encrypted value based on `mySecretKey123`. The same key must be present to decrypt it (e.g., via a Java program running in that server context).

---

### Decoding with a Custom Key
Since `securityUtility` doesn’t offer a `decode` option, you need to use a Java program like the one I provided earlier (`PasswordUtil.decode`), and it must run in the Liberty server context where the custom key is defined. Here’s why:
- The `PasswordUtil` class automatically retrieves the `wlp.password.encryption.key` value from the server’s configuration (e.g., `server.xml` or `bootstrap.properties`) when running in that environment.
- If you run the program outside the server context, you’d need to manually supply the custom key, but `PasswordUtil` doesn’t provide a public API to pass the key directly—it relies on the runtime configuration.

Updated Java example with context awareness:
```java
import com.ibm.websphere.crypto.PasswordUtil;

public class DecodeAesPassword {
    public static void main(String[] args) {
        String encryptedPassword = "{aes}YSPuwMQqjeo/DlSNYnUZ3E6z6WLVmEaAtDmMaFg6JCY=";
        try {
            String decryptedPassword = PasswordUtil.decode(encryptedPassword);
            System.out.println("Decrypted Password: " + decryptedPassword);
        } catch (Exception e) {
            System.err.println("Error decoding password: " + e.getMessage());
        }
    }
}
```
- **Run this**:
  - Deploy it as a simple app on the Liberty server with the custom key defined.
  - Ensure the `server.xml` includes `<variable name="wlp.password.encryption.key" value="yourCustomKey"/>`.
  - The program will use `yourCustomKey` to decrypt the password.

---

### Answering Your Question Directly
- **Custom key ≠ `.keystore` or `.p12`**: It’s not a reference to a keystore file or a cryptographic key in a `.p12` format. It’s a plaintext string you define.
- **Not tied to `server.properties`**: Liberty doesn’t use a `server.properties` file by default, but you could define the key in `bootstrap.properties` if preferred. Typically, it’s in `server.xml`.

---

### What to Do Next
1. **Check for the Custom Key**:
   - Look in your `server.xml` for:
     ```xml
     <variable name="wlp.password.encryption.key" value="yourCustomKey"/>
     ```
   - Or in `bootstrap.properties` for:
     ```
     wlp.password.encryption.key=yourCustomKey
     ```
   - If it’s not defined, Liberty used a default key, and decoding requires running in the server context.

2. **Decode the Password**:
   - Use the Java program above, executed on the Liberty server with the custom key configured.
   - If you know the custom key (e.g., `yourCustomKey`), you can also test encoding a suspected plaintext password to see if it matches the encrypted value:
     ```bash
     bin/securityUtility encode --encoding=aes --key=yourCustomKey "suspectedPassword"
     ```

3. **Fallback**: If decoding isn’t practical, reset the Oracle password and re-encrypt it with `securityUtility` using the same custom key.

Let me know if you’ve found the custom key in your setup or need help running the Java code!