import { motion } from 'framer-motion'
import { Sparkles, Zap } from 'lucide-react'

export default function Header() {
  return (
    <header className="bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 text-white">
      <div className="container mx-auto px-4 py-12 max-w-7xl">
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="text-center"
        >
          <div className="flex items-center justify-center gap-3 mb-4">
            <Sparkles className="w-10 h-10 text-yellow-300" />
            <h1 className="text-5xl font-bold text-white drop-shadow-lg">
              ResumeForge AI
            </h1>
            <Zap className="w-10 h-10 text-yellow-300" />
          </div>
          
          <p className="text-xl text-blue-100 max-w-3xl mx-auto mb-6">
            Transform your resume with cutting-edge AI technology. 
            Get ATS-optimized resumes, career guidance, and quality scores in seconds.
          </p>
          
          <div className="flex items-center justify-center gap-6 text-sm">
            <div className="flex items-center gap-2">
              <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
              <span className="text-blue-100">Multi-Agent AI</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
              <span className="text-blue-100">85+ ATS Score</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
              <span className="text-blue-100">PDF Export</span>
            </div>
          </div>
        </motion.div>
      </div>
    </header>
  )
}
