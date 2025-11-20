'use client'

import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'

export default function ResultsPage() {
  const router = useRouter()
  const [results, setResults] = useState<any>(null)

  useEffect(() => {
    const data = sessionStorage.getItem('resumeData')
    if (!data) {
      router.push('/generate')
      return
    }
    setResults(JSON.parse(data))
  }, [router])

  if (!results) {
    return <div>Loading...</div>
  }

  const { resume, scores, paths } = results
  const evaluationScore = scores?.evaluation?.total_score || 0
  const factualityScore = scores?.factuality?.factuality_score || 0

  const handlePreview = () => {
    sessionStorage.setItem('previewResume', JSON.stringify(resume))
    router.push('/preview')
  }

  const handleNewResume = () => {
    sessionStorage.removeItem('resumeData')
    router.push('/generate')
  }

  return (
    <>
      {/* Mesh Background */}
      <div className="mesh-bg">
        <div className="mesh-orb mesh-orb-1"></div>
        <div className="mesh-orb mesh-orb-2"></div>
        <div className="mesh-orb mesh-orb-3"></div>
        <div className="mesh-orb mesh-orb-4"></div>
      </div>

      {/* Header */}
      <header style={{ 
        borderBottom: '1px solid var(--border-light)', 
        background: 'rgba(255, 255, 255, 0.95)',
        backdropFilter: 'blur(10px)',
        position: 'sticky',
        top: 0,
        zIndex: 40,
        boxShadow: '0 1px 6px rgba(32,33,36,.12)'
      }}>
        <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '0 40px' }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', height: '64px' }}>
            <button 
              onClick={() => router.push('/')}
              style={{
                background: 'none',
                border: 'none',
                cursor: 'pointer',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'flex-start'
              }}
            >
              <h1 style={{ 
                fontFamily: 'Product Sans, sans-serif', 
                fontSize: '1.75rem', 
                fontWeight: 700,
                background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
                WebkitBackgroundClip: 'text',
                WebkitTextFillColor: 'transparent',
                backgroundClip: 'text'
              }}>
                LMARO
              </h1>
            </button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main style={{ 
        minHeight: 'calc(100vh - 64px)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        position: 'relative',
        zIndex: 1,
        padding: '40px'
      }}>
        <div style={{ maxWidth: '1000px', width: '100%' }}>
          {/* Success Message */}
          <div style={{ textAlign: 'center', marginBottom: '48px' }}>
            <div style={{ fontSize: '4rem', marginBottom: '16px' }}>🎉</div>
            <h2 style={{
              fontFamily: 'Product Sans, sans-serif',
              fontSize: '2.5rem',
              fontWeight: 700,
              color: 'var(--text-primary)',
              marginBottom: '16px'
            }}>
              Resume Generated Successfully!
            </h2>
            <p style={{
              fontFamily: 'Google Sans, sans-serif',
              fontSize: '1.1rem',
              color: 'var(--text-secondary)'
            }}>
              Your optimized resume is ready
            </p>
          </div>

          {/* Score Cards */}
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '24px', marginBottom: '32px' }}>
            <ScoreCard 
              title="Evaluation Score"
              subtitle="Match against job description"
              score={evaluationScore}
              color="var(--google-blue)"
              icon="analytics"
            />
            <ScoreCard 
              title="Factuality Score"
              subtitle="Accuracy verification"
              score={factualityScore}
              color="var(--google-green)"
              icon="verified"
            />
          </div>

          {/* Action Buttons */}
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '16px', marginBottom: '24px' }}>
            <button
              onClick={handlePreview}
              className="btn-google btn-google-primary"
              style={{ padding: '16px', fontSize: '1.05rem' }}
            >
              <span className="material-icons" style={{ fontSize: '22px' }}>visibility</span>
              Preview Resume
            </button>
            <button
              onClick={handleNewResume}
              className="btn-google btn-google-secondary"
              style={{ padding: '16px', fontSize: '1.05rem' }}
            >
              <span className="material-icons" style={{ fontSize: '22px' }}>refresh</span>
              Generate New Resume
            </button>
          </div>

          {/* Download Options */}
          <div className="card-google p-6">
            <h3 style={{
              fontFamily: 'Product Sans, sans-serif',
              fontSize: '1.3rem',
              fontWeight: 600,
              color: 'var(--text-primary)',
              marginBottom: '16px',
              display: 'flex',
              alignItems: 'center',
              gap: '8px'
            }}>
              <span className="material-icons" style={{ color: 'var(--google-blue)' }}>download</span>
              Download Options
            </h3>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px' }}>
              <button
                onClick={() => {
                  const blob = new Blob([JSON.stringify(resume, null, 2)], { type: 'application/json' })
                  const url = URL.createObjectURL(blob)
                  const a = document.createElement('a')
                  a.href = url
                  a.download = `resume_${paths?.job_id || 'output'}.json`
                  a.click()
                }}
                style={{
                  padding: '12px 24px',
                  background: 'var(--bg-light)',
                  border: '1px solid var(--border-light)',
                  borderRadius: '8px',
                  fontFamily: 'Google Sans, sans-serif',
                  fontSize: '0.95rem',
                  fontWeight: 500,
                  color: 'var(--text-primary)',
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  gap: '8px',
                  transition: 'all 0.2s ease'
                }}
                onMouseEnter={(e) => {
                  e.currentTarget.style.background = 'white'
                  e.currentTarget.style.borderColor = 'var(--google-blue)'
                }}
                onMouseLeave={(e) => {
                  e.currentTarget.style.background = 'var(--bg-light)'
                  e.currentTarget.style.borderColor = 'var(--border-light)'
                }}
              >
                <span className="material-icons" style={{ fontSize: '20px' }}>code</span>
                Download JSON
              </button>
              <button
                onClick={() => alert('DOCX download will be implemented with file serving from backend')}
                style={{
                  padding: '12px 24px',
                  background: 'var(--bg-light)',
                  border: '1px solid var(--border-light)',
                  borderRadius: '8px',
                  fontFamily: 'Google Sans, sans-serif',
                  fontSize: '0.95rem',
                  fontWeight: 500,
                  color: 'var(--text-primary)',
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  gap: '8px',
                  transition: 'all 0.2s ease'
                }}
                onMouseEnter={(e) => {
                  e.currentTarget.style.background = 'white'
                  e.currentTarget.style.borderColor = 'var(--google-blue)'
                }}
                onMouseLeave={(e) => {
                  e.currentTarget.style.background = 'var(--bg-light)'
                  e.currentTarget.style.borderColor = 'var(--border-light)'
                }}
              >
                <span className="material-icons" style={{ fontSize: '20px' }}>description</span>
                Download DOCX
              </button>
            </div>
          </div>
        </div>
      </main>
    </>
  )
}

function ScoreCard({ title, subtitle, score, color, icon }: { title: string, subtitle: string, score: number, color: string, icon: string }) {
  return (
    <div className="card-google p-6">
      <div style={{ display: 'flex', alignItems: 'start', justifyContent: 'space-between', marginBottom: '16px' }}>
        <div>
          <h3 style={{
            fontFamily: 'Product Sans, sans-serif',
            fontSize: '1.2rem',
            fontWeight: 600,
            color: 'var(--text-primary)',
            marginBottom: '4px'
          }}>
            {title}
          </h3>
          <p style={{
            fontFamily: 'Google Sans, sans-serif',
            fontSize: '0.9rem',
            color: 'var(--text-secondary)'
          }}>
            {subtitle}
          </p>
        </div>
        <div style={{
          width: '56px',
          height: '56px',
          borderRadius: '50%',
          background: `${color}20`,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center'
        }}>
          <span className="material-icons" style={{ fontSize: '28px', color: color }}>
            {icon}
          </span>
        </div>
      </div>
      <div style={{
        fontFamily: 'Product Sans, sans-serif',
        fontSize: '3rem',
        fontWeight: 700,
        color: color
      }}>
        {score}<span style={{ fontSize: '1.5rem', opacity: 0.7 }}>/100</span>
      </div>
    </div>
  )
}
