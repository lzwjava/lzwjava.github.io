void setup() {
  // Initialize Serial communication at 9600 baud rate
  Serial.begin(9600);
  // Wait for Serial to connect (optional, mainly for some boards like Leonardo)
  while (!Serial) {
    ;
  }
  Serial.println("Starting Fibonacci LED Blink...");
  
  // Set the built-in LED pin (pin 13) as output
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // First 8 Fibonacci numbers (in seconds)
  int fib[] = {0, 1, 1, 2, 3, 5, 8, 13};
  static int index = 0; // Current position in the sequence
  static bool forward = true; // Direction of traversal (true: forward, false: backward)
  
  // Get the current delay in seconds and convert to milliseconds
  int delaySeconds = fib[index];
  int delayMs = delaySeconds * 1000;

  // Log the current state
  Serial.print("Index: ");
  Serial.print(index);
  Serial.print(", Delay: ");
  Serial.print(delaySeconds);
  Serial.print("s, Direction: ");
  Serial.println(forward ? "Forward" : "Backward");

  // Turn the LED on
  digitalWrite(LED_BUILTIN, HIGH);
  delay(delayMs); // Wait for the Fibonacci duration

  // Turn the LED off
  digitalWrite(LED_BUILTIN, LOW);
  delay(delayMs); // Wait for the same Fibonacci duration

  // Update the index based on direction
  if (forward) {
    index++;
    if (index == 8) { // Reached the end (13), switch to backward
      index = 7; // Start from 13 again
      forward = false;
      Serial.println("Switching to Backward");
    }
  } else {
    index--;
    if (index == -1) { // Reached the start (0), switch to forward
      index = 0; // Start from 0 again
      forward = true;
      Serial.println("Switching to Forward");
    }
  }
}