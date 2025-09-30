# 🚀 COMMANDS TO RUN - ResumeForge AI

**Your complete command guide to run the project from scratch.**

---

## ⚡ QUICK START (Copy & Paste)

### **Step 1: Backend Setup**

#### **Windows (PowerShell):**
```powershell
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file (you'll need to edit this)
copy .env.example .env

# Edit .env and add your OpenAI API key
notepad .env
```

#### **macOS/Linux:**
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

**⚠️ IMPORTANT: Edit `.env` file and add your OpenAI API key:**
```env
OPENAI_API_KEY=sk-your-actual-openai-api-key-here
PORT=8000
ENVIRONMENT=development
```

---

### **Step 2: Frontend Setup**

```bash
# Open NEW terminal/command prompt
cd frontend

# Install dependencies
npm install

# This will take 2-3 minutes
```

---

### **Step 3: Run Both Services**

#### **Terminal 1 - Backend:**

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

✅ **Backend will start at:** http://localhost:8000
✅ **API Docs at:** http://localhost:8000/api/docs

#### **Terminal 2 - Frontend:**

```bash
cd frontend
npm run dev
```

✅ **Frontend will start at:** http://localhost:3000

---

## 🎯 Access the Application

1. **Open your browser**
2. **Go to:** http://localhost:3000
3. **You should see:** Beautiful ResumeForge AI interface

---

## 🧪 Test the Application

### **Test 1: Health Check**
```bash
# Open browser or use curl
curl http://localhost:8000/api/health
```

**Expected Response:**
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

### **Test 2: Upload Resume**
1. Go to http://localhost:3000
2. Drag & drop a resume file (PDF, DOCX, or TXT)
3. Enter job title: "Software Engineer"
4. Paste a job description
5. Click "Optimize My Resume"
6. Wait 30-60 seconds
7. See results in 4 tabs
8. Download as PDF or DOCX

---

## 🔄 Daily Development Commands

### **Starting Work (Every Day):**

**Terminal 1 (Backend):**
```bash
cd backend
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows
uvicorn backend.api.main:app --reload --port 8000
```

**Terminal 2 (Frontend):**
```bash
cd frontend
npm run dev
```

### **Stopping Services:**
```
Press Ctrl + C in both terminals
```

---

## 🛠️ Troubleshooting Commands

### **Backend Issues:**

**Check Python version:**
```bash
python --version
# Should be 3.10 or higher
```

**Check installed packages:**
```bash
pip list
```

**Reinstall dependencies:**
```bash
pip install -r requirements.txt --force-reinstall
```

**Check if backend is running:**
```bash
curl http://localhost:8000/
```

### **Frontend Issues:**

**Check Node version:**
```bash
node --version
# Should be 18 or higher
```

**Clear cache and reinstall:**
```bash
rm -rf node_modules
rm package-lock.json
npm install
```

**Run on different port:**
```bash
npm run dev -- --port 3001
```

### **Port Conflicts:**

**Kill process on port 8000:**
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID_NUMBER> /F

# macOS/Linux
lsof -ti:8000 | xargs kill -9
```

**Kill process on port 3000:**
```bash
# Windows
netstat -ano | findstr :3000
taskkill /PID <PID_NUMBER> /F

# macOS/Linux
lsof -ti:3000 | xargs kill -9
```

---

## 📦 Build for Production

### **Backend:**
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt
gunicorn backend.api.main:app \
  --workers 2 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000
```

### **Frontend:**
```bash
cd frontend
npm install
npm run build
npm run preview -- --port 3000 --host 0.0.0.0
```

---

## 🌐 Deploy to Render

### **Quick Deploy:**

```bash
# 1. Initialize Git (if not already)
git init

# 2. Add all files
git add .

# 3. Commit
git commit -m "Initial commit: ResumeForge AI v2.0"

# 4. Create GitHub repo and push
git remote add origin https://github.com/YOUR_USERNAME/resumeforge-ai.git
git branch -M main
git push -u origin main

# 5. Go to Render.com
# - Click "New" → "Blueprint"
# - Connect your GitHub repo
# - Render will auto-detect render.yaml
# - Add OPENAI_API_KEY in environment variables
# - Click "Apply"
```

See `DEPLOYMENT_GUIDE.md` for detailed instructions.

---

## 📝 Environment Variables

### **Backend (.env):**
```env
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx
PORT=8000
ENVIRONMENT=development
ALLOWED_ORIGINS=http://localhost:3000
```

### **Frontend (.env) - Optional:**
```env
VITE_API_URL=http://localhost:8000
```

---

## 🔍 Verification Checklist

Run these commands to verify everything is set up correctly:

```bash
# 1. Check Python version
python --version

# 2. Check Node version
node --version

# 3. Check if backend dependencies are installed
cd backend
pip list | grep crewai
pip list | grep fastapi

# 4. Check if frontend dependencies are installed
cd frontend
npm list react
npm list vite

# 5. Check if .env file exists
cd backend
cat .env  # or type .env on Windows

# 6. Test backend health
curl http://localhost:8000/api/health

# 7. Test frontend
curl http://localhost:3000
```

---

## 📚 Additional Resources

- **Full Documentation:** `README.md`
- **Deployment Guide:** `DEPLOYMENT_GUIDE.md`
- **Quick Start:** `START.md`
- **All Changes:** `CHANGES.md`
- **Project Summary:** `PROJECT_SUMMARY.md`
- **Setup Commands:** `SETUP_COMMANDS.md`

---

## 🎯 Success Indicators

You're ready when:
- ✅ Backend runs without errors on http://localhost:8000
- ✅ Frontend runs without errors on http://localhost:3000
- ✅ Health check returns `"status": "healthy"`
- ✅ You can upload a resume and get results
- ✅ PDF download works
- ✅ No errors in browser console (F12)

---

## 🆘 Common Errors & Solutions

### **Error: "Module not found: crewai"**
```bash
cd backend
source venv/bin/activate
pip install -r requirements.txt
```

### **Error: "AuthenticationError: Incorrect API key"**
```bash
# Check your .env file
cd backend
cat .env

# Make sure OPENAI_API_KEY is set correctly
# No spaces, quotes, or extra characters
```

### **Error: "Port 8000 already in use"**
```bash
# Kill the process
lsof -ti:8000 | xargs kill -9  # macOS/Linux
netstat -ano | findstr :8000   # Windows (then taskkill)
```

### **Error: "CORS policy blocked"**
```bash
# Make sure backend is running on port 8000
# Frontend will proxy requests automatically via vite.config.js
```

### **Error: "npm ERR! code ENOENT"**
```bash
# Delete and reinstall
rm -rf node_modules package-lock.json
npm install
```

---

## 🎉 You're All Set!

If you've followed these commands and everything is running:

1. ✅ Backend: http://localhost:8000 ✓
2. ✅ Frontend: http://localhost:3000 ✓
3. ✅ Health check passing ✓
4. ✅ Can upload and process resumes ✓

**Congratulations! You're ready to optimize resumes with AI! 🚀**

---

## 📞 Need More Help?

- Read `START.md` for detailed troubleshooting
- Check `DEPLOYMENT_GUIDE.md` for production setup
- Review `README.md` for complete documentation
- See `SETUP_COMMANDS.md` for more commands

---

**Happy Coding! 🎯**
