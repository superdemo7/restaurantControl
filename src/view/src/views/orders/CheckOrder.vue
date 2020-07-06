<template>
  <div style="color:white">
      <p>Informacion</p>
      <ul>
        <li>id: {{order.id}} &nbsp;&nbsp;&nbsp;Mesa: {{order.table}} &nbsp;&nbsp;&nbsp;Total: {{order.total}}$ &nbsp;&nbsp;&nbsp;Fecha: {{order.date}} &nbsp;&nbsp;&nbsp;Tipo: {{order.type}} &nbsp;&nbsp;&nbsp;Nombre: {{order.waitress}}</li>
      </ul>
      <br>
      <p>Consumio:</p>
      <ul v-for="info in order.products" :key="info.id">
        <li>Platillo: {{info.name}} &nbsp;&nbsp;&nbsp;Cantidad: {{info.quantity}} &nbsp;&nbsp;&nbsp;Precio: {{info.price}}$ </li>
      </ul>
        
  </div>
</template>

<script>
export default {
  data() {
    return {
      order: []
    };
  },
  mounted() {
    this.get_order();
  },
  methods: {
    get_order() {
      this.order = {
        id: 1,
        table: "1-A",
        total: 75.0,
        date: "2020-02-20 06:00:04",
        type: "Aqui",
        waitress: "Pedro",
        products: [
          {
            name: "Tostada de ceviche",
            quantity: 4,
            price: 35
          },
          {
            name: "Coctel",
            quantity: 4,
            price: 35
          },
          {
            name: "Tostada de Marlin",
            quantity: 4,
            price: 35
          }
        ]
      };
    }
  }
};
</script>

<style>
</style>