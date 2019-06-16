<template>

  <div>
      <div class="tabheader">
        <button class="tablinks" @click="chooseTab('Status')" 
        :style="getTab() === 'Status'? 'background-color: #405d27;' : 'background-color: #82b74b'">Status</button>
        <button class="tablinks" @click="chooseTab('Tab2')" 
        :style="getTab() === 'Tab2'? 'background-color: #405d27' : 'background-color: #82b74b'">Tab2</button>
        <button class="tablinks" @click="chooseTab('Tab3')" 
        :style="getTab() === 'Tab3'? 'background-color: #405d27' : 'background-color: #82b74b'">Tab3</button>
    </div>

    <div v-if="currentTab === 'Status'" class="tabcontent">
      <h3>Status!</h3>
      <p>This is the current status of the greenhouse</p>
    </div>

    <div v-if="currentTab === 'Tab2'" class="tabcontent">
      <h3>Tab2</h3>
      <p>Under construction</p>
    </div>

    <div v-if="currentTab === 'Tab3'" class="tabcontent">
      <h3>Tab3</h3>
      <p>Under construction</p>
    </div>

  </div>
</template>

<script>

export default {
  name: 'Index',
  data: function () {
    return {
      currentTab: "Status",
    }
  },
  methods: {
    chooseTab(button) {
      this.currentTab = button;
    },
    getTab() {
      return this.currentTab;
    },
    statusIsSelected() {
      console.log(this.currentTab);
      return this.currentTab === "Status";
    }
  }
}
</script>

<style lang="scss" scoped>
  .pagebody {
    margin-left: 50px;
    margin-right: 50px;
  }
  
  .tabheader {
    width: 100%;
    height: 48px;
    background-color: #82b74b;
  }

  .tablinks {
    border: none;
    font-family: "Lato", sans-serif;
    display: inline-block;
    background-color: #82b74b;
    color: black;
    text-align: center;

    padding: 14px 16px;
    font-size: 17px;
  }

  .tabcontent {
    margin:  0 50px 0 50px;
    height: 1000px;
    padding: 6px 12px;
    border: 1px solid #ccc;
    border-top: none;
  }
</style>
