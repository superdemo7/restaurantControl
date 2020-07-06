<template>
  <div>
    <strong style="color:white; text-align: center;">Agrega un producto</strong>
    <br><br><br>
    <p style="color:white">Nombre de Producto</p>
    <b-field>
            <b-input v-model="name"></b-input>
    </b-field>
    <p style="color:white">Precio</p>
    <b-field>
      <b-input type="number" v-model.number="price"></b-input>
    </b-field>
    <p style="color:white">Categoria</p>
    <b-field>
            <b-select placeholder="Selecciona una Categoria">
                <option
                    v-for="option in categories"
                    :value="option.id"
                    :key="option.id">
                    {{ option.name }}
                </option>
            </b-select>
        </b-field>
        <p align="right">
      <b-button type="is-success" >Guardar</b-button>
      </p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      product: {
        name: "",
        price: 0.0,
        category: 0
      },
      categories: [
        { id: 1, name: "Tostadas" },
        { id: 2, name: "Platillos" },
        { id: 3, name: "Bebidad" },
        { id: 4, name: "Postres" }
      ]
    };
  }
};
</script>

<style>
</style>