<template>
  <div id="app">
    <div id="nav">
      <template v-if="show">
        <router-link to="/orders/delivery">Ordenes</router-link>&nbsp;|
        <router-link to="/menu">Menú</router-link>&nbsp;|
        <router-link to="/system">Sistema</router-link>&nbsp;|
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
      show: false
    };
  },
  watch: {
    $route(to, from) {
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
