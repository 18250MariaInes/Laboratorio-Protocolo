'''
Maria Jose Castro 181202
Diana de Leon 18607
Camila Gonzalez 18398
Maria Ines Vasquez 18250
'''
#codigo extraido de 
#https://wizardforcel.gitbooks.io/practical-cryptography-for-developers-book/content/more-cryptographic-concepts/one-time-passwords-otp-example.html

#librería para generar OTP en python
import pyotp
#Librería para llevar control del tiempo
import time

#base de 32 bits para generar OTP
base32secret = 'S3K3TPI5MYA2M67V'
print('Secret:', base32secret)

#se genera OTP con el "secreto" establecido anteriormente
totp = pyotp.TOTP(base32secret)
print('OTP code:', totp.now())
time.sleep(10)
#se vuelve a generar 10 segundos más tarde
print('Después de 10 s:')
print('OTP code:', totp.now())