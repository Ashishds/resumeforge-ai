"""
Resume Format Template
Defines the standard formatting structure for all resume outputs
"""

RESUME_FORMAT_TEMPLATE = """
**Full Name**
email@example.com
+Country_Code Phone_Number
City, State/Region

---

**SUMMARY**
Professional summary paragraph highlighting key achievements, skills, and career objectives. 
Should be 3-5 sentences that capture the candidate's value proposition.

---

**SKILLS**

**Programming Languages:**
- Python
- SQL

**Category Name:**
- Skill 1
- Skill 2
- Skill 3

**Another Category:**
- Technology A
- Technology B

---

**PROFESSIONAL EXPERIENCE**

**Job Title**
**Company Name, City, Country**
**Month Year - Month Year**
- Achievement bullet point with quantified metrics (X% improvement, $Y saved, Z projects delivered)
- Another achievement demonstrating impact using STAR method (Situation, Task, Action, Result)
- Third bullet highlighting collaboration, leadership, or technical skills with measurable outcomes

**Previous Job Title**
**Previous Company, City, Country**
**Month Year - Month Year**
- Achievement with specific numbers and business impact
- Another accomplishment showing progression and growth

---

**EDUCATION**

**Degree Name**
**University Name, City, Country**
**Graduation Year**

---

**CERTIFICATIONS** (Optional)

- Certification Name - Issuing Organization (Year)
- Another Certification - Issuing Organization (Year)

---
"""

FORMAT_RULES = """
FORMATTING RULES:
1. Use **Bold** for section headers, names, job titles, company names
2. Use --- (three dashes) as horizontal dividers between major sections
3. Use single blank line between subsections
4. Use double blank line between major sections (after ---)
5. Start bullet points with '-' (single dash with space)
6. Contact info: Name bold on first line, then email, phone, location on separate lines
7. Job entries: Title bold, Company bold with location, Dates bold on separate lines
8. Skills: Group by category with category name in bold followed by colon
9. Keep consistent spacing throughout
10. Use proper capitalization for section headers (all caps for main sections)

EXAMPLE CONTACT SECTION:
**Sayantan Ghosh**
sayantanghosh.work@gmail.com
+91 6290200929
Kolkata, West Bengal

EXAMPLE SKILLS SECTION:
**SKILLS**

**Programming Languages:**
- Python
- SQL (MySQL)

**Machine Learning & NLP:**
- PyTorch
- TensorFlow/Keras
- Hugging Face Transformers

EXAMPLE EXPERIENCE SECTION:
**PROFESSIONAL EXPERIENCE**

**AI Solutions Engineer**
**XYZ Technologies, Kolkata, India**
**June 2021 - Present**
- Developed and implemented 7 advanced ML models analyzing 20M+ data points, enhancing accuracy by 35%
- Spearheaded cloud migration leading 4 engineers, reducing costs by 30% and improving deployment speed by 50%
- Collaborated with product managers to optimize AI chatbot, reducing response time by 25%
"""


def get_format_template() -> str:
    """Return the standard resume format template"""
    return RESUME_FORMAT_TEMPLATE


def get_format_rules() -> str:
    """Return the formatting rules"""
    return FORMAT_RULES


def validate_resume_format(resume_text: str) -> tuple[bool, list[str]]:
    """
    Validate if resume follows the proper format
    
    Args:
        resume_text: Resume text to validate
        
    Returns:
        Tuple of (is_valid, list of issues found)
    """
    issues = []
    
    # Check for section dividers
    if '---' not in resume_text:
        issues.append("Missing section dividers (---)")
    
    # Check for bold headers
    if '**' not in resume_text:
        issues.append("Missing bold formatting for headers")
    
    # Check for key sections
    required_sections = ['SUMMARY', 'SKILLS', 'EXPERIENCE']
    for section in required_sections:
        if section.upper() not in resume_text.upper():
            issues.append(f"Missing required section: {section}")
    
    # Check bullet points format
    if '\n-' not in resume_text and '\n- ' not in resume_text:
        issues.append("Bullet points should use '- ' format")
    
    is_valid = len(issues) == 0
    return is_valid, issues
