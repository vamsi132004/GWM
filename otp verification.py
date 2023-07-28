import time
import hashlib

class OTP:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    
    def generate_otp(self):
        timestamp = int(time.time() // 30)  
        message = str(timestamp).encode() + self.secret_key.encode()
        otp_hash = hashlib.sha1(message).hexdigest()
        return otp_hash[-6:]  # Extract the last 6 digits as the OTP

    
    def verify_otp(self, otp_to_verify):
        
        expected_otp = self.generate_otp()
        return otp_to_verify == expected_otp



SECRET_KEY = "YOUR_SECRET_KEY"


otp_instance = OTP(SECRET_KEY)


otp = otp_instance.generate_otp()
print("Generated OTP:", otp)


user_entered_otp = input("Enter OTP: ")


if otp_instance.verify_otp(user_entered_otp):
    print("OTP is valid. Verification successful!")
else:
    print("OTP is invalid. Verification failed!")

