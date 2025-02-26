import cv2
import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

class ImageEncryptorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Encryptor/Decryptor")
        self.master.geometry("400x300")

        self.label = tk.Label(master, text="Select an operation:")
        self.label.pack(pady=20)

        self.encrypt_button = tk.Button(master, text="Encrypt Image", command=self.encrypt_mode)
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = tk.Button(master, text="Decrypt Image", command=self.decrypt_mode)
        self.decrypt_button.pack(pady=10)

        self.message_label = tk.Label(master, text="")
        self.message_label.pack(pady=20)

        self.mode = None  

    def encrypt_mode(self):
        self.mode = 'encrypt'
        self.select_file()

    def decrypt_mode(self):
        self.mode = 'decrypt'
        self.select_file()

    def select_file(self):
        file_path = filedialog.askopenfilename(title="Select an Image File", 
                                                filetypes=[("Image Files", "*.png;*.bmp;*.jpeg;*.jpg")])
        if file_path:
            if self.mode == 'encrypt':
                self.process_encryption(file_path)
            elif self.mode == 'decrypt':
                self.process_decryption(file_path)

    def process_encryption(self, file_path):
        img = cv2.imread(file_path)
        if img is None:
            self.display_message("Invalid image file.")
            return

        msg = simpledialog.askstring("Input", "Enter secret message:")
        if not msg:
            return

        encrypted_img = self.encrypt_image(img, msg)

        output_path = "encrypted_image.png"
        cv2.imwrite(output_path, encrypted_img)
        
        if os.name == "nt":
            os.startfile(output_path)
        else:
            os.system(f"xdg-open {output_path}")

        self.display_message("Image encrypted successfully!")

    def process_decryption(self, file_path):
        img = cv2.imread(file_path)
        if img is None:
            self.display_message("Invalid image file.")
            return

        decrypted_msg = self.decrypt_image(img)
        if decrypted_msg:
            messagebox.showinfo("Decrypted Message", decrypted_msg)
        else:
            self.display_message("Decryption failed.")

    def encrypt_image(self, img, msg):
        msg += "####"  # Delimiter to indicate end of message
        binary_msg = ''.join(format(ord(char), '08b') for char in msg)
        
        h, w, _ = img.shape
        total_pixels = h * w * 3  # Considering all RGB channels

        if len(binary_msg) > total_pixels:
            messagebox.showerror("Error", "Message is too long to be hidden in the image.")
            return img

        data_index = 0
        for i in range(h):
            for j in range(w):
                for c in range(3):  # Iterate over RGB
                    if data_index < len(binary_msg):
                        img[i, j, c] = (img[i, j, c] & 254) | int(binary_msg[data_index])  # Modify LSB
                        data_index += 1
                    else:
                        break
        return img

    def decrypt_image(self, img):
        binary_msg = ""
        h, w, _ = img.shape

        for i in range(h):
            for j in range(w):
                for c in range(3):  
                    binary_msg += str(img[i, j, c] & 1)  # Extract LSB

        # Convert binary to text
        msg = ""
        for i in range(0, len(binary_msg), 8):
            char = chr(int(binary_msg[i:i+8], 2))
            if msg.endswith("####"):  
                return msg[:-4]  # Remove delimiter
            msg += char
        
        return None  # If no valid message is found

    def display_message(self, message):
        self.message_label.config(text=message)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptorApp(root)
    root.mainloop()
