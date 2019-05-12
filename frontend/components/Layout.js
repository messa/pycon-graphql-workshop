import Head from 'next/head'
import Link from 'next/link'

function NavLink({ active, href, title }) {
  if (active) {
    return (
      <strong>{title}</strong>
    )
  } else {
    return (
      <Link href={href}><a>{title}</a></Link>
    )
  }
}

function Layout({ children, currentPage }) {
  return (
    <div className='mainContent'>
      <Head>
        <title>GQL Workshop</title>
        <style>{css}</style>
      </Head>
      <nav>
        <NavLink href='/' title='Home' active={currentPage === 'home'} />
        <NavLink href='/about' title='About' active={currentPage === 'about'} />
      </nav>
      {children}
    </div>
  )
}

const css = `
  body {
    font-family: sans-serif;
  }
  a {
    color: #00f;
  }
  .mainContent {
    max-width: 700px;
    margin: 0 auto;
    padding: 12px;
  }
  nav {
    text-align: right;
  }
  nav a, nav strong {
    padding: 1px 8px;
  }
`

export default Layout
