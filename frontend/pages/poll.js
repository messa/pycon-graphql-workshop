import React from 'react'
import Link from 'next/link'
import { graphql } from 'react-relay'
import Layout from '../components/Layout'
import withData from '../lib/withData'

class PollPage extends React.Component {

  render() {
    return (
      <Layout>
        <h1>Poll: {this.props.poll.title}</h1>
      </Layout>
    )
  }
}

export default withData(PollPage, {
  getVariables: ({ query }) => ({ pollId: query.id }),
  query: graphql`
    query pollQuery($pollId: ID!) {
      poll: node(id: $pollId) {
        id
        ... on Poll {
          title
        }
      }
    }
  `
})
