<template>
  <div class="container is-fluid" style="color:white;">
    <strong>Agregar una Orden</strong>
    <br />
    <p>Mesa:</p>
    <b-field>
      <b-select placeholder="Selecciona una Mesa" v-model="order.table">
        <option
          v-for="option in tables"
          :value="option.table_id"
          :key="option.table_id"
        >{{ option.name }}</option>
      </b-select>
    </b-field>
    <p v-if="order.table == 0">Añadir Direccion</p>
    <b-field v-if="order.table == 0">
      <b-input v-model="order.address"></b-input>
    </b-field>
    <b-field>
      <b-select placeholder="Selecciona un platillo" v-model="selectedproduct" expanded>
        <option v-for="option in products" :value="option" :key="option.id">{{ option.name }}</option>
      </b-select>
    </b-field>
    <p>Elige un platillo</p>
    <p align="right">
      <b-button type="is-info" @click="add_product">Agregar Producto</b-button>
    </p>
  </div>
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
      selectedProduct: {
        id: 0,
        name: "",
        price: 0.0
      },
      products: [],
      tables: [],
      selectedproduct: {
        id: 0,
        name: "",
        price: 0.0
      }
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
      this.tables = [
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
    },
    add_product() {
      const selectedProduct = this.selectedproduct;
      if (selectedProduct.id == 0) {
        this.$buefy.toast.open({
          message: "Tienes que seleccionar un producto",
          type: "is-danger"
        });
      } else {
        const { id, name, price } = selectedProduct;
        const product = {
          id,
          name,
          quantity: 1,
          specifications: "",
          price,
          total: price
        };
        this.order.products.push(product);
      }
      console.log(this.order);
    }
  }
};
</script>

<style>
</style>