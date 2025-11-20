'use client'

interface GenerationStatusProps {
  stage: string
  message: string
  progress: number
}

export function GenerationStatus({ stage, message, progress }: GenerationStatusProps) {
  const getStageIcon = (stage: string) => {
    switch (stage) {
      case 'setup':
        return '⚙️'
      case 'generating':
      case 'generated':
        return '✏️'
      case 'evaluating':
      case 'evaluation_result':
      case 'evaluation_passed':
        return '📊'
      case 'revising_evaluation':
        return '🔄'
      case 'checking_factuality':
      case 'factuality_result':
      case 'factuality_passed':
        return '✅'
      case 'revising_factuality':
        return '🔄'
      case 'saving':
        return '💾'
      case 'rendering':
        return '📝'
      case 'complete':
        return '🎉'
      case 'error':
        return '❌'
      default:
        return '⏳'
    }
  }

  const getStageColor = (stage: string) => {
    if (stage.includes('error')) return 'text-red-600'
    if (stage.includes('complete')) return 'text-green-600'
    if (stage.includes('passed')) return 'text-green-600'
    return 'text-blue-600'
  }

  return (
    <div className="max-w-4xl mx-auto mt-8">
      <div className="card">
        <div className="text-center mb-6">
          <div className="text-6xl mb-4">{getStageIcon(stage)}</div>
          <h3 className={`text-xl font-semibold mb-2 ${getStageColor(stage)}`}>
            {message}
          </h3>
        </div>

        {/* Progress Bar */}
        <div className="mb-4">
          <div className="flex justify-between items-center mb-2">
            <span className="text-sm font-medium text-gray-700">Progress</span>
            <span className="text-sm font-semibold text-gray-900">{progress}%</span>
          </div>
          <div className="w-full h-3 bg-gray-200 rounded-full overflow-hidden">
            <div
              className="h-full bg-gradient-to-r from-blue-500 to-indigo-600 transition-all duration-500 ease-out"
              style={{ width: `${progress}%` }}
            />
          </div>
        </div>

        {/* Stage Timeline */}
        <div className="mt-8 space-y-3">
          <StageItem 
            icon="⚙️" 
            label="Setup" 
            active={stage === 'setup'}
            completed={progress > 5}
          />
          <StageItem 
            icon="✏️" 
            label="Generating Resume" 
            active={stage.includes('generat')}
            completed={progress > 25}
          />
          <StageItem 
            icon="📊" 
            label="Evaluating Quality" 
            active={stage.includes('evaluat')}
            completed={progress > 50}
          />
          <StageItem 
            icon="✅" 
            label="Checking Factuality" 
            active={stage.includes('factuality')}
            completed={progress > 80}
          />
          <StageItem 
            icon="📝" 
            label="Creating Documents" 
            active={stage.includes('saving') || stage.includes('rendering')}
            completed={progress > 95}
          />
          <StageItem 
            icon="🎉" 
            label="Complete" 
            active={stage === 'complete'}
            completed={stage === 'complete'}
          />
        </div>

        {/* Processing Info */}
        <div className="mt-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
          <p className="text-sm text-gray-700">
            <span className="font-medium">💡 Tip:</span> This process takes 30-60 seconds. 
            We're analyzing the job description, tailoring your experience, and verifying accuracy.
          </p>
        </div>
      </div>
    </div>
  )
}

function StageItem({ 
  icon, 
  label, 
  active, 
  completed 
}: { 
  icon: string
  label: string
  active: boolean
  completed: boolean
}) {
  return (
    <div className="flex items-center gap-3">
      <div className={`text-2xl transition-all duration-300 ${
        active ? 'scale-125' : completed ? 'opacity-50' : 'opacity-30'
      }`}>
        {completed && !active ? '✓' : icon}
      </div>
      <div className="flex-1">
        <div className={`text-sm font-medium transition-colors ${
          active ? 'text-blue-600' : completed ? 'text-green-600' : 'text-gray-400'
        }`}>
          {label}
        </div>
      </div>
      {active && (
        <div className="flex gap-1">
          <div className="w-2 h-2 bg-blue-600 rounded-full animate-bounce" style={{ animationDelay: '0ms' }} />
          <div className="w-2 h-2 bg-blue-600 rounded-full animate-bounce" style={{ animationDelay: '150ms' }} />
          <div className="w-2 h-2 bg-blue-600 rounded-full animate-bounce" style={{ animationDelay: '300ms' }} />
        </div>
      )}
      {completed && !active && (
        <div className="text-green-600 text-sm font-medium">Done</div>
      )}
    </div>
  )
}
