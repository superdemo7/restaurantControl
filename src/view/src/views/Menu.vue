<template>
  <div>Menu -- {{test}}</div>
</template>

<script>
export default {
  data() {
    return {
      test: "Esperando respuesta..."
    };
  },
  async mounted() {
    const test = await eel.test()();
    console.log(test);
    const orders = [{id:1,address:'Calle falsa 123', time_elapsed:5}]

    this.test = test;
  }
};
</script>

<style>
</style>