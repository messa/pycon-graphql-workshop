import Layout from '../components/Layout'

const githubRepo = 'https://github.com/messa/graphql-workshop'

function AboutPage() {
  return (
    <Layout currentPage='about'>
      <h1>About</h1>
      <p>Github repo: <a href={githubRepo}>{githubRepo}</a></p>
    </Layout>
  )
}

export default AboutPage
