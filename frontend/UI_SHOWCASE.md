# LMARO Frontend - UI Design Showcase

## Design System

### Colors
```
Primary Gradient: #3b82f6 → #764ba2 (Blue to Purple)
Background: Soft gradient from blue-50 to indigo-50
Text: Gray-900 (headings), Gray-600 (body)
Accents: Blue-600, Indigo-600
Success: Green-600
Cards: White with subtle shadows
```

### Typography
```
Headings: Poppins (Google Font)
  - H1: 3rem (48px), font-bold
  - H2: 2.5rem (40px), font-bold
  - H3: 1.125rem (18px), font-semibold

Body: Inter (Google Font)
  - Regular: 1rem (16px)
  - Small: 0.875rem (14px)
```

### Spacing
```
Cards: p-6 (24px padding)
Sections: mb-8 (32px margin)
Elements: gap-4 to gap-6 (16-24px)
Container: max-w-7xl (1280px)
```

## Page Layouts

### Header (Sticky)
```
┌─────────────────────────────────────────────────────────┐
│  LMARO                                    Home  History │
│  AI-Powered Resume Optimizer                            │
└─────────────────────────────────────────────────────────┘
  ↑ Gradient text logo        ↑ Navigation links
  ↑ White background with backdrop blur (glass effect)
```

### Home Page - Generator View
```
┌─────────────────────────────────────────────────────────┐
│                                                           │
│         Generate Your Perfect Resume                      │
│    Paste any job description and let AI create...        │
│                                                           │
│  ┌───────────────────────────────────────────────────┐  │
│  │                                                     │  │
│  │  Company Name         │  Role                      │  │
│  │  [Google          ]   │  [Software Engineer]       │  │
│  │                                                     │  │
│  │  Job Description             [Paste Sample JD]     │  │
│  │  ┌─────────────────────────────────────────────┐  │  │
│  │  │                                               │  │  │
│  │  │  Paste the complete job description...       │  │  │
│  │  │                                               │  │  │
│  │  └─────────────────────────────────────────────┘  │  │
│  │                                                     │  │
│  │  ✨ AI-powered optimization    [Generate Resume]  │  │
│  │                                                     │  │
│  └───────────────────────────────────────────────────┘  │
│                                                           │
│   🎯              ✅              📊                      │
│  Tailored      Factuality     Scored &                   │
│  Content       Verified       Optimized                  │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

### Results Page - Score Display
```
┌─────────────────────────────────────────────────────────┐
│  Resume Generated! 🎉           [Generate New Resume]   │
│  Your optimized resume for Google                        │
│                                                           │
│  ┌───────────────────────┐  ┌───────────────────────┐  │
│  │ Evaluation Score  95  │  │ Factuality Score  98  │  │
│  │ Match against JD  ──  │  │ Accuracy check    ──  │  │
│  │                       │  │                       │  │
│  │ Summary       92/100  │  │ Summary       100/100 │  │
│  │ ███████████████▒▒▒▒▒  │  │ █████████████████████ │  │
│  │                       │  │                       │  │
│  │ Experience    95/100  │  │ Experience    95/100  │  │
│  │ ██████████████████▒▒  │  │ ██████████████████▒▒  │  │
│  │                       │  │                       │  │
│  │ Skills        98/100  │  │ Projects      100/100 │  │
│  │ ███████████████████▒  │  │ █████████████████████ │  │
│  └───────────────────────┘  └───────────────────────┘  │
│                                                           │
│  ┌───────────────────────────────────────────────────┐  │
│  │ Detailed Feedback                                  │  │
│  │                                                     │  │
│  │ │ Summary                                          │  │
│  │ │ Excellent alignment with job requirements...     │  │
│  │                                                     │  │
│  │ │ Experience                                       │  │
│  │ │ Strong technical experience highlighted...       │  │
│  └───────────────────────────────────────────────────┘  │
│                                                           │
│  ┌───────────────────────────────────────────────────┐  │
│  │ Resume Preview                                     │  │
│  │ ┌───────────────────────────────────────────────┐ │  │
│  │ │ JOHN DOE | MS CS @ NEU | Keywords             │ │  │
│  │ │ ────────────────────────────────────────────── │ │  │
│  │ │ PROFESSIONAL SUMMARY                           │ │  │
│  │ │ Experienced software engineer with...          │ │  │
│  │ │                                                 │ │  │
│  │ │ TECHNICAL SKILLS                               │ │  │
│  │ │ Languages: Python, Java, Go, JavaScript...     │ │  │
│  │ └───────────────────────────────────────────────┘ │  │
│  └───────────────────────────────────────────────────┘  │
│                                                           │
│         [📄 Download JSON]  [📝 Download DOCX]          │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

## Component Details

### Button Styles
```css
Primary Button (Gradient):
- Background: Blue-600 → Indigo-600 gradient
- Text: White, font-medium
- Padding: 12px 24px
- Border radius: 8px
- Shadow: Large, hover increases
- Transform: Subtle lift on hover (-2px)
- Transition: All 200ms

Secondary Button (Outlined):
- Background: White
- Text: Gray-700
- Border: Gray-300
- Hover: Gray-50 background
```

### Card Component
```css
Card:
- Background: White
- Border radius: 12px (rounded-xl)
- Shadow: Large (shadow-lg)
- Padding: 24px
- Border: 1px solid Gray-100
- Hover: Increased shadow (shadow-xl)
```

### Input Fields
```css
Text Input:
- Width: Full
- Padding: 12px 16px
- Border: 1px solid Gray-300
- Border radius: 8px
- Focus: 2px blue ring, no border

Textarea:
- Same as text input
- Resize: None (fixed height)
- Rows: 12 (for JD input)
```

### Progress Bar
```css
Progress Bar:
- Background: Gray-200
- Fill: Blue-600 (eval) / Green-600 (fact)
- Height: 8px
- Border radius: Full (pill shape)
- Transition: Width 500ms (animated)
```

### Score Badge
```css
Score Badge:
- Background: Blue-100 / Green-100
- Text: Blue-800 / Green-800
- Border: 2px solid Blue-200 / Green-200
- Padding: 8px 16px
- Border radius: Full (circular)
- Font: Bold, 2rem (score) + sm (suffix)
```

## Animations

### Loading Spinner
```
Rotating circle with animated arc
Color: Blue-600
Size: 20px (h-5 w-5)
Animation: Spin (infinite)
```

### Page Transitions
```
Components fade in on mount
Scores animate from 0 to value
Progress bars fill smoothly
Hover effects on all interactive elements
```

## Responsive Breakpoints

### Desktop (1280px+)
- 2-column score cards
- Full-width form
- Centered content (max-w-7xl)

### Tablet (768px - 1279px)
- 2-column score cards
- Full-width form
- Adjusted padding

### Mobile (<768px)
- Single column layout
- Stacked score cards
- Compressed padding
- Smaller typography

## Visual Hierarchy

1. **Primary Action**: "Generate Resume" button (gradient, prominent)
2. **Scores**: Large badges with color coding
3. **Feedback**: Section breakdown with progress bars
4. **Preview**: Scrollable content area
5. **Download**: Secondary action buttons

## Accessibility

- Semantic HTML (header, main, section, etc.)
- Proper heading hierarchy (h1 → h6)
- ARIA labels on interactive elements
- Keyboard navigation support
- Color contrast ratios (WCAG AA)
- Focus indicators on all inputs

## Brand Identity

### Logo
```
LMARO
(Gradient text: Blue → Purple)
Tagline: "AI-Powered Resume Optimizer"
```

### Voice
- Professional but friendly
- Clear and concise
- Action-oriented
- Encouraging

### Color Psychology
- Blue: Trust, professionalism, technology
- Purple: Innovation, creativity
- Green: Success, accuracy
- White: Clean, modern, space

## Key Visual Elements

1. **Gradient Backgrounds**: Soft, non-distracting
2. **Glass Effects**: Modern, premium feel
3. **Shadows**: Depth and hierarchy
4. **Rounded Corners**: Friendly, approachable
5. **Progress Indicators**: Visual feedback
6. **Icon Usage**: 🎯 ✅ 📊 📄 📝 (sparingly)

## Implementation Notes

- Uses Tailwind CSS utility classes
- Custom components in globals.css (.btn-primary, .card, etc.)
- Google Fonts loaded via CDN in globals.css
- Responsive with mobile-first approach
- Dark mode not implemented (future enhancement)

---

**The UI is designed to be clean, modern, professional, and user-friendly!**
