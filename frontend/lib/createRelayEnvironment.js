import { Environment, Network, RecordSource, Store } from 'relay-runtime'
import fetch from 'isomorphic-unfetch'

const defaultGraphQLEndpoint = 'http://127.0.0.1:8080/graphql'

let relayEnvironment = null

// Define a function that fetches the results of an operation (query/mutation/etc)
// and returns its results as a Promise:
async function fetchQuery (operation, variables, cacheConfig, uploadables) {
  const graphQLEndpoint = process.browser ? '/graphql' : (process.env.GRAPHQL_ENDPOINT || defaultGraphQLEndpoint)
  const fetchOptions = {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json'
    }, // Add authentication and other headers here
    body: JSON.stringify({
      query: operation.text, // GraphQL text from input
      variables
    })
  }
  const response = await fetch(graphQLEndpoint, fetchOptions)
  return await response.json()
}

export default function initEnvironment ({ records = {} } = {}) {
  // Create a network layer from the fetch function
  const network = Network.create(fetchQuery)
  const store = new Store(new RecordSource(records))

  // Make sure to create a new Relay environment for every server-side request so that data
  // isn't shared between connections (which would be bad)
  if (!process.browser) {
    return new Environment({
      network,
      store
    })
  }

  // reuse Relay environment on client-side
  if (!relayEnvironment) {
    relayEnvironment = new Environment({
      network,
      store
    })
  }

  return relayEnvironment
}
