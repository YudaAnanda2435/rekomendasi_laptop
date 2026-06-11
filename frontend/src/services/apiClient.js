const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000'

function buildUrl(endpoint) {
  const normalizedEndpoint = endpoint.startsWith('/') ? endpoint : `/${endpoint}`

  return `${API_BASE_URL.replace(/\/$/, '')}${normalizedEndpoint}`
}

async function parseResponse(response) {
  const contentType = response.headers.get('content-type') || ''

  if (!contentType.includes('application/json')) {
    return null
  }

  return response.json()
}

export async function request(endpoint, options = {}) {
  const { headers, ...requestOptions } = options

  let response

  try {
    response = await fetch(buildUrl(endpoint), {
      ...requestOptions,
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
    })
  } catch (error) {
    throw new Error(
      error?.message
        ? `Tidak dapat terhubung ke backend: ${error.message}`
        : 'Tidak dapat terhubung ke backend. Pastikan server FastAPI aktif.',
      { cause: error },
    )
  }

  const body = await parseResponse(response)
  const backendMessage = body?.message

  if (!response.ok) {
    throw new Error(
      backendMessage || `Request gagal dengan status ${response.status} ${response.statusText}`.trim(),
    )
  }

  if (body && body.success === false) {
    throw new Error(backendMessage || 'Backend mengembalikan response yang tidak berhasil.')
  }

  return body
}

export { API_BASE_URL }
