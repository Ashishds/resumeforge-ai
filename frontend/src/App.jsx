import { useState } from 'react'
import { Toaster } from 'react-hot-toast'
import Header from './components/Header'
import UploadSection from './components/UploadSection'
import ResultsSection from './components/ResultsSection'
import FeaturesSection from './components/FeaturesSection'

function App() {
  const [results, setResults] = useState(null)
  const [isProcessing, setIsProcessing] = useState(false)

  return (
    <div className="min-h-screen">
      <Toaster position="top-right" />
      
      <Header />
      
      <main className="container mx-auto px-4 py-8 max-w-7xl">
        {!results ? (
          <>
            <UploadSection 
              setResults={setResults} 
              isProcessing={isProcessing}
              setIsProcessing={setIsProcessing}
            />
            <FeaturesSection />
          </>
        ) : (
          <ResultsSection 
            results={results} 
            onReset={() => setResults(null)} 
          />
        )}
      </main>
      
      <footer className="bg-white border-t border-gray-200 mt-20">
        <div className="container mx-auto px-4 py-8 max-w-7xl">
          <div className="text-center text-gray-600">
            <p className="text-sm">
              © 2025 ResumeForge AI. Transform your career with intelligent resume optimization.
            </p>
          </div>
        </div>
      </footer>
    </div>
  )
}

export default App
