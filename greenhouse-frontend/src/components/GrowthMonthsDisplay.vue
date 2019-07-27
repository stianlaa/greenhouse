<template>
    <div class="month-container"> 
        <h4 style="padding-right: 15px; margin-bottom: 0px;"> Suitable growth months</h4>
        <canvas ref="growthMonths" class="grownth-month-canvas"/> 
    </div>
</template>

<script>
export default {
data: function () {
    return {
      months: ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"],
    }
  },
props: {
    selectedPlant: {},
},
watch: {
selectedPlant: function(updatedSelectedPlant) {
        if (updatedSelectedPlant && updatedSelectedPlant.idealGrowthMonths && updatedSelectedPlant.idealGrowthMonths.length == 12) {
            const context = this.$refs.growthMonths.getContext('2d') 
            const centerX = 200;
            const centerY = 50;

            const segments = this.selectedPlant.idealGrowthMonths.length;
            const percentageShift = 0.4/segments 
            const compensation = 0.7;
            
            for(let i = 0; i < segments; i++){
                this.placeText(context, this.months[i], centerX*2*(i/segments - percentageShift)*0.49 + 57, centerY - 10);
                if (this.selectedPlant.idealGrowthMonths[i]) {
                    this.drawMonth(context, centerX*2*compensation, centerY*2, (i/segments - percentageShift)*compensation, (i/segments + percentageShift)*compensation, "#617B30");
                } else {
                    this.drawMonth(context, centerX*2*compensation, centerY*2, (i/segments - percentageShift)*compensation, (i/segments + percentageShift)*compensation, "#A9A9A9");
                }
                }
            }
        },
    },
methods: {
    drawMonth(context, width, height, fromPercentage, toPercentage, color) {
            const rectWidth = width*(toPercentage - fromPercentage)
            const rectHeight = height/2

            const rectXPos = width*(fromPercentage + toPercentage)/2 - rectWidth/2 + 80
            const rectYPos = height/2

            context.fillStyle = color;
            context.fillRect(rectXPos - rectHeight/2, rectYPos - rectWidth/2, rectWidth, rectHeight);
            context.stroke();
        },
        placeText(context, text, locationX, locationY) {
            context.fillStyle = "#000000";
            context.font = "15px Arial";
            context.fillText(text, locationX, locationY);
        }
    },
}
</script>

<style lang="less" scoped>
    .grownth-month-canvas{
        height: 100px;
        width: 400px;
    }

    .month-container{
        display: flex;
        justify-content: center;
        flex-direction: column;
        text-align: center;
    }
</style>
