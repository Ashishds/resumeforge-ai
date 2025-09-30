# 🚀 Deployment Guide - ResumeForge AI

Complete guide for deploying ResumeForge AI to production on Render.com.

---

## 📋 Prerequisites

Before deploying, ensure you have:
- ✅ OpenAI API Key ([Get one here](https://platform.openai.com/api-keys))
- ✅ GitHub account
- ✅ Render.com account ([Sign up free](https://render.com))
- ✅ Git installed locally

---

## 🔧 Step 1: Prepare Your Code

### **1.1 Clone/Setup Repository**

```bash
# If starting fresh, create a new repo
git init
git add .
git commit -m "Initial commit: ResumeForge AI v2.0"

# Create GitHub repository and push
git remote add origin https://github.com/YOUR_USERNAME/resumeforge-ai.git
git branch -M main
git push -u origin main
```

### **1.2 Environment Variables Setup**

Create necessary environment files:

**Backend (.env):**
```env
OPENAI_API_KEY=sk-your-actual-api-key-here
PORT=8000
ENVIRONMENT=production
```

**Frontend (.env):**
```env
VITE_API_URL=https://resumeforge-api.onrender.com
```

> **Note:** Don't commit `.env` files to Git! They're already in `.gitignore`.

---

## 🌐 Step 2: Deploy to Render

### **Option A: Automated Deployment (Blueprint)**

This is the **recommended** method using the `render.yaml` file.

1. **Go to Render Dashboard:**
   - Visit [https://dashboard.render.com](https://dashboard.render.com)
   - Sign in or create account

2. **Create New Blueprint:**
   - Click **"New +"** → **"Blueprint"**
   - Connect your GitHub repository
   - Grant Render access to the repository

3. **Render Auto-Detection:**
   - Render will detect `render.yaml` automatically
   - Review the services:
     - `resumeforge-api` (Backend)
     - `resumeforge-frontend` (Frontend)

4. **Configure Environment Variables:**
   
   **For Backend Service:**
   - Click on `resumeforge-api` service
   - Go to **"Environment"** tab
   - Add:
     ```
     OPENAI_API_KEY = sk-your-actual-key
     ENVIRONMENT = production
     ```

   **For Frontend Service:**
   - Click on `resumeforge-frontend` service
   - Go to **"Environment"** tab
   - Add:
     ```
     VITE_API_URL = https://resumeforge-api.onrender.com
     ```
   - Replace with your actual backend URL

5. **Deploy:**
   - Click **"Apply"**
   - Render will build and deploy both services
   - Wait 5-10 minutes for initial deployment

---

### **Option B: Manual Deployment**

If you prefer manual control:

#### **Deploy Backend:**

1. **Create Web Service:**
   - Click **"New +"** → **"Web Service"**
   - Connect GitHub repository
   - Select repository

2. **Configure Backend:**
   ```
   Name: resumeforge-api
   Region: Oregon (US West)
   Branch: main
   Root Directory: backend
   Runtime: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn backend.api.main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
   Plan: Free
   ```

3. **Add Environment Variables:**
   ```
   OPENAI_API_KEY = sk-your-key
   PYTHON_VERSION = 3.10.0
   ENVIRONMENT = production
   ```

4. **Create Service**

#### **Deploy Frontend:**

1. **Create Web Service:**
   - Click **"New +"** → **"Web Service"**
   - Connect same repository

2. **Configure Frontend:**
   ```
   Name: resumeforge-frontend
   Region: Oregon (US West)
   Branch: main
   Root Directory: frontend
   Runtime: Node
   Build Command: npm install && npm run build
   Start Command: npm run preview -- --port $PORT --host 0.0.0.0
   Plan: Free
   ```

3. **Add Environment Variables:**
   ```
   NODE_VERSION = 18
   VITE_API_URL = https://resumeforge-api.onrender.com
   ```

4. **Create Service**

---

## 🔄 Step 3: Post-Deployment Configuration

### **3.1 Update CORS Settings**

After deployment, update backend CORS to allow frontend:

1. Go to backend service settings
2. Add environment variable:
   ```
   ALLOWED_ORIGINS = https://your-frontend.onrender.com,http://localhost:3000
   ```

### **3.2 Update Frontend API URL**

Ensure frontend points to correct backend:

1. Go to frontend service settings
2. Verify `VITE_API_URL` matches backend URL
3. Redeploy if needed

### **3.3 Test Deployment**

1. **Backend Health Check:**
   ```
   https://resumeforge-api.onrender.com/api/health
   ```
   Should return:
   ```json
   {
     "status": "healthy",
     "api_key_configured": true
   }
   ```

2. **Frontend Access:**
   ```
   https://resumeforge-frontend.onrender.com
   ```
   Should load the application

3. **End-to-End Test:**
   - Upload a test resume
   - Enter job details
   - Verify optimization works
   - Test PDF download

---

## ⚡ Step 4: Performance Optimization

### **4.1 Enable Caching**

Add to backend environment:
```env
CACHE_ENABLED=true
```

### **4.2 Optimize Build Time**

For faster deployments, use build caching:

**Backend:**
```bash
# Add to render_build.sh
pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt
```

**Frontend:**
```bash
# Use npm ci instead of npm install
npm ci
npm run build
```

### **4.3 Keep Services Warm**

Free tier Render services sleep after 15 minutes of inactivity:

**Option 1: UptimeRobot**
- Set up free monitoring at [uptimerobot.com](https://uptimerobot.com)
- Ping your services every 5-10 minutes

**Option 2: Upgrade to Starter Plan**
- $7/month for always-on service
- Better performance and no cold starts

---

## 🔒 Step 5: Security Best Practices

### **5.1 Secure API Keys**

- ✅ Never commit API keys to Git
- ✅ Use Render's environment variables
- ✅ Rotate keys regularly
- ✅ Monitor API usage on OpenAI dashboard

### **5.2 Rate Limiting**

Add to backend for production:

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.post("/api/optimize-file")
@limiter.limit("5/minute")
async def optimize_resume_file(...):
    ...
```

### **5.3 Input Validation**

Already implemented:
- File size limits
- Content length validation
- File type restrictions

---

## 📊 Step 6: Monitoring & Maintenance

### **6.1 Monitor Logs**

**Render Dashboard:**
- Click on service → **"Logs"** tab
- Real-time log streaming
- Error tracking

**Key Metrics to Watch:**
- API response time
- Error rates
- Memory usage
- Request volume

### **6.2 Set Up Alerts**

In Render dashboard:
- Enable email notifications
- Set up Slack/Discord webhooks
- Monitor deployment failures

### **6.3 Cost Monitoring**

**OpenAI Costs:**
- Set usage limits in OpenAI dashboard
- Monitor token consumption
- Estimated cost: $0.01-0.03 per resume

**Render Costs:**
- Free tier: $0/month
- Starter: $7/month per service
- Standard: $25/month per service

---

## 🚀 Step 7: Continuous Deployment

### **7.1 Enable Auto-Deploy**

In Render service settings:
- Enable **"Auto-Deploy"**
- Every push to `main` triggers deployment
- Automatic rollback on failures

### **7.2 Git Workflow**

```bash
# Make changes
git add .
git commit -m "Feature: Add new functionality"
git push origin main

# Render automatically deploys
```

### **7.3 Staging Environment**

Create separate services for testing:

```yaml
# render-staging.yaml
services:
  - type: web
    name: resumeforge-api-staging
    branch: develop
    # ... same config as production
```

---

## 🐛 Step 8: Troubleshooting

### **Common Deployment Issues**

**1. Build Fails - Backend**

```
Error: Could not find a version that satisfies the requirement crewai
```

**Solution:**
- Check `requirements.txt` syntax
- Ensure Python version matches (3.10+)
- Try: `pip install --upgrade pip`

**2. Build Fails - Frontend**

```
Error: Module not found
```

**Solution:**
- Delete `node_modules`
- Run `npm install` locally
- Commit `package-lock.json`
- Redeploy

**3. API Connection Error**

```
CORS policy blocked
```

**Solution:**
- Check `ALLOWED_ORIGINS` in backend
- Verify `VITE_API_URL` in frontend
- Ensure both services are running

**4. OpenAI API Error**

```
AuthenticationError: Incorrect API key
```

**Solution:**
- Verify `OPENAI_API_KEY` is set correctly
- Check API key hasn't expired
- Ensure billing is active on OpenAI account

**5. Service Sleeping (Free Tier)**

```
Service unavailable - waking up
```

**Solution:**
- First request takes 30-60 seconds
- Use UptimeRobot for keep-alive
- Upgrade to paid plan

---

## 🎯 Step 9: Custom Domain (Optional)

### **9.1 Add Custom Domain**

1. **Purchase Domain:**
   - Namecheap, GoDaddy, Google Domains, etc.

2. **Configure in Render:**
   - Service Settings → **"Custom Domains"**
   - Add domain: `app.yourdomain.com`

3. **Update DNS:**
   - Add CNAME record pointing to Render

4. **SSL Certificate:**
   - Render auto-provisions Let's Encrypt SSL
   - HTTPS enabled automatically

---

## 📈 Step 10: Scaling for Production

### **10.1 Database Integration**

For storing user data:

```python
# Add PostgreSQL
DATABASE_URL=postgresql://user:pass@host:5432/db

# Use with SQLAlchemy
from sqlalchemy import create_engine
engine = create_engine(os.getenv("DATABASE_URL"))
```

### **10.2 Redis Caching**

For faster responses:

```python
# Add Redis
REDIS_URL=redis://user:pass@host:6379

# Cache optimization results
import redis
cache = redis.from_url(os.getenv("REDIS_URL"))
```

### **10.3 Horizontal Scaling**

Increase workers in Procfile:

```
web: gunicorn backend.api.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker
```

---

## ✅ Deployment Checklist

Before going live:

- [ ] OpenAI API key configured
- [ ] Backend deployed successfully
- [ ] Frontend deployed successfully
- [ ] CORS configured correctly
- [ ] Environment variables set
- [ ] Health check endpoint working
- [ ] End-to-end test passed
- [ ] PDF download working
- [ ] Error handling tested
- [ ] Logs monitoring setup
- [ ] Cost monitoring active
- [ ] Auto-deploy enabled
- [ ] Custom domain (optional)
- [ ] SSL certificate active

---

## 🎉 Success!

Your ResumeForge AI platform is now live!

**Next Steps:**
1. Share with users
2. Monitor performance
3. Collect feedback
4. Iterate and improve

**Support:**
- Check logs for errors
- Monitor OpenAI usage
- Respond to user feedback

---

## 📞 Need Help?

- **Render Docs:** [https://render.com/docs](https://render.com/docs)
- **FastAPI Docs:** [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com)
- **React Docs:** [https://react.dev](https://react.dev)
- **OpenAI Support:** [https://help.openai.com](https://help.openai.com)

---

**Happy Deploying! 🚀**
