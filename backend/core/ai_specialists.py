"""
AI Specialist Agents Configuration
Defines specialized AI agents for resume optimization workflow
"""

from crewai import Agent
import os

# AI Model Configuration
AI_MODEL = "gpt-4o-mini"
TEMPERATURE_PRECISE = 0.0
TEMPERATURE_BALANCED = 0.2
TEMPERATURE_CREATIVE = 0.3
MAX_ITERATIONS = 1
EXECUTION_TIMEOUT = 60  # Reduced from 120 to 60 seconds for faster response


class AISpecialistFactory:
    """Factory class for creating specialized AI agents"""
    
    @staticmethod
    def create_document_sanitizer():
        """
        Creates an AI agent specialized in document cleaning and normalization
        
        Returns:
            Agent: Document sanitization specialist
        """
        return Agent(
            role="Document Sanitization Specialist",
            goal="Transform raw document text into clean, structured content optimized for AI processing.",
            backstory=(
                "You are a meticulous document processing expert with years of experience "
                "cleaning and normalizing text from various sources. Your expertise lies in "
                "removing formatting artifacts, normalizing structure, and preserving critical "
                "content while eliminating noise. You work with precision and efficiency."
            ),
            model=AI_MODEL,
            temperature=TEMPERATURE_PRECISE,
            max_iter=MAX_ITERATIONS,
            max_execution_time=EXECUTION_TIMEOUT
        )
    
    @staticmethod
    def create_ats_strategist():
        """
        Creates an AI agent specialized in ATS optimization and keyword strategy
        
        Returns:
            Agent: ATS optimization strategist
        """
        return Agent(
            role="ATS Optimization Strategist",
            goal="Engineer high-performance resumes that achieve 85+ ATS compatibility scores.",
            backstory=(
                "You are a senior recruitment technology consultant who has reverse-engineered "
                "Applicant Tracking Systems used by Fortune 500 companies. Your deep understanding "
                "of ATS algorithms allows you to strategically position keywords, structure content, "
                "and format resumes for maximum parsing accuracy. You combine technical expertise "
                "with storytelling to create compelling, ATS-friendly narratives."
            ),
            model=AI_MODEL,
            temperature=TEMPERATURE_CREATIVE,
            max_iter=MAX_ITERATIONS,
            max_execution_time=EXECUTION_TIMEOUT
        )
    
    @staticmethod
    def create_achievement_architect():
        """
        Creates an AI agent specialized in crafting impactful achievement statements
        
        Returns:
            Agent: Achievement architecture specialist
        """
        return Agent(
            role="Achievement Architecture Specialist",
            goal="Transform ordinary descriptions into quantified, high-impact achievement statements.",
            backstory=(
                "You are an executive resume writer who specializes in the STAR method "
                "(Situation, Task, Action, Result). Your superpower is identifying implicit "
                "achievements and quantifying impact with metrics. You craft bullet points that "
                "combine powerful action verbs, specific contributions, and measurable outcomes "
                "to create compelling professional narratives."
            ),
            model=AI_MODEL,
            temperature=TEMPERATURE_BALANCED,
            max_iter=MAX_ITERATIONS,
            max_execution_time=EXECUTION_TIMEOUT
        )
    
    @staticmethod
    def create_compatibility_analyst():
        """
        Creates an AI agent specialized in resume scoring and gap analysis
        
        Returns:
            Agent: Compatibility analysis specialist
        """
        return Agent(
            role="ATS Compatibility Analyst",
            goal="Deliver precise ATS compatibility scores with actionable optimization roadmaps.",
            backstory=(
                "You are a data-driven recruitment analytics expert who evaluates resumes "
                "against ATS algorithms. Your systematic approach analyzes keyword density, "
                "structural integrity, formatting compliance, and content quality. You provide "
                "detailed scoring breakdowns and prioritized recommendations that hiring "
                "managers can immediately implement."
            ),
            model=AI_MODEL,
            temperature=TEMPERATURE_PRECISE,
            max_iter=MAX_ITERATIONS,
            max_execution_time=EXECUTION_TIMEOUT
        )
    
    @staticmethod
    def create_career_navigator():
        """
        Creates an AI agent specialized in career guidance and strategic advice
        
        Returns:
            Agent: Career navigation specialist
        """
        return Agent(
            role="Career Navigation Strategist",
            goal="Provide personalized career guidance and strategic next-step recommendations.",
            backstory=(
                "You are a seasoned career coach with 15+ years of experience guiding professionals "
                "through career transitions. You analyze industry trends, skill gaps, and market "
                "demands to provide actionable career advice. Your recommendations are specific, "
                "achievable, and aligned with current job market realities."
            ),
            model=AI_MODEL,
            temperature=TEMPERATURE_BALANCED,
            max_iter=MAX_ITERATIONS,
            max_execution_time=EXECUTION_TIMEOUT
        )
    
    @staticmethod
    def create_metrics_evaluator():
        """
        Creates an AI agent specialized in resume quality scoring
        
        Returns:
            Agent: Metrics evaluation specialist
        """
        return Agent(
            role="Resume Quality Metrics Evaluator",
            goal="Conduct comprehensive resume assessments across 10+ quality dimensions.",
            backstory=(
                "You are a resume quality auditor who has evaluated thousands of resumes "
                "across industries. You assess content on multiple dimensions including clarity, "
                "impact, keyword optimization, quantification, formatting, and storytelling. "
                "Your multi-dimensional scoring system helps candidates understand exactly "
                "where their resume excels and where it needs improvement."
            ),
            model=AI_MODEL,
            temperature=TEMPERATURE_PRECISE,
            max_iter=MAX_ITERATIONS,
            max_execution_time=EXECUTION_TIMEOUT
        )


# Convenience functions for backward compatibility
def create_document_sanitizer():
    return AISpecialistFactory.create_document_sanitizer()

def create_ats_strategist():
    return AISpecialistFactory.create_ats_strategist()

def create_achievement_architect():
    return AISpecialistFactory.create_achievement_architect()

def create_compatibility_analyst():
    return AISpecialistFactory.create_compatibility_analyst()

def create_career_navigator():
    return AISpecialistFactory.create_career_navigator()

def create_metrics_evaluator():
    return AISpecialistFactory.create_metrics_evaluator()
