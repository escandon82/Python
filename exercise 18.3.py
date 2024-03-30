# Generate 6 digit random secure OTP

import secrets

OTPgenerator=secrets.SystemRandom()

print("six digit random OTP")

otp=OTPgenerator.randrange(100000,999999)

print("secure OTP is ",otp)