<template>
  <div class="container is-fluid">
    <div class="columns">
      <div class="column" v-for="order in orders" :key="order.id">
        <article class="panel is-info">
          <p class="panel-heading">{{`Mesa: ${order.table}`}} {{`Tiempo: ${order.time_elapsed} min`}}</p>
          <div v-for="product in order.products" :key="product.id">
            <a class="panel-block is-active">{{product.name}}: {{product.quantity}}</a>
            <a class="panel-block">{{product.specification}}</a>
          </div>
        </article>
      </div>
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
        {
          table: "1-A",
          time_elapsed: 2,
          products: [
            {
              name: "Tostada de ceviche",
              quantity: 1,
              specification: "Sin aguacate"
            },
            {
              name: "Coctel GDE",
              quantity: 2,
              specification: "1 con todo, 1 sin jitomate"
            }
          ]
        },
        {
          table: "5",
          time_elapsed: 10,
          products: [
            {
              name: "Tostada de ceviche",
              quantity: 1,
              specification: "Sin aguacate"
            },
            {
              name: "Coctel GDE",
              quantity: 4,
              specification: "1 con todo, 3 sin jitomate"
            }
          ]
        },
        {
          table: "llevar",
          time_elapsed: 2,
          products: [
            {
              name: "Tostada de ceviche",
              quantity: 1,
              specification: "doble aguacate"
            },
            {
              name: "Coctel GDE",
              quantity: 2,
              specification: "1 con todo, 1 sin jitomate"
            }
          ]
        },
        {
          table: "domicilio",
          time_elapsed: 9,
          products: [
            {
              name: "Tostada de ceviche",
              quantity: 1,
              specification: "Sin aguacate"
            },
            {
              name: "Coctel GDE",
              quantity: 2,
              specification: "1 con todo, 1 sin jitomate"
            }
          ]
        }
      ];
    }
  }
};
</script>

<style>
</style>