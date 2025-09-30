"""
Workflow Orchestration Engine
Manages the multi-stage AI processing pipeline for resume optimization
"""

import os
from typing import Dict, Any, Tuple
from crewai import Crew, Process
from .ai_specialists import (
    create_document_sanitizer,
    create_ats_strategist,
    create_achievement_architect,
    create_compatibility_analyst,
    create_career_navigator,
    create_metrics_evaluator
)
from .workflow_tasks import (
    generate_sanitization_workflow,
    generate_optimization_workflow,
    generate_enhancement_workflow,
    generate_evaluation_workflow,
    generate_career_guidance_workflow,
    generate_quality_scoring_workflow
)


class OptimizationPipeline:
    """
    Multi-stage resume optimization pipeline orchestrator
    
    Manages the sequential execution of AI agents for comprehensive
    resume transformation and analysis.
    """
    
    def __init__(self, verbose: bool = False):
        """
        Initialize the optimization pipeline
        
        Args:
            verbose: Enable detailed logging of agent activities
        """
        self.verbose = verbose
        self._cache = {}
    
    def _execute_stage(
        self, 
        stage_name: str, 
        agents: list, 
        tasks: list
    ) -> str:
        """
        Execute a single pipeline stage
        
        Args:
            stage_name: Identifier for the processing stage
            agents: List of AI agents for this stage
            tasks: List of tasks to execute
            
        Returns:
            str: Processed output from the stage
        """
        crew = Crew(
            agents=agents,
            tasks=tasks,
            process=Process.sequential,
            verbose=self.verbose
        )
        
        result = crew.kickoff()
        output = str(result).strip()
        
        # Cache intermediate results
        self._cache[stage_name] = output
        
        return output
    
    def execute_full_optimization(
        self,
        raw_document_text: str,
        target_position: str,
        position_requirements: str
    ) -> Tuple[str, str, str, str]:
        """
        Execute the complete 4-stage optimization pipeline
        
        Args:
            raw_document_text: Raw resume text from uploaded file
            target_position: Job title or role being targeted
            position_requirements: Job description or requirements
            
        Returns:
            Tuple containing:
                - sanitized_content: Cleaned resume text
                - optimized_content: ATS-optimized resume
                - enhanced_content: Final polished resume
                - evaluation_report: Detailed assessment
        """
        # Stage 1: Document Sanitization
        sanitizer = create_document_sanitizer()
        sanitization_task = generate_sanitization_workflow(sanitizer, raw_document_text)
        
        sanitized_content = self._execute_stage(
            "sanitization",
            [sanitizer],
            [sanitization_task]
        )
        
        # Stage 2: ATS Optimization
        strategist = create_ats_strategist()
        optimization_task = generate_optimization_workflow(
            strategist,
            sanitized_content,
            target_position,
            position_requirements
        )
        
        optimized_content = self._execute_stage(
            "optimization",
            [strategist],
            [optimization_task]
        )
        
        # Stage 3: Achievement Enhancement
        architect = create_achievement_architect()
        enhancement_task = generate_enhancement_workflow(architect, optimized_content)
        
        enhanced_content = self._execute_stage(
            "enhancement",
            [architect],
            [enhancement_task]
        )
        
        # Stage 4: Compatibility Evaluation
        analyst = create_compatibility_analyst()
        evaluation_task = generate_evaluation_workflow(
            analyst,
            enhanced_content,
            target_position,
            position_requirements
        )
        
        evaluation_report = self._execute_stage(
            "evaluation",
            [analyst],
            [evaluation_task]
        )
        
        return sanitized_content, optimized_content, enhanced_content, evaluation_report
    
    def execute_career_guidance(
        self,
        resume_content: str,
        target_position: str,
        position_requirements: str
    ) -> str:
        """
        Generate personalized career guidance and next steps
        
        Args:
            resume_content: Current resume content
            target_position: Desired job title
            position_requirements: Job requirements/description
            
        Returns:
            str: Career guidance report
        """
        navigator = create_career_navigator()
        guidance_task = generate_career_guidance_workflow(
            navigator,
            resume_content,
            target_position,
            position_requirements
        )
        
        return self._execute_stage(
            "career_guidance",
            [navigator],
            [guidance_task]
        )
    
    def execute_quality_assessment(
        self,
        resume_content: str,
        target_position: str
    ) -> str:
        """
        Perform comprehensive quality scoring across multiple dimensions
        
        Args:
            resume_content: Resume to evaluate
            target_position: Target job role
            
        Returns:
            str: Detailed quality metrics report
        """
        evaluator = create_metrics_evaluator()
        scoring_task = generate_quality_scoring_workflow(
            evaluator,
            resume_content,
            target_position
        )
        
        return self._execute_stage(
            "quality_scoring",
            [evaluator],
            [scoring_task]
        )
    
    def get_cached_stage(self, stage_name: str) -> str:
        """
        Retrieve cached result from a previous stage
        
        Args:
            stage_name: Name of the stage to retrieve
            
        Returns:
            str: Cached stage output or empty string
        """
        return self._cache.get(stage_name, "")
    
    def clear_cache(self):
        """Clear all cached pipeline results"""
        self._cache.clear()


# Legacy compatibility function
def run_pipeline(
    raw_resume_text: str,
    job_title: str,
    job_description: str
) -> Tuple[str, str, str, str]:
    """
    Legacy compatibility wrapper for the optimization pipeline
    
    Args:
        raw_resume_text: Raw resume content
        job_title: Target job title
        job_description: Job description/requirements
        
    Returns:
        Tuple: (cleaned, rewritten, final_resume, evaluation)
    """
    pipeline = OptimizationPipeline(verbose=False)
    return pipeline.execute_full_optimization(
        raw_resume_text,
        job_title,
        job_description
    )
