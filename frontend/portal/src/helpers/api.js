import axios from 'axios'
export default {
  get (request) {
    request.method = 'get'
    return this.doRequest(request)
  },
  put (request) {
    request.method = 'put'
    return this.doRequest(request)
  },
  post (request) {
    request.method = 'post'
    return this.doRequest(request)
  },
  delete (request) {
    request.method = 'delete'
    return this.doRequest(request)
  },
  doRequest (request) {
    const method = request.method || 'post'
    const url = request.url || ''
    const data = request.data || null
    let queryParams = ''
    if (request.queryParams) {
      const str = []
      queryParams = '?'
      /* eslint-disable-next-line */
      for (const [key, value] of Object.entries(request.queryParams)) {
        if (value) {
          str.push(`${encodeURIComponent(key)}=${encodeURIComponent(value)}`);
        }
      }
      queryParams += str.join('&')
    }
    const config = {
      method,
      url: `http://hockey-portal.ru/api/${url}${queryParams}`,
      headers: {
        'Content-Type': 'application/json; charset=UTF-8'
      },
      data,
      json: true
    }
    return new Promise((resolve, reject) => {
      axios(config)
        .then((response) => {
          resolve(response.data)
        })
        .catch((error) => {
          reject(error.response)
        })
    })
  }
}
