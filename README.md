# Port Scanner

An educational network security tool developed in Python for port scanning. This project demonstrates network reconnaissance by implementing a dual-stack TCP scanner that queries administrative and standard service ports in the range of $1$ to $1024$.

---
## 1. Reconnaissance Logic

To optimize performance and reliability in modern network environments, the script operates under the following mechanisms:

- **Dual-Stack Resolution:** Before starting the scan, the program performs an automatic validation of the Internet Protocol (IP) version. It dynamically binds the correct socket configuration (`socket.AF_INET` or `socket.AF_INET6`) based on the format of the destination address, without requiring manual user intervention.
- **TCP Connection Scan:** The script performs the three-way TCP handshake using Python's native `socket` library. It attempts to connect to each designated port within the established range to determine its current state.

### 1.1 Technical and Mathematical Operation

The scanner utilizes the low-level `socket.connect_ex()` method to attempt the connection. The program does not use exception handling for failures; instead, this method returns a numerical error code:

- A return code of $0$ indicates a successful connection, meaning the destination port is active and open.
- Any non-zero return value indicates a connection failure, signaling that the port is closed or blocked.

During the connection attempts, the `for port in range(1, 1025)` loop defines the subset of ports to be tested. The `range` method generates a half-open interval:

$$P = \{x \in \mathbb{Z} \mid 1 \le x < 1025\}$$

- $P = 1024$ represents the cardinality of the set of intervals of well-known ports, reserved for essential web services.

To optimize scanning speed and prevent the program from hanging indefinitely when encountering ports with dropped packets or protected by security systems, a strict connection timeout ($T$) is applied:

$$T = 0.5 \text{ seconds}$$

This ensures that the total port scanning time remains predictable and highly efficient.

---
## 2. Features

- **Stylized Command Line:** Uses the external `pyfiglet` library to customize the command-line interface (CLI).
- **Robust Input Sanitization:** Uses the native `ipaddress` library to validate the target's IP format before starting network connections, preventing execution failures due to invalid address types.
- **No External Network Dependencies:** Built entirely on Python's standard networking library, ensuring a lightweight and secure execution.

---
## 3. Prerequisites

To run this script, **Python 3.10** or newer must be installed on your machine due to the use of the `match-case` control flow structure.

- **Dependency Installation:** The only external dependency required is the `pyfiglet` library. Install it by running the command below in your terminal:
    - `pip install pyfiglet`
- **Execution:** Clone the repository or download the `port_scanner.py` file. Then, navigate to the file's folder in the terminal and run:
    - `python port_scanner.py`

### 3.1 Disclaimer

This tool was developed exclusively for **educational, research, and security awareness purposes**.

- Scanning networks or systems without prior and explicit authorization from the infrastructure owner can be considered a malicious activity and is illegal in several jurisdictions.
- The author of this software is not responsible for any damages, security incidents, or legal consequences resulting from the improper or malicious use of this tool.
- Use responsibly and only on networks or environments you own or where you have express authorization to test.
