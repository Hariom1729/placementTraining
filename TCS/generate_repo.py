import os

repo_name = "TCS-NQT-2027-Preparation"
base_dir = os.path.join(os.getcwd(), repo_name)

dirs = [
    "Aptitude",
    "Reasoning",
    "Verbal",
    "DSA/Arrays",
    "DSA/Strings",
    "DSA/Searching",
    "DSA/Sorting",
    "DSA/Hashing",
    "DSA/Recursion",
    "DSA/LinkedList",
    "DSA/Stack",
    "DSA/Queue",
    "DSA/Trees",
    "DSA/Graphs",
    "Coding_Questions/TCS_2022",
    "Coding_Questions/TCS_2023",
    "Coding_Questions/TCS_2024",
    "Coding_Questions/TCS_2025",
    "Coding_Questions/TCS_2026",
    "Technical_Interview",
    "HR_Interview",
    "Study_Plans",
    "Revision",
    "Progress_Tracker"
]

files = {
    "Aptitude/Number_System.md": "# Number System\n\n## Theory\n\n## Key Formulas\n\n## Practice Problems\n",
    "Aptitude/Profit_Loss.md": "# Profit and Loss\n\n## Theory\n\n## Key Formulas\n\n## Practice Problems\n",
    "Aptitude/Probability.md": "# Probability\n\n## Theory\n\n## Key Formulas\n\n## Practice Problems\n",
    "Aptitude/Time_and_Work.md": "# Time and Work\n\n## Theory\n\n## Key Formulas\n\n## Practice Problems\n",
    "Aptitude/Speed_Time_Distance.md": "# Speed, Time and Distance\n\n## Theory\n\n## Key Formulas\n\n## Practice Problems\n",
    "Aptitude/Percentages.md": "# Percentages\n\n## Theory\n\n## Key Formulas\n\n## Practice Problems\n",
    "Aptitude/PYQs.md": "# Previous Year Questions - Aptitude\n",
    "Reasoning/Coding_Decoding.md": "# Coding and Decoding\n",
    "Reasoning/Blood_Relation.md": "# Blood Relations\n",
    "Reasoning/Seating_Arrangement.md": "# Seating Arrangement\n",
    "Reasoning/Number_Series.md": "# Number Series\n",
    "Reasoning/PYQs.md": "# Previous Year Questions - Reasoning\n",
    "Verbal/Grammar.md": "# English Grammar\n",
    "Verbal/Reading_Comprehension.md": "# Reading Comprehension\n",
    "Verbal/Vocabulary.md": "# Vocabulary\n",
    "Verbal/PYQs.md": "# Previous Year Questions - Verbal\n",
    "Technical_Interview/OOP.md": "# Object Oriented Programming\n\n## Core Concepts\n- Encapsulation\n- Abstraction\n- Inheritance\n- Polymorphism\n\n## Frequently Asked Questions\n",
    "Technical_Interview/DBMS.md": "# Database Management Systems\n\n## Core Concepts\n- ACID Properties\n- Normalization\n- Transaction Management\n\n## Frequently Asked Questions\n",
    "Technical_Interview/OS.md": "# Operating Systems\n",
    "Technical_Interview/CN.md": "# Computer Networks\n",
    "Technical_Interview/SQL.md": "# SQL Interview Questions\n",
    "Technical_Interview/C++.md": "# C++ Interview Questions\n",
    "HR_Interview/Tell_Me_About_Yourself.md": "# Tell Me About Yourself\n\n## Best Approach\nKeep it concise: Present, Past, Future.\n",
    "HR_Interview/Strengths_Weaknesses.md": "# Strengths and Weaknesses\n",
    "HR_Interview/Why_TCS.md": "# Why TCS?\n",
    "HR_Interview/HR_FAQ.md": "# Frequently Asked HR Questions\n",
    "Study_Plans/30_Days.md": "# 30 Days Fast-Track Plan\n",
    "Study_Plans/60_Days.md": "# 60 Days Standard Plan\n",
    "Study_Plans/90_Days.md": "# 90 Days Comprehensive Plan\n",
    "Revision/Aptitude_Revision.md": "# Aptitude Quick Revision\n",
    "Revision/DSA_Revision.md": "# DSA Quick Revision\n",
    "Revision/CS_Fundamentals_Revision.md": "# CS Fundamentals Quick Revision\n",
    "Progress_Tracker/DSA_Checklist.md": "# DSA Progress Checklist\n\n- [ ] Arrays\n- [ ] Strings\n- [ ] LinkedList\n- [ ] Trees\n- [ ] Graphs\n",
    "Progress_Tracker/Aptitude_Checklist.md": "# Aptitude Progress Checklist\n",
    "Progress_Tracker/Interview_Checklist.md": "# Interview Progress Checklist\n"
}

readme_content = """# 🚀 TCS NQT 2027 Complete Preparation Repository

Welcome to the ultimate preparation guide for **TCS Ninja, Digital, and Prime** recruitment 2027. This repository contains everything you need from scratch to an advanced level to crack the exam and interviews.

## 🌟 Repository Overview

This repository is structured systematically to help you cover all aspects of the TCS NQT:
- **Aptitude, Reasoning, Verbal:** Comprehensive notes, formulas, and previous year questions.
- **DSA Roadmap:** A structured guide to mastering Data Structures and Algorithms with C++/Java solutions.
- **Coding Questions:** Real past coding problems with varying difficulty levels (TCS 2022-2026).
- **CS Fundamentals:** High-yield notes for OOP, DBMS, OS, CN, SQL, and C++.
- **HR & Technical Interviews:** Frequently asked questions with best answers.
- **Study Plans:** Curated 30, 60, and 90-day roadmaps.
- **Progress Trackers:** Checklists to monitor your preparation.

## 📂 Structure

- `Aptitude/`
- `Reasoning/`
- `Verbal/`
- `DSA/`
- `Coding_Questions/`
- `Technical_Interview/`
- `HR_Interview/`
- `Study_Plans/`
- `Revision/`
- `Progress_Tracker/`

## 💡 How to Use This Repository

1. **Assess Your Timeline:** Choose a study plan from the `Study_Plans/` directory based on how much time you have.
2. **Track Progress:** Fork this repo and use the checklists in `Progress_Tracker/`.
3. **Daily Grind:** Practice 2-3 aptitude topics, 1 reasoning topic, and solve 2-3 DSA problems daily.
4. **Mock Interviews:** Use the `Technical_Interview` and `HR_Interview` sections to prepare with a friend.

---

### 🌟 Give it a Star!
If you find this repository helpful in your preparation journey, please give it a ⭐ to help others discover it!
"""

def create_structure():
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    for d in dirs:
        dir_path = os.path.join(base_dir, d)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    for file_path, content in files.items():
        full_path = os.path.join(base_dir, file_path)
        with open(full_path, "w") as f:
            f.write(content)
            
    with open(os.path.join(base_dir, "README.md"), "w") as f:
        f.write(readme_content)

    print("Repository structure generated successfully in", base_dir)

if __name__ == "__main__":
    create_structure()
