'use client'

import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'

export default function PreviewPage() {
  const router = useRouter()
  const [resume, setResume] = useState<any>(null)

  useEffect(() => {
    const data = sessionStorage.getItem('previewResume')
    if (!data) {
      router.push('/results')
      return
    }
    setResume(JSON.parse(data))
  }, [router])

  if (!resume) {
    return <div>Loading...</div>
  }

  return (
    <>
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
              onClick={() => router.back()}
              style={{
                background: 'none',
                border: 'none',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                fontFamily: 'Google Sans, sans-serif',
                fontSize: '0.95rem',
                fontWeight: 500,
                color: 'var(--google-blue)'
              }}
            >
              <span className="material-icons">arrow_back</span>
              Back to Results
            </button>
            <button
              onClick={() => {
                window.print()
              }}
              className="btn-google btn-google-primary"
              style={{ padding: '8px 24px' }}
            >
              <span className="material-icons" style={{ fontSize: '20px' }}>print</span>
              Print
            </button>
          </div>
        </div>
      </header>

      {/* Resume Preview */}
      <main style={{ 
        minHeight: 'calc(100vh - 64px)',
        background: 'var(--bg-light)',
        padding: '40px 20px'
      }}>
        <div style={{ 
          maxWidth: '850px', 
          margin: '0 auto',
          background: 'white',
          boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
          borderRadius: '8px',
          overflow: 'hidden'
        }}>
          {/* Resume Content */}
          <div style={{ padding: '60px 80px' }}>
            {/* Header */}
            {resume.header && (
              <div style={{ 
                borderBottom: '3px solid var(--text-primary)', 
                paddingBottom: '16px', 
                marginBottom: '32px' 
              }}>
                <h1 style={{ 
                  fontFamily: 'Product Sans, sans-serif',
                  fontSize: '2rem',
                  fontWeight: 700,
                  color: 'var(--text-primary)',
                  marginBottom: '8px'
                }}>
                  {resume.header.title}
                </h1>
              </div>
            )}

            {/* Summary */}
            {resume.summary && (
              <section style={{ marginBottom: '32px' }}>
                <h2 style={{ 
                  fontFamily: 'Product Sans, sans-serif',
                  fontSize: '1.1rem',
                  fontWeight: 700,
                  color: 'var(--text-primary)',
                  textTransform: 'uppercase',
                  letterSpacing: '1px',
                  marginBottom: '12px'
                }}>
                  Professional Summary
                </h2>
                <p style={{ 
                  fontFamily: 'Google Sans, sans-serif',
                  fontSize: '0.95rem',
                  color: 'var(--text-secondary)',
                  lineHeight: 1.6,
                  textAlign: 'justify'
                }}>
                  {resume.summary}
                </p>
              </section>
            )}

            {/* Skills */}
            {resume.skills && resume.skills.length > 0 && (
              <section style={{ marginBottom: '32px' }}>
                <h2 style={{ 
                  fontFamily: 'Product Sans, sans-serif',
                  fontSize: '1.1rem',
                  fontWeight: 700,
                  color: 'var(--text-primary)',
                  textTransform: 'uppercase',
                  letterSpacing: '1px',
                  marginBottom: '12px'
                }}>
                  Technical Skills
                </h2>
                <div style={{ display: 'grid', gap: '8px' }}>
                  {resume.skills.map((skill: any, idx: number) => (
                    <div key={idx} style={{ 
                      fontFamily: 'Google Sans, sans-serif',
                      fontSize: '0.9rem',
                      color: 'var(--text-secondary)'
                    }}>
                      <span style={{ fontWeight: 600, color: 'var(--text-primary)' }}>
                        {skill.category}:
                      </span>{' '}
                      {skill.items}
                    </div>
                  ))}
                </div>
              </section>
            )}

            {/* Experience */}
            {resume.experience && resume.experience.length > 0 && (
              <section style={{ marginBottom: '32px' }}>
                <h2 style={{ 
                  fontFamily: 'Product Sans, sans-serif',
                  fontSize: '1.1rem',
                  fontWeight: 700,
                  color: 'var(--text-primary)',
                  textTransform: 'uppercase',
                  letterSpacing: '1px',
                  marginBottom: '16px'
                }}>
                  Professional Experience
                </h2>
                <div style={{ display: 'grid', gap: '24px' }}>
                  {resume.experience.map((exp: any, idx: number) => (
                    <div key={idx}>
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start', marginBottom: '8px' }}>
                        <div>
                          <h3 style={{ 
                            fontFamily: 'Product Sans, sans-serif',
                            fontSize: '1rem',
                            fontWeight: 700,
                            color: 'var(--text-primary)',
                            marginBottom: '4px'
                          }}>
                            {exp.role}
                          </h3>
                          <p style={{ 
                            fontFamily: 'Google Sans, sans-serif',
                            fontSize: '0.9rem',
                            color: 'var(--text-secondary)'
                          }}>
                            {exp.company} • {exp.location}
                          </p>
                        </div>
                        <span style={{ 
                          fontFamily: 'Google Sans, sans-serif',
                          fontSize: '0.85rem',
                          color: 'var(--text-secondary)',
                          whiteSpace: 'nowrap'
                        }}>
                          {exp.duration}
                        </span>
                      </div>
                      <ul style={{ 
                        margin: '8px 0 0 20px',
                        padding: 0,
                        listStyleType: 'disc'
                      }}>
                        {exp.bullets.map((bullet: string, bidx: number) => (
                          <li key={bidx} style={{ 
                            fontFamily: 'Google Sans, sans-serif',
                            fontSize: '0.9rem',
                            color: 'var(--text-secondary)',
                            lineHeight: 1.6,
                            marginBottom: '6px'
                          }}>
                            {bullet}
                          </li>
                        ))}
                      </ul>
                    </div>
                  ))}
                </div>
              </section>
            )}

            {/* Projects */}
            {resume.projects && resume.projects.length > 0 && (
              <section>
                <h2 style={{ 
                  fontFamily: 'Product Sans, sans-serif',
                  fontSize: '1.1rem',
                  fontWeight: 700,
                  color: 'var(--text-primary)',
                  textTransform: 'uppercase',
                  letterSpacing: '1px',
                  marginBottom: '16px'
                }}>
                  Projects
                </h2>
                <div style={{ display: 'grid', gap: '20px' }}>
                  {resume.projects.map((project: any, idx: number) => (
                    <div key={idx}>
                      <h3 style={{ 
                        fontFamily: 'Product Sans, sans-serif',
                        fontSize: '1rem',
                        fontWeight: 700,
                        color: 'var(--text-primary)',
                        marginBottom: '4px'
                      }}>
                        {project.title}
                      </h3>
                      <p style={{ 
                        fontFamily: 'Google Sans, sans-serif',
                        fontSize: '0.85rem',
                        color: 'var(--text-secondary)',
                        marginBottom: '8px',
                        fontStyle: 'italic'
                      }}>
                        {project.tech}
                      </p>
                      <ul style={{ 
                        margin: '0 0 0 20px',
                        padding: 0,
                        listStyleType: 'disc'
                      }}>
                        <li style={{ 
                          fontFamily: 'Google Sans, sans-serif',
                          fontSize: '0.9rem',
                          color: 'var(--text-secondary)',
                          lineHeight: 1.6,
                          marginBottom: '4px'
                        }}>
                          {project.bullet1}
                        </li>
                        <li style={{ 
                          fontFamily: 'Google Sans, sans-serif',
                          fontSize: '0.9rem',
                          color: 'var(--text-secondary)',
                          lineHeight: 1.6
                        }}>
                          {project.bullet2}
                        </li>
                      </ul>
                    </div>
                  ))}
                </div>
              </section>
            )}
          </div>
        </div>
      </main>

      {/* Print Styles */}
      <style jsx global>{`
        @media print {
          header {
            display: none !important;
          }
          main {
            padding: 0 !important;
            background: white !important;
          }
          main > div {
            box-shadow: none !important;
            max-width: 100% !important;
          }
        }
      `}</style>
    </>
  )
}
