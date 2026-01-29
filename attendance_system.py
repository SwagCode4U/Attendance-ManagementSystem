"""
📚 SMART ATTENDANCE MANAGER
===========================
A student-focused attendance tracker that calculates eligibility 
and tells exactly how many classes you can skip (or need must attend)!

Author: Coders Jaunt by @mit
Purpose: Teaching Python dictionaries, math, and logic integration
"""

# ============================================================================
# GLOBAL DATA STRUCTURES
# ============================================================================

# Subject Database
# Dictionary Format: { 'SubjectName': {'total': 0, 'attended': 0} }
subjects = {}

# Minimum Attendance Requirement (Percentage)
MIN_ATTENDANCE_PCT = 75

# ============================================================================
# CORE FUNCTIONS
# ============================================================================

def add_subject():
    """Add new subjects to track."""
    print("\n--- ➕ ADD NEW SUBJECT ---")
    while True:
        name = input("Enter Subject Name (or 'done' to finish): ").strip().title()
        if name.lower() == 'done':
            break
        
        if not name:
            print("❌ Subject name cannot be empty.")
            continue
            # condition sub exists
        if name in subjects:
            print("⚠️  Subject already exists!")
            continue
            
        # Initialize subject with 0 classes
        subjects[name] = {'total': 0, 'attended': 0}
        print(f"✅ Added {name}")

# ============================================================================
# ATTENDANCE MARKING - LOGIC - INPUT HANDLING
# ===========================================================================
def mark_attendance():
    """
    Mark attendance for a specific subject.
    Updates 'total' and 'attended' counters.
    """
    print("\n--- 📝 MARK ATTENDANCE ---")
    if not subjects:
        print("📭 No subjects added yet! Use Option 1 first.")
        return

    # Show available subjects
    print("Subjects available:")
    subject_list = list(subjects.keys())        # sub list for indexing
    for i, sub in enumerate(subject_list, 1):       # enumerate from 1 ordered list of subjects
        print(f"  {i}. {sub}")
    # try-except for input validation for error handling
    try:
        choice = int(input("\nEnter Subject Number: "))
        if choice < 1 or choice > len(subject_list):        # Out of range check
            print("❌ Invalid choice.")
            return
            
        selected_subject = subject_list[choice - 1]
        
        print(f"\nMarking for: {selected_subject}")
        status = input("Present (P) or Absent (A)? ").strip().upper()
        
        if status == 'P':
            subjects[selected_subject]['total'] += 1        # incrmnt total
            subjects[selected_subject]['attended'] += 1   # incrmnt attended
            print(f"✅ Marked PRESENT for {selected_subject}")      # Success message
        elif status == 'A':
            subjects[selected_subject]['total'] += 1
            # Attended count stays same
            print(f"❌ Marked ABSENT for {selected_subject}")
        else:
            print("❌ Invalid input! Use 'P' or 'A'.")
            
    except ValueError:
        print("❌ Invalid input! Please enter a number.")

# ===========================================================================
# ANALYTICS & SMART LOGIC - DASHBOARD VIEW
# ===========================================================================

def view_dashboard():
    """
    Display a summary of all subjects with percentages and status indicators.
    """
    print("\n" + "="*60)
    print(f"{'📊 ATTENDANCE DASHBOARD':^60}")
    print("="*60)
    
    if not subjects:
        print("📭 No subjects to display.")
        return

    print(f"{'Subject':<20} {'Attended/Total':<15} {'%':<8} {'Status'}")
    print("-" * 60)
    
    total_classes = 0
    total_attended = 0
    # Per-Subject Stats for loop
    for sub, data in subjects.items():
        total = data['total']
        attended = data['attended']
        total_classes += total
        total_attended += attended
        
        if total == 0:
            percentage = 0.0
            status = "🆕 New"
        else:
            percentage = (attended / total) * 100   # * 100 to get pct% not decimal
            
            # Status Logic
            if percentage >= MIN_ATTENDANCE_PCT:
                status = "🟢 Safe"
            elif percentage >= 65:
                status = "🟡 Warning"
            else:
                status = "🔴 Critical"
        
        print(f"{sub:<20} {f'{attended}/{total}':<15} {percentage:<6.1f}%  {status}")
    
    print("-" * 60)
    
    # Overall Stats
    if total_classes > 0:
        overall_pct = (total_attended / total_classes) * 100
        print(f"📈 Overall Attendance: {overall_pct:.1f}%")     # 1f % enough with one digit/figure
    print("="*60)

# ===========================================================================
# ELIGIBILITY CHECKER (BUNK MANAGER)
# ===========================================================================
def check_eligibility():
    """
    The 'Not Boring' part: Calculates Bunking Allowance or Recovery Plan.
    Tells you exactly how many classes you can skip or need to attend.
    """
    print("\n--- 🎓 ELIGIBILITY CHECKER (Bunk Manager) ---")
    if not subjects:    # condition when no subjects
        print("📭 No subjects found.")
        return
        
    print(f"Target Requirement: {MIN_ATTENDANCE_PCT}%")
    print("-" * 60)
    
    for sub, data in subjects.items():      # per subject data
        total = data['total']
        attended = data['attended']
        
        if total == 0:          # keeping zero with strict check
            continue
            
        current_pct = (attended / total) * 100
        
        # LOGIC: 
        # Target: attended_new / total_new >= 0.75
        
        if current_pct >= MIN_ATTENDANCE_PCT:
            # Case 1: Attendance is GOOD. How many can I skip?
            # We want to find 'x' (classes to skip) such that:
            # attended / (total + x) >= 0.75
            # attended >= 0.75 * (total + x)
            # attended / 0.75 >= total + x
            # (attended / 0.75) - total >= x
            
            bunkable = int((attended / (MIN_ATTENDANCE_PCT/100)) - total)
            if bunkable > 0:
                print(f"🟢 {sub:<15}: Safe! You can BUNK the next {bunkable} classes. 😎")
            else:
                print(f"🟢 {sub:<15}: Safe! But don't miss the next class. 😬")
                
        else:
            # Case 2: Attendance is LOW. How many MUST I attend?
            # We want to find 'x' (classes to attend) such that:
            # (attended + x) / (total + x) >= 0.75
            # attended + x >= 0.75 * total + 0.75 * x
            # x - 0.75*x >= 0.75*total - attended
            # 0.25 * x >= 0.75*total - attended
            # x >= (0.75*total - attended) / 0.25
            
            required_pct = MIN_ATTENDANCE_PCT / 100
            numerator = (required_pct * total) - attended
            denominator = 1 - required_pct
            
            needed = int(numerator / denominator) + 1 # Round up (simplified)
            
            print(f"🔴 {sub:<15}: Low! You MUST attend the next {needed} classes. 🥺")

# ============================================================================
# MAIN PROGRAM - MENU INTERFACE - Run While Loop - Run Until Exit
# ============================================================================

def main():
    # Pre-populate some data for better testing UX (Optional - removed for clean start)
    # subjects['Python'] = {'total': 10, 'attended': 8}
    
    while True:
        print("\n" + "="*50)
        print("📚  SMART ATTENDANCE MANAGER")
        print("="*50)
        print("1. ➕ Add Subjects")
        print("2. 📝 Mark Attendance")
        print("3. 📊 View Dashboard")
        print("4. 🎓 Check Eligibility (Bunk Calc)")
        print("5. 🚪 Exit")
        print("="*50)
        
        choice = input("Enter Choice (1-5): ").strip()
        
        if choice == '1':
            add_subject()
        elif choice == '2':
            mark_attendance()
        elif choice == '3':
            view_dashboard()
        elif choice == '4':
            check_eligibility()
        elif choice == '5':
            print("\n👋 Stay regular! Exiting...")
            break
        else:
            print("❌ Invalid Choice!")


# ============================================================================
# ENTRY POINT
# ============================================================================
if __name__ == "__main__":
    main()
