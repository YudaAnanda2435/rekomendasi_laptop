import { useEffect, useState } from 'react'
import { getHealth } from '../../services/healthService'

function HealthStatus() {
  const [status, setStatus] = useState({
    loading: true,
    connected: false,
    message: 'Memeriksa koneksi...',
  })

  useEffect(() => {
    let isMounted = true

    async function checkHealth() {
      try {
        await getHealth()

        if (isMounted) {
          setStatus({
            loading: false,
            connected: true,
            message: 'System Online - FastAPI Connected',
          })
        }
      } catch {
        if (isMounted) {
          setStatus({
            loading: false,
            connected: false,
            message: 'Backend belum terhubung',
          })
        }
      }
    }

    checkHealth()

    return () => {
      isMounted = false
    }
  }, [])

  const statusClass = status.connected ? 'health-dot-online' : 'health-dot-offline'

  return (
    <span className="health-status">
      <span className={`health-dot ${status.loading ? 'health-dot-loading' : statusClass}`} />
      {status.message}
    </span>
  )
}

export default HealthStatus
