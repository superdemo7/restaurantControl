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
              <b-button type="is-primary" @click="saveUser" expanded>Guardar</b-button>
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
      <b-modal :active.sync="addTable">
        <div class="box">
          <b-field label="Nombre de mesa">
            <b-input v-model="newTable"></b-input>
          </b-field>
          <div class="buttons">
            <b-button type="is-primary" @click="saveTable" expanded>Guardar</b-button>
          </div>
        </div>
      </b-modal>
      <b-tab-item label="Mesas" icon="grid">
        <div class="columns">
          <div class="column is-4 is-offset-8">
            <div class="buttons">
              <b-button type="is-success" @click="addTable = true" expanded>Agregar Mesa</b-button>
            </div>
          </div>
        </div>
        <div class="columns">
          <div class="column is-11 is-offset-1">
            <table class="table">
              <thead>
                <tr>
                  <th>Nombre</th>
                  <th>Acciones</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="table in tables" :key="`table_${table.id}`">
                  <td>{{table.name}}</td>
                  <td>
                    <b-button type="is-danger">Borrar</b-button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
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
      },
      addTable: false,
      newTable: "",
      tables: []
    };
  },
  mounted() {
    this.getUsers();
    this.getTables();
  },
  methods: {
    async saveTable() {
      const newTable = this.newTable;
      const response = await eel.tables_addTable(newTable)();
      console.log(response);
      if (response.success) {
        this.$buefy.toast.open("Se agrego la mesa");
      } else {
        this.$buefy.toast.open({
          message: response.msg,
          type: "is-danger"
        });
      }
      this.getTables();
    },
    async saveUser() {
      const newUser = this.newUser;
      const response = await eel.users_saveUser(newUser)();
      console.log(response);
      if (response.success) {
        this.$buefy.toast.open("Se agrego el usuario");
      } else {
        this.$buefy.toast.open({
          message: response.msg,
          type: "is-danger"
        });
      }
      this.getUsers();
    },
    async getTables() {
      const tables = await eel.tables_getAll()();
      this.tables = tables;
    },
    async getUsers() {
      const users = await eel.users_getAll()();
      this.users = users;
    },
    async deleteUser(id) {
      await eel.users_deleteUser(id)();
      this.getUsers();
    },
    async deleteTable(id) {
      await eel.tables_deleteTable(id)();
      this.getTables();
    }
  }
};
</script>

<style>
</style>