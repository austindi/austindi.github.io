<template>
    <div>
      <header>
        <h1>Projects</h1>
      </header>
  
      <nav class="navbar">
        <NuxtLink to="/">Home</NuxtLink>
        <NuxtLink to="/passion">About Me</NuxtLink>
        <NuxtLink to="/projects">Projects</NuxtLink>
        <NuxtLink to="/presentations">Presentations</NuxtLink>
        <NuxtLink to="/skills">Skills</NuxtLink>
      </nav>
  
      <main>
        <section>
          <h1>Simulated Scanning Tunneling Spectroscopy Data</h1>
          <p>
            Density Functional Theory (DFT) is a computational method used to study the electronic structure of materials at the atomic level...
          </p>
          <p>
            Scanning Tunneling Spectroscopy (STS) is an experimental technique that measures the electronic properties of a material by analyzing how electrons "tunnel" between a sharp tip and the material’s surface...
          </p>
          <p>
            Simulating STS data using DFT results is crucial because it bridges theory and experiment...
          </p>
        </section>
      </main>
  
      <footer>
        <p>
          Contact: <a href="mailto:austindi1133@gmail.com">austindi1133@gmail.com</a> |
          Phone: +1-(864)-384-9579 |
          <a href="https://github.com/austindi" target="_blank">GitHub</a> |
          <a href="https://www.linkedin.com/in/dave-austin-ph-d-616865a9" target="_blank">LinkedIn</a>
        </p>
      </footer>
    </div>
  </template>
  
  <style scoped>
  header {
    background: #333;
    color: #fff;
    padding: 1em 0;
    text-align: center;
  }
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    line-height: 1.6;
  }
  .navbar {
    display: flex;
    justify-content: space-around;
    align-items: center;
    background-color: #333;
    padding: 10px 0;
  }
  .navbar a {
    background-color: #0078d7;
    color: white;
    padding: 10px 20px;
    text-decoration: none;
    font-size: 16px;
    border-radius: 5px;
    transition: background-color 0.3s ease;
  }
  .navbar a:hover {
    background-color: #005bb5;
  }
  main {
    padding: 20px;
  }
  footer {
    background-color: #333;
    color: white;
    text-align: center;
    padding: 10px 0;
    font-size: 14px;
  }
  footer a {
    color: #0078d7;
    text-decoration: none;
    margin: 0 10px;
  }
  footer a:hover {
    text-decoration: underline;
  }
  @media (max-width: 768px) {
    .navbar {
      flex-wrap: wrap;
      justify-content: center;
    }
    .navbar a {
      margin: 5px;
    }
  }
  </style>
  