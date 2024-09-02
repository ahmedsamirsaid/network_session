# Task 1: Implementing a Reliable UDP Communication

- **Objective:** Develop both a server and a client to ensure reliable data transfer over UDP, including handling simulated connection losses.
- **Steps:**
  1. **Initialize:** Both the server and the client should start with an initial packet number set to 0, representing the last packet received.
  2. **Client Request:** The client should request the next packet by sending the current packet number to the server.
  3. **Server Response:** Upon receiving the request, the server should send the packet corresponding to the requested number.
  4. **Client Processing:** When the client receives the packet, it should increment the packet number and continue the process in a loop.
  5. **Connection Loss Simulation:** Introduce a mechanism to simulate packet loss or connection drops. The client should be able to detect when a packet is lost and re-request the same packet until it is successfully received. **Hint :** choose rondomly yo send the packet or not.

- **Goal:** Ensure that each packet is reliably received and acknowledged in the correct sequence, even in the presence of simulated connection losses.







# Task 2 Web server 
You will gain hands-on experience with socket programming in Python by implementing a basic web client and a multi-threaded web server. The goal is to understand the foundational concepts of HTTP and socket communication.

## Task Details

### Part 1: Multi-threaded Web Server

- **Objective:** Develop a multi-threaded web server in Python that handles basic HTTP requests.
- **Requirements:**
  - The server should accept incoming connections, handle `GET` and `POST` requests, and respond appropriately.
  - For `GET` requests, the server should fetch and send the requested file if it exists or return a 404 error if not.
  - For `POST` requests, the server should acknowledge and save the uploaded file.
  - Implement persistent connections and handle multiple requests over a single connection.
  - You may need to implement a multi-threaded using Python's threading.

### Part 2: HTTP Web Client

- **Objective:** Create a web client in Python that communicates with your server using the HTTP protocol.
- **Requirements:**
  - The client should handle `GET` and `POST` commands.
  - Establish a TCP connection with the server, send requests, and handle responses accordingly.
  - The client should store received files in the local directory and close the connection after all operations are completed.


### Part 3: Real Web server  

- **Test with Real Web Browser:** Test your server with a real web browser to ensure compatibility.

## Notes

- Use Python for development.
- This task should be completed in teams of two members.
