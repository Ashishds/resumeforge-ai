import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

/**
 * Optimize resume from uploaded file
 */
export const optimizeResumeFile = async (file, jobTitle, jobDescription) => {
  const formData = new FormData()
  formData.append('file', file)
  formData.append('job_title', jobTitle)
  formData.append('job_description', jobDescription)

  const response = await apiClient.post('/api/optimize-file', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  })

  return response.data
}

/**
 * Optimize resume from text
 */
export const optimizeResumeText = async (resumeText, jobTitle, jobDescription) => {
  const response = await apiClient.post('/api/optimize', {
    resume_text: resumeText,
    job_title: jobTitle,
    job_description: jobDescription,
  })

  return response.data
}

/**
 * Get career guidance
 */
export const getCareerGuidance = async (resumeText, jobTitle, jobDescription) => {
  const response = await apiClient.post('/api/career-guidance', {
    resume_text: resumeText,
    job_title: jobTitle,
    job_description: jobDescription,
  })

  return response.data
}

/**
 * Get quality score
 */
export const getQualityScore = async (resumeText, jobTitle) => {
  const response = await apiClient.post('/api/quality-score', {
    resume_text: resumeText,
    job_title: jobTitle,
  })

  return response.data
}

/**
 * Download resume as PDF
 */
export const downloadPDF = async (resumeText, filename = 'resume.pdf') => {
  const formData = new FormData()
  formData.append('resume_text', resumeText)
  formData.append('filename', filename)

  const response = await apiClient.post('/api/download/pdf', formData, {
    responseType: 'blob',
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  })

  // Create download link
  const url = window.URL.createObjectURL(new Blob([response.data]))
  const link = document.createElement('a')
  link.href = url
  link.setAttribute('download', filename)
  document.body.appendChild(link)
  link.click()
  link.remove()
  window.URL.revokeObjectURL(url)
}

/**
 * Download resume as DOCX
 */
export const downloadDOCX = async (resumeText, filename = 'resume.docx') => {
  const formData = new FormData()
  formData.append('resume_text', resumeText)
  formData.append('filename', filename)

  const response = await apiClient.post('/api/download/docx', formData, {
    responseType: 'blob',
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  })

  // Create download link
  const url = window.URL.createObjectURL(new Blob([response.data]))
  const link = document.createElement('a')
  link.href = url
  link.setAttribute('download', filename)
  document.body.appendChild(link)
  link.click()
  link.remove()
  window.URL.revokeObjectURL(url)
}

export default apiClient
