<template>
    <div class="month-container"> 
        <h4 style="padding-right: 15px; margin-bottom: 0px;"> Plant maturity</h4>
        <canvas ref=maturity class="grownth-month-canvas"/> 
    </div>
</template>

<script>
export default {
props: {
    selectedPlant: {},
},
watch: {
    selectedPlant: function (updatedSelectedPlant) {
        if (updatedSelectedPlant && updatedSelectedPlant.maturityPercentage) {
            const context = this.$refs.maturity.getContext('2d')
            const centerX = 200;
            const centerY = 50;
            const compensation = 0.5;
            const rightShift = 45;

            this.drawPercentage(context, centerX*2*compensation, centerY*2, updatedSelectedPlant.maturityPercentage, rightShift, "#A9A9A9", "#321321")
            }
        },
    },
methods: {
    drawPercentage(context, width, height, percentage, rightShift, colorBackground, colorProgress) {
            const rectWidth = width*percentage
            const rectHeight = height/2
            const rectXPos = rightShift
            const rectYPos = height/2

            context.fillStyle = colorBackground;
            context.fillRect(rectXPos, rectYPos, width, rectHeight);
            context.stroke();
            context.fillStyle = colorProgress;
            context.fillRect(rectXPos, rectYPos, width*percentage, rectHeight);
            context.stroke();
        },
    }
}
</script>

<style lang="scss" scoped>
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
