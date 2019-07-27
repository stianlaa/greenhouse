<template>
    <div class="tabcontent align-vertically">
        <div class="sideborders align-horizontally-spaceevenly">
            <div class="align-horizontally-spaceevenly" style="width: 200px; padding-top: 80px">
                <img svg-inline src="@/assets/flowerpot.svg" style="height: 75px; width: 75px; padding-top: 10px;"/>
                <div>
                    <h3>{{this.selectedPlant.plantType}}</h3>
                    <h3>{{parsePlantId(this.selectedPlant.plantType)}}</h3>
                </div>
            </div>
            <div>
                <h3>Tray: {{this.selectedPlant.trayId}}</h3>
                <h3>Planted date: {{parsePlantedDate()}}</h3>
                <h3>Harvest date: {{this.selectedPlant.expectedHarvestDate}}</h3>
                <h3>Seed water need: {{this.selectedPlant.seedWaterNeed}} ml</h3>
                <h3>Mature water need: {{this.selectedPlant.matureWaterNeed}} ml</h3>
                <h3>Current water need: {{calculateWaterNeed()}} ml</h3>
            </div>
            <div class="align-vertically"> 
                <div style="width: 400px, height: 100px;">
                    <GrowthDisplay :selectedPlant="this.selectedPlant"> </GrowthDisplay>
                </div>
                <div style="width: 400px, height: 100px;">
                    <MaturityDisplay :selectedPlant="this.selectedPlant"> </MaturityDisplay>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState } from 'vuex'
import GrowthDisplay from '@/components/GrowthMonthsDisplay.vue'
import MaturityDisplay from '@/components/MaturityDisplay.vue'

export default {
    data: function () {
    return {
      chosenId: "",
      selectedPlant: {},
    }
  },
  components: {
      GrowthDisplay,
      MaturityDisplay,
  },
    computed: mapState({
        allPlants: (state) => {
            return state.plants
        },
    }),
    watch: {
        chosenId: (updatedId) => {
            if (updatedId) this.chosenId = updatedId;
        },
        allPlants: function (updatedPlants) {
            if (updatedPlants) {
                const plants = Object.entries(updatedPlants);
                    for(let i = 0; i < plants.length; i++){
                        if (plants[i][1].plantId == this.chosenId) {
                            this.selectedPlant = plants[i][1];
                        }
                    }
            }
        },
    },
    methods: {
        parsePlantId() {
            if (!this.selectedPlant || !this.selectedPlant.plantId) return ""; 
            return this.selectedPlant.plantId.length > 7 ? this.selectedPlant.plantId.substring(1,7) : this.selectedPlant.plantId;    
        },
        parsePlantedDate() {
            if (this.selectedPlant && this.selectedPlant.plantedDateTime) {
                return this.selectedPlant.plantedDateTime.substring(0,10)
            }
        },
        calculateWaterNeed() {
            if (this.selectedPlant) {
                var waterNeed = this.selectedPlant.seedWaterNeed + (this.selectedPlant.matureWaterNeed - this.selectedPlant.seedWaterNeed)*this.selectedPlant.maturityPercentage
                return waterNeed.toFixed(2);
                }
        }
    },
    beforeMount() {
        this.$store.dispatch('loadAllPlants')
        this.chosenId=this.$route.params.id
    },
}
</script>

<style lang="less" scoped>
    .tabcontent {
        margin:  0 50px 0 50px;
        height: 1000px;
        padding: 6px 12px;
    }

    .align-horizontally-center {
        display: flex;
        justify-content: center;
        flex-direction: row;
        text-align: center;
    }

    .align-horizontally-spaceevenly {
        display: flex;
        justify-content: space-evenly;
        flex-direction: row;
        text-align: left;
    }

    .sideborders {
        border: 2px solid #000;
        border-top: none;
        border-bottom: none;
        padding: 1rem;
        border-radius: 25px;
    }

    .symbols{
        display: flex;
        justify-content: center;
        flex-direction: column;
        text-align: center;
    }
</style>
