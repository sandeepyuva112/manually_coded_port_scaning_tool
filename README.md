# TCP Port Scanner

A simple and modular **TCP port scanner written in Python** for learning network scanning, TCP connections, port enumeration, input validation, logging, and report generation.

The scanner attempts TCP connections to specified ports and reports which ports are accepting connections.

> **For educational and authorized security testing only. Scan systems that you own or have explicit permission to test.**

---

## Features

- TCP connect-based port scanning
- Scan individual ports
- Scan multiple ports
- Scan port ranges
- Remove duplicate ports automatically
- IPv4 address validation
- Port-number validation
- Configurable log-file path
- Terminal output for open ports
- Text report generation
- Command-line interface
- Modular project structure
- Graceful handling of invalid input and scan cancellation

---

## How It Works

The scanner uses a TCP socket to attempt a connection to each requested port.

Conceptually:

```text
Target IP
    |
    v
Choose Port
    |
    v
Create TCP Socket
    |
    v
Attempt TCP Connection
    |
    +----------------------+
    |                      |
    v                      v
Connection succeeds    Connection fails
    |                      |
    v                      v
   OPEN                Not reported
```

A successful TCP connection indicates that the target port is accepting TCP connections.

---

## Architecture

```text
                         TCP PORT SCANNER
                                |
             +------------------+------------------+
             |                                     |
        Target Input                         Scan Configuration
             |                                     |
        IP Address                         Ports / Timeout
             |                                     |
             +------------------+------------------+
                                |
                                v
                         Scanner Engine
                                |
                                v
                         TCP Connection
                                |
                    +-----------+-----------+
                    |                       |
                    v                       v
               Connection              Timeout /
                succeeds                refused
                    |                       |
                    v                       v
                  OPEN                 Not OPEN
                    |
                    v
              Result Processing
                    |
          +---------+---------+
          |                   |
          v                   v
      Terminal             Report
       Output              Output
```

---

## Project Structure

```text
tcp_port_scanner/
│
├── tcp-port-scanner/
│   │
│   └── src/
│       │
│       ├── main.py
│       │
│       ├── scanner/
│       │   ├── __init__.py
│       │   ├── tcp_scanner.py
│       │   ├── connection.py
│       │   └── result.py
│       │
│       ├── utils/
│       │   ├── __init__.py
│       │   ├── validators.py
│       │   └── logger.py
│       │
│       └── output/
│           ├── __init__.py
│           ├── terminal.py
│           └── report.py
│
├── README.md
└── .gitignore
```

The project is intentionally divided into separate modules so that scanning, validation, logging, and output handling are not all implemented inside one file.

---

## Requirements

- Python 3.x
- Standard Python library

The scanner currently uses Python's built-in networking functionality, so no external scanning library is required.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/sandeepyuva112/tcp_port_scanner.git
```

Enter the project:

```bash
cd tcp_port_scanner
```

Enter the scanner directory:

```bash
cd tcp-port-scanner
```

Run the scanner with Python:

```bash
python src/main.py
```

---

## Usage

### Basic Scan

The default port range is `1-1024`.

```bash
python src/main.py 192.168.1.10
```

---

### Scan Specific Ports

```bash
python src/main.py 192.168.1.10 -p 22,80,443
```

---

### Scan a Port Range

```bash
python src/main.py 192.168.1.10 -p 8000-8010
```

---

### Scan Ports and Ranges Together

```bash
python src/main.py 192.168.1.10 -p 22,80,443,8000-8010
```

---

### Generate a Report

Use `--report` to create a text report containing the discovered open ports.

```bash
python src/main.py 192.168.1.10 -p 22,80,443 --report
```

The report is written to:

```text
open_ports_report.txt
```

---

### Specify a Log File

The scanner supports a custom log-file path:

```bash
python src/main.py 192.168.1.10 -p 22,80,443 --log scan.log
```

---

## Command-Line Options

```text
usage: main.py [-h] [-p PORTS] [-r] [-l LOG] ip
```

| Option | Description |
|---|---|
| `ip` | Target IPv4 address |
| `-p`, `--ports` | Ports or port ranges to scan |
| `-r`, `--report` | Generate a text report |
| `-l`, `--log` | Specify the log-file path |
| `-h`, `--help` | Show help information |

---

## Example

Command:

```bash
python src/main.py 172.29.36.93 -p 22,80,8000-8010 --report
```

Example output:

```text
Open Ports:
Port 22 is open.
Port 80 is open.
Report written to open_ports_report.txt
```

Generated report:

```text
Open Ports Report:
Port 22 is open.
Port 80 is open.
```

---

## Port Parsing

The scanner supports several formats.

### Single port

```text
22
```

### Multiple ports

```text
22,80,443
```

### Port range

```text
8000-8010
```

### Combination

```text
22,80,443,8000-8010
```

Duplicate ports are automatically removed before scanning.

---

## Input Validation

The scanner validates IPv4 addresses before starting the scan.

Example:

```text
192.168.1.10
```

is valid.

An invalid address such as:

```text
192.168.1.999
```

is rejected.

Ports are also checked against the valid TCP port range.

---

## Scanning Method

This project currently performs a **TCP connect scan**.

For each selected port, the scanner:

1. Creates a TCP socket.
2. Sets a connection timeout.
3. Attempts to connect to the target.
4. Checks the connection result.
5. Records the port when the connection succeeds.
6. Closes the socket.

The current scanner uses Python's `socket` module and `connect_ex()` for the connection attempt.

---

## Current Limitations

This project is intentionally simple and is still being developed.

Current limitations include:

- IPv4 address input only
- No hostname resolution interface
- Sequential port scanning
- Fixed connection timeout in the scanner
- Basic open/not-open result handling
- No service/banner detection
- Text reporting only
- No JSON or CSV output yet
- No concurrent scanning yet
- No advanced scan techniques

These limitations are part of the project's development roadmap rather than implemented features.

---

## Development History

The project was developed incrementally rather than as one large script.

Major development stages included:

```text
Initial project
      |
      v
Project structure
      |
      v
README and TCP concepts
      |
      v
Connection module
      |
      v
Result module
      |
      v
TCP scanner
      |
      v
Report generation
      |
      v
Terminal output
      |
      v
Logging
      |
      v
Input validation
      |
      v
Argument parsing
      |
      v
Integrated TCP scanner
```

Recent commits include:

- `coded tcp_scanner`
- `codeed connection.py`
- `codeed result.py`
- `add report generation`
- `add terminla output`
- `add logging`
- `add validation`
- `remove test directory`
- `Implement TCP port scanning functionality with argument parsing and logging`

This incremental history reflects the project's progression from individual modules toward a working command-line scanner.

---

## Learning Goals

This project is being developed to understand:

- TCP/IP fundamentals
- TCP connections
- Network ports
- Socket programming
- Port scanning concepts
- Input validation
- CLI application design
- Modular Python architecture
- Logging
- Security reconnaissance fundamentals
- Report generation

---

## Roadmap

### Scanner Improvements

- [ ] Configurable connection timeout
- [ ] Hostname support
- [ ] Better connection-state classification
- [ ] Concurrent port scanning
- [ ] Scan progress information
- [ ] Configurable worker count

### Service Detection

- [ ] Common service identification
- [ ] Service-name mapping
- [ ] Banner grabbing
- [ ] Basic service information

### Output

- [ ] JSON output
- [ ] CSV output
- [ ] Improved text reports
- [ ] Scan summary
- [ ] Scan duration

### Testing

- [ ] Unit tests
- [ ] Scanner tests
- [ ] Parser tests
- [ ] Validator tests
- [ ] Output tests
- [ ] Automated CI testing

### Documentation

- [ ] Detailed TCP documentation
- [ ] Architecture documentation
- [ ] Testing documentation
- [ ] More usage examples

---

## Security and Ethical Use

This tool is intended for:

- Learning
- Local network testing
- CTF environments
- Lab environments
- Systems you own
- Systems where you have explicit authorization to perform security testing

**Do not scan systems or networks without permission.**

Unauthorized port scanning may violate organizational policies, terms of service, or applicable laws.

---

## Author

**Sandeep**

GitHub:

https://github.com/sandeepyuva112

Project:

https://github.com/sandeepyuva112/tcp_port_scanner

---

## Project Status

**Status: Active Development**

The current version provides a functional TCP connect scanner with:

- command-line arguments
- port parsing
- IPv4 validation
- TCP connection attempts
- terminal output
- logging
- text report generation

The project will continue to evolve toward a more capable network reconnaissance and learning tool.
