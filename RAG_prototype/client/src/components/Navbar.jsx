import React from 'react'

function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
  <a className="navbar-brand" href="/">RAG Prototype</a>
  <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span className="navbar-toggler-icon"></span>
  </button>

  <div className="collapse navbar-collapse" id="navbarSupportedContent">
    <ul className="navbar-nav mr-auto">

      <li className="nav-item active">
        <a className="nav-link" href="/">Chat</a>
      </li>

      <li className="nav-item">
        <a className="nav-link" href="/upload">Upload</a>
      </li>

      <li className="nav-item">
        <a className="nav-link" href="/translate">Translate</a>
      </li>

      <li className="nav-item">
        <a className="nav-link" href="/combine">Combine</a>
      </li>

      <li className="nav-item">
        <a className="nav-link" href="/combinetogether">Combine (Together)</a>
      </li>

    </ul>
  </div>
</nav>
  )
}

export default Navbar