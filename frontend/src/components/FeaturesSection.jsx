import { motion } from 'framer-motion'
import { 
  Zap, 
  Target, 
  TrendingUp, 
  Award, 
  Download,
  Shield
} from 'lucide-react'

const features = [
  {
    icon: Zap,
    title: 'AI-Powered Optimization',
    description: 'Multi-agent AI system analyzes and transforms your resume for maximum impact'
  },
  {
    icon: Target,
    title: 'ATS-Friendly Format',
    description: 'Optimized to pass through Applicant Tracking Systems with 85+ compatibility score'
  },
  {
    icon: TrendingUp,
    title: 'Keyword Matching',
    description: 'Strategic keyword placement aligned with job requirements and industry standards'
  },
  {
    icon: Award,
    title: 'Achievement Enhancement',
    description: 'Transform bullet points into quantified, high-impact achievement statements'
  },
  {
    icon: Download,
    title: 'Multiple Export Formats',
    description: 'Download your optimized resume as PDF, DOCX, or plain text'
  },
  {
    icon: Shield,
    title: 'Quality Scoring',
    description: 'Comprehensive evaluation with actionable recommendations for improvement'
  }
]

export default function FeaturesSection() {
  return (
    <section className="mt-16">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, delay: 0.2 }}
      >
        <h2 className="text-3xl font-bold text-center text-gray-800 mb-4">
          Why Choose ResumeForge AI?
        </h2>
        <p className="text-center text-gray-600 mb-12 max-w-2xl mx-auto">
          Our advanced AI technology ensures your resume stands out from the competition
        </p>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {features.map((feature, index) => {
            const Icon = feature.icon
            return (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 0.1 * index }}
                className="card hover:scale-105 transition-transform duration-300"
              >
                <div className="flex items-start gap-4">
                  <div className="flex-shrink-0">
                    <div className="w-12 h-12 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-lg flex items-center justify-center">
                      <Icon className="w-6 h-6 text-white" />
                    </div>
                  </div>
                  <div>
                    <h3 className="font-semibold text-gray-800 mb-2">
                      {feature.title}
                    </h3>
                    <p className="text-sm text-gray-600">
                      {feature.description}
                    </p>
                  </div>
                </div>
              </motion.div>
            )
          })}
        </div>
      </motion.div>
    </section>
  )
}
