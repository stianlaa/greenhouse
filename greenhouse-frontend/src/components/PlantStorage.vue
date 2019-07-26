<template>
    <div class="sideborders">
            <div v-for="tray in allTrays" :key='tray.trayId' class="tray"> 
                <Tray :trayData="tray"/>
            </div>

            <!-- <div>
                {{allTrays}}
            </div> -->
    </div>
</template>

<script>
import { mapState } from 'vuex'
import Tray from '@/components/Tray.vue'

export default {
components: {
    Tray
},
    computed: mapState({
      allTrays: (state) => {
          return state.trays;
      }
  }),
  beforeMount() {   
    this.$store.dispatch('loadAllTrays')
  }
}
</script>

<style lang="scss" scoped>
    .tray {
        margin-bottom: 20px;
    }
    
    .sideborders {
        border: 2px solid #000;
        border-top: none;
        border-bottom: none;
        padding: 1rem;
        border-radius: 25px;

        min-height: 600px;
    }
</style>
