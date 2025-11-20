# 🎨 LMARO Frontend

Modern Next.js 15 frontend with Google Material Design for intuitive resume generation.

<p align="center">
  <a href="../README.md">← Back to Main README</a>
</p>

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Pages & Routes](#pages--routes)
- [Components](#components)
- [Installation](#installation)
- [Development](#development)
- [Design System](#design-system)
- [Deployment](#deployment)

## 🎯 Overview

The frontend provides a beautiful, intuitive interface for resume generation with real-time progress tracking. Built with Next.js 15 App Router and styled with Google's Material Design principles.

### Key Highlights

- **Google Material Design** - Professional UI following Google's design guidelines
- **Multi-Page Flow** - Smooth navigation through generation process
- **Real-Time Updates** - SSE-powered progress modal with live stage indicators
- **Responsive Design** - Works seamlessly on desktop and mobile
- **Material Icons** - Consistent iconography throughout
- **Mesh Backgrounds** - Animated floating gradient orbs
- **TypeScript** - Full type safety

## ✨ Features

### Visual Design
- ✅ **Google Sans & Product Sans Fonts** - Authentic Google typography
- ✅ **Material Icons** - Official Google icons via CDN
- ✅ **4-Color Palette** - Blue (#4285f4), Red (#ea4335), Yellow (#fbbc04), Green (#34a853)
- ✅ **Mesh Gradient Backgrounds** - Animated floating orbs
- ✅ **Glass-morphism Effects** - Subtle backdrop blur
- ✅ **Smooth Animations** - Cubic-bezier transitions
- ✅ **Loading Screen** - Google-style bouncing dots

### User Experience
- ✅ **Single-Screen Pages** - No scrolling needed (fits viewport)
- ✅ **Progress Modal** - Real-time stage tracking with animations
- ✅ **Score Visualization** - Circular progress indicators
- ✅ **Resume Preview** - Full-page formatted view
- ✅ **Print Support** - One-click resume printing
- ✅ **Download Options** - JSON and DOCX export
- ✅ **Back Navigation** - Smooth page transitions

### Technical
- ✅ **Server-Sent Events** - Real-time backend updates
- ✅ **Session Storage** - Data persistence between pages
- ✅ **Type Safety** - Full TypeScript coverage
- ✅ **Hot Reload** - Instant development feedback
- ✅ **Optimized Build** - Fast production deployment

## 🗺️ Pages & Routes

### 1. Landing Page (`/`)

**Purpose:** Hero page with call-to-action

**Features:**
- Full-screen hero with animated gradient background
- LMARO title with Google color gradient
- Feature stat cards (90+, 100%, 3x, ∞)
- "Get Started" button with pulse animation
- Feature chips (Factuality Checked, 90+ Score, etc.)

**Flow:** User clicks "Get Started" → Navigates to `/generate`

---

### 2. Generate Page (`/generate`)

**Purpose:** Form to input job details

**Features:**
- Company name input
- Role input
- Job description textarea (with character count)
- "Paste Sample JD" quick-fill button
- Form validation
- "Generate Resume" button with Material Icons

**Flow:** User fills form → Clicks generate → Modal appears → Auto-navigate to `/results` on completion

---

### 3. Results Page (`/results`)

**Purpose:** Display scores and download options

**Features:**
- Success message with celebration icon
- Two score cards:
  - Evaluation Score (blue, analytics icon)
  - Factuality Score (green, verified icon)
- Action buttons:
  - "Preview Resume" (primary)
  - "Generate New Resume" (secondary)
- Download options:
  - JSON download (immediate)
  - DOCX download (placeholder)

**Flow:** 
- Data loaded from `sessionStorage`
- Click "Preview Resume" → Navigate to `/preview`
- Click "Generate New" → Navigate to `/generate`

---

### 4. Preview Page (`/preview`)

**Purpose:** Full resume view with print support

**Features:**
- Resume displayed in professional format
- Back to Results button (top-left)
- Print button (top-right)
- Sections: Header, Summary, Skills, Experience, Projects
- Print-optimized CSS (hides header on print)

**Flow:**
- Data loaded from `sessionStorage`
- Click back → Return to `/results`
- Click print → Browser print dialog

---

### Progress Modal (Overlay)

**Purpose:** Real-time generation tracking

**Appears On:** Generate page during processing

**Features:**
- Animated stage icon (Material Icons)
- Stage-specific colors
- Progress bar (0-100%)
- Timeline with 5 stages:
  1. Setup (⚙️)
  2. Generating Resume (✏️)
  3. Evaluating Quality (📊)
  4. Checking Factuality (✅)
  5. Creating Documents (📝)
- Animated dots for active stage
- Info box with tip

**Stages:**
- Active: Highlighted with color + animated dots
- Completed: Green checkmark + "Done"
- Upcoming: Gray with reduced opacity

## 🧩 Components

### `GenerationModal.tsx`

Real-time progress tracking overlay.

**Props:**
```typescript
{
  stage: string         // Current stage name
  message: string       // Status message
  progress: number      // 0-100
  isOpen: boolean      // Show/hide modal
}
```

**Features:**
- Stage-specific Material Icons
- Color-coded progress
- Animated timeline
- Shimmer effect on progress bar

---

### `ResumeGenerator.tsx`

Form component for job input.

**Props:**
```typescript
{
  onGenerate: (data) => void  // Submit handler
  isGenerating: boolean       // Loading state
}
```

**Features:**
- Company and role inputs
- Job description textarea
- Sample JD quick-fill
- Character counter
- Form validation
- Feature cards (3 cards with icons)

---

### Header Component

**Used On:** Generate, Results, Preview pages

**Features:**
- LMARO logo (clickable → home)
- Gradient text styling
- Back button (on relevant pages)
- Action buttons (on preview)

---

### Score Card Component

**Used On:** Results page

**Features:**
- Title and subtitle
- Large score display (X/100)
- Material Icon in colored circle
- Hover effects

## 🚀 Installation

### Prerequisites

- Node.js 18+
- npm or yarn

### Setup

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

**Runs on:** http://localhost:3000

### Dependencies

**Core:**
```json
{
  "react": "^19.0.0",
  "react-dom": "^19.0.0",
  "next": "^15.0.0"
}
```

**Development:**
```json
{
  "typescript": "^5",
  "tailwindcss": "^3.4.0",
  "@types/react": "^19",
  "@types/node": "^20"
}
```

## 💻 Development

### Project Structure

```
frontend/
├── app/
│   ├── page.tsx              # Landing page
│   ├── layout.tsx            # Root layout (Material Icons)
│   ├── globals.css           # Google Material Design styles
│   ├── generate/
│   │   └── page.tsx         # Form page
│   ├── results/
│   │   └── page.tsx         # Results page
│   └── preview/
│       └── page.tsx         # Resume preview
├── components/
│   ├── GenerationModal.tsx   # Progress modal
│   └── ResumeGenerator.tsx   # Form component
├── public/                   # Static assets
├── package.json
├── tsconfig.json
├── tailwind.config.js
└── next.config.js
```

### Running Locally

```bash
# Development (hot reload)
npm run dev

# Production build
npm run build
npm start

# Linting
npm run lint
```

### Environment Variables

Currently hardcoded:
```typescript
const API_URL = 'http://localhost:8000'
```

For production, use Next.js environment variables:
```bash
# .env.local
NEXT_PUBLIC_API_URL=https://your-api.com
```

Then in code:
```typescript
const API_URL = process.env.NEXT_PUBLIC_API_URL
```

## 🎨 Design System

### Colors

**Google Palette:**
```css
--google-blue: #4285f4
--google-red: #ea4335
--google-yellow: #fbbc04
--google-green: #34a853
```

**Neutrals:**
```css
--text-primary: #202124
--text-secondary: #5f6368
--bg-white: #ffffff
--bg-light: #f8f9fa
--border-light: #dadce0
```

### Typography

**Fonts:**
- **Product Sans** - All headings (h1-h6, titles)
- **Google Sans** - Body text, labels, descriptions

**CDN Import:**
```css
@import url('https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&family=Product+Sans:wght@400;700&display=swap');
```

### Icons

**Material Icons** via Google CDN:
```html
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" />
```

**Usage:**
```tsx
<span className="material-icons">rocket_launch</span>
```

**Common Icons:**
- `home` - Home navigation
- `history` - History page
- `rocket_launch` - Get Started
- `analytics` - Evaluation score
- `verified` - Factuality score
- `visibility` - Preview button
- `refresh` - Generate new
- `download` - Download options
- `print` - Print button
- `arrow_back` - Back navigation

### Components

**Google Button:**
```tsx
<button className="btn-google btn-google-primary">
  <span className="material-icons">icon_name</span>
  Button Text
</button>
```

**Google Card:**
```tsx
<div className="card-google p-8">
  Content
</div>
```

**Google Input:**
```tsx
<input className="input-google" />
<textarea className="textarea-google" />
```

### Animations

**Mesh Orbs:**
- 4 floating gradient orbs
- 25-second animation loop
- Blur: 80px
- Colors: Blue, Red, Yellow, Green

**Loading Dots:**
- 4 bouncing dots
- Staggered delays (0s, 0.2s, 0.4s, 0.6s)
- Colors: Blue, Red, Yellow, Green

**Progress Bar:**
- Gradient fill (Blue → Red → Yellow → Green)
- Shimmer overlay effect
- 0.5s smooth transition

## 🚢 Deployment

### Build for Production

```bash
# Create optimized build
npm run build

# Test production build locally
npm start
```

### Deploy to Vercel (Recommended)

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

**Configuration:**
- Framework: Next.js
- Build Command: `npm run build`
- Output Directory: `.next`
- Install Command: `npm install`

### Deploy to Other Platforms

**Netlify:**
```bash
npm run build
# Upload .next folder
```

**AWS/Azure/GCP:**
- Use Docker with Node.js image
- Run `npm run build && npm start`

### Environment Variables

Set in deployment platform:
```
NEXT_PUBLIC_API_URL=https://your-backend-api.com
```

## 🧪 Testing

### Manual Testing Checklist

**Landing Page:**
- [ ] Loads without errors
- [ ] Gradient background visible
- [ ] "Get Started" button works
- [ ] Navigates to /generate

**Generate Page:**
- [ ] Form fields work
- [ ] Sample JD button fills form
- [ ] Character count updates
- [ ] Generate button triggers modal
- [ ] Modal shows progress
- [ ] Auto-navigates on completion

**Results Page:**
- [ ] Scores display correctly
- [ ] Preview button works
- [ ] Download JSON works
- [ ] Generate new navigates to /generate

**Preview Page:**
- [ ] Resume renders correctly
- [ ] Back button works
- [ ] Print button opens dialog
- [ ] All sections visible

### Browser Testing

Test on:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🐛 Troubleshooting

### Common Issues

**Hot Reload Not Working:**
```bash
# Delete .next folder
rm -rf .next
npm run dev
```

**Material Icons Not Loading:**
- Check `app/layout.tsx` has CDN link
- Verify internet connection
- Clear browser cache

**API Connection Failed:**
- Verify backend is running on port 8000
- Check browser console for CORS errors
- Ensure correct API URL

**Build Errors:**
```bash
# Clear cache and rebuild
rm -rf .next node_modules
npm install
npm run build
```

**Port 3000 Already in Use:**
```bash
# Kill process
lsof -ti:3000 | xargs kill -9  # Mac/Linux
netstat -ano | findstr :3000   # Windows

# Or use different port
PORT=3001 npm run dev
```

## 🔗 Related Documentation

- [Main README](../README.md)
- [Backend README](../backend/README.md)
- [API Reference](../backend/api/docs/API_REFERENCE.md)

## 📧 Support

For frontend-specific issues:
- Open an issue on GitHub
- Email: chandan.keelara@gmail.com
- Include: Browser, OS, screenshots, console errors

<p align="right">(<a href="#readme-top">back to top</a>)</p>
