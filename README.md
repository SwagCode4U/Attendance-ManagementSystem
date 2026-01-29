# 📚 Smart Attendance Management System by @mit

A Python-based attendance tracker designed for students who want to manage their attendance smartly. It doesn't just count days—it tells you if you're safe to "bunk" or if you're in the "danger zone"!

## 🎯 What It Does

1. **Subject-wise Tracking**: Monitor attendance for specific subjects (e.g., Python, Maths).
2. **Mark Attendance**: Easily mark yourself Present (P) or Absent (A).
3. **Smart Dashboard**: View your current status with visual indicators (🟢 Safe, 🟡 Warning, 🔴 Critical).
4. **Eligibility Checker (The "Bunk Calculator")**: 
   - Calculates exactly how many classes you can skip while staying above 75%.
   - Warns you how many classes you *must* attend to recover from low attendance.

## 🚀 How to Run

```bash
# Navigate to the project directory
cd /home/john/Downloads/Attendance-ManagementSystem

# Run the system - Konsole or cmd
python attendance_system.py
python3 attendance_system.py
   or
code . 
pycharm .
```

## ✨ Why This is "Not Boring"

- **Relatable Problem**: Solves the #1 stress for college students—eligibility.
- **Actionable Advice**: Instead of just saying "60%", it says "You MUST attend the next 5 classes."
- **Visuals**: Uses emojis to make the status instantly readable.

## 💡 Sample Usage

```
📚  SMART ATTENDANCE MANAGER
==================================================
1. ➕ Add Subjects
2. 📝 Mark Attendance
3. 📊 View Dashboard
4. 🎓 Check Eligibility (Bunk Calc)
5. 🚪 Exit
==================================================

Enter Choice (1-5): 4

--- 🎓 ELIGIBILITY CHECKER (Bunk Manager) ---
Target Requirement: 75%
------------------------------------------------------------
🟢 Python         : Safe! You can BUNK the next 2 classes. 😎
🔴 Maths          : Low! You MUST attend the next 4 classes. 🥺
```

============================================================
                   📊 ATTENDANCE DASHBOARD                   
============================================================
Subject              Attended/Total  %        Status
------------------------------------------------------------
Python               1/1             100.0 %  🟢 Safe
Js                   1/1             100.0 %  🟢 Safe
Java                 0/1             0.0   %  🔴 Critical
Cpp                  0/0             0.0   %  🆕 New
------------------------------------------------------------
📈 Overall Attendance: 66.7%
============================================================
```
## 🔧 Technical Details

- **Data Structure**: Uses dictionaries to store subject data (Total vs. Attended).
- **Logic**: Implements mathematical formulas to project future attendance requirements.
- **Python Concepts**: Loops, conditionals, user input handling, and formatted output.

---
**Perfect for**: Students who want to learn Python while solving a real-life problem!
