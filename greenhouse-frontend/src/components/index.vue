<template>

  <div>
      <div class="tabheader">
        <button class="tablinks" @click="chooseTab('Status')" 
        :style="getTab() === 'Status'? 'background-color: #617B30;' : 'background-color: #A3BF45'">
        <img svg-inline class="icon" src="@/assets/flowerpot.svg"/> status
        </button>
        <button class="tablinks" @click="chooseTab('Tab2')" 
        :style="getTab() === 'Tab2'? 'background-color: #617B30' : 'background-color: #A3BF45'">
        <img svg-inline class="icon" src="@/assets/graph.svg"/> history
        </button>
        <button class="tablinks" @click="chooseTab('Tab3')" 
        :style="getTab() === 'Tab3'? 'background-color: #617B30' : 'background-color: #A3BF45'">
        <img svg-inline class="icon" src="@/assets/gear.svg"/> control
        </button>
    </div>

    <div v-if="currentTab === 'Status'" class="tabcontent">
      <StatusPanel/>
      <PlantStorage/>
    </div>

    <div v-if="currentTab === 'Tab2'" class="tabcontent">
      <h3>Tab2</h3>
      <p>Under construction, temperature graphs, and live camera image from greenhouse</p>
    </div>

    <div v-if="currentTab === 'Tab3'" class="tabcontent">
      <h3>Tab3</h3>
      <p>Under construction, adjust the regulation of greenhouse conditions</p>
    </div>
    
  </div>
</template>


<script>
import StatusPanel from '@/components/StatusPanel.vue';
import PlantStorage from '@/components/PlantStorage.vue';
import { constants } from 'crypto';

export default {
  name: 'Index',
  data: function () {
    return {
      currentTab: "Status",
      weather: {}
    }
  },
  components: {
    StatusPanel,
    PlantStorage,
  },
  methods: {
    chooseTab(button) {
      this.currentTab = button;
    },
    getTab() {
      return this.currentTab;
    }
  }
}
</script>


<style lang="scss" scoped>
  
  .tabheader {
    width: 100%;
    height: 120px;
    background-color: transparent;
  }

  .tablinks {
    border: none;
    font-family: "Lato", sans-serif;
    display: inline-block;
    background-color: #82b74b;
    color: white;
    text-align: center;

    padding: 14px 16px;
    font-size: 17px;
    min-width: 90px;

    &:focus {
      outline: none;
    }

    &:hover {
      cursor: pointer;
    }
  }

  .tabcontent {
    margin:  0 50px 0 50px;
    height: 1000px;
    padding: 6px 12px;
  }
</style>
