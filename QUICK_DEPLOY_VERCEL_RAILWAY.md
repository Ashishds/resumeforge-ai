# ⚡ Quick Deploy - Vercel + Railway

**Fastest way to deploy ResumeForge AI for free!**

---

## 🚀 One-Click Deployment

### **Step 1: Deploy Backend (Railway)**

1. Go to [railway.app](https://railway.app)
2. Click **"New Project"** → **"Deploy from GitHub repo"**
3. Select your repository
4. Railway auto-detects Python backend
5. Add environment variable:
   ```
   OPENAI_API_KEY = sk-your-key-here
   ```
6. Wait 2-3 minutes for deployment
7. **Copy your backend URL** (e.g., `https://your-app.railway.app`)

### **Step 2: Deploy Frontend (Vercel)**

1. Go to [vercel.com](https://vercel.com)
2. Click **"New Project"** → Import from GitHub
3. Select your repository
4. Vercel auto-detects Vite project
5. Add environment variable:
   ```
   VITE_API_URL = https://your-backend.railway.app
   ```
6. Click **"Deploy"**
7. Wait 2-3 minutes for deployment
8. **Copy your frontend URL** (e.g., `https://your-app.vercel.app`)

### **Step 3: Update CORS**

In Railway backend, add environment variable:
```
ALLOWED_ORIGINS = https://your-frontend.vercel.app
```

---

## ✅ Test Your Deployment

1. **Backend Health:** `https://your-backend.railway.app/api/health`
2. **Frontend:** `https://your-frontend.vercel.app`
3. **Upload a resume and test!**

---

## 💰 Cost: $0/month

- **Vercel:** Free (unlimited deployments)
- **Railway:** Free ($5 credit monthly)
- **OpenAI:** Pay-per-use (~$0.01-0.03 per resume)

---

## 🎯 Why This Setup?

- ✅ **No sleep time** (unlike Render free tier)
- ✅ **Fast deployment** (2-3 minutes)
- ✅ **Easy maintenance** (Git-based auto-deploy)
- ✅ **Professional URLs** (custom domains included)
- ✅ **Great performance** (global CDN)

---

**That's it! Your AI resume optimizer is live! 🚀**
