import qrcode

# Data to encode
data = "https://www.example.com"

# Create a QR Code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR Code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill="black", back_color="white")

# Save the image
img.save("qrcode.png")

print("QR Code generated and saved as qrcode.png")
