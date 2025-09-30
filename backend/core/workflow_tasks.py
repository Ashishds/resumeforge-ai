"""
Workflow Task Definitions
Defines AI tasks for each stage of the resume optimization pipeline
"""

from crewai import Task


def generate_sanitization_workflow(agent, raw_document_text: str) -> Task:
    """
    Create a document sanitization task
    
    Args:
        agent: AI agent to execute the task
        raw_document_text: Raw text to clean
        
    Returns:
        Task: Configured sanitization task
    """
    # Truncate for efficiency while preserving context
    content_preview = (
        raw_document_text[:1000] + "..." 
        if len(raw_document_text) > 1000 
        else raw_document_text
    )
    
    return Task(
        description=(
            f"DOCUMENT SANITIZATION REQUEST\n\n"
            f"Process and clean the following resume text:\n\n{content_preview}\n\n"
            f"REQUIREMENTS:\n"
            f"1. Remove headers, footers, page numbers, and formatting artifacts\n"
            f"2. Normalize all bullet points to use '-' consistently\n"
            f"3. Preserve all substantive content (names, dates, achievements)\n"
            f"4. Maintain logical section structure\n"
            f"5. Remove excessive whitespace and line breaks\n"
            f"6. Fix encoding issues and special characters\n\n"
            f"OUTPUT FORMAT:\n"
            f"**Name**\n"
            f"email@example.com\n"
            f"+91 phone number\n"
            f"Location\n\n"
            f"---\n\n"
            f"**SUMMARY**\n"
            f"Brief professional summary...\n\n"
            f"---\n\n"
            f"**SKILLS**\n"
            f"**Category:**\n"
            f"- Skill 1\n"
            f"- Skill 2\n\n"
            f"---\n\n"
            f"**PROFESSIONAL EXPERIENCE**\n"
            f"**Job Title**\n"
            f"**Company Name, Location**\n"
            f"**Date - Date**\n"
            f"- Achievement bullet point\n\n"
            f"DELIVERABLE: Clean, structured resume text ready for optimization."
        ),
        agent=agent,
        expected_output="Sanitized resume text with preserved structure and normalized formatting using the specified format."
    )


def generate_optimization_workflow(
    agent,
    sanitized_content: str,
    target_position: str,
    position_requirements: str
) -> Task:
    """
    Create an ATS optimization task
    
    Args:
        agent: AI agent to execute the task
        sanitized_content: Cleaned resume text
        target_position: Target job title
        position_requirements: Job description/requirements
        
    Returns:
        Task: Configured optimization task
    """
    # Intelligent truncation
    resume_preview = (
        sanitized_content[:800] + "..." 
        if len(sanitized_content) > 800 
        else sanitized_content
    )
    requirements_preview = (
        position_requirements[:200] + "..." 
        if len(position_requirements) > 200 
        else position_requirements
    )
    
    return Task(
        description=(
            f"ATS OPTIMIZATION REQUEST\n\n"
            f"TARGET POSITION: {target_position}\n\n"
            f"JOB REQUIREMENTS:\n{requirements_preview}\n\n"
            f"CURRENT RESUME:\n{resume_preview}\n\n"
            f"OPTIMIZATION STRATEGY:\n"
            f"1. Extract critical keywords from job requirements\n"
            f"2. Strategically integrate keywords in summary, skills, and experience\n"
            f"3. Use standard ATS-friendly section headers (SUMMARY, SKILLS, EXPERIENCE, EDUCATION)\n"
            f"4. Employ strong action verbs (Led, Architected, Spearheaded, Delivered)\n"
            f"5. Include both acronyms and full terms (AI / Artificial Intelligence)\n"
            f"6. Ensure keyword density of 2-3% for critical terms\n"
            f"7. Structure for easy ATS parsing (clear hierarchy, consistent formatting)\n"
            f"8. Maintain truthfulness while maximizing keyword relevance\n\n"
            f"REQUIRED OUTPUT FORMAT:\n"
            f"**Full Name**\n"
            f"email@example.com\n"
            f"+Country_Code Phone_Number\n"
            f"City, State/Region\n\n"
            f"---\n\n"
            f"**SUMMARY**\n"
            f"Professional summary paragraph with keywords...\n\n"
            f"---\n\n"
            f"**SKILLS**\n\n"
            f"**Category Name:**\n"
            f"- Skill 1\n"
            f"- Skill 2\n\n"
            f"**Another Category:**\n"
            f"- Skill A\n"
            f"- Skill B\n\n"
            f"---\n\n"
            f"**PROFESSIONAL EXPERIENCE**\n\n"
            f"**Job Title**\n"
            f"**Company Name, City, Country**\n"
            f"**Month Year - Month Year**\n"
            f"- Achievement with metrics and impact\n"
            f"- Another achievement with quantified results\n\n"
            f"TARGET SCORE: 85+ ATS compatibility\n\n"
            f"DELIVERABLE: ATS-optimized resume tailored to {target_position} in the exact format specified above."
        ),
        agent=agent,
        expected_output="ATS-optimized resume with strategic keyword placement, professional structure, and proper formatting."
    )


def generate_enhancement_workflow(agent, optimized_content: str) -> Task:
    """
    Create an achievement enhancement task
    
    Args:
        agent: AI agent to execute the task
        optimized_content: ATS-optimized resume
        
    Returns:
        Task: Configured enhancement task
    """
    content_preview = (
        optimized_content[:700] + "..." 
        if len(optimized_content) > 700 
        else optimized_content
    )
    
    return Task(
        description=(
            f"ACHIEVEMENT ENHANCEMENT REQUEST\n\n"
            f"RESUME TO ENHANCE:\n{content_preview}\n\n"
            f"ENHANCEMENT OBJECTIVES:\n"
            f"1. Transform weak bullets into powerful achievement statements\n"
            f"2. Add quantified metrics (percentages, dollar amounts, time saved)\n"
            f"3. Use STAR method: Situation → Task → Action → Result\n"
            f"4. Begin each bullet with a strong action verb\n"
            f"5. Include scope and scale (team size, budget, users impacted)\n"
            f"6. Highlight business impact and outcomes\n"
            f"7. Ensure consistent parallel structure\n"
            f"8. Maintain 2-3 lines per bullet maximum\n\n"
            f"EXAMPLE TRANSFORMATION:\n"
            f"BEFORE: 'Worked on machine learning projects'\n"
            f"AFTER: 'Architected 5 production ML models processing 10M+ daily transactions, "
            f"reducing prediction latency by 40% and generating $2M annual cost savings'\n\n"
            f"MAINTAIN EXACT FORMAT:\n"
            f"**Full Name**\n"
            f"email@example.com\n"
            f"+Country_Code Phone_Number\n"
            f"City, State/Region\n\n"
            f"---\n\n"
            f"**SUMMARY**\n"
            f"Enhanced professional summary...\n\n"
            f"---\n\n"
            f"**SKILLS**\n\n"
            f"**Category:**\n"
            f"- Skills listed clearly\n\n"
            f"---\n\n"
            f"**PROFESSIONAL EXPERIENCE**\n\n"
            f"**Job Title**\n"
            f"**Company Name, Location**\n"
            f"**Date - Date**\n"
            f"- Enhanced achievement bullet with quantified metrics and business impact\n"
            f"- Another enhanced bullet with specific numbers, percentages, and outcomes\n\n"
            f"CRITICAL: Maintain the exact formatting with bold section headers, proper spacing, "
            f"and horizontal dividers (---) between sections.\n\n"
            f"DELIVERABLE: Resume with polished, high-impact achievement statements in the specified format."
        ),
        agent=agent,
        expected_output="Enhanced resume with quantified, impactful achievement statements and proper formatting."
    )


def generate_evaluation_workflow(
    agent,
    final_content: str,
    target_position: str,
    position_requirements: str
) -> Task:
    """
    Create a compatibility evaluation task
    
    Args:
        agent: AI agent to execute the task
        final_content: Final optimized resume
        target_position: Target job title
        position_requirements: Job requirements
        
    Returns:
        Task: Configured evaluation task
    """
    resume_preview = (
        final_content[:600] + "..." 
        if len(final_content) > 600 
        else final_content
    )
    requirements_preview = (
        position_requirements[:150] + "..." 
        if len(position_requirements) > 150 
        else position_requirements
    )
    
    return Task(
        description=(
            f"Score this resume for {target_position}.\n\n"
            f"JOB REQUIREMENTS: {requirements_preview}\n\n"
            f"RESUME: {resume_preview}\n\n"
            f"Rate 1-5 on: keyword_match, section_structure, quantified_metrics, action_verbs, format_quality.\n"
            f"Calculate overall_score (0-100).\n\n"
            f"Output ONLY valid JSON (no markdown, no extra text):\n"
            f"{{\n"
            f'  "overall_score": 85,\n'
            f'  "breakdown": {{"keyword_match": 4.5, "section_structure": 5, "quantified_metrics": 4, "action_verbs": 4.5, "format_quality": 5}},\n'
            f'  "missing_keywords": ["keyword1", "keyword2"],\n'
            f'  "quick_wins": ["suggestion1", "suggestion2"],\n'
            f'  "summary": "Brief evaluation summary"\n'
            f"}}"
        ),
        agent=agent,
        expected_output="Pure JSON object with scores and recommendations (no markdown formatting)."
    )


def generate_career_guidance_workflow(
    agent,
    resume_content: str,
    target_position: str,
    position_requirements: str
) -> Task:
    """
    Create a career guidance task
    
    Args:
        agent: AI agent to execute the task
        resume_content: Current resume
        target_position: Target role
        position_requirements: Job requirements
        
    Returns:
        Task: Configured career guidance task
    """
    resume_preview = resume_content[:800] + "..." if len(resume_content) > 800 else resume_content
    requirements_preview = position_requirements[:300] + "..." if len(position_requirements) > 300 else position_requirements
    
    return Task(
        description=(
            f"CAREER NAVIGATION REQUEST\n\n"
            f"TARGET ROLE: {target_position}\n\n"
            f"JOB REQUIREMENTS:\n{requirements_preview}\n\n"
            f"CURRENT RESUME:\n{resume_preview}\n\n"
            f"ANALYSIS OBJECTIVES:\n"
            f"1. Identify skill gaps between current profile and target role\n"
            f"2. Recommend specific courses, certifications, or projects\n"
            f"3. Suggest realistic timeline for career transition\n"
            f"4. Highlight transferable skills to emphasize\n"
            f"5. Provide 3-5 actionable next steps\n"
            f"6. Recommend relevant job boards or companies\n"
            f"7. Suggest networking strategies\n\n"
            f"OUTPUT FORMAT (JSON):\n"
            f"{{\n"
            f'  "skill_gaps": ["cloud architecture", "system design"],\n'
            f'  "recommended_actions": [\n'
            f'    {{\n'
            f'      "action": "Complete AWS Solutions Architect certification",\n'
            f'      "timeline": "2-3 months",\n'
            f'      "priority": "High"\n'
            f'    }}\n'
            f'  ],\n'
            f'  "transferable_skills": ["problem solving", "team leadership"],\n'
            f'  "target_companies": ["Amazon", "Microsoft"],\n'
            f'  "networking_tips": "Join AWS user groups, attend cloud conferences"\n'
            f"}}\n\n"
            f"DELIVERABLE: Personalized career roadmap with actionable steps."
        ),
        agent=agent,
        expected_output="JSON-formatted career guidance with specific, actionable recommendations."
    )


def generate_quality_scoring_workflow(
    agent,
    resume_content: str,
    target_position: str
) -> Task:
    """
    Create a comprehensive quality scoring task
    
    Args:
        agent: AI agent to execute the task
        resume_content: Resume to score
        target_position: Target role
        
    Returns:
        Task: Configured quality scoring task
    """
    content_preview = resume_content[:800] + "..." if len(resume_content) > 800 else resume_content
    
    return Task(
        description=(
            f"RESUME QUALITY ASSESSMENT REQUEST\n\n"
            f"TARGET POSITION: {target_position}\n\n"
            f"RESUME TO ASSESS:\n{content_preview}\n\n"
            f"ASSESSMENT DIMENSIONS (Rate 0-10):\n"
            f"1. Clarity: Clear, concise language\n"
            f"2. Impact: Demonstrates value and results\n"
            f"3. Keyword Optimization: Relevant industry terms\n"
            f"4. Quantification: Use of metrics and data\n"
            f"5. Formatting: Professional, consistent layout\n"
            f"6. Achievement Focus: Results-oriented content\n"
            f"7. Storytelling: Coherent career narrative\n"
            f"8. Skills Relevance: Aligned with target role\n"
            f"9. Experience Depth: Sufficient detail\n"
            f"10. Overall Polish: Professional presentation\n\n"
            f"OUTPUT FORMAT (JSON):\n"
            f"{{\n"
            f'  "overall_score": 85,\n'
            f'  "dimension_scores": {{\n'
            f'    "clarity": 9,\n'
            f'    "impact": 8,\n'
            f'    "keyword_optimization": 7,\n'
            f'    "quantification": 8,\n'
            f'    "formatting": 9,\n'
            f'    "achievement_focus": 8,\n'
            f'    "storytelling": 7,\n'
            f'    "skills_relevance": 9,\n'
            f'    "experience_depth": 8,\n'
            f'    "overall_polish": 9\n'
            f'  }},\n'
            f'  "strengths": ["Strong quantification", "Excellent formatting"],\n'
            f'  "weaknesses": ["Limited keyword optimization"],\n'
            f'  "improvement_priority": [\n'
            f'    "Add more industry-specific keywords",\n'
            f'    "Strengthen career narrative"\n'
            f'  ]\n'
            f"}}\n\n"
            f"DELIVERABLE: Comprehensive quality assessment with detailed scoring."
        ),
        agent=agent,
        expected_output="JSON-formatted multi-dimensional quality assessment with improvement recommendations."
    )
