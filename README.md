# 🚀 ResumeForge AI - Intelligent Resume Optimization Platform

Transform your resume with cutting-edge multi-agent AI technology. Get ATS-optimized resumes, career guidance, and comprehensive quality scores—all in seconds.

![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![React](https://img.shields.io/badge/react-18.2-blue.svg)

## ✨ Features

### 🤖 **Multi-Agent AI System**
- **Document Sanitization Specialist**: Cleans and normalizes resume text
- **ATS Optimization Strategist**: Engineers high-performance, ATS-friendly resumes
- **Achievement Architect**: Transforms bullets into quantified impact statements
- **Compatibility Analyst**: Provides detailed ATS scoring and gap analysis
- **Career Navigator**: Offers personalized career guidance and next steps
- **Quality Metrics Evaluator**: Conducts 10-dimensional quality assessment

### 📊 **Key Capabilities**
- ✅ 85+ ATS Compatibility Score
- ✅ Strategic Keyword Matching
- ✅ Quantified Achievement Enhancement
- ✅ Multi-Format Support (PDF, DOCX, TXT)
- ✅ Professional PDF Export
- ✅ Comprehensive Quality Scoring
- ✅ Career Guidance & Roadmaps

### 🎨 **Modern Tech Stack**

**Backend:**
- FastAPI (High-performance async API)
- CrewAI (Multi-agent orchestration)
- GPT-4o-mini (Cost-effective AI)
- ReportLab (Professional PDF generation)

**Frontend:**
- React 18 with Vite
- Tailwind CSS (Modern UI)
- Framer Motion (Smooth animations)
- Axios (API communication)

---

## 🚀 Quick Start

### **Prerequisites**
- Python 3.10+
- Node.js 18+
- OpenAI API Key

### **Backend Setup**

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# Run backend server
uvicorn backend.api.main:app --reload --port 8000
```

Backend will run at: **http://localhost:8000**

API Documentation: **http://localhost:8000/api/docs**

### **Frontend Setup**

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

Frontend will run at: **http://localhost:3000**

---

## 📁 Project Structure

```
resume_parse_crewai/
├── backend/                      # Python FastAPI backend
│   ├── api/
│   │   └── main.py              # FastAPI application & endpoints
│   ├── core/
│   │   ├── ai_specialists.py    # 6 AI agent definitions
│   │   ├── workflow_orchestrator.py  # Pipeline orchestration
│   │   └── workflow_tasks.py    # Task definitions
│   ├── services/
│   │   └── document_processor.py # File parsing & PDF generation
│   └── requirements.txt         # Python dependencies
├── frontend/                     # React frontend
│   ├── src/
│   │   ├── components/          # React components
│   │   │   ├── Header.jsx
│   │   │   ├── UploadSection.jsx
│   │   │   ├── ResultsSection.jsx
│   │   │   └── FeaturesSection.jsx
│   │   ├── services/
│   │   │   └── api.js           # API client
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── package.json             # Node dependencies
│   └── vite.config.js           # Vite configuration
├── vercel.json                  # Vercel deployment config
├── railway.json                 # Railway deployment config
├── nixpacks.toml               # Railway build config
├── STEP_BY_STEP_DEPLOYMENT.md  # Beginner-friendly deployment guide
├── QUICK_DEPLOY_VERCEL_RAILWAY.md # Quick deployment steps
├── DEPLOYMENT_GUIDE_VERCEL_RAILWAY.md # Complete deployment guide
└── README.md                    # This file
```

---

## 🔧 API Endpoints

### **Core Endpoints**

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check |
| `GET` | `/api/health` | Detailed health status |
| `POST` | `/api/optimize-file` | Optimize resume from file upload |
| `POST` | `/api/optimize` | Optimize resume from text |
| `POST` | `/api/career-guidance` | Get career guidance |
| `POST` | `/api/quality-score` | Get quality assessment |
| `POST` | `/api/download/pdf` | Download resume as PDF |
| `POST` | `/api/download/docx` | Download resume as DOCX |

### **Example API Usage**

```bash
# Upload and optimize resume
curl -X POST http://localhost:8000/api/optimize-file \
  -F "file=@resume.pdf" \
  -F "job_title=Senior Software Engineer" \
  -F "job_description=Looking for Python expert..."
```

---

## 🎯 How It Works

### **1. Document Upload**
User uploads resume (PDF, DOCX, or TXT) via drag-and-drop interface.

### **2. AI Processing Pipeline**
```
Document → Sanitization → ATS Optimization → Achievement Enhancement → Evaluation
```

**Stage 1: Sanitization**
- Remove artifacts and normalize formatting
- Preserve all substantive content
- Clean structure for AI processing

**Stage 2: ATS Optimization**
- Extract keywords from job description
- Strategic keyword placement
- Standard ATS-friendly section headers
- Optimize for 85+ compatibility score

**Stage 3: Achievement Enhancement**
- Transform bullets using STAR method
- Add quantified metrics (%, $, time)
- Employ strong action verbs
- Highlight business impact

**Stage 4: Compatibility Evaluation**
- Multi-dimensional scoring (5 categories)
- Identify missing keywords
- Provide actionable quick wins
- Generate comprehensive report

### **3. Results Display**
- 4 tabs showing each processing stage
- Interactive evaluation dashboard
- One-click PDF/DOCX download
- Professional formatting

---

## 🌟 New Features (v2.0)

### **1. Enhanced Resume Scoring System**
Comprehensive 10-dimensional quality assessment:
- Clarity
- Impact
- Keyword Optimization
- Quantification
- Formatting
- Achievement Focus
- Storytelling
- Skills Relevance
- Experience Depth
- Overall Polish

### **2. AI Career Coach**
Personalized career guidance including:
- Skill gap analysis
- Recommended certifications/courses
- Career transition timeline
- Transferable skills identification
- Target company suggestions
- Networking strategies

### **3. Professional PDF Export**
- Clean, ATS-friendly formatting
- Professional typography
- Optimized for printing and digital viewing
- Consistent spacing and structure

---

## 🚀 Deployment - Vercel + Railway (Recommended)

### **Quick Deploy (2-3 minutes)**

**Backend (Railway):**
1. Go to [railway.app](https://railway.app) → "New Project"
2. Connect GitHub repository
3. Add environment variable: `OPENAI_API_KEY = sk-your-key`
4. Deploy automatically

**Frontend (Vercel):**
1. Go to [vercel.com](https://vercel.com) → "New Project"
2. Connect GitHub repository  
3. Add environment variable: `VITE_API_URL = https://your-backend.railway.app`
4. Deploy automatically

**Why Vercel + Railway?**
- ✅ **No sleep time** (unlike Render free tier)
- ✅ **Faster deployment** (2-3 minutes vs 10+ minutes)
- ✅ **Better performance** (global CDN)
- ✅ **Easier setup** (no complex config files)
- ✅ **Free forever** (generous limits)

📖 **Step-by-Step Guide:** [STEP_BY_STEP_DEPLOYMENT.md](./STEP_BY_STEP_DEPLOYMENT.md) (Beginner-friendly)
⚡ **Quick Deploy:** [QUICK_DEPLOY_VERCEL_RAILWAY.md](./QUICK_DEPLOY_VERCEL_RAILWAY.md)
📚 **Full Guide:** [DEPLOYMENT_GUIDE_VERCEL_RAILWAY.md](./DEPLOYMENT_GUIDE_VERCEL_RAILWAY.md)

### **Manual Deployment**

**Backend:**
```bash
cd backend
pip install -r requirements.txt
gunicorn backend.api.main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker
```

**Frontend:**
```bash
cd frontend
npm install
npm run build
npm run preview
```

---

## 🔒 Environment Variables

### **Railway Backend**
```env
OPENAI_API_KEY=sk-your-actual-key-here
ENVIRONMENT=production
ALLOWED_ORIGINS=https://your-frontend.vercel.app
```

### **Vercel Frontend**
```env
VITE_API_URL=https://your-backend.railway.app
```

### **Local Development**
```env
# Backend (.env)
OPENAI_API_KEY=sk-your-actual-key-here
PORT=8000
ENVIRONMENT=development

# Frontend
VITE_API_URL=http://localhost:8000
```

---

## 📊 Performance Metrics

- **Processing Time:** 25-50 seconds per resume
- **ATS Score Target:** 85+/100
- **Keyword Match Rate:** 80-95%
- **Cost per Resume:** ~$0.01-0.03 (GPT-4o-mini)
- **Supported File Sizes:** Up to 200MB
- **Concurrent Users:** Optimized for 100+ simultaneous users

---

## 🛠️ Development

### **Run Tests**
```bash
# Backend
cd backend
pytest

# Frontend
cd frontend
npm test
```

### **Linting**
```bash
# Backend
flake8 backend/

# Frontend
npm run lint
```

### **Build for Production**
```bash
# Frontend
npm run build
```

---

## 🐛 Troubleshooting

### **Common Issues**

**1. API Key Error**
```
AuthenticationError: Incorrect API key
```
**Solution:** Verify `OPENAI_API_KEY` in `.env` file

**2. CORS Error**
```
Access-Control-Allow-Origin error
```
**Solution:** Update `ALLOWED_ORIGINS` in Railway backend environment variables

**3. File Upload Fails**
```
Could not extract text from file
```
**Solution:** Ensure file is valid PDF/DOCX with readable text

**4. Port Already in Use**
```
Address already in use
```
**Solution:** Kill process on port 8000/3000 or use different port

---

## 📈 Roadmap

### **Coming Soon**
- [ ] Multi-language support
- [ ] Industry-specific templates
- [ ] Batch processing
- [ ] A/B testing for resume variants
- [ ] Integration with LinkedIn
- [ ] Chrome extension
- [ ] Mobile app (React Native)

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- **CrewAI** for multi-agent orchestration
- **OpenAI** for GPT models
- **FastAPI** for modern Python APIs
- **React** for dynamic UIs
- **Tailwind CSS** for beautiful styling

---

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**🎯 Transform your career with AI-powered resume optimization!**

**Ready to get started?**
1. Follow the [Step-by-Step Deployment Guide](./STEP_BY_STEP_DEPLOYMENT.md)
2. Deploy to Vercel + Railway (free)
3. Upload your resume
4. Get your ATS-optimized resume in seconds!

**Deployment Guides:**
- 📖 [Step-by-Step Guide](./STEP_BY_STEP_DEPLOYMENT.md) (Beginner-friendly)
- ⚡ [Quick Deploy](./QUICK_DEPLOY_VERCEL_RAILWAY.md) (Fast setup)
- 📚 [Complete Guide](./DEPLOYMENT_GUIDE_VERCEL_RAILWAY.md) (Detailed)

**After Deployment:**
- 🌐 **Your App:** `https://your-app.vercel.app`
- 🔧 **API:** `https://your-app.railway.app`
- 📚 **API Docs:** `https://your-app.railway.app/api/docs`

---

Built with ❤️ using FastAPI, React, and CrewAI