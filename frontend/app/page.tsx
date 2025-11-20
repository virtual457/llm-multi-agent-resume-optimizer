'use client'

import { useRouter } from 'next/navigation'
import { useEffect, useState } from 'react'

export default function Home() {
  const router = useRouter()
  const [showLoader, setShowLoader] = useState(true)

  useEffect(() => {
    const timer = setTimeout(() => {
      setShowLoader(false)
    }, 2000)
    return () => clearTimeout(timer)
  }, [])

  return (
    <>
      {/* Google Loading Screen */}
      {showLoader && (
        <div className="loading-screen">
          <div className="google-loader">
            <div className="loader-dot"></div>
            <div className="loader-dot"></div>
            <div className="loader-dot"></div>
            <div className="loader-dot"></div>
          </div>
          <p style={{ 
            marginTop: '30px', 
            fontFamily: 'Google Sans, sans-serif', 
            fontSize: '1.1rem', 
            color: 'var(--text-secondary)' 
          }}>
            Loading LMARO...
          </p>
        </div>
      )}

      {/* Mesh Background */}
      <div className="mesh-bg">
        <div className="mesh-orb mesh-orb-1"></div>
        <div className="mesh-orb mesh-orb-2"></div>
        <div className="mesh-orb mesh-orb-3"></div>
        <div className="mesh-orb mesh-orb-4"></div>
      </div>

      {/* Main Content - Full Screen Hero */}
      <main style={{ 
        minHeight: '100vh',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        position: 'relative',
        zIndex: 1,
        padding: '40px'
      }}>
        <div style={{ maxWidth: '900px', textAlign: 'center' }}>
          {/* Logo/Title */}
          <h1 style={{ 
            fontFamily: 'Product Sans, sans-serif', 
            fontSize: 'clamp(3rem, 10vw, 6rem)', 
            fontWeight: 700,
            background: 'linear-gradient(135deg, #4285f4 0%, #ea4335 25%, #fbbc04 50%, #34a853 75%, #4285f4 100%)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
            backgroundClip: 'text',
            marginBottom: '24px',
            lineHeight: 1.1
          }}>
            LMARO
          </h1>

          {/* Tagline */}
          <h2 style={{
            fontFamily: 'Google Sans, sans-serif',
            fontSize: 'clamp(1.5rem, 4vw, 2.5rem)',
            fontWeight: 500,
            color: 'var(--text-primary)',
            marginBottom: '32px',
            lineHeight: 1.3
          }}>
            AI-Powered Resume Optimizer
          </h2>

          {/* Description */}
          <p style={{
            fontFamily: 'Google Sans, sans-serif',
            fontSize: 'clamp(1rem, 2.5vw, 1.3rem)',
            color: 'var(--text-secondary)',
            lineHeight: 1.7,
            marginBottom: '48px',
            maxWidth: '700px',
            margin: '0 auto 48px'
          }}>
            Generate tailored, ATS-optimized resumes using advanced AI. 
            Our multi-agent system evaluates, optimizes, and verifies your resume 
            to match any job description perfectly.
          </p>

          {/* Feature Stats */}
          <div style={{ 
            display: 'grid', 
            gridTemplateColumns: 'repeat(auto-fit, minmax(140px, 1fr))',
            gap: '24px',
            maxWidth: '700px',
            margin: '0 auto 60px'
          }}>
            <StatCard number="90+" label="Match Score" color="var(--google-blue)" />
            <StatCard number="100%" label="Factually Accurate" color="var(--google-red)" />
            <StatCard number="3x" label="Faster Process" color="var(--google-yellow)" />
            <StatCard number="∞" label="Iterations" color="var(--google-green)" />
          </div>

          {/* CTA Button */}
          <button
            onClick={() => router.push('/generate')}
            className="btn-google btn-google-primary"
            style={{ 
              fontSize: '1.1rem',
              padding: '16px 48px',
              boxShadow: '0 4px 12px rgba(66, 133, 244, 0.4)',
              animation: 'pulse 2s ease-in-out infinite'
            }}
          >
            <span className="material-icons" style={{ fontSize: '24px' }}>rocket_launch</span>
            Get Started
          </button>

          {/* Features List */}
          <div style={{ 
            display: 'flex',
            flexWrap: 'wrap',
            gap: '16px',
            justifyContent: 'center',
            marginTop: '60px'
          }}>
            <FeatureChip icon="verified_user" text="Factuality Checked" />
            <FeatureChip icon="trending_up" text="90+ Score Guaranteed" />
            <FeatureChip icon="description" text="DOCX Export" />
            <FeatureChip icon="speed" text="30-60 Seconds" />
            <FeatureChip icon="psychology" text="AI-Powered" />
          </div>
        </div>
      </main>

      <style jsx>{`
        @keyframes pulse {
          0%, 100% {
            transform: scale(1);
            box-shadow: 0 4px 12px rgba(66, 133, 244, 0.4);
          }
          50% {
            transform: scale(1.05);
            box-shadow: 0 8px 24px rgba(66, 133, 244, 0.6);
          }
        }
      `}</style>
    </>
  )
}

function StatCard({ number, label, color }: { number: string, label: string, color: string }) {
  return (
    <div 
      className="card-google"
      style={{ 
        padding: '24px',
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
      <div style={{ 
        fontFamily: 'Product Sans, sans-serif',
        fontSize: '2rem',
        fontWeight: 700,
        color: color,
        marginBottom: '8px'
      }}>
        {number}
      </div>
      <div style={{
        fontFamily: 'Google Sans, sans-serif',
        fontSize: '0.875rem',
        color: 'var(--text-secondary)'
      }}>
        {label}
      </div>
    </div>
  )
}

function FeatureChip({ icon, text }: { icon: string, text: string }) {
  return (
    <div style={{
      display: 'flex',
      alignItems: 'center',
      gap: '8px',
      padding: '8px 16px',
      background: 'var(--bg-light)',
      borderRadius: '20px',
      border: '1px solid var(--border-light)',
      fontFamily: 'Google Sans, sans-serif',
      fontSize: '0.875rem',
      color: 'var(--text-secondary)',
      transition: 'all 0.2s ease'
    }}
    onMouseEnter={(e) => {
      e.currentTarget.style.background = 'white'
      e.currentTarget.style.borderColor = 'var(--google-blue)'
      e.currentTarget.style.color = 'var(--google-blue)'
      e.currentTarget.style.transform = 'translateY(-2px)'
    }}
    onMouseLeave={(e) => {
      e.currentTarget.style.background = 'var(--bg-light)'
      e.currentTarget.style.borderColor = 'var(--border-light)'
      e.currentTarget.style.color = 'var(--text-secondary)'
      e.currentTarget.style.transform = 'translateY(0)'
    }}
    >
      <span className="material-icons" style={{ fontSize: '18px' }}>{icon}</span>
      {text}
    </div>
  )
}
