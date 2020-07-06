<template>
  <div class="container is-fluid">
      <b-field label="ID de Usuario">
            <b-input v-model="usuario"></b-input>
        </b-field>
       <b-field label="contraseña">
            <b-input type="password"
                v-model="pass"
                password-reveal>
            </b-input>
        </b-field>
      <b-button type="is-primary" @click="ingresar">Iniciar Sesion</b-button>
  </div>
</template>

<script>
export default {
  data() {
    return { pass: "admin", usuario: "admin123" };
  },
  methods: {
    async ingresar() {
      const usuario = this.usuario;
      const pass = this.pass;
      const res = {success:true,msg:"",type:"chef"}//await eel.login(usuario, pass)();
      if (res.success) {
        this.$buefy.toast.open({
                    message: "ingresaste correctamente",
                    type: 'is-success'
                })
        console.log(`orders/${res.type}`)
        this.$router.push(`orders/${res.type}`)
      } else {
        this.$buefy.toast.open({
                    message: res.msg,
                    type: 'is-danger'
                })
      }

    }
  }
};
</script>

<style>
</style>