
import qrcode

# Το GitHub Pages URL σας
redirect_url = "https://csd4537.github.io/index.html/"

# Δημιουργία QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(redirect_url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("dynamic_qr.png")
print("QR generated successfully!")
