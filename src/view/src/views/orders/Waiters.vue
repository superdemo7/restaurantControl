<template>
  <div class="container is-fluid">
      <div class="columns">
  <div class="column">
    activas
  </div>
  <div class="column">
    finalizadas
  </div>
</div>
  </div>
</template>

<script>
export default {data() {
    return {
        orders: []

    }
},mounted(){this.get_orders()},
methods: {
    get_orders() {
        
    }
}
}
</script>

<style>

</style>