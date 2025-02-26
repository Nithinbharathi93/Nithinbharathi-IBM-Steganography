# Nithinbharathi-IBM-Secure Data Hiding in Images Using Steganography

## 📌 Overview
This project implements **image-based steganography** to securely hide and retrieve secret messages within images. It enhances security by integrating **passcode-based encryption**, ensuring that only authorized users can decrypt the hidden data.

## 🚀 Features
- **Passcode-Protected Encryption** – Only authorized users can extract hidden messages.  
- **LSB Steganography** – Uses the Least Significant Bit (LSB) technique to embed data.  
- **XOR Encryption** – Adds an extra layer of security.  
- **User-Friendly GUI** – Built using Tkinter for easy interaction.  
- **Supports Multiple Image Formats** – Works with **JPEG, PNG, BMP** files.

## 🛠️ Technologies Used
- **Python** – Core programming language  
- **OpenCV** – Image processing  
- **Tkinter** – GUI for user interaction  
- **NumPy** – Efficient image data handling  
- **LSB Steganography** – Data hiding technique  
- **XOR Encryption** – Additional security layer  

## 🔧 Installation
1. **Clone the repository**  
   ```bash
   git clone https://github.com/Nithinbharathi93/Nithinbharathi-IBM-Steganography.git
   cd Nithinbharathi-IBM-Steganography
   ```
2. **Install required dependencies**  
   ```bash
   pip install opencv-python numpy tkinter
   ```
3. **Run the application**  
   ```bash
   python main.py
   ```

## 📷 How It Works
1. **Encryption Mode**  
   - Select an image.  
   - Enter the secret message and passcode.  
   - The program hides the message and generates an encrypted image.  

2. **Decryption Mode**  
   - Select the encrypted image.  
   - Enter the passcode.  
   - The program retrieves and displays the hidden message.  

## 👨‍💻 Author
**[Nithinbharathi.T](https://github.com/Nithinbharathi93/)**  
