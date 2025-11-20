# Renderer Setup and Testing

## What is the Renderer?

The **Renderer** converts resume JSON (from the Generator Agent) into a formatted Word DOCX file **without opening Microsoft Word**. It uses pure `python-docx` manipulation, making it server-compatible.

## Files Created

- `backend/aro/renderer.py` - Main renderer class
- `backend/test_renderer.py` - Standalone test script

## Setup Steps

### 1. Copy Template File

The renderer needs the base Word template:

**From:**
```
D:\Git\virtual457-projects\job-application-automator\templates\Chandan_Resume_Format.docx
```

**To:**
```
D:\Git\virtual457-projects\llm-multi-agent-resume-optimizer\templates\Chandan_Resume_Format.docx
```

**Quick Command (Windows):**
```bash
copy "D:\Git\virtual457-projects\job-application-automator\templates\Chandan_Resume_Format.docx" "D:\Git\virtual457-projects\llm-multi-agent-resume-optimizer\templates\"
```

### 2. Verify Dependencies

Make sure `python-docx` is installed:
```bash
cd D:\Git\virtual457-projects\llm-multi-agent-resume-optimizer\backend
pip install python-docx
```

## Testing the Renderer

### Run the Test

```bash
cd D:\Git\virtual457-projects\llm-multi-agent-resume-optimizer\backend
python test_renderer.py
```

### What the Test Does

1. Loads the Word template
2. Takes sample resume JSON (similar to Generator output)
3. Updates all sections:
   - Header with hyperlinks (LinkedIn, GitHub, etc.)
   - Summary with **bold markers**
   - Skills (7 categories with tab alignment)
   - Work Experience (LSEG 5 bullets + Infosys 4 bullets)
   - Projects (3 projects with GitHub hyperlinks)
4. Saves to: `../output/Test_Generated_Resume.docx`

### Expected Output

```
============================================================
RENDERER TEST - JSON → DOCX CONVERSION
============================================================

📂 Checking for template...
   Expected location: D:\...\templates\Chandan_Resume_Format.docx
   ✅ Template found!

🔧 Initializing renderer...
   ✅ Renderer ready!

🚀 Rendering resume from JSON...

============================================================
RESUME RENDERER - JSON → DOCX
============================================================

📂 Loading Word template...
   ✅ Template loaded (XX paragraphs)

📝 Updating header...
   ✅ Header updated (with hyperlinks)
📝 Updating summary...
   ✅ Summary updated (with bold markers)
📝 Updating technical skills...
   ✅ Updated 7 skill categories
📝 Updating work experience...
   ✅ Updated 5 bullets for LSEG
   ✅ Updated 4 bullets for Infosys
   ✅ Work experience section complete
📝 Updating projects...
   ✅ Updated 3 projects (with GitHub hyperlinks)

💾 Saving generated resume...
   ✅ Saved to: ...\output\Test_Generated_Resume.docx

============================================================
✅ RENDERING COMPLETE!
============================================================

📄 Output file: D:\...\output\Test_Generated_Resume.docx

============================================================
✅ TEST PASSED - RENDERING SUCCESSFUL!
============================================================
```

## Features

### Bold Markers Support
Text with `**markers**` is rendered bold in Word:
```python
"Built **AWS Lambda** pipeline"  →  "Built AWS Lambda pipeline" (Lambda is bold)
```

### Hyperlinks
- Contact info (Email, LinkedIn, Portfolio, GitHub)
- Project titles link to GitHub repos
- All links are clickable and blue

### Tab Alignment
Skills section uses fixed tab alignment at 35 characters (2.45 inches) for consistent formatting.

### No Word Automation
The renderer works **without opening Microsoft Word**, making it suitable for:
- Server environments
- Automated workflows
- Headless systems

## Integration with Generator

Once tested, the renderer can be integrated into the main workflow:

```python
from aro.agents.generator import GeneratorAgent
from aro.renderer import ResumeRenderer
from aro.llm_adapter import create_llm_adapter

# Generate resume JSON
llm = create_llm_adapter("gemini")
generator = GeneratorAgent(llm)
resume_json = generator.generate(jd_text, profile_data)

# Render to DOCX
renderer = ResumeRenderer("templates/Chandan_Resume_Format.docx")
output_path = renderer.render(resume_json, "output/Generated_Resume.docx")
```

## Next Steps

After renderer works:
1. ✅ Renderer (DONE)
2. **Build Evaluator** - Score resumes against JD
3. **Build Iteration Controller** - Loop generate → evaluate → improve
4. **Integrate into FastAPI** - API endpoints

## Troubleshooting

### Template Not Found
```
❌ Template not found at: .../templates/Chandan_Resume_Format.docx
```
**Solution:** Copy template file as described in Setup Step 1

### ImportError: python-docx
```
ModuleNotFoundError: No module named 'docx'
```
**Solution:** 
```bash
pip install python-docx
```

### Paragraph Index Errors
If you get errors about paragraph indices, the template structure might be different. Check that the template has:
- Paragraphs 0-2: Header (Name, Title, Contact)
- "TECHNICAL SKILLS" heading
- "WORK EXPERIENCE" heading  
- "PROJECTS" heading

## Template Structure Expected

```
Paragraph 0: Chandan Gowda K S
Paragraph 1: [Title line]
Paragraph 2: [Contact line]
...
TECHNICAL SKILLS
[7 skill paragraphs]
...
WORK EXPERIENCE
[Company header]
[5 bullets for LSEG]
[Company header]
[4 bullets for Infosys]
...
PROJECTS
[Project 1 title]
[Bullet 1]
[Bullet 2]
[Project 2 title]
...
```

## Code Quality

The renderer:
- ✅ Handles errors gracefully
- ✅ Provides detailed logging
- ✅ Validates inputs
- ✅ Works without Word application
- ✅ Supports all formatting (bold, hyperlinks, tabs)
- ✅ Matches original simple_generator.py functionality
