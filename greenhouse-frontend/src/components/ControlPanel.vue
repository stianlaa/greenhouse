<template>
    <div class="sideborders">
        <h3>Watering controls</h3>
        <p>Should contain: start, stop, watertray (with input field with validation for volume, and select for tray) </p>
        <button @click="incrementWaterVolume()"> +10 </button>
        <input @keyup.enter="waterPlants(waterVolumeTarget)" :value="waterVolumeTarget" placeholder="Water volume (ml)"/>
        <button @click="decrementWaterVolume()"> -10 </button>

        <button @click="waterPlants()"> water </button>
    </div>
</template>

<script>
export default {
    data: function() {
        return {
            waterVolumeTarget: 10,
        }
    },
    methods: {
        incrementWaterVolume: function() {
            this.waterVolumeTarget +=10;
        },
        decrementWaterVolume: function() {
            this.waterVolumeTarget -=10;
        },
        waterPlants(value) {
            
            console.log("watering plants with:")
            console.log(value)
            console.log(this.waterVolumeTarget)
            console.log(this.capVolume(this.waterVolumeTarget))
        },
        capVolume(volume) {
            if (volume < 0 ) {
                this.waterVolumeTarget = 0;
            } else if (volume > 200) {
                this.waterVolumeTarget = 200;
            }
            return this.waterVolumeTarget;
        }
    }
}
</script>

<style lang="less" scoped>
    .sideborders {
        border: 2px solid #000;
        border-top: none;
        border-bottom: none;
        padding: 1rem;
        border-radius: 25px;
    }
</style>
