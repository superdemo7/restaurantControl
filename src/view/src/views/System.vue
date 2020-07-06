<template>
  <div class="container is-fluid">
    <b-tabs vertical>
      <b-tab-item label="Usuarios" icon="account">
        <div class="columns">
          <div class="column is-4 is-offset-8">
            <div class="buttons">
              <b-button type="is-success" @click="addUser = true" expanded>Agregar usuario</b-button>
            </div>
          </div>
        </div>
        <b-modal :active.sync="addUser">
          <div class="box">
            <b-field label="Nombre">
              <b-input v-model="newUser.name"></b-input>
            </b-field>
            <b-field label="Contraseña">
              <b-input type="password" v-model="newUser.password" password-reveal></b-input>
            </b-field>
            <b-field label="Rol">
              <b-select v-model="newUser.type" placeholder="Selecciona un rol" expanded>
                <option value="admin">Administrador</option>
                <option value="waiter">Mesero</option>
                <option value="delivery">Repartidor</option>
                <option value="chef">Cocinero</option>
              </b-select>
            </b-field>
            <div class="buttons">
              <b-button type="is-primary" expanded>Guardar</b-button>
            </div>
          </div>
        </b-modal>
        <div class="columns">
          <div class="column is-11 is-offset-1">
            <table class="table">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Nombre</th>
                  <th>Rol</th>
                  <th>Acciones</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="user in users" :key="`users_${user.id}`">
                  <td>{{user.id}}</td>
                  <td>{{user.name}}</td>
                  <td>{{user.type}}</td>
                  <td>
                    <b-button type="is-danger">Borrar</b-button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </b-tab-item>

      <b-tab-item label="Mesas" icon="grid">
        What light is light, if Silvia be not seen?
        <br />What joy is joy, if Silvia be not by—
        <br />Unless it be to think that she is by
        <br />And feed upon the shadow of perfection?
        <br />Except I be by Silvia in the night,
        <br />There is no music in the nightingale.
      </b-tab-item>
    </b-tabs>
  </div>
</template>

<script>
export default {
  data() {
    return {
      users: [],
      addUser: false,
      newUser: {
        name: "",
        password: "",
        type: ""
      }
    };
  },
  mounted() {
    this.getUsers();
  },
  methods: {
    async getUsers() {
      const users = await eel.users_getAll()();
      console.log(users);
      this.users = users;
    }
  }
};
</script>

<style>
</style>