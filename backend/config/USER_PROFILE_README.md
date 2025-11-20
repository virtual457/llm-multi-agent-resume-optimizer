# User Profile System - How It Works

## 📂 Profile Data Storage

**Profile data is now centralized and switchable!**

**Profile File:** `backend/config/user_profile.py`

This file contains ALL user data:
- Personal information
- Education details  
- Work experience (companies, metrics, achievements)
- Project summaries
- Technologies
- Certifications

**Source of Truth:** Based on comprehensive documentation in:
- `D:\Git\virtual457-projects\job-application-automator\docs\user_profile\CHANDAN_PROFILE_MASTER.md`
- `D:\Git\virtual457-projects\job-application-automator\docs\user_profile\WORK_EXPERIENCE_DATABASE.md`

---

## 🔄 How to Switch Users

**To use a different candidate's profile:**

### Option 1: Edit the Config File
Edit `backend/config/user_profile.py` and change the data in `load_profile()` method.

### Option 2: Create Multiple Profile Files
```
backend/config/
├── user_profile.py          # Active profile loader
├── profiles/
│   ├── chandan.py          # Chandan's data
│   ├── john_doe.py         # Another candidate
│   └── jane_smith.py       # Another candidate
```

Then switch by changing which file is imported.

### Option 3: YAML-based Profiles (Future Enhancement)
```yaml
# config/profiles/chandan.yaml
personal_info:
  name: "Chandan Gowda K S"
  email: "..."
```

---

## 💡 How the Generator Uses Profile Data

**When generating resumes, the Generator Agent:**

1. **Loads profile:** `profile = UserProfileLoader.load_profile()`
2. **Extracts relevant data:** Name, GPA, metrics, technologies
3. **Passes to LLM:** As context for resume generation
4. **LLM generates bullets:** Using real metrics from profile

**Example:**
```python
# Generator reads from profile
metrics = profile['work_experience']['lseg']['metrics']
# Uses: metrics['records_processed'] = "7.5M+"
# LLM generates: "Engineered pipeline processing **7.5M+ records**..."
```

---

## ✅ Benefits of This Approach

**1. Centralized Data:**
- All user info in one place
- No hardcoded data scattered across files
- Easy to update

**2. Switchable Users:**
- Change profile file → new candidate
- Same system works for anyone
- Can generate resumes for multiple people

**3. Factual Accuracy:**
- Metrics stored in profile
- LLM can't fabricate numbers
- Generated bullets use real data

**4. Maintainability:**
- Update profile once → affects all generations
- Clear separation: data vs logic
- Easy to validate data correctness

---

## 🧪 Testing Profile Loader

```bash
# Test the profile loader directly
python config/user_profile.py
```

**Expected output:**
```
============================================================
USER PROFILE LOADER TEST
============================================================

📋 Loaded Profile:
   Name: Chandan Gowda K S
   Email: chandan.keelara@gmail.com
   GPA: 3.89/4.0

💼 Work Experience:
   LSEG: 7.5M+ records
   Infosys: 3x throughput

📝 Profile Summary:
MS Computer Science student at Northeastern University (GPA: 3.89/4.0)
...

✅ Profile loaded successfully!
```

---

## 🔮 Future Enhancements

**Multi-User Support:**
```python
# Load specific user profile
profile = UserProfileLoader.load_profile(user_id="chandan")
profile = UserProfileLoader.load_profile(user_id="john_doe")
```

**YAML-based Profiles:**
- Easier to edit than Python
- Can be uploaded via UI
- Non-programmers can modify

**Profile Validation:**
- Check required fields present
- Validate data types
- Ensure metrics are realistic

---

## 📝 Current Profile Data

**Stored in:** `backend/config/user_profile.py`

**Contains:**
- Personal info (name, email, phone, links)
- Education (MS + BE with GPAs)
- Work experience:
  - LSEG: All metrics, technologies, achievements
  - Infosys: All metrics, technologies, achievements
- Project summaries
- Certifications
- Publications

**All resume generations now use this data source!**

---

## ✅ What This Means

**Before:** Data hardcoded in generator.py, prompts.py, etc.
**Now:** Data in one config file, loaded dynamically

**To update your resume data:**
1. Edit `backend/config/user_profile.py`
2. Change metrics, add new projects, update achievements
3. All future generations use new data automatically

**To help a friend with their resume:**
1. Create new profile file with their data
2. Switch the profile loader
3. Same system generates resumes for them!

---

**The system is now USER-AGNOSTIC and DATA-DRIVEN!** 🎉
