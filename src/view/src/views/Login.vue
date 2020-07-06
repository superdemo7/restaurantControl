<template>
  <div class="container is-fluid">
    <b-field label="ID de Usuario">
      <b-input type="number" v-model.number="id"></b-input>
    </b-field>
    <b-field label="Contraseña">
      <b-input type="password" v-model="pass" password-reveal></b-input>
    </b-field>
    <b-button type="is-primary" @click="login">Iniciar Sesion</b-button>
  </div>
</template>

<script>
export default {
  data() {
    return { pass: "", id: "" };
  },
  methods: {
    async login() {
      const id = this.id;
      const pass = this.pass;
      const res = await eel.users_login(id, pass)();
      if (res.success) {
        this.$buefy.toast.open({
          message: "ingresaste correctamente",
          type: "is-success"
        });
        switch (res.type) {
          case "admin":
          case "waiters":
            this.$router.push(`orders/waiters`);
            break;
          case "delivery":
            this.$router.push(`orders/delivery`);
            break;
          case "chef":
            this.$router.push(`orders/chef`);
            break;
          default:
            this.$buefy.toast.open({
              message: "Tipo de usuario desconocido",
              type: "is-danger"
            });
            break;
        }
      } else {
        this.$buefy.toast.open({
          message: res.msg,
          type: "is-danger"
        });
      }
    }
  }
};
</script>

<style>
</style>