'use client'

interface ResultsDisplayProps {
  results: any
  onReset: () => void
}

export function ResultsDisplay({ results, onReset }: ResultsDisplayProps) {
  const { resume, scores, paths } = results
  
  // Extract scores safely
  const evaluationScore = scores?.evaluation?.total_score || 0
  const factualityScore = scores?.factuality?.factuality_score || 0
  const evaluationSections = scores?.evaluation?.section_scores || {}
  const factualitySections = scores?.factuality?.section_scores || {}
  const detailedFeedback = scores?.evaluation?.detailed_feedback || {}

  const downloadJSON = () => {
    const blob = new Blob([JSON.stringify(resume, null, 2)], { type: 'application/json' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `resume_${paths?.job_id || 'output'}.json`
    a.click()
  }

  const downloadDOCX = async () => {
    try {
      // The DOCX file should be at the path returned by the API
      alert('DOCX download will be implemented with file serving from backend')
    } catch (error) {
      console.error('Error downloading DOCX:', error)
    }
  }

  return (
    <div className="max-w-6xl mx-auto">
      {/* Header */}
      <div className="flex items-center justify-between mb-8">
        <div>
          <h2 className="text-4xl font-bold text-gray-900 mb-2">Resume Generated! 🎉</h2>
          <p className="text-gray-600">
            Your optimized resume for <span className="font-semibold">{resume?.company || 'the position'}</span>
          </p>
        </div>
        <button onClick={onReset} className="btn-secondary">
          Generate New Resume
        </button>
      </div>

      {/* Scores Section */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
        {/* Evaluation Score */}
        <div className="card">
          <div className="flex items-start justify-between mb-6">
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-1">Evaluation Score</h3>
              <p className="text-sm text-gray-600">Match against job description</p>
            </div>
            <ScoreBadge score={evaluationScore} />
          </div>
          
          {Object.keys(evaluationSections).length > 0 && (
            <div className="space-y-3">
              {Object.entries(evaluationSections).map(([section, score]: [string, any]) => (
                <div key={section}>
                  <div className="flex items-center justify-between mb-1">
                    <span className="text-sm font-medium text-gray-700 capitalize">
                      {section.replace('_', ' ')}
                    </span>
                    <span className="text-sm font-semibold text-gray-900">{score}/100</span>
                  </div>
                  <ProgressBar value={score} />
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Factuality Score */}
        <div className="card">
          <div className="flex items-start justify-between mb-6">
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-1">Factuality Score</h3>
              <p className="text-sm text-gray-600">Accuracy verification</p>
            </div>
            <ScoreBadge score={factualityScore} color="green" />
          </div>
          
          {Object.keys(factualitySections).length > 0 && (
            <div className="space-y-3">
              {Object.entries(factualitySections).map(([section, score]: [string, any]) => (
                <div key={section}>
                  <div className="flex items-center justify-between mb-1">
                    <span className="text-sm font-medium text-gray-700 capitalize">
                      {section.replace('_', ' ')}
                    </span>
                    <span className="text-sm font-semibold text-gray-900">{score}/100</span>
                  </div>
                  <ProgressBar value={score} color="green" />
                </div>
              ))}
            </div>
          )}
        </div>
      </div>

      {/* Feedback Section */}
      {Object.keys(detailedFeedback).length > 0 && (
        <div className="card mb-8">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Detailed Feedback</h3>
          <div className="space-y-4">
            {Object.entries(detailedFeedback).map(([section, feedback]: [string, any]) => (
              <div key={section} className="border-l-4 border-blue-500 pl-4">
                <h4 className="font-medium text-gray-900 capitalize mb-2">
                  {section.replace('_', ' ')}
                </h4>
                <p className="text-sm text-gray-700">{feedback}</p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Resume Preview */}
      <div className="card mb-8">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">Resume Preview</h3>
        <div className="bg-gray-50 rounded-lg p-6 space-y-6 max-h-96 overflow-y-auto">
          {/* Header */}
          {resume?.header && (
            <div className="border-b border-gray-300 pb-4">
              <h4 className="text-xl font-bold text-gray-900">{resume.header.title}</h4>
            </div>
          )}

          {/* Summary */}
          {resume?.summary && (
            <div>
              <h5 className="text-sm font-semibold text-gray-700 mb-2">PROFESSIONAL SUMMARY</h5>
              <p className="text-sm text-gray-800 leading-relaxed">{resume.summary}</p>
            </div>
          )}

          {/* Skills */}
          {resume?.skills && (
            <div>
              <h5 className="text-sm font-semibold text-gray-700 mb-2">TECHNICAL SKILLS</h5>
              <div className="space-y-1">
                {resume.skills.map((skill: any, idx: number) => (
                  <div key={idx} className="text-sm text-gray-800">
                    <span className="font-medium">{skill.category}:</span> {skill.items}
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Experience */}
          {resume?.experience && (
            <div>
              <h5 className="text-sm font-semibold text-gray-700 mb-2">PROFESSIONAL EXPERIENCE</h5>
              <div className="space-y-4">
                {resume.experience.map((exp: any, idx: number) => (
                  <div key={idx}>
                    <div className="flex justify-between items-start mb-2">
                      <div>
                        <div className="font-semibold text-gray-900">{exp.role}</div>
                        <div className="text-sm text-gray-700">{exp.company} - {exp.location}</div>
                      </div>
                      <div className="text-sm text-gray-600">{exp.duration}</div>
                    </div>
                    <ul className="list-disc list-inside space-y-1 text-sm text-gray-800">
                      {exp.bullets.map((bullet: string, bidx: number) => (
                        <li key={bidx}>{bullet}</li>
                      ))}
                    </ul>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Projects */}
          {resume?.projects && (
            <div>
              <h5 className="text-sm font-semibold text-gray-700 mb-2">PROJECTS</h5>
              <div className="space-y-3">
                {resume.projects.map((project: any, idx: number) => (
                  <div key={idx}>
                    <div className="font-semibold text-gray-900">{project.title}</div>
                    <div className="text-sm text-gray-600 mb-1">{project.tech}</div>
                    <ul className="list-disc list-inside space-y-1 text-sm text-gray-800">
                      <li>{project.bullet1}</li>
                      <li>{project.bullet2}</li>
                    </ul>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Download Buttons */}
      <div className="flex items-center gap-4 justify-center">
        <button onClick={downloadJSON} className="btn-primary">
          📄 Download JSON
        </button>
        <button onClick={downloadDOCX} className="btn-primary">
          📝 Download DOCX
        </button>
      </div>

      {/* File Paths Info */}
      {paths && (
        <div className="mt-8 p-4 bg-blue-50 rounded-lg border border-blue-200">
          <p className="text-sm text-gray-700">
            <span className="font-medium">Files saved:</span>
          </p>
          <p className="text-xs text-gray-600 mt-1">JSON: {paths.json_path}</p>
          <p className="text-xs text-gray-600">DOCX: {paths.docx_path}</p>
        </div>
      )}
    </div>
  )
}

function ScoreBadge({ score, color = 'blue' }: { score: number; color?: string }) {
  const colorClasses = {
    blue: 'bg-blue-100 text-blue-800 border-blue-200',
    green: 'bg-green-100 text-green-800 border-green-200',
  }

  return (
    <div className={`px-4 py-2 rounded-full border-2 ${colorClasses[color as keyof typeof colorClasses]}`}>
      <span className="text-2xl font-bold">{score}</span>
      <span className="text-sm">/100</span>
    </div>
  )
}

function ProgressBar({ value, color = 'blue' }: { value: number; color?: string }) {
  const colorClasses = {
    blue: 'bg-blue-600',
    green: 'bg-green-600',
  }

  return (
    <div className="w-full h-2 bg-gray-200 rounded-full overflow-hidden">
      <div
        className={`h-full ${colorClasses[color as keyof typeof colorClasses]} transition-all duration-500`}
        style={{ width: `${value}%` }}
      />
    </div>
  )
}
