'use client'

import { useState } from 'react'

interface ResumeGeneratorProps {
  onGenerate: (data: any) => void
  isGenerating: boolean
}

export function ResumeGenerator({ onGenerate, isGenerating }: ResumeGeneratorProps) {
  const [jdText, setJdText] = useState('')
  const [company, setCompany] = useState('')
  const [role, setRole] = useState('')

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    
    if (!jdText.trim() || !company.trim() || !role.trim()) {
      alert('Please fill in all fields')
      return
    }

    onGenerate({ jdText, company, role })
  }

  const handlePasteSample = () => {
    setJdText(`We are seeking a talented Software Engineer Intern to join our team for Spring/Summer 2026.

Responsibilities:
- Design and develop scalable backend systems using modern frameworks
- Collaborate with cross-functional teams on feature development
- Write clean, maintainable, and well-documented code
- Participate in code reviews and contribute to team discussions
- Debug and optimize application performance

Requirements:
- Currently pursuing MS in Computer Science or related field
- Strong proficiency in Python, Java, or Go
- Experience with distributed systems and cloud technologies
- Knowledge of databases, APIs, and microservices architecture
- Excellent problem-solving and communication skills
- Previous internship or co-op experience preferred`)
    setCompany('Google')
    setRole('Software Engineer Intern')
  }

  return (
    <div style={{ maxWidth: '900px', margin: '0 auto' }}>
      {/* Hero Section */}
      <div style={{ textAlign: 'center', marginBottom: '60px' }}>
        <h2 style={{ 
          fontFamily: 'Product Sans, sans-serif',
          fontSize: 'clamp(2.5rem, 8vw, 4rem)',
          fontWeight: 700,
          color: 'var(--text-primary)',
          marginBottom: '24px',
          lineHeight: 1.2
        }}>
          Generate Your Perfect Resume
        </h2>
        <p style={{ 
          fontSize: 'clamp(1rem, 3vw, 1.3rem)',
          color: 'var(--text-secondary)',
          lineHeight: 1.6,
          maxWidth: '700px',
          margin: '0 auto',
          fontFamily: 'Google Sans, sans-serif'
        }}>
          Paste any job description and let AI create a tailored, ATS-optimized resume 
          that highlights your relevant skills and experience.
        </p>
      </div>

      {/* Form Card */}
      <div className="card-google p-8">
        <form onSubmit={handleSubmit}>
          {/* Company and Role */}
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '24px', marginBottom: '24px' }}>
            <div>
              <label 
                htmlFor="company" 
                style={{ 
                  display: 'block',
                  fontFamily: 'Google Sans, sans-serif',
                  fontSize: '0.95rem',
                  fontWeight: 500,
                  color: 'var(--text-primary)',
                  marginBottom: '8px'
                }}
              >
                Company Name
              </label>
              <input
                type="text"
                id="company"
                value={company}
                onChange={(e) => setCompany(e.target.value)}
                placeholder="e.g., Google, Microsoft, Amazon"
                className="input-google"
                disabled={isGenerating}
                style={{ fontFamily: 'Google Sans, sans-serif' }}
              />
            </div>
            <div>
              <label 
                htmlFor="role" 
                style={{ 
                  display: 'block',
                  fontFamily: 'Google Sans, sans-serif',
                  fontSize: '0.95rem',
                  fontWeight: 500,
                  color: 'var(--text-primary)',
                  marginBottom: '8px'
                }}
              >
                Role
              </label>
              <input
                type="text"
                id="role"
                value={role}
                onChange={(e) => setRole(e.target.value)}
                placeholder="e.g., Software Engineer Intern"
                className="input-google"
                disabled={isGenerating}
                style={{ fontFamily: 'Google Sans, sans-serif' }}
              />
            </div>
          </div>

          {/* Job Description */}
          <div style={{ marginBottom: '24px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
              <label 
                htmlFor="jdText" 
                style={{ 
                  fontFamily: 'Google Sans, sans-serif',
                  fontSize: '0.95rem',
                  fontWeight: 500,
                  color: 'var(--text-primary)'
                }}
              >
                Job Description
              </label>
              <button
                type="button"
                onClick={handlePasteSample}
                disabled={isGenerating}
                style={{
                  fontFamily: 'Google Sans, sans-serif',
                  fontSize: '0.875rem',
                  fontWeight: 500,
                  color: 'var(--google-blue)',
                  background: 'none',
                  border: 'none',
                  cursor: isGenerating ? 'not-allowed' : 'pointer',
                  opacity: isGenerating ? 0.5 : 1,
                  display: 'flex',
                  alignItems: 'center',
                  gap: '4px'
                }}
              >
                <span className="material-icons" style={{ fontSize: '18px' }}>content_paste</span>
                Paste Sample JD
              </button>
            </div>
            <textarea
              id="jdText"
              value={jdText}
              onChange={(e) => setJdText(e.target.value)}
              placeholder="Paste the complete job description here..."
              rows={14}
              className="textarea-google"
              disabled={isGenerating}
              style={{ fontFamily: 'Google Sans, sans-serif' }}
            />
            <p style={{ fontSize: '0.875rem', color: 'var(--text-secondary)', marginTop: '8px', fontFamily: 'Google Sans, sans-serif' }}>
              {jdText.length} characters
            </p>
          </div>

          {/* Submit Button */}
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingTop: '16px', borderTop: '1px solid var(--border-light)' }}>
            <div style={{ fontSize: '0.875rem', color: 'var(--text-secondary)', fontFamily: 'Google Sans, sans-serif' }}>
              {isGenerating ? (
                <span style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <LoadingSpinner />
                  Generating your optimized resume...
                </span>
              ) : (
                <span style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <span className="material-icons" style={{ fontSize: '18px', color: 'var(--google-blue)' }}>auto_awesome</span>
                  AI-powered optimization with factuality verification
                </span>
              )}
            </div>
            <button
              type="submit"
              disabled={isGenerating}
              className="btn-google btn-google-primary"
              style={{ opacity: isGenerating ? 0.6 : 1, cursor: isGenerating ? 'not-allowed' : 'pointer' }}
            >
              <span className="material-icons" style={{ fontSize: '20px' }}>
                {isGenerating ? 'hourglass_empty' : 'rocket_launch'}
              </span>
              {isGenerating ? 'Generating...' : 'Generate Resume'}
            </button>
          </div>
        </form>
      </div>

      {/* Features */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '24px', marginTop: '60px' }}>
        <FeatureCard 
          icon="track_changes"
          title="Tailored Content"
          description="Automatically matches your skills and experience to job requirements"
          color="var(--google-blue)"
        />
        <FeatureCard 
          icon="verified_user"
          title="Factuality Verified"
          description="Ensures all claims are backed by your actual experience and achievements"
          color="var(--google-red)"
        />
        <FeatureCard 
          icon="trending_up"
          title="Scored & Optimized"
          description="Iteratively improved until it achieves 90+ match score with the JD"
          color="var(--google-green)"
        />
      </div>
    </div>
  )
}

function LoadingSpinner() {
  return (
    <svg
      style={{ animation: 'spin 1s linear infinite', width: '20px', height: '20px' }}
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
    >
      <circle
        style={{ opacity: 0.25 }}
        cx="12"
        cy="12"
        r="10"
        stroke="currentColor"
        strokeWidth="4"
      ></circle>
      <path
        style={{ opacity: 0.75 }}
        fill="currentColor"
        d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
      ></path>
      <style jsx>{`
        @keyframes spin {
          to { transform: rotate(360deg); }
        }
      `}</style>
    </svg>
  )
}

function FeatureCard({ icon, title, description, color }: { icon: string, title: string, description: string, color: string }) {
  return (
    <div 
      className="card-google" 
      style={{ 
        padding: '32px',
        textAlign: 'center',
        transition: 'all 0.3s ease'
      }}
      onMouseEnter={(e) => {
        e.currentTarget.style.borderColor = color
        e.currentTarget.style.boxShadow = `0 8px 24px ${color}30`
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.borderColor = 'var(--border-light)'
        e.currentTarget.style.boxShadow = '0 2px 8px rgba(0,0,0,0.06)'
      }}
    >
      <div 
        style={{ 
          width: '64px',
          height: '64px',
          margin: '0 auto 20px',
          borderRadius: '12px',
          background: `${color}20`,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center'
        }}
      >
        <span className="material-icons" style={{ fontSize: '36px', color: color }}>
          {icon}
        </span>
      </div>
      <h3 style={{ 
        fontFamily: 'Product Sans, sans-serif',
        fontSize: '1.25rem',
        fontWeight: 600,
        color: 'var(--text-primary)',
        marginBottom: '8px'
      }}>
        {title}
      </h3>
      <p style={{ fontSize: '0.95rem', color: 'var(--text-secondary)', lineHeight: 1.5, fontFamily: 'Google Sans, sans-serif' }}>
        {description}
      </p>
    </div>
  )
}
