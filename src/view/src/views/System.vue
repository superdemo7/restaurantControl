<template>
  <div class="container is-fluid">
    <b-tabs vertical>
      <b-tab-item label="Usuarios" icon="account">
        <div class="columns">
          <div class="column is-4 is-offset-8">
            <div class="buttons">
              <b-button type="is-success" @click="addUser" expanded>Agregar usuario</b-button>
            </div>
          </div>
        </div>
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
      users: []
    };
  },
  mounted() {
    this.getUsers();
  },
  methods: {
    async addUser() {
      let age = 0;
      const prompt = this.$buefy.dialog.prompt({
        message: `What's your age?`,
        inputAttrs: {
          type: "number",
          placeholder: "Type your age",
          value: "18",
          maxlength: 2,
          min: 18
        },
        trapFocus: true,
        onConfirm: value => (age = value)
      });
      console.log({ age, prompt });
      console.log("fin");
    },
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