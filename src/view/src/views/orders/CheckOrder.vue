<template>
  <div style="color:white">
      <p>Informacion</p>
      <ul>
        <li>id: {{order.id}} <br/>  Mesa: {{order.table}} <br/> Total: {{order.total}}$ <br/> Fecha: {{order.date}} <br/>Tipo: {{order.type}} <br/>Nombre: {{order.waitress}}</li>
      </ul>
      <br>
      <p>Consumió:</p>
      <ul v-for="info in order.products" :key="info.id">
        <li>Platillo: {{info.name}} <br/> Cantidad: {{info.quantity}} <br/> Precio: {{info.price}}$ </li>
        <br/>
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