'use client'

interface GenerationModalProps {
  stage: string
  message: string
  progress: number
  isOpen: boolean
}

export function GenerationModal({ stage, message, progress, isOpen }: GenerationModalProps) {
  if (!isOpen) return null

  const getStageIcon = (stage: string): string => {
    if (stage.includes('setup')) return 'settings'
    if (stage.includes('generat') && !stage.includes('revising')) return 'edit'
    if (stage.includes('evaluat')) return 'analytics'
    if (stage.includes('revising')) return 'refresh'
    if (stage.includes('factuality')) return 'verified'
    if (stage.includes('saving')) return 'save'
    if (stage.includes('rendering')) return 'description'
    if (stage.includes('complete')) return 'celebration'
    if (stage.includes('error')) return 'error'
    return 'hourglass_empty'
  }

  const getStageColor = (stage: string) => {
    if (stage.includes('error')) return '#ea4335'
    if (stage.includes('complete')) return '#34a853'
    if (stage.includes('passed')) return '#34a853'
    return '#4285f4'
  }

  return (
    <div className="modal-overlay">
      <div className="modal-content p-8">
        {/* Icon */}
        <div className="text-center mb-6">
          <div 
            className="inline-flex items-center justify-center animate-bounce-slow"
            style={{
              width: '80px',
              height: '80px',
              borderRadius: '50%',
              background: `${getStageColor(stage)}20`,
              marginBottom: '16px'
            }}
          >
            <span 
              className="material-icons" 
              style={{ 
                fontSize: '48px',
                color: getStageColor(stage)
              }}
            >
              {getStageIcon(stage)}
            </span>
          </div>
        </div>

        {/* Message */}
        <h3 
          className="text-xl font-semibold text-center mb-6 transition-colors duration-300"
          style={{ color: getStageColor(stage), fontFamily: 'Product Sans, sans-serif' }}
        >
          {message}
        </h3>

        {/* Progress */}
        <div className="mb-6">
          <div className="flex justify-between items-center mb-2">
            <span className="text-sm font-medium" style={{ color: 'var(--text-secondary)', fontFamily: 'Google Sans, sans-serif' }}>
              Progress
            </span>
            <span className="text-sm font-bold" style={{ color: 'var(--text-primary)', fontFamily: 'Google Sans, sans-serif' }}>
              {progress}%
            </span>
          </div>
          <div className="progress-bar-container">
            <div 
              className="progress-bar-fill"
              style={{ width: `${progress}%` }}
            />
          </div>
        </div>

        {/* Timeline */}
        <div className="space-y-3 mb-6">
          <TimelineItem 
            icon="settings"
            label="Setup"
            active={stage.includes('setup')}
            completed={progress > 5}
            color="#4285f4"
          />
          <TimelineItem 
            icon="edit"
            label="Generating Resume"
            active={stage.includes('generat') && !stage.includes('revising')}
            completed={progress > 25}
            color="#ea4335"
          />
          <TimelineItem 
            icon="analytics"
            label="Evaluating Quality"
            active={stage.includes('evaluat')}
            completed={progress > 50}
            color="#fbbc04"
          />
          <TimelineItem 
            icon="verified"
            label="Checking Factuality"
            active={stage.includes('factuality')}
            completed={progress > 80}
            color="#34a853"
          />
          <TimelineItem 
            icon="description"
            label="Creating Documents"
            active={stage.includes('saving') || stage.includes('rendering')}
            completed={progress > 95}
            color="#4285f4"
          />
        </div>

        {/* Info */}
        <div 
          className="p-4 rounded-lg"
          style={{ 
            background: 'rgba(66, 133, 244, 0.08)', 
            border: '1px solid rgba(66, 133, 244, 0.2)' 
          }}
        >
          <div className="flex items-start gap-2">
            <span className="material-icons" style={{ fontSize: '20px', color: 'var(--google-blue)' }}>
              info
            </span>
            <p className="text-sm" style={{ color: 'var(--text-secondary)', fontFamily: 'Google Sans, sans-serif', lineHeight: 1.5 }}>
              This process takes 30-60 seconds. We're analyzing the job description and tailoring your resume!
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}

function TimelineItem({ 
  icon, 
  label, 
  active, 
  completed,
  color
}: { 
  icon: string
  label: string
  active: boolean
  completed: boolean
  color: string
}) {
  return (
    <div 
      className="flex items-center gap-3 px-4 py-3 rounded-lg transition-all duration-300"
      style={{ 
        background: active ? `${color}15` : 'transparent',
        border: active ? `1px solid ${color}40` : '1px solid transparent'
      }}
    >
      <div 
        className="flex-shrink-0 transition-all duration-300"
        style={{
          opacity: active ? 1 : completed ? 0.6 : 0.3,
          transform: active ? 'scale(1.2)' : 'scale(1)'
        }}
      >
        {completed && !active ? (
          <span className="material-icons" style={{ fontSize: '24px', color: '#34a853' }}>
            check_circle
          </span>
        ) : (
          <span className="material-icons" style={{ fontSize: '24px', color: color }}>
            {icon}
          </span>
        )}
      </div>
      <div className="flex-1">
        <div 
          className="text-sm font-medium transition-colors duration-300"
          style={{
            color: active ? color : completed ? '#34a853' : 'var(--text-secondary)',
            fontFamily: 'Google Sans, sans-serif'
          }}
        >
          {label}
        </div>
      </div>
      {active && (
        <div className="flex gap-1">
          {[0, 150, 300].map((delay, i) => (
            <div
              key={i}
              className="w-2 h-2 rounded-full animate-bounce"
              style={{ 
                background: color,
                animationDelay: `${delay}ms`
              }}
            />
          ))}
        </div>
      )}
      {completed && !active && (
        <div className="text-sm font-medium" style={{ color: '#34a853', fontFamily: 'Google Sans, sans-serif' }}>
          Done
        </div>
      )}
    </div>
  )
}
