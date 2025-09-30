import { useState } from 'react'
import { motion } from 'framer-motion'
import { 
  Download, 
  FileText, 
  CheckCircle, 
  TrendingUp, 
  Award,
  RefreshCw,
  Star,
  Target
} from 'lucide-react'
import toast from 'react-hot-toast'
import { downloadPDF, downloadDOCX } from '../services/api'

export default function ResultsSection({ results, onReset }) {
  const [activeTab, setActiveTab] = useState('enhanced')

  const tabs = [
    { id: 'sanitized', label: 'Cleaned', icon: FileText },
    { id: 'optimized', label: 'ATS-Optimized', icon: TrendingUp },
    { id: 'enhanced', label: 'Final Enhanced', icon: Star },
    { id: 'evaluation', label: 'Evaluation', icon: Award },
  ]

  const handleDownloadPDF = async () => {
    const toastId = toast.loading('Generating PDF...')
    try {
      await downloadPDF(results.enhanced)
      toast.success('PDF downloaded successfully!', { id: toastId })
    } catch (error) {
      toast.error('Failed to download PDF', { id: toastId })
    }
  }

  const handleDownloadDOCX = async () => {
    const toastId = toast.loading('Generating DOCX...')
    try {
      await downloadDOCX(results.enhanced)
      toast.success('DOCX downloaded successfully!', { id: toastId })
    } catch (error) {
      toast.error('Failed to download DOCX', { id: toastId })
    }
  }

  const renderEvaluationContent = () => {
    const evaluation = results.evaluation

    if (!evaluation || typeof evaluation !== 'object') {
      return (
        <div className="text-gray-600">
          <pre className="whitespace-pre-wrap bg-gray-50 p-4 rounded-lg">
            {JSON.stringify(evaluation, null, 2)}
          </pre>
        </div>
      )
    }

    return (
      <div className="space-y-6">
        {/* Overall Score */}
        {evaluation.overall_score !== undefined && (
          <div className="text-center">
            <div className="inline-flex items-center justify-center w-32 h-32 rounded-full bg-gradient-to-br from-green-400 to-blue-500 text-white">
              <div>
                <div className="text-4xl font-bold">{evaluation.overall_score}</div>
                <div className="text-sm">/ 100</div>
              </div>
            </div>
            <p className="mt-4 text-lg font-semibold text-gray-700">ATS Compatibility Score</p>
          </div>
        )}

        {/* Breakdown */}
        {evaluation.breakdown && (
          <div>
            <h4 className="font-semibold text-gray-800 mb-3 flex items-center gap-2">
              <Target className="w-5 h-5 text-blue-600" />
              Score Breakdown
            </h4>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              {Object.entries(evaluation.breakdown).map(([key, value]) => (
                <div key={key} className="bg-gray-50 p-3 rounded-lg">
                  <div className="flex justify-between items-center">
                    <span className="text-sm text-gray-600 capitalize">
                      {key.replace(/_/g, ' ')}
                    </span>
                    <span className="font-semibold text-blue-600">
                      {typeof value === 'number' ? value.toFixed(1) : value} / 5
                    </span>
                  </div>
                  <div className="mt-2 bg-gray-200 rounded-full h-2">
                    <div
                      className="bg-gradient-to-r from-blue-500 to-green-500 h-2 rounded-full transition-all duration-500"
                      style={{ width: `${((typeof value === 'number' ? value : 0) / 5) * 100}%` }}
                    />
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Missing Keywords */}
        {evaluation.missing_keywords && evaluation.missing_keywords.length > 0 && (
          <div>
            <h4 className="font-semibold text-gray-800 mb-3">Missing Keywords</h4>
            <div className="flex flex-wrap gap-2">
              {evaluation.missing_keywords.map((keyword, index) => (
                <span
                  key={index}
                  className="px-3 py-1 bg-red-50 text-red-700 rounded-full text-sm border border-red-200"
                >
                  {keyword}
                </span>
              ))}
            </div>
          </div>
        )}

        {/* Quick Wins */}
        {evaluation.quick_wins && evaluation.quick_wins.length > 0 && (
          <div>
            <h4 className="font-semibold text-gray-800 mb-3 flex items-center gap-2">
              <CheckCircle className="w-5 h-5 text-green-600" />
              Quick Wins
            </h4>
            <ul className="space-y-2">
              {evaluation.quick_wins.map((win, index) => (
                <li
                  key={index}
                  className="flex items-start gap-2 text-gray-700 bg-green-50 p-3 rounded-lg border border-green-200"
                >
                  <CheckCircle className="w-5 h-5 text-green-600 flex-shrink-0 mt-0.5" />
                  <span>{win}</span>
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Summary */}
        {evaluation.summary && (
          <div>
            <h4 className="font-semibold text-gray-800 mb-3">Summary</h4>
            <p className="text-gray-700 bg-blue-50 p-4 rounded-lg border border-blue-200">
              {evaluation.summary}
            </p>
          </div>
        )}
      </div>
    )
  }

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.5 }}
      className="space-y-6"
    >
      {/* Action Buttons */}
      <div className="flex flex-wrap gap-4 justify-between items-center">
        <h2 className="text-2xl font-bold text-gray-800 flex items-center gap-2">
          <CheckCircle className="w-7 h-7 text-green-600" />
          Your Optimized Resume
        </h2>
        
        <div className="flex gap-3">
          <button onClick={handleDownloadPDF} className="btn-primary flex items-center gap-2">
            <Download className="w-4 h-4" />
            Download PDF
          </button>
          <button onClick={handleDownloadDOCX} className="btn-secondary flex items-center gap-2">
            <Download className="w-4 h-4" />
            Download DOCX
          </button>
          <button onClick={onReset} className="btn-secondary flex items-center gap-2">
            <RefreshCw className="w-4 h-4" />
            New Resume
          </button>
        </div>
      </div>

      {/* Tabs */}
      <div className="card">
        <div className="flex gap-2 border-b border-gray-200 mb-6 overflow-x-auto">
          {tabs.map((tab) => {
            const Icon = tab.icon
            return (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`flex items-center gap-2 px-4 py-3 font-medium transition-all duration-200 border-b-2 whitespace-nowrap ${
                  activeTab === tab.id
                    ? 'border-blue-600 text-blue-600'
                    : 'border-transparent text-gray-600 hover:text-gray-800'
                }`}
              >
                <Icon className="w-4 h-4" />
                {tab.label}
              </button>
            )
          })}
        </div>

        {/* Tab Content */}
        <div className="min-h-[400px]">
          {activeTab === 'evaluation' ? (
            renderEvaluationContent()
          ) : (
            <div className="bg-gray-50 p-6 rounded-lg border border-gray-200">
              <pre className="whitespace-pre-wrap text-sm text-gray-800 font-mono">
                {results[activeTab]}
              </pre>
            </div>
          )}
        </div>
      </div>
    </motion.div>
  )
}
