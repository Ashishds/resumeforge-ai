# 🚀 Quick Start Guide

Get ResumeForge AI running in 5 minutes!

---

## 🎯 Prerequisites

Make sure you have:
- ✅ Python 3.10+ installed ([Download](https://python.org))
- ✅ Node.js 18+ installed ([Download](https://nodejs.org))
- ✅ OpenAI API Key ([Get one](https://platform.openai.com/api-keys))
- ✅ Git installed ([Download](https://git-scm.com))

---

## 📥 Step 1: Clone & Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd resume_parse_crewai
```

---

## 🔧 Step 2: Backend Setup

### **Windows:**
```powershell
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
copy .env.example .env

# Edit .env and add your OpenAI API key
notepad .env
```

### **macOS/Linux:**
```bash
# Navigate to backend
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env and add your OpenAI API key
nano .env
```

**Edit `.env` file:**
```env
OPENAI_API_KEY=sk-your-actual-api-key-here
PORT=8000
ENVIRONMENT=development
```

---

## 🎨 Step 3: Frontend Setup

```bash
# Navigate to frontend (open new terminal)
cd frontend

# Install dependencies
npm install
```

---

## ▶️ Step 4: Run the Application

### **Terminal 1: Start Backend**

**Windows:**
```powershell
cd backend
venv\Scripts\activate
uvicorn backend.api.main:app --reload --port 8000
```

**macOS/Linux:**
```bash
cd backend
source venv/bin/activate
uvicorn backend.api.main:app --reload --port 8000
```

✅ Backend running at: **http://localhost:8000**

✅ API Docs at: **http://localhost:8000/api/docs**

### **Terminal 2: Start Frontend**

```bash
cd frontend
npm run dev
```

✅ Frontend running at: **http://localhost:3000**

---

## 🎉 Step 5: Test the Application

1. **Open browser:** http://localhost:3000

2. **Upload a resume:**
   - Drag & drop or click to browse
   - Supported formats: PDF, DOCX, TXT

3. **Enter job details:**
   - Target job title (e.g., "Senior Software Engineer")
   - Paste job description

4. **Click "Optimize My Resume"**

5. **View results:**
   - See 4 stages of optimization
   - Download as PDF or DOCX
   - Review ATS evaluation

---

## 🔍 Verify Everything Works

### **Backend Health Check:**
Open browser: http://localhost:8000/api/health

Should see:
```json
{
  "status": "healthy",
  "api_key_configured": true,
  "services": {
    "document_extraction": "operational",
    "ai_pipeline": "operational",
    "pdf_generation": "operational"
  }
}
```

### **Frontend Check:**
Open: http://localhost:3000

Should see:
- Beautiful gradient header
- "ResumeForge AI" title
- File upload area
- Job title and description fields

---

## 🐛 Troubleshooting

### **Backend won't start:**
```bash
# Check Python version
python --version  # Should be 3.10+

# Reinstall dependencies
pip install -r requirements.txt

# Check .env file exists
cat .env  # or type .env on Windows
```

### **Frontend won't start:**
```bash
# Check Node version
node --version  # Should be 18+

# Clear cache and reinstall
rm -rf node_modules
npm install

# Try different port
npm run dev -- --port 3001
```

### **API Key Error:**
```
AuthenticationError: Incorrect API key
```
**Solution:**
- Verify `OPENAI_API_KEY` in `backend/.env`
- Ensure no extra spaces
- Check key is active on OpenAI dashboard

### **CORS Error:**
```
Access-Control-Allow-Origin
```
**Solution:**
- Ensure backend is running on port 8000
- Frontend should proxy to backend via Vite config

### **Port Already in Use:**

**Windows:**
```powershell
# Kill process on port 8000
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

**macOS/Linux:**
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9
```

---

## 📖 Next Steps

### **Explore Features:**
1. Try different resume formats (PDF, DOCX, TXT)
2. Test various job descriptions
3. Download results as PDF
4. Check API documentation: http://localhost:8000/api/docs

### **Customize:**
1. Modify AI agents in `backend/core/ai_specialists.py`
2. Adjust UI in `frontend/src/components/`
3. Change colors in `frontend/tailwind.config.js`

### **Deploy:**
1. Read `DEPLOYMENT_GUIDE.md`
2. Push to GitHub
3. Deploy to Render.com

---

## 📚 Documentation

- **Complete README:** `README.md`
- **Deployment Guide:** `DEPLOYMENT_GUIDE.md`
- **Command Reference:** `SETUP_COMMANDS.md`
- **Project Summary:** `PROJECT_SUMMARY.md`

---

## 🆘 Need Help?

### **Check Logs:**

**Backend:**
```bash
# Terminal will show detailed logs
# Look for errors in red
```

**Frontend:**
```bash
# Check browser console (F12)
# Look for network errors
```

### **Common Commands:**

```bash
# Stop servers: Ctrl + C

# Restart backend:
cd backend
source venv/bin/activate  # or venv\Scripts\activate
uvicorn backend.api.main:app --reload

# Restart frontend:
cd frontend
npm run dev

# Fresh install:
rm -rf venv node_modules
# Then repeat setup steps
```

---

## ✅ Quick Checklist

Before testing:
- [ ] Python 3.10+ installed
- [ ] Node.js 18+ installed
- [ ] OpenAI API key obtained
- [ ] Backend dependencies installed
- [ ] Frontend dependencies installed
- [ ] `.env` file created with API key
- [ ] Backend running on port 8000
- [ ] Frontend running on port 3000
- [ ] Health check successful
- [ ] No errors in terminal

---

## 🎯 Success!

If you can:
1. ✅ Access http://localhost:3000
2. ✅ See the upload form
3. ✅ Upload a test resume
4. ✅ Get optimized results
5. ✅ Download PDF

**Congratulations! Your setup is complete! 🎉**

---

## 📞 Support

- Check `README.md` for detailed documentation
- Review `DEPLOYMENT_GUIDE.md` for production setup
- See `SETUP_COMMANDS.md` for command reference

---

**Happy Resume Optimizing! 🚀**
