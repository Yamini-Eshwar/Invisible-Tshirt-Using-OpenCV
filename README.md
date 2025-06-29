# 👕 Invisible T-shirt Using OpenCV

Make your clothes *disappear* in real-time using Python and OpenCV — no green screen required!

This fun computer vision project demonstrates background subtraction, color detection, and morphological filtering to create a real-life “invisible cloak” effect (in this case, a red t-shirt disappears!).

---

https://github.com/user-attachments/assets/13643b7e-a936-4b51-8afd-79570e0a3b44



## 📸 Demo



---

## 🧠 How It Works

1. Capture a clean background (without the person)
2. Detect a specific color (red) using HSV color space
3. Create a binary mask for that color
4. Use morphological operations to clean the mask
5. Replace the red region with the background frame
6. Display the final output in real-time

---

## 🚀 Run it Yourself

```bash
pip install opencv-python numpy
