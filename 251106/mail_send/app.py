dir_path = r'C:\Users\abkashy2\Downloads' 
attachments = [
    f'{dir_path}/test1.jpg',
]
from mail import send_gmail_attach
from config import to_address 
result = send_gmail_attach(to_address, "Cisco - 06-11-2025 - Photos", "Hello from abhishek!", attachments)
print("Mail sent successfully?" , result)
