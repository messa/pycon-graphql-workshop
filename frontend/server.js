const express = require('express')
const next = require('next')
const proxy = require('express-http-proxy')

const port = parseInt(process.env.PORT, 10) || 3000
const dev = process.env.NODE_ENV !== 'production'
const app = next({ dev })
const handle = app.getRequestHandler()

const graphQLEndpoint = process.env.GRAPHQL_ENDPOINT || 'http://127.0.0.1:8080/graphql'

app.prepare().then(() => {
  const server = express()

  server.use('/graphql', proxy(graphQLEndpoint, {
    proxyReqPathResolver: req => new URL(graphQLEndpoint).pathname
  }))

  server.use((req, res, next) => {
    // make graphQLEndpoint value accessible to further code
    req.graphQLEndpoint = graphQLEndpoint
    next()
  })

  server.get('*', (req, res) => handle(req, res))

  server.listen(port, err => {
    if (err) throw err
    console.log(`> Ready on http://localhost:${port}`)
  })
})
