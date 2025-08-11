import socket
import struct
import json
import time

class JavaAgentConnector:
    def __init__(self, host='localhost', port=8888):
        self.host = host
        self.port = port
        self.socket = None
    
    def connect(self):
        """Connect to Java agent"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            print(f"Connected to Java agent at {self.host}:{self.port}")
            return True
        except Exception as e:
            print(f"Failed to connect: {e}")
            return False
    
    def send_command(self, command, data=None):
        """Send command to Java agent"""
        if not self.socket:
            print("Not connected to agent")
            return None
        
        try:
            message = {
                'command': command,
                'data': data or {},
                'timestamp': int(time.time())
            }
            
            json_data = json.dumps(message).encode('utf-8')
            length = struct.pack('!I', len(json_data))
            
            self.socket.send(length + json_data)
            
            # Read response
            response_length = struct.unpack('!I', self.socket.recv(4))[0]
            response_data = self.socket.recv(response_length)
            
            return json.loads(response_data.decode('utf-8'))
        
        except Exception as e:
            print(f"Error sending command: {e}")
            return None
    
    def get_jvm_info(self):
        """Get JVM information"""
        return self.send_command('jvm_info')
    
    def get_memory_usage(self):
        """Get memory usage statistics"""
        return self.send_command('memory_usage')
    
    def get_thread_info(self):
        """Get thread information"""
        return self.send_command('thread_info')
    
    def disconnect(self):
        """Disconnect from agent"""
        if self.socket:
            self.socket.close()
            self.socket = None
            print("Disconnected from Java agent")

# Usage example
if __name__ == "__main__":
    agent = JavaAgentConnector()
    
    if agent.connect():
        # Get JVM info
        jvm_info = agent.get_jvm_info()
        print("JVM Info:", jvm_info)
        
        # Get memory usage
        memory = agent.get_memory_usage()
        print("Memory Usage:", memory)
        
        # Get thread info
        threads = agent.get_thread_info()
        print("Thread Info:", threads)
        
        agent.disconnect()