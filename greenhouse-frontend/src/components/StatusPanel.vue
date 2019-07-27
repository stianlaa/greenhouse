<template>
    <div class="statuspanel align-horizontally">
        <div style="width: 10%">
            <div>
                <img v-if="connected" svg-inline src="@/assets/leaf.svg" style="transform: rotateY(180deg); fill:#A3BF45" />
                <img v-if="!connected" svg-inline src="@/assets/leaf.svg" style="transform: rotateY(180deg); fill:#FFCC00" />
            </div>
        </div>
        <div style="width: 65%; padding-right: 250px;">
            <div class="align-horizontally">
                <div class="infofield">
                    <h3> Temperature in: {{tempval}}</h3>
                    <h3> Temperature out: {{currentWeather.temperature}} C</h3>
                </div>

                <div class="infofield">
                    <h3> Current cloudiness: {{currentWeather.cloudiness}} %</h3>
                    <h3> Current waterlevel: {{tempval}} %</h3>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  data: function () {
    return {
      tempval: "WIP",
      connected: true,
      info: null,
      loading: true,
      errored: false
    }
  },
  computed: mapState({
      currentWeather: (state) => {
          return state.weather;
      }
  }),
  beforeMount() {
    this.$store.dispatch('loadCurrentWeather')
  }
}
</script>

<style lang="less" scoped>
    .infofield {
        display: flex;
        flex-wrap: wrap;
        justify-content: left;
        max-width: 250px;
    }

    .connected-leaf {
        min-height: 100px;
        height: 100px;
    }

    .statuspanel {
        border: 2px solid #000;
        border-top: none;
        border-bottom: none;
        padding: 1rem;
        border-radius: 25px;

        min-height: 100px;
        margin-bottom: 1rem;
    }

    .align-horizontally {
        display: flex;
        justify-content: space-between;
        flex-direction: row;
        text-align: center;
    }
</style>