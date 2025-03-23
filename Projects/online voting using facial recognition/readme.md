# 🗳️ Secure Online Voting System Using Facial Recognition

## 📋 Overview
This project presents a **Secure Online Voting System** that incorporates **Facial Recognition** technology using a combination of **Histogram of Oriented Gradients (HOG)** for face detection and **Eigenfaces with K-Nearest Neighbors (KNN)** classifier for facial authentication.

The system aims to provide a more **secure**, **efficient**, and **accessible** way of conducting elections, overcoming limitations present in traditional methods such as paper ballots and EVMs.

---

## 🎯 Features
- 🔒 **Multi-level voter authentication** (Unique ID, Voter ID, Facial Recognition)
- 🖼️ **Face Detection using HOG**
- 🧠 **Face Recognition using Eigenfaces + KNN**
- 🗳️ **Online Voting interface** with one-time voting restriction
- 🧑‍💼 **Admin module** for managing nominees and viewing results
- 🗄️ **MySQL database integration** for securely storing voter and voting data
- 🖥️ **Desktop GUI** using **PyQt5**

---

## ⚙️ Technologies Used
- **Python 3.6**
- **PyQt5** (GUI)
- **OpenCV** (Computer Vision)
- **Scikit-learn** (KNN classifier)
- **Face Recognition Library**
- **MySQL + SQLyog** (Database)
- **Pillow (PIL)** (Image Processing)
- **Pickle** (Model serialization)

---

## 📚 Modules Breakdown
### Admin
- Add nominee (Name, Symbol)
- View nominee list
- View live election results

### Voter
- Voter registration (Personal details + Facial image capture)
- Secure login with credentials
- Facial authentication via live webcam capture
- Cast vote (one-time)
- View election results

---

## 💠 System Requirements

### Hardware
- Minimum **1 GB RAM**
- Minimum **100 GB HDD**
- Standard Processor

### Software
- **Windows OS**
- **Python 3.6**
- **PyCharm (Recommended IDE)**
- **MySQL + SQLyog**

---

## 🏠 System Architecture

The system follows a **2-user architecture**:
1. **Admin**
   - Manages nominees
   - Views voting results
2. **Voter**
   - Registers, logs in, and authenticates via facial recognition before voting

---

## 🧩 Algorithms Used
### 1️⃣ Histogram of Oriented Gradients (HOG)
- Used for **face detection** by computing localized gradient orientation histograms.

### 2️⃣ Eigenfaces + KNN Classifier
- **Eigenfaces (PCA-based)** dimensionality reduction for face feature extraction.
- **KNN** classifier for comparing live image encodings to registered voters and authenticating the user.

---

## 🧪 Testing
The system was tested using:
- **Unit Testing** (Individual module-level testing)
- **Integration Testing** (Combining modules)
- **System Testing** (End-to-end testing)
- **Test Cases** covering:
  - Successful login and vote
  - Duplicate voting attempts
  - Incorrect login credentials
  - Face mismatch or multiple faces in frame

---

## 🖼️ Screenshots
- Home page
- Admin login
- Voter registration
- Admin dashboard
- Voting interface
- Results page
- Database tables (Nominee, Voter, Votes)

---

## 🚀 How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/online-voting-facial-recognition.git
   cd online-voting-facial-recognition
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure **MySQL** database:
   - Create the required tables: `nominee`, `register`, and `voting`.
   - Update the `DBConnection.py` file with your MySQL credentials.

4. Run the application:
   ```bash
   python Main.py
   ```

---

## 🔮 Future Enhancements
- Add **Deep Learning models** (e.g., CNN-based recognition)
- **Enhance UI/UX** for smoother user experience
- **Multi-factor authentication** (e.g., OTP + Face)
- **Real-time monitoring** and logging of voting process
- Accessibility support (e.g., screen reader integration)

---

## 📝 References
- Turk, Matthew A & Pentland, Alex P. "Face recognition using eigenfaces"
- Dalal, N., Triggs, B. "Histograms of Oriented Gradients for Human Detection"
- Scikit-learn documentation
- OpenCV documentation
- Face_recognition library (by Adam Geitgey)
- Other scholarly articles listed in Chapter 10 of the project report

