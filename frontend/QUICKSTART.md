# Quick Start Guide - LMARO Frontend

## Prerequisites
- Node.js 18+ installed
- Backend running on http://localhost:8000

## Installation (One-time)

```bash
# Navigate to frontend directory
cd D:\Git\virtual457-projects\llm-multi-agent-resume-optimizer\frontend

# Install dependencies
npm install
```

## Running the Application

### Terminal 1 - Backend
```bash
cd D:\Git\virtual457-projects\llm-multi-agent-resume-optimizer\backend
python main.py
```
Wait for: `INFO: Uvicorn running on http://0.0.0.0:8000`

### Terminal 2 - Frontend
```bash
cd D:\Git\virtual457-projects\llm-multi-agent-resume-optimizer\frontend
npm run dev
```
Wait for: `Ready on http://localhost:3000`

## Access the Application

Open browser: **http://localhost:3000**

## First Test

1. Click **"Paste Sample JD"** button
2. Click **"Generate Resume"** button
3. Wait 30-60 seconds
4. View your optimized resume with scores!

## Troubleshooting

### Frontend won't start
```bash
# Delete node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Can't connect to backend
- Check backend is running on port 8000
- Check URL in browser dev console for errors
- Try: `curl http://localhost:8000/api/health`

### CORS errors
Backend already has CORS enabled for localhost:3000

### Build errors
```bash
# Clear Next.js cache
rm -rf .next
npm run dev
```

## Development

### Edit UI Components
- `components/ResumeGenerator.tsx` - Input form
- `components/ResultsDisplay.tsx` - Results page

### Edit Styles
- `app/globals.css` - Global styles
- `tailwind.config.js` - Tailwind theme

### Edit API Integration
- `app/page.tsx` - Main API call logic

## Production Build

```bash
npm run build
npm start
```

## File Structure Quick Reference

```
frontend/
├── app/
│   ├── page.tsx          ← Main page logic
│   ├── layout.tsx        ← Root layout
│   └── globals.css       ← Global styles
├── components/
│   ├── ResumeGenerator.tsx   ← Input form
│   └── ResultsDisplay.tsx    ← Results view
└── package.json          ← Dependencies
```

## Common Commands

```bash
# Install dependencies
npm install

# Start dev server
npm run dev

# Build for production
npm run build

# Run production build
npm start

# Run linter
npm run lint
```

## URLs

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs

## Support

Check the full documentation in:
- `SETUP_COMPLETE.md` - Complete setup guide
- `README.md` - Project overview
- `../backend/api/docs/API_REFERENCE.md` - API documentation

---

**Happy coding! 🚀**
