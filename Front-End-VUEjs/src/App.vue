<script >
import { RouterLink, RouterView } from 'vue-router'
export default{
  name:'App',
  BeforeUnloadEvent(){
    this.$store.commit("initializeStore")
    const access = this.$$store.state.access
    if (access) {
      axios.defaults.headers.common['Authorization'] = "JWT" + access
    }else{
      axios.defaults.headers.common['Authorization'] = ''
    }
  }
}
</script>

<template>
  <div id="app" style="overflow:hidden;">
    <router-view/>
  </div>
</template>
<style scoped>

</style>