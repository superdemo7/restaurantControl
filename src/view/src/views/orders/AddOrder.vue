<template>
  <div class="container is-fluid">AddOrder</div>
</template>

<script>
export default {
  data() {
    return {
      order: {
        table: 0,
        address: "",
        products: []
      },
      products: [],
      tables: []
    };
  },
  mounted() {
    this.get_products();
    this.get_tables();
  },
  methods: {
    get_products() {
      this.products = [
        {
          id: 1,
          name: "Tostada de ceviche",
          price: 12.5
        },
        {
          id: 2,
          name: "Tostada de Marlin",
          price: 10.2
        },
        {
          id: 3,
          name: "Coctel grande",
          price: 12.5
        },
        {
          id: 4,
          name: "Coctel chico",
          price: 15
        },
        {
          id: 5,
          name: "Orden de Ceviche",
          price: 130
        }
      ];
    },
    get_tables() {
      this.table = [
        {
          type: "togo",
          name: "Domicilio",
          table_id: 0
        },
        {
          type: "table",
          name: "1-A",
          table_id: 1
        },
        {
          type: "togo",
          name: "2",
          table_id: 2
        }
      ];
    }
  }
};
</script>

<style>
</style>