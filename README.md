# port scsanning tool
ports are the access point in the network.
# DAY 1

- IP address → the building's address
- Port → a particular door
- Service → the person/business behind that door
- Port scanner → someone checking which doors respond

For example:

```
Target: 192.168.1.10

Port     State
22       OPEN
80       OPEN
443      OPEN
23       CLOSED

```
Conceptually:

```
Scanner
   |
   |  TCP connection request
   |------------------------>
   |
   |       Target
   |
   |<------------------------
   |  response

```
TCP scanner flow

```
Target IP
   ↓
Choose port
   ↓
Create TCP socket
   ↓
Attempt connection
   ↓
┌───────────────┐
│ What happened?│
└───────┬───────┘
        │
   ┌────┴─────┐
   ↓          ↓
Success     Refused/timeout
   ↓          ↓
 OPEN       Not OPEN

```

architecture :

```
                    TCP PORT SCANNER
                           │
             ┌─────────────┴─────────────┐
             │                           │
         Target Input                Scan Config
       IP / hostname               ports / timeout
             │                           │
             └─────────────┬─────────────┘
                           ↓
                    TCP Scanner Engine
                           │
                  ┌────────┴────────┐
                  ↓                 ↓
              Connection        Timeout /
               succeeds          refused
                  ↓                 ↓
                 OPEN            CLOSED
                  │
                  ↓
             Service Detection
                  │
                  ↓
             Result Processing
                  │
          ┌───────┼────────┐
          ↓       ↓        ↓
       Terminal   JSON     CSV
          │
          ↓
      Final Report

```