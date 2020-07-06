<template>
  <div id="app">
    <div id="nav">
      <template v-if="show">
        <router-link :to="`/orders/${order_view}`">Órdenes</router-link>&nbsp;|
        <router-link to="/menu">Menú</router-link>&nbsp;|
        <router-link v-if="user.type == 'admin'" to="/system">Sistema</router-link>&nbsp;|
        <a href="#" @click="logout">Salir</a>
      </template>
    </div>
    <router-view />
  </div>
</template>
<script>
export default {
  data() {
    return {
      show: false,
      user: {
        type: ""
      },
      order_view: ""
    };
  },
  onIdle() {
    if (this.$route.path != "/") {
      this.logout();
      this.$buefy.dialog.alert("Tu sesión se ha cerrado por inactividad");
    }
  },
  watch: {
    async $route(to, from) {
      const user = await eel.users_getUser()();
      if (user) {
        this.user = user;
        switch (user.type) {
          case "admin":
          case "waiters":
            this.order_view = "waiters";
            break;
          case "delivery":
            this.order_view = "delivery";
            break;
          case "chef":
            this.order_view = "chef";
            break;
          default:
            this.order_view = "";
            break;
        }
      } else {
        this.user = {
          type: ""
        };
        this.order_view = "";
      }
      const path = to.path;
      if (path == "/") {
        this.show = false;
      } else {
        this.show = true;
      }
    }
  },
  methods: {
    async logout() {
      const logout = await eel.users_logout();
      if (logout) {
        this.$router.push("/");
      }
    }
  }
};
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
