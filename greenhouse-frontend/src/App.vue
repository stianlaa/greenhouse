

<template>
    <div class="app">
    <div class="topheader">
      <div class="logo-container">
        <nav id="menu">
          <a href="http://localhost:8080/">
          <img svg-inline class="icon" src="./assets/leaf.svg"/>
          <h1 class="logotext">Greenhouse</h1>
          </a>
        </nav>
      </div>
    </div>

    <index/>

  </div>
</template>

<script>
import index from './components/index.vue';

export default {
  name: 'app',
  components: {
    index
  },
}
</script>

<style>
  body { 
    margin: 0; 
  }

 .topheader {
    background-color: #405d27;
    width: 100%;
    height: 100px;
  }

  .tabheader {
    width: 100%;
    height: 40px;
    background-color: #82b74b;
  }

  .logo-container {
    padding: 1rem;
  }

  .logotext {
    color: white;
    display: inline-block;
  }

  a {
    color: black;
    text-decoration: none;
  }

  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

</style>
