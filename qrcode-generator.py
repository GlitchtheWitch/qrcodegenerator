"""
QR Code Generator
"""
import qrcode


def main():

    # User input
    website_link = input("Enter the website link: ")
    qrcode_filename = input("Enter the filename for the QR code: ") + '.png'

    # Create the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=2)
    qr.add_data(website_link)
    qr.make()

    # Generate and save the QR code image
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(qrcode_filename)


if __name__ == '__main__':
    main()
