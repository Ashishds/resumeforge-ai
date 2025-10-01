# 🚀 Command-Based Deployment Guide - Vercel + Railway

**Step-by-step commands to deploy ResumeForge AI for FREE**

---

## 📋 Prerequisites Checklist

Before we start, make sure you have:

- [ ] **OpenAI API Key** ([Get one here](https://platform.openai.com/api-keys))
- [ ] **GitHub account** (free)
- [ ] **Vercel account** ([Sign up free](https://vercel.com))
- [ ] **Railway account** ([Sign up free](https://railway.app))
- [ ] **Git installed** on your computer

---

## 🎯 Step 1: Prepare Your Repository

### **1.1 Check Current Status**

```bash
# Navigate to your project directory
cd F:\resume_parse_crewai

# Check git status
git status
```

**Expected output:** Should show "working tree clean" or list any uncommitted changes.

### **1.2 Commit All Changes**

```bash
# Add all files to git
git add .

# Commit changes
git commit -m "Prepare for Vercel + Railway deployment"

# Push to GitHub
git push origin main
```

**✅ Check:** Go to GitHub.com and verify your code is updated.

---

## 🚀 Step 2: Deploy Backend to Railway

### **2.1 Open Railway Website**

```bash
# Open Railway in your browser
start https://railway.app
```

**Alternative:** Copy and paste `https://railway.app` in your browser.

### **2.2 Sign In to Railway**

1. Click **"Sign in"** (top right)
2. Choose **"Sign in with GitHub"**
3. Authorize Railway to access your GitHub

### **2.3 Create New Project**

1. Click **"New Project"** (big blue button)
2. Select **"Deploy from GitHub repo"**
3. Find **"resume_parse_crewai"** in the list
4. Click on it to select

### **2.4 Configure Backend Service**

Railway should auto-detect Python. If not:

1. Click **"Settings"** on your service
2. Set **Root Directory:** `backend`
3. Railway will use the `railway.json` file automatically

### **2.5 Add Environment Variables**

1. Click on your service name
2. Go to **"Variables"** tab
3. Click **"New Variable"**
4. Add these variables one by one:

```
OPENAI_API_KEY = sk-your-actual-openai-key-here
ENVIRONMENT = production
```

**⚠️ Important:** Replace `sk-your-actual-openai-key-here` with your real OpenAI API key!

### **2.6 Wait for Deployment**

1. Railway will automatically start building
2. Wait 2-3 minutes for deployment
3. You'll see logs in real-time
4. When done, you'll get a URL like: `https://your-app-name.railway.app`

**✅ Save this URL!** You'll need it for the frontend.

### **2.7 Test Backend**

```bash
# Test your backend health (replace with your actual URL)
curl https://your-app-name.railway.app/api/health
```

**Expected output:**
```json
{
  "status": "healthy",
  "api_key_configured": true
}
```

---

## 🌐 Step 3: Deploy Frontend to Vercel

### **3.1 Open Vercel Website**

```bash
# Open Vercel in your browser
start https://vercel.com
```

**Alternative:** Copy and paste `https://vercel.com` in your browser.

### **3.2 Sign In to Vercel**

1. Click **"Sign up"** or **"Login"**
2. Choose **"Continue with GitHub"**
3. Authorize Vercel to access your GitHub

### **3.3 Import Your Project**

1. Click **"New Project"** (big button)
2. You'll see your GitHub repositories
3. Find **"resume_parse_crewai"** and click **"Import"**

### **3.4 Configure Frontend**

Vercel should auto-detect it's a Vite project. If not:

1. **Framework Preset:** Vite
2. **Root Directory:** `frontend`
3. **Build Command:** `npm run build`
4. **Output Directory:** `dist`

### **3.5 Add Environment Variables**

1. Scroll down to **"Environment Variables"**
2. Click **"Add"**
3. Add this variable:

```
VITE_API_URL = https://your-backend-url.railway.app
```

**⚠️ Important:** Replace `https://your-backend-url.railway.app` with your actual Railway backend URL from Step 2!

### **3.6 Deploy Frontend**

1. Click **"Deploy"** (big blue button)
2. Wait 2-3 minutes for deployment
3. You'll see build logs in real-time
4. When done, you'll get a URL like: `https://your-app-name.vercel.app`

**✅ Save this URL!** This is your live application.

---

## 🔧 Step 4: Connect Frontend and Backend

### **4.1 Update CORS in Railway**

1. Go back to your Railway dashboard
2. Click on your backend service
3. Go to **"Variables"** tab
4. Click **"New Variable"**
5. Add:

```
ALLOWED_ORIGINS = https://your-frontend-url.vercel.app
```

**⚠️ Important:** Replace `https://your-frontend-url.vercel.app` with your actual Vercel frontend URL from Step 3!

### **4.2 Wait for Redeploy**

1. Railway will automatically redeploy when you add the variable
2. Wait 1-2 minutes for the update

---

## ✅ Step 5: Test Your Deployment

### **5.1 Test Backend Health**

```bash
# Test your backend (replace with your actual URL)
curl https://your-backend-url.railway.app/api/health
```

**Expected output:**
```json
{
  "status": "healthy",
  "api_key_configured": true
}
```

### **5.2 Test Frontend**

1. Open your browser
2. Go to: `https://your-frontend-url.vercel.app`
3. You should see the ResumeForge AI application
4. The page should load without errors

### **5.3 Test Full Application**

1. On your frontend page, try uploading a resume (PDF or DOCX)
2. Enter a job title and description
3. Click **"Optimize Resume"**
4. Wait for the AI to process (30-60 seconds)
5. You should see results in different tabs
6. Try downloading the PDF

**✅ If everything works, your deployment is successful!**

---

## 🎉 Step 6: You're Live!

### **Your Live URLs:**

- **🌐 Frontend (Your App):** `https://your-frontend-url.vercel.app`
- **🔧 Backend API:** `https://your-backend-url.railway.app`
- **📚 API Documentation:** `https://your-backend-url.railway.app/api/docs`

### **Share Your App:**

You can now share your ResumeForge AI with anyone! They can:
- Upload their resume
- Get AI-optimized versions
- Download professional PDFs
- Get career guidance

---

## 🔄 Step 7: Auto-Deployment Setup

### **Both platforms support auto-deployment:**

**Railway:**
- ✅ Automatically deploys when you push to GitHub
- ✅ No additional setup needed

**Vercel:**
- ✅ Automatically deploys when you push to GitHub
- ✅ Preview deployments for other branches

### **To update your app:**

```bash
# Make changes to your code
git add .
git commit -m "Update: Add new feature"
git push origin main

# Both platforms automatically deploy the updates!
```

---

## 🛠️ Troubleshooting Commands

### **Check Backend Status**

```bash
# Test backend health
curl https://your-backend-url.railway.app/api/health

# Test backend root
curl https://your-backend-url.railway.app/
```

### **Check Frontend Status**

```bash
# Test frontend (open in browser)
start https://your-frontend-url.vercel.app
```

### **Check Git Status**

```bash
# Check if everything is committed
git status

# Check recent commits
git log --oneline -5
```

### **Check Environment Variables**

**Railway:**
1. Go to Railway dashboard
2. Click on your service
3. Go to "Variables" tab
4. Verify all variables are set

**Vercel:**
1. Go to Vercel dashboard
2. Click on your project
3. Go to "Settings" → "Environment Variables"
4. Verify all variables are set

---

## 🚨 Common Issues & Solutions

### **Problem: Backend not working**

**Check:**
```bash
curl https://your-backend-url.railway.app/api/health
```

**If error:**
1. Check Railway logs
2. Verify OpenAI API key is correct
3. Check environment variables

### **Problem: Frontend not connecting to backend**

**Check:**
1. Is `VITE_API_URL` set correctly in Vercel?
2. Is `ALLOWED_ORIGINS` set correctly in Railway?
3. Are both services running?

**Solution:**
1. Verify environment variables
2. Check both service URLs
3. Redeploy if needed

### **Problem: CORS error**

**Error message:** `Access-Control-Allow-Origin`

**Solution:**
1. Go to Railway backend variables
2. Update `ALLOWED_ORIGINS` with your exact Vercel URL
3. Redeploy backend

### **Problem: OpenAI API error**

**Error message:** `AuthenticationError: Incorrect API key`

**Solution:**
1. Check your OpenAI API key is correct
2. Verify you have credits in your OpenAI account
3. Test the key at [platform.openai.com](https://platform.openai.com)

---

## 💰 Cost Breakdown

### **Monthly Costs:**

- **✅ Vercel:** $0 (free tier)
- **✅ Railway:** $0 (free tier - $5 credit monthly)
- **💰 OpenAI:** $1-5 (depending on usage)
- **📊 Total:** $1-5/month

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

---

## ✅ Success Checklist

Before you're done, verify:

- [ ] ✅ Backend deployed on Railway
- [ ] ✅ Frontend deployed on Vercel
- [ ] ✅ Environment variables set correctly
- [ ] ✅ CORS configured
- [ ] ✅ Backend health check working
- [ ] ✅ Frontend loading without errors
- [ ] ✅ Full application test passed
- [ ] ✅ PDF download working
- [ ] ✅ Auto-deployment enabled

---

## 🚀 Next Steps

### **Optional Enhancements:**

1. **Custom Domain:**
   - Add your own domain (e.g., `resumeforge.yourdomain.com`)
   - Both platforms support custom domains

2. **Monitoring:**
   - Set up monitoring with UptimeRobot (free)
   - Monitor your services 24/7

3. **Analytics:**
   - Add Vercel Analytics (free)
   - Track your app usage

### **Share Your Success:**

1. **Test with friends:** Share your app URL
2. **Get feedback:** Ask users to try it
3. **Iterate:** Make improvements based on feedback
4. **Scale:** Monitor usage and upgrade if needed

---

## 📞 Need Help?

### **If you get stuck:**

1. **Check the logs** in both Railway and Vercel dashboards
2. **Verify environment variables** are set correctly
3. **Test each step** individually
4. **Ask for help** in the comments

### **Useful Resources:**

- **Railway Docs:** [https://docs.railway.app](https://docs.railway.app)
- **Vercel Docs:** [https://vercel.com/docs](https://vercel.com/docs)
- **OpenAI API:** [https://platform.openai.com](https://platform.openai.com)

---

## 🎉 Congratulations!

**You've successfully deployed ResumeForge AI for FREE!**

Your AI-powered resume optimizer is now live and ready to help people create better resumes. 

**Share your success and help others optimize their careers! 🚀**

---

*This command-based guide ensures you can follow each step with clear commands and expected outputs.*
