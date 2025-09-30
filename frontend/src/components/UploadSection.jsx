import { useState } from 'react'
import { motion } from 'framer-motion'
import { Upload, Briefcase, FileText, Loader } from 'lucide-react'
import toast from 'react-hot-toast'
import { optimizeResumeFile } from '../services/api'

export default function UploadSection({ setResults, isProcessing, setIsProcessing }) {
  const [file, setFile] = useState(null)
  const [jobTitle, setJobTitle] = useState('')
  const [jobDescription, setJobDescription] = useState('')
  const [dragActive, setDragActive] = useState(false)

  const handleDrag = (e) => {
    e.preventDefault()
    e.stopPropagation()
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true)
    } else if (e.type === "dragleave") {
      setDragActive(false)
    }
  }

  const handleDrop = (e) => {
    e.preventDefault()
    e.stopPropagation()
    setDragActive(false)
    
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      setFile(e.dataTransfer.files[0])
      toast.success('File uploaded successfully!')
    }
  }

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0])
      toast.success('File uploaded successfully!')
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    
    if (!file) {
      toast.error('Please upload a resume file')
      return
    }
    
    if (!jobTitle.trim()) {
      toast.error('Please enter a job title')
      return
    }
    
    if (!jobDescription.trim()) {
      toast.error('Please enter a job description')
      return
    }

    setIsProcessing(true)
    const loadingToast = toast.loading('AI agents are optimizing your resume...')

    try {
      const data = await optimizeResumeFile(file, jobTitle, jobDescription)
      
      if (data.success) {
        setResults(data)
        toast.success('Resume optimized successfully!', { id: loadingToast })
      } else {
        toast.error(data.message || 'Optimization failed', { id: loadingToast })
      }
    } catch (error) {
      console.error('Optimization error:', error)
      toast.error(error.message || 'An error occurred during optimization', { id: loadingToast })
    } finally {
      setIsProcessing(false)
    }
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="max-w-4xl mx-auto"
    >
      <div className="card">
        <h2 className="text-2xl font-bold text-gray-800 mb-6 text-center">
          Upload Your Resume & Get Started
        </h2>

        <form onSubmit={handleSubmit} className="space-y-6">
          {/* File Upload */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              <FileText className="inline w-4 h-4 mr-2" />
              Resume File (PDF, DOCX, or TXT)
            </label>
            <div
              className={`border-2 border-dashed rounded-lg p-8 text-center transition-all duration-200 ${
                dragActive
                  ? 'border-blue-500 bg-blue-50'
                  : file
                  ? 'border-green-500 bg-green-50'
                  : 'border-gray-300 hover:border-blue-400'
              }`}
              onDragEnter={handleDrag}
              onDragLeave={handleDrag}
              onDragOver={handleDrag}
              onDrop={handleDrop}
            >
              <input
                type="file"
                id="resume-upload"
                accept=".pdf,.docx,.txt"
                onChange={handleFileChange}
                className="hidden"
              />
              <label htmlFor="resume-upload" className="cursor-pointer">
                <Upload className="w-12 h-12 mx-auto mb-4 text-gray-400" />
                {file ? (
                  <div>
                    <p className="text-green-600 font-semibold">{file.name}</p>
                    <p className="text-sm text-gray-500 mt-1">
                      Click to change file
                    </p>
                  </div>
                ) : (
                  <div>
                    <p className="text-gray-600 font-medium">
                      Drag & drop your resume here
                    </p>
                    <p className="text-sm text-gray-500 mt-1">
                      or click to browse files
                    </p>
                  </div>
                )}
              </label>
            </div>
          </div>

          {/* Job Title */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              <Briefcase className="inline w-4 h-4 mr-2" />
              Target Job Title
            </label>
            <input
              type="text"
              value={jobTitle}
              onChange={(e) => setJobTitle(e.target.value)}
              placeholder="e.g., Senior Software Engineer"
              className="input-field"
            />
          </div>

          {/* Job Description */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Job Description / Requirements
            </label>
            <textarea
              value={jobDescription}
              onChange={(e) => setJobDescription(e.target.value)}
              placeholder="Paste the job description here..."
              rows="8"
              className="textarea-field"
            />
          </div>

          {/* Submit Button */}
          <button
            type="submit"
            disabled={isProcessing}
            className="btn-primary w-full flex items-center justify-center gap-2"
          >
            {isProcessing ? (
              <>
                <Loader className="w-5 h-5 animate-spin" />
                Processing with AI...
              </>
            ) : (
              <>
                <Briefcase className="w-5 h-5" />
                Optimize My Resume
              </>
            )}
          </button>
        </form>
      </div>
    </motion.div>
  )
}
