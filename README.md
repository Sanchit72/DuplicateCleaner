# 📁 Duplicate File Remover (Python)

## 📌 Overview
This project is a **Python-based utility** that helps you **find and delete duplicate files** from a directory. 
It uses **MD5 hashing** to compare file contents and identify duplicates efficiently.

---

## 🚀 Features
- 🔍 Detect duplicate files using **checksum (MD5 hash)**
- 📂 Works on **all file types** (text, images, videos, etc.)
- 🔄 Recursively scans directories
- 🧹 Automatically deletes duplicate files
- 📊 Displays duplicate file details

---

## 🛠️ Technologies Used
- Python
- `hashlib` (for MD5 hashing)
- `os` (for file handling)

---

## 📂 Project Structure


---

## ⚙️ How It Works

### 1. Calculate Checksum
- Reads file in binary mode
- Generates **MD5 hash**
- Same content → same hash

### 2. Find Duplicates
- Traverses directory using `os.walk()`
- Stores file paths based on checksum
- Groups duplicate files together

### 3. Display Results
- Shows duplicate file paths
- Counts number of duplicates

### 4. Delete Duplicates
- Keeps **first file**
- Deletes remaining duplicate files

---

## ▶️ Usage

### Step 1: Run the Script
```bash
python duplicate_remover.py
