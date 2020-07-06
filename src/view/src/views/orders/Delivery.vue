<template>
  <div class="container is-fluid" style= "display: grid; justify-content: center;">
    <strong>Ordenes de Repartidores</strong>
    <div>
      <table class="table">
        <thead>
          <tr>
            <th>
              <strong> Orden </strong>
            </th>
            <th>
              <strong>Domicilio</strong>
            </th>
            <th>
              <strong>Tiempo</strong>
            </th>
            <th>
              <strong>Acciones</strong>
            </th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="(order, index) in orders" :key="index">
            <td v-text="order.id"  style="text-align: center"></td>
            <td v-text="order.address"  style="text-align: center"></td>
            <td v-text="`${order.time_elapsed} min`"  style="text-align: center"></td>
            <td>
              <b-button type="is-info">Ver</b-button> <b-button type="is-success">Recibo</b-button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      orders: []
    };
  },
  mounted() {
    this.get_orders();
  },
  methods: {
    get_orders() {
      this.orders = [
        { id: 1, address: "Calle falsa 123", time_elapsed: 5 },
        { id: 2, address: "Calle falsa 123", time_elapsed: 5 },
        { id: 3, address: "Calle falsa 123", time_elapsed: 5 },
        { id: 4, address: "Calle falsa 123", time_elapsed: 5 },
        { id: 5, address: "Calle falsa 123", time_elapsed: 5 }
      ];
    }
  }
};
</script>

<style>
</style>