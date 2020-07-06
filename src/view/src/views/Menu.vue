<template>
  <div class="container is-fluid">
    <b-tabs vertical >
      <b-tab-item v-for="category in categories" :key="category.id" :label="category.name">
        <table class="table">
          <thead>
            <tr>
              <th>
                <abbr title="Nombre">Nombre</abbr>
              </th>
              <th>
                <abbr title="Precio">Precio</abbr>
              </th>
              <th>
                <abbr title="Disponibilidad">Disponibilidad</abbr>
              </th>
              <th>
                <abbr title="Acciones">Acciones</abbr>
              </th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="product in category.products" :key="product.id">
              <td style="text-align: center">{{product.name}}</td>
              <td style="text-align: center">{{product.price}}</td>
              <td style="text-align: center">{{product.status}}</td>
              <td><b-button type="is-warning">Modificar</b-button> <b-button type="is-success">Eliminar</b-button></td>
            </tr>
          </tbody>
        </table>
      </b-tab-item>
    </b-tabs>
  </div>
</template>

<script>
export default {
  data() {
    return {
      categories: []
    };
  },
  mounted() {
    this.get_categories();
  },
  methods: {
    get_categories() {
      this.categories = [
        {
          id: 1,
          name: "Cocteles",
          products: [
            { id: 1, name: "Marlin", price: "$17", status: true },
            { id: 2, name: "ceviche", price: "$15", status: true },
            { id: 3, name: "aguachile", price: "$35", status: false },
            { id: 4, name: "Camaron", price: "$35", status: true }
          ]
        },
        {
          id: 2,
          name: "Tostadas",
          products: [
            { id: 1, name: "Marlin", price: "$17", status: true },
            { id: 2, name: "ceviche", price: "$15", status: true },
            { id: 3, name: "aguachile", price: "$35", status: false },
            { id: 4, name: "Camaron", price: "$35", status: true }
          ]
        },
        {
          id: 3,
          name: "Platillos",
          products: [
            { id: 1, name: "Marlin", price: "$17", status: true },
            { id: 2, name: "ceviche", price: "$15", status: true },
            { id: 3, name: "aguachile", price: "$35", status: false },
            { id: 4, name: "Camaron", price: "$35", status: true }
          ]
        },
        {
          id: 4,
          name: "Bebidas",
          products: [
            { id: 1, name: "Marlin", price: "$17", status: true },
            { id: 2, name: "ceviche", price: "$15", status: true },
            { id: 3, name: "aguachile", price: "$35", status: false },
            { id: 4, name: "Camaron", price: "$35", status: true }
          ]
        },
        {
          id: 5,
          name: "Postres",
          products: [
            { id: 1, name: "Marlin", price: "$17", status: true },
            { id: 2, name: "ceviche", price: "$15", status: true },
            { id: 3, name: "aguachile", price: "$35", status: false },
            { id: 4, name: "Camaron", price: "$35", status: true }
          ]
        }
      ];
    }
  }
};
</script>

<style>
</style>