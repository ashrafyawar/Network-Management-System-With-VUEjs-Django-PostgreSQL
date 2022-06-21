<template>
 <div class="container-fluied">
    <nav class="row navbar navbar-expand-md navbar-dark fixed-top">
      <div class="col-lg-4">
      <RouterLink to="/" class="navbar-brand">GTU Network Management System</RouterLink>
      <button type="button" class="navbar-toggler" data-toggle="collapse" data-target="#navbarCollapse">
        <span class="navbar-toggler-icon"></span>
      </button>
      </div>
      <div class="col-lg-6"></div>

      <div class="col-lg-2 navbar-collapse " id="navbarCollapse">
        <div class="navbar-nav">
          <RouterLink to="/aboutsystempage" class="nav-item nav-link">System Usage</RouterLink>
          <RouterLink to="/techsupportpage" class="nav-item nav-link">Tech Support</RouterLink>
        </div>
      </div>
    </nav>
  </div>
</template>

<script >
    export default{
        name:'Navbar',
    }
</script>

<style scoped>
  nav{
    background:  #1e1f1e;
  }
  .bs-example {
    margin: 0px;
  }
  .navbar-nav{
    margin-left:11rem;
  }
  .navbar-brand {
    font-size: 20px;
    font-family: sans-serif;
  }

  /* On screens that are 992px or less, set the background color to blue */
  @media screen and (max-width: 2000px) {
    .navbar-nav{
      margin-left: 3rem;
    }
  }
</style>