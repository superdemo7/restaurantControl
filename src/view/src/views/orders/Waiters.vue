<template>
  <div class="container is-fluid">
    <div class="columns">
      <div class="column" style="display: grid; justify-content: center;">
        <strong>Ordenes activas</strong>
        <table class="table">
          <thead>
            <tr>
              <th>
                <strong>Orden</strong>
              </th>
              <th>
                <strong>Mesa</strong>
              </th>
              <th>
                <strong>Estado</strong>
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
            <tr v-for="(order, index) in orders.active" :key="index">
              <td v-text="order.id" style="text-align: center"></td>
              <td v-text="order.table" style="text-align: center"></td>
              <td v-text="order.status" style="text-align: center"></td>
              <td v-text="`${order.time_elapsed} min`" style="text-align: center"></td>
              <td>
                <b-button type="is-info">Editar</b-button>
                <b-button type="is-danger">Cerrar</b-button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="column" style="display: grid; justify-content: center;">
        <strong>Ordenes Finalizadas</strong>
        <table class="table">
          <thead>
            <tr>
              <th>
                <strong>Orden</strong>
              </th>
              <th>
                <strong>Mesa</strong>
              </th>
              <th>
                <strong>Acciones</strong>
              </th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="(order, index) in orders.finished" :key="index">
              <td v-text="order.id" style="text-align: center"></td>
              <td v-text="order.table" style="text-align: center"></td>
              <td>
                <b-button type="is-info" @click="viewOrder(order.id)">Ver</b-button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import CheckOrder from "./CheckOrder.vue";
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
    viewOrder(id) {
      this.$buefy.modal.open({
        parent: this,
        component: CheckOrder,
        trapFocus: true
      });
    },
    get_orders() {
      this.orders = {
        active: [
          { id: 1, table: "1", status: "served", time_elapsed: 0 },
          { id: 2, table: "4", status: "serving", time_elapsed: 5 },
          { id: 3, table: "2", status: "serving", time_elapsed: 4 },
          { id: 4, table: "5-B", status: "serving", time_elapsed: 9 },
          { id: 5, table: "5-A", status: "served", time_elapsed: 0 }
        ],
        finished: [
          { id: 5, table: "5-A" },
          { id: 4, table: "5-A" },
          { id: 9, table: "5-A" },
          { id: 10, table: "5-A" }
        ]
      };
    }
  }
};
</script>

<style>
</style>