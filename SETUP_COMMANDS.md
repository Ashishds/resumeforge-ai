# 📋 Complete Setup Commands

Quick reference guide for all setup and run commands.

---

## 🖥️ Local Development

### **Full Stack Setup (First Time)**

```bash
# 1. Clone repository
git clone https://github.com/YOUR_USERNAME/resumeforge-ai.git
cd resumeforge-ai

# 2. Backend Setup
cd backend
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
copy .env.example .env  # Windows
cp .env.example .env    # macOS/Linux
# Edit .env and add your OPENAI_API_KEY

# 3. Frontend Setup
cd ../frontend
npm install

# Configure environment
copy .env.example .env  # Windows
cp .env.example .env    # macOS/Linux
# Edit .env if needed
```

---

## 🚀 Running the Application

### **Terminal 1: Backend**

```bash
cd backend

# Activate venv (if not already)
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Run server
uvicorn backend.api.main:app --reload --port 8000
```

Backend runs at: **http://localhost:8000**

API Docs at: **http://localhost:8000/api/docs**

### **Terminal 2: Frontend**

```bash
cd frontend

# Run dev server
npm run dev
```

Frontend runs at: **http://localhost:3000**

---

## 🔄 Quick Start (Subsequent Runs)

### **Windows (PowerShell)**

```powershell
# Terminal 1: Backend
cd backend
venv\Scripts\activate
uvicorn backend.api.main:app --reload --port 8000

# Terminal 2: Frontend
cd frontend
npm run dev
```

### **macOS/Linux**

```bash
# Terminal 1: Backend
cd backend
source venv/bin/activate
uvicorn backend.api.main:app --reload --port 8000

# Terminal 2: Frontend
cd frontend
npm run dev
```

---

## 🧪 Testing Commands

### **Backend Testing**

```bash
cd backend
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install test dependencies
pip install pytest pytest-cov httpx

# Run tests
pytest

# With coverage
pytest --cov=backend tests/
```

### **Frontend Testing**

```bash
cd frontend

# Run tests
npm test

# Run with coverage
npm test -- --coverage
```

---

## 🏗️ Build Commands

### **Frontend Production Build**

```bash
cd frontend

# Build for production
npm run build

# Preview production build
npm run preview
```

### **Backend Production**

```bash
cd backend

# Install production dependencies
pip install -r requirements.txt

# Run with gunicorn
gunicorn backend.api.main:app \
  --workers 2 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000
```

---

## 🧹 Cleanup Commands

### **Clear Cache and Dependencies**

```bash
# Backend
cd backend
rm -rf __pycache__
rm -rf venv
rm -rf *.pyc

# Frontend
cd frontend
rm -rf node_modules
rm -rf dist
rm -rf .vite
```

### **Fresh Install**

```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Frontend
cd frontend
npm install
```

---

## 📦 Package Management

### **Backend: Add New Package**

```bash
cd backend
source venv/bin/activate

# Install package
pip install package-name

# Update requirements.txt
pip freeze > requirements.txt
```

### **Frontend: Add New Package**

```bash
cd frontend

# Install package
npm install package-name

# Install dev dependency
npm install -D package-name
```

---

## 🔍 Debugging Commands

### **Backend Debugging**

```bash
# Run with detailed logs
uvicorn backend.api.main:app --reload --log-level debug

# Check Python version
python --version

# List installed packages
pip list

# Check specific package
pip show crewai
```

### **Frontend Debugging**

```bash
# Clear cache and rebuild
npm run build -- --force

# Check Node version
node --version

# List dependencies
npm list

# Check for outdated packages
npm outdated
```

---

## 🌐 Production Deployment

### **Render Deployment**

```bash
# 1. Commit changes
git add .
git commit -m "Your commit message"
git push origin main

# 2. Render auto-deploys
# Monitor at: https://dashboard.render.com
```

### **Manual Production Build**

```bash
# Backend
cd backend
pip install -r requirements.txt
gunicorn backend.api.main:app \
  --workers 2 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:$PORT

# Frontend
cd frontend
npm install
npm run build
npm run preview -- --port $PORT --host 0.0.0.0
```

---

## 🔧 Environment Setup

### **Create .env Files**

**Backend (.env):**
```bash
cd backend
cat > .env << EOF
OPENAI_API_KEY=sk-your-key-here
PORT=8000
ENVIRONMENT=development
ALLOWED_ORIGINS=http://localhost:3000
EOF
```

**Frontend (.env):**
```bash
cd frontend
cat > .env << EOF
VITE_API_URL=http://localhost:8000
EOF
```

---

## 📊 Monitoring Commands

### **Check Application Health**

```bash
# Backend health
curl http://localhost:8000/api/health

# Test optimization endpoint
curl -X POST http://localhost:8000/api/optimize \
  -H "Content-Type: application/json" \
  -d '{
    "resume_text": "Test resume",
    "job_title": "Software Engineer",
    "job_description": "Looking for Python developer"
  }'
```

### **Check Logs**

```bash
# Backend logs (if running with systemd)
journalctl -u resumeforge-api -f

# Frontend logs
npm run dev -- --debug
```

---

## 🛠️ Utility Commands

### **Format Code**

```bash
# Backend (Black formatter)
pip install black
black backend/

# Frontend (Prettier)
npm install -D prettier
npx prettier --write src/
```

### **Lint Code**

```bash
# Backend
pip install flake8
flake8 backend/

# Frontend
npm run lint
```

### **Type Checking**

```bash
# Backend (MyPy)
pip install mypy
mypy backend/

# Frontend (TypeScript - if using)
npm run type-check
```

---

## 📱 Quick Reference

### **Common Issues**

**Port already in use:**
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:8000 | xargs kill -9
```

**Module not found:**
```bash
# Backend
pip install -r requirements.txt

# Frontend
rm -rf node_modules
npm install
```

**CORS errors:**
```bash
# Check ALLOWED_ORIGINS in backend/.env
# Should include: http://localhost:3000
```

---

## ✅ Daily Development Workflow

```bash
# Morning: Start development
cd resumeforge-ai

# Terminal 1: Backend
cd backend && source venv/bin/activate && uvicorn backend.api.main:app --reload

# Terminal 2: Frontend
cd frontend && npm run dev

# Make changes, git commit, push

# Evening: Stop servers
# Ctrl+C in both terminals
```

---

**Happy Coding! 🚀**
