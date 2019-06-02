import Layout from '../components/Layout'
import { graphql } from 'react-relay'
import withData from '../lib/withData'

function IndexPage(props) {
  const polls = props.polls && props.polls.edges.map(edge => edge.node)
  return (
    <Layout currentPage='home'>
      <h1>Polls</h1>
      {polls.map(poll => (
        <div key={poll.id}>
          <h2>{poll.title}</h2>
        </div>
      ))}
    </Layout>
  )
}

export default withData(IndexPage, {
  query: graphql`
    query pages_indexQuery {
      polls {
        edges {
          node {
            id
            title
          }
        }
      }
    }
  `
})
