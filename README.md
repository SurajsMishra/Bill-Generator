# Bill-Generator
# 🛒 Super Mart Billing Software

A complete **GUI-based Billing Software with Login & Signup System** built using **Python Tkinter**.
This project simulates a supermarket billing system with authentication, bill generation, tax calculation, saving bills, and searching past bills.

---

## 🚀 Features

### 🔐 User Authentication System

* User Signup
* Login Validation
* Forgot Password / Reset Password
* User data stored locally in `users.txt`

### 🧾 Billing System

* Categorized products:

  * 🍫 Snacks
  * 🛒 Grocery
  * 🧴 Beauty & Hygiene
* Automatic price calculation
* Automatic tax calculation:

  * Snacks: 5%
  * Grocery: 1%
  * Beauty & Hygiene: 10%
* Generates formatted bill in Bill Area
* Auto-generated Bill Number
* Customer details support

### 💾 Bill Management

* Save bill as `.txt` file
* Search previous bills by Bill Number
* Bills stored inside `/bills` directory

### 🖥️ User Interface

* Fullscreen modern Tkinter GUI
* Clean layout using Frames & LabelFrames
* Scrollable Bill Area
* Error handling with message boxes

---

## 🛠️ Technologies Used

* Python 3
* Tkinter (GUI)
* OS module (file handling)
* Random module (bill number generation)

---

## 📂 Project Structure

```
📁 SuperMartBilling
│
├── main.py
├── users.txt (auto-created)
├── 📁 bills (auto-created when saving bills)
│    └── BillNumber_XXXX.txt
└── README.md
```

---

## ▶️ How To Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2️⃣ Run the Application

```bash
python main.py
```

> Make sure Python 3 is installed on your system.

---

## 🔄 Application Flow

1. Application starts with Login Screen
2. New users can Sign Up
3. Existing users Login
4. Billing window opens after successful login
5. Generate bill → Save bill → Search bill

---

## 📸 Screens Included

* Login Window
* Signup Window
* Password Reset Window
* Billing Dashboard
* Bill Preview Area

(You can add screenshots here later for better presentation)

---

## 🧮 Tax Calculation Logic

| Category         | Tax Rate |
| ---------------- | -------- |
| Snacks           | 5%       |
| Grocery          | 1%       |
| Beauty & Hygiene | 10%      |

---

## 📌 Key Functionalities Implemented

* File handling
* GUI design with Tkinter
* Data validation
* Exception handling
* Modular programming
* Local storage system

---

## ⚠️ Limitations

* Passwords are stored in plain text (for learning purposes only)
* No database integration
* No encryption
* Desktop application only

---

## 🔮 Future Improvements

* Add SQLite database
* Add password hashing
* Add invoice PDF export
* Add product management system
* Add admin panel
* Improve UI styling

---

## 👨‍💻 Author

**Suraj Mishra**

---

## 🤝 Contributors

* **Vishesh Paul**
* **Vivek Mishra**

---

## 📜 License

This project is created for educational purposes.
Feel free to use and modify it.

---

⭐ If you like this project, consider giving it a star on GitHub!
