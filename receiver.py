# Save as: receiver.py
import socket

def start_ps5_receiver():
    # إنشاء اتصال TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 9023)) 
    sock.listen(1)
    print(" status: WAITING FOR PS5 CONNECTION ON PORT 9023...")
    
    conn, addr = sock.accept()
    print(f" status: CONNECTED TO PS5 AT {addr}")
    
    with open("ps5_full_dump.bin", "wb") as f:
        try:
            while True:
                data = conn.recv(1024 * 1024) # استلام 1 ميجا في كل مرة
                if not data: break
                f.write(data)
                print(f" Progress: Receiving system data...", end='\r')
        except Exception as e:
            print(f"\n Error: {e}")
            
    print("\n[!] SUCCESS: FULL SYSTEM DUMP SAVED AS ps5_full_dump.bin")
    conn.close()

if __name__ == "__main__":
    start_ps5_receiver()