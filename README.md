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
resumeforge-ai/
├── backend/
│   ├── api/
│   │   ├── __init__.py
│   │   └── main.py              # FastAPI application & endpoints
│   ├── core/
│   │   ├── __init__.py
│   │   ├── ai_specialists.py    # AI agent definitions
│   │   ├── workflow_orchestrator.py  # Pipeline orchestration
│   │   └── workflow_tasks.py    # Task definitions
│   ├── services/
│   │   ├── __init__.py
│   │   └── document_processor.py # File parsing & PDF generation
│   ├── requirements.txt
│   ├── .env.example
│   └── Procfile                 # Render.com deployment config
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Header.jsx
│   │   │   ├── UploadSection.jsx
│   │   │   ├── ResultsSection.jsx
│   │   │   └── FeaturesSection.jsx
│   │   ├── services/
│   │   │   └── api.js           # API client
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
├── render.yaml                  # Render.com deployment config
└── README.md
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

## 🚀 Deployment on Render

### **Automated Deployment**

1. **Push to GitHub:**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin YOUR_REPO_URL
git push -u origin main
```

2. **Connect to Render:**
- Go to [Render Dashboard](https://dashboard.render.com)
- Click "New" → "Blueprint"
- Connect your GitHub repository
- Render will auto-detect `render.yaml`

3. **Configure Environment Variables:**
- Set `OPENAI_API_KEY` in backend service settings
- Update `VITE_API_URL` in frontend to your backend URL

4. **Deploy:**
- Render automatically deploys both services
- Backend: `https://YOUR-API.onrender.com`
- Frontend: `https://YOUR-FRONTEND.onrender.com`

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

### **Backend (.env)**
```env
OPENAI_API_KEY=sk-...
PORT=8000
ENVIRONMENT=production
ALLOWED_ORIGINS=https://your-frontend.onrender.com
```

### **Frontend**
```env
VITE_API_URL=https://your-backend.onrender.com
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
**Solution:** Update `ALLOWED_ORIGINS` in backend `.env`

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
1. Clone this repository
2. Follow the Quick Start guide
3. Upload your resume
4. Get your ATS-optimized resume in seconds!

**Live Demo:** [Coming Soon]

**Documentation:** [API Docs](http://localhost:8000/api/docs)

---

Built with ❤️ using FastAPI, React, and CrewAI