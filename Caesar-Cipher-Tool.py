import customtkinter as ctk

# Set the appearance and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class CaesarApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Modern Caesar Cipher")
        self.geometry("500x500")

        # --- UI Elements ---
        self.label = ctk.CTkLabel(self, text="Caesar Cipher Tool", font=("Arial", 24, "bold"))
        self.label.pack(pady=20)

        # Input Text
        self.entry_text = ctk.CTkTextbox(self, height=100, width=400)
        self.entry_text.insert("0.0", "Type your message here...")
        self.entry_text.pack(pady=10)

        # Shift Selection (Key)
        self.shift_label = ctk.CTkLabel(self, text="Select Shift (1-25):")
        self.shift_label.pack()

        # Label to display current shift value
        self.shift_value_label = ctk.CTkLabel(self, text="Current Shift: 13", font=("Arial", 14, "bold"), text_color="#3b8ed0")
        self.shift_value_label.pack()

        # Slider with command to update label
        self.shift_slider = ctk.CTkSlider(self, from_=1, to=25, number_of_steps=24, command=self.update_shift_label)
        self.shift_slider.set(13)
        self.shift_slider.pack(pady=10)

        # Action Buttons
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=10)

        self.encrypt_btn = ctk.CTkButton(self.button_frame, text="Encrypt", command=self.encrypt)
        self.encrypt_btn.grid(row=0, column=0, padx=10)

        self.decrypt_btn = ctk.CTkButton(self.button_frame, text="Decrypt", command=self.decrypt)
        self.decrypt_btn.grid(row=0, column=1, padx=10)

        # Result Display
        self.result_text = ctk.CTkTextbox(self, height=100, width=400, fg_color="#2b2b2b")
        self.result_text.pack(pady=20)