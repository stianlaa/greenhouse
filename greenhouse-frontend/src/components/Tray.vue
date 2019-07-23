<template>
    <div class="tray align-horizontally">
        <div style="width: 10%">
            <div>
                <img svg-inline src="@/assets/tray.svg" style="transform: rotateY(180deg); fill:#A3BF45" />
                <h4> Tray {{getTrayId()}}</h4>
            </div>
        </div>
        <div v-for="plant in trayData" :key='plant.plantId' class="plantField">
            <a href="http://localhost:8080/" class="tray align-horizontally">
            <img svg-inline src="@/assets/flowerpot.svg" style="height: 75px; width: 75px;"/>
            <div>
                <p>{{plant.plantType}}</p>
                <p>{{parsePlantId(plant.plantId)}}</p>
            </div>
            </a>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        trayData: {}
    },
    methods: {
        getPlantsGroupedByType() {

        },
        parsePlantId(plantId) {
            return plantId.length > 7 ? plantId.substring(1,7) : plantId;    
        },
        getTrayId() {
            console.log()
            return (this.trayData) ? this.trayData[1].trayId: "";
        }
    }
}
</script>

<style lang="scss" scoped>
    .plantField {

        margin-left: 2rem;
        border-bottom: 2px solid #000;
        border-radius: 25px;
        max-height: 110px;
        min-width: 175px;
    }
    
    .tray {
        background-color: blue($color: #000000);
        min-width: 100px;
        min-height: 100px;
    }

    .align-horizontally {
        display: flex;
        justify-content: left;
        flex-direction: row;
        text-align: center;
    }
</style>
