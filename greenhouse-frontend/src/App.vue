

<template>
    <div class="app">
    <div class="topheader">
      <div class="logo-container">
        <nav id="menu">
          <a href="http://localhost:8080/" class="logo-container-inner">
            <div style="display: inline-block">
              <img svg-inline class="icon" src="./assets/leafbulb.svg" style="transform: rotateY(180deg);"/>
            </div>
            <div style="display: inline-block;">
              <h1 class="logotext">Greenhouse</h1>
            </div>
          </a>
        </nav>
      </div>
    </div>

    <index/>

  </div>
</template>

<script>
import Index from './components/Index.vue';

export default {
  name: 'app',
  components: {
    Index
  },
}
</script>

<style>
  body { 
    margin: 0; 
  }

 .topheader {
    background-color: #617B30;
    width: 100%;
    height: 100px;
  }

  .tabheader {
    width: 100%;
    height: 40px;
    background-color: #82b74b;
  }

  .logo-container-inner {
    display: flex;
    justify-content: center;
    flex-direction: row;
    text-align: center;
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
