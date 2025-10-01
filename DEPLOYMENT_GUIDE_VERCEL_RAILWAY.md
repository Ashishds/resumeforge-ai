# 🚀 ResumeForge AI - Vercel + Railway Deployment Guide

Complete guide for deploying ResumeForge AI using **Vercel (Frontend) + Railway (Backend)** - the best free alternative to Render.

---

## 🎯 Why Vercel + Railway?

### **Vercel (Frontend)**
- ✅ **Free tier:** No sleep, generous limits
- ✅ **Perfect for React:** Optimized for Vite/React apps
- ✅ **Fast CDN:** Global edge network
- ✅ **Easy deployment:** Git-based auto-deploy
- ✅ **Custom domains:** Free SSL included

### **Railway (Backend)**
- ✅ **Free tier:** $5 credit monthly (enough for small apps)
- ✅ **No sleep:** Always-on services
- ✅ **Python support:** Native FastAPI support
- ✅ **Easy setup:** One-click deployment
- ✅ **Database support:** PostgreSQL included

---

## 📋 Prerequisites

Before deploying, ensure you have:
- ✅ OpenAI API Key ([Get one here](https://platform.openai.com/api-keys))
- ✅ GitHub account
- ✅ Vercel account ([Sign up free](https://vercel.com))
- ✅ Railway account ([Sign up free](https://railway.app))
- ✅ Git installed locally

---

## 🚀 Step 1: Deploy Backend to Railway

### **1.1 Prepare Repository**

```bash
# Ensure your code is committed
git add .
git commit -m "Prepare for Railway deployment"
git push origin main
```

### **1.2 Deploy to Railway**

1. **Go to Railway:**
   - Visit [https://railway.app](https://railway.app)
   - Sign in with GitHub

2. **Create New Project:**
   - Click **"New Project"**
   - Select **"Deploy from GitHub repo"**
   - Choose your repository

3. **Configure Backend Service:**
   - Railway will auto-detect Python
   - Set **Root Directory:** `backend`
   - Railway will use the `railway.json` config

4. **Add Environment Variables:**
   - Click on your service
   - Go to **"Variables"** tab
   - Add:
     ```
     OPENAI_API_KEY = sk-your-actual-key-here
     ENVIRONMENT = production
     ```

5. **Deploy:**
   - Railway will automatically build and deploy
   - Wait 2-3 minutes for deployment
   - Note your backend URL (e.g., `https://your-app.railway.app`)

---

## 🌐 Step 2: Deploy Frontend to Vercel

### **2.1 Deploy to Vercel**

1. **Go to Vercel:**
   - Visit [https://vercel.com](https://vercel.com)
   - Sign in with GitHub

2. **Import Project:**
   - Click **"New Project"**
   - Import your GitHub repository
   - Vercel will auto-detect it's a Vite project

3. **Configure Build Settings:**
   - **Framework Preset:** Vite
   - **Root Directory:** `frontend`
   - **Build Command:** `npm run build`
   - **Output Directory:** `dist`

4. **Add Environment Variables:**
   - Go to **"Environment Variables"**
   - Add:
     ```
     VITE_API_URL = https://your-backend.railway.app
     ```
   - Replace with your actual Railway backend URL

5. **Deploy:**
   - Click **"Deploy"**
   - Wait 2-3 minutes
   - Get your frontend URL (e.g., `https://your-app.vercel.app`)

---

## 🔧 Step 3: Update CORS Settings

### **3.1 Update Backend CORS**

In your Railway backend service, add environment variable:

```
ALLOWED_ORIGINS = https://your-frontend.vercel.app,http://localhost:3000
```

### **3.2 Update Frontend API URL**

In your Vercel project, update the environment variable:

```
VITE_API_URL = https://your-backend.railway.app
```

---

## ✅ Step 4: Test Deployment

### **4.1 Backend Health Check**

Visit: `https://your-backend.railway.app/api/health`

Should return:
```json
{
  "status": "healthy",
  "api_key_configured": true
}
```

### **4.2 Frontend Access**

Visit: `https://your-frontend.vercel.app`

Should load the ResumeForge AI application.

### **4.3 End-to-End Test**

1. Upload a test resume (PDF/DOCX)
2. Enter job title and description
3. Click "Optimize Resume"
4. Verify all tabs show results
5. Test PDF download functionality

---

## 🔄 Step 5: Continuous Deployment

### **5.1 Auto-Deploy Setup**

Both platforms support auto-deploy:

**Railway:**
- Automatically deploys on `main` branch push
- No additional setup needed

**Vercel:**
- Automatically deploys on `main` branch push
- Preview deployments for other branches

### **5.2 Git Workflow**

```bash
# Make changes
git add .
git commit -m "Feature: Add new functionality"
git push origin main

# Both platforms automatically deploy
```

---

## 💰 Cost Analysis

### **Free Tier Limits:**

**Vercel:**
- ✅ Unlimited deployments
- ✅ 100GB bandwidth/month
- ✅ No sleep time
- ✅ Custom domains included

**Railway:**
- ✅ $5 credit monthly
- ✅ No sleep time
- ✅ 1GB RAM, 1 vCPU
- ✅ 1GB disk space

### **Estimated Monthly Cost:**
- **Vercel:** $0 (free tier sufficient)
- **Railway:** $0 (free tier sufficient for small apps)
- **OpenAI:** $1-5 (depending on usage)
- **Total:** $1-5/month

---

## 🚀 Alternative: All-in-One Railway Deployment

If you prefer a single platform, Railway can host both:

### **Railway Full-Stack Setup:**

1. **Deploy Backend:**
   - Same as above
   - Root directory: `backend`

2. **Deploy Frontend:**
   - Create second service
   - Root directory: `frontend`
   - Build command: `npm run build`
   - Start command: `npx serve -s dist -l $PORT`

3. **Environment Variables:**
   ```
   VITE_API_URL = https://your-backend.railway.app
   ```

---

## 🛠️ Troubleshooting

### **Common Issues:**

**1. Build Fails - Railway Backend**
```
Error: Could not find a version that satisfies the requirement
```

**Solution:**
- Check `backend/requirements.txt`
- Ensure Python 3.10+ is used
- Try updating pip in `nixpacks.toml`

**2. Build Fails - Vercel Frontend**
```
Error: Module not found
```

**Solution:**
- Check `frontend/package.json`
- Ensure all dependencies are listed
- Try `npm install` locally first

**3. CORS Error**
```
Access-Control-Allow-Origin error
```

**Solution:**
- Update `ALLOWED_ORIGINS` in Railway
- Verify `VITE_API_URL` in Vercel
- Check both services are running

**4. API Connection Error**
```
Failed to fetch
```

**Solution:**
- Verify backend URL is correct
- Check Railway service is running
- Test backend health endpoint

---

## 📊 Monitoring & Maintenance

### **Railway Dashboard:**
- Real-time logs
- Resource usage
- Deployment history
- Environment variables

### **Vercel Dashboard:**
- Build logs
- Performance metrics
- Domain management
- Analytics

### **Key Metrics to Monitor:**
- API response time
- Error rates
- Memory usage
- Request volume

---

## 🔒 Security Best Practices

### **Environment Variables:**
- ✅ Never commit API keys to Git
- ✅ Use platform environment variables
- ✅ Rotate keys regularly
- ✅ Monitor API usage

### **CORS Configuration:**
- ✅ Only allow your frontend domain
- ✅ Remove localhost in production
- ✅ Use HTTPS only

### **Rate Limiting:**
Consider adding rate limiting for production:

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.post("/api/optimize-file")
@limiter.limit("5/minute")
async def optimize_resume_file(...):
    ...
```

---

## 🎯 Production Optimization

### **Railway Optimizations:**
- Use `nixpacks.toml` for faster builds
- Enable health checks
- Monitor resource usage

### **Vercel Optimizations:**
- Enable edge functions for API calls
- Use Vercel Analytics
- Optimize bundle size

### **Performance Tips:**
- Cache API responses
- Optimize images
- Use CDN for static assets
- Monitor OpenAI usage

---

## ✅ Deployment Checklist

Before going live:

- [ ] OpenAI API key configured in Railway
- [ ] Backend deployed successfully on Railway
- [ ] Frontend deployed successfully on Vercel
- [ ] CORS configured correctly
- [ ] Environment variables set
- [ ] Health check endpoint working
- [ ] End-to-end test passed
- [ ] PDF download working
- [ ] Custom domain (optional)
- [ ] SSL certificates active
- [ ] Monitoring setup

---

## 🎉 Success!

Your ResumeForge AI platform is now live on Vercel + Railway!

**URLs:**
- Frontend: `https://your-app.vercel.app`
- Backend: `https://your-app.railway.app`
- API Docs: `https://your-app.railway.app/api/docs`

**Next Steps:**
1. Share with users
2. Monitor performance
3. Collect feedback
4. Iterate and improve

---

## 📞 Support Resources

- **Vercel Docs:** [https://vercel.com/docs](https://vercel.com/docs)
- **Railway Docs:** [https://docs.railway.app](https://docs.railway.app)
- **FastAPI Docs:** [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com)
- **React Docs:** [https://react.dev](https://react.dev)

---

**Happy Deploying! 🚀**

*This setup gives you the best free deployment experience with no sleep time and excellent performance.*
