<template>
  <div>
    <nav class="menu" tabindex="0">
      <div class="smartphone-menu-trigger"></div>
      <header class="avatar">
        <h2>Admin</h2>
      </header>
      <ul>
        <li tabindex="0" class="icon-dashboard"> <RouterLink to='/admindashboardpage' style="color:white; text-decoration:none;"><span>Summary</span></RouterLink> </li>
        <div class="give-padding"></div>
        <li tabindex="0" class="icon-calendar"> <RouterLink to='/admindashboardmicroslicingpage' style="color:white; text-decoration:none;"><span>SystemReviews</span></RouterLink></li>
        <div class="give-padding"></div>
        <li tabindex="0" class="icon-dashboard"> <RouterLink to='/admindashboarddevicespage' style="color:white; text-decoration:none;"><span>Devices</span></RouterLink> </li>
        <div class="give-padding"></div>
        <li tabindex="0" class="icon-customers"> <RouterLink to='/admindashboarddevicegroupspage' style="color:white; text-decoration:none;"><span>App Security</span></RouterLink></li>
        <div class="give-padding"></div>
        <li tabindex="0" class="icon-customers"> <RouterLink to='/admindashboardsitespage' style="color:white; text-decoration:none;"><span>Sites</span></RouterLink></li>
        <div class="give-padding"></div>
        <li tabindex="0" class="icon-users"> <RouterLink to='/admindashboardedgeclusterspage' style="color:white; text-decoration:none;"><span>Edge Clusters</span></RouterLink></li>
        <div class="give-padding"></div>
        <li tabindex="0" class="icon-calendar"> <RouterLink to='/admindashboardaccesspointspage' style="color:white; text-decoration:none;"><span>Access Points</span></RouterLink></li>
        <div class="give-padding"></div>
        <li tabindex="0" class="icon-users"> <RouterLink to='/admindashboardapplicationspage' style="color:white; text-decoration:none;"><span>Applications</span></RouterLink></li>
      </ul>
    </nav>

    <main>
      <div class="bs-example">
        <nav class="navbar navbar-expand-md  navbar-dark fixed-top" style="background:#1e1f1e;">
            <RouterLink to = '/admindashboardpage' class="navbar-brand">GTU NETWORK MANAGEMENT SYSTEM</RouterLink>
            <button type="button" class="navbar-toggler" data-toggle="collapse" data-target="#navbarCollapse">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse justify-content-between" id="navbarCollapse">
              <div class="navbar-nav" style=" margin-left: 80%;">
                  <RouterLink to='/' class="nav-item nav-link">Logout</RouterLink>
              </div>
            </div>
        </nav>
      </div>
    </main>
    
  </div>
</template>

<script>
  export default{
    name:'AdminDashboardBaseView',
    components:{},
    data:function(){return{}},
    methods:{}
  }
  
</script>

<style scoped>

  @import '../assets/base.css';
  a:link {
    text-decoration: none;
  }
  .give-padding{
    padding-bottom: 10px;
  }
  a {
    color: white;
  }

  a:hover {
    color: white;
  }

  #ftr {
    padding: 20px;
  }

  .fa {

    font-size: 23px;
    width: 60px;
    text-align: center;
    text-decoration: none;
    margin: 5px 2px;
    border-radius: 50%;
  }

  .fa:hover {
    opacity: 0.5;
    text-decoration: none;
  }

  p {
    text-align: center;
  }

  div {
    padding-left: 120px;
  }
  div .bs-example{
    padding-left: 21px;
  }
  main {
    position: relative;
    height: 15vh;
  }

  .menu {
    background: #505251;
    height: 100vh;
    width: 142px;
    position: fixed;
    top: 0px;
    left: 0;
    z-index: 5;
    outline: none;
  }
  .menu .avatar {
    background: rgba(0, 0, 0, 0.1);
    text-align: center;
    border-radius: 15px; 
  }
  .menu .avatar h2 {
    color: #969292;
    font-weight: normal;
    margin-bottom: 0;
  }
  .menu ul {
    list-style: none;
    padding: 0.5em 0;
    margin: 0;
  }
  .menu ul li {

    padding: 0.5em 1em .5em 3em;
    font-size: 0.95em;
    font-weight: regular;
    background-repeat: no-repeat;
    background-position: left 15px center;
    background-size: auto 20px;
    transition: all 0.15s linear;
    cursor: pointer;
  }
  .menu ul li.icon-dashboard {
    background-image: url("http://www.entypo.com/images//gauge.svg");
  }
  .menu ul li.icon-customers {
    background-image: url("http://www.entypo.com/images//briefcase.svg");
  }
  .menu ul li.icon-users {
    background-image: url("http://www.entypo.com/images//users.svg");
  }
  .menu ul li.icon-calendar {
    background-image: url("http://www.entypo.com/images//calendar.svg");
  }

  .menu ul li:hover {
    background-color: rgba(0, 0, 0, 0.1);
  }
  .menu ul li:focus {
    outline: none;
  }
  @media screen and (max-width: 900px) and (min-width: 400px) {
    body {
      padding-left: 90px;
    }
    .menu {
      width: 90px;
    }
    .menu .avatar {
      padding: 0.5em;
      position: relative;
    }
    .menu .avatar img {
      width: 60px;
    }
    .menu .avatar h2 {
      opacity: 0;
      position: absolute;
      top: 50%;
      left: 100px;
      margin: 0;
      min-width: 200px;
      border-radius: 4px;
      background: rgba(0, 0, 0, 0.4);
      transform: translate3d(-20px, -50%, 0);
      transition: all 0.15s ease-in-out;
    }
    .menu .avatar:hover h2 {
      opacity: 1;
      transform: translate3d(0px, -50%, 0);
    }
    .menu ul li {
      height: 60px;
      background-position: center center;
      background-size: 30px auto;
      position: relative;
    }
    .menu ul li span {
      opacity: 0;
      position: absolute;
      background: rgba(0, 0, 0, 0.5);
      padding: 0.2em 0.5em;
      border-radius: 4px;
      top: 50%;
      left: 80px;
      transform: translate3d(-15px, -50%, 0);
      transition: all 0.15s ease-in-out;
    }
    .menu ul li span:before {
      content: '';
      width: 0;
      height: 0;
      position: absolute;
      top: 50%;
      left: -5px;
      border-top: 5px solid transparent;
      border-bottom: 5px solid transparent;
      border-right: 5px solid rgba(0, 0, 0, 0.5);
      transform: translateY(-50%);
    }
    .menu ul li:hover span {
      opacity: 1;
      transform: translate3d(0px, -50%, 0);
    }
  }
  @media screen and (max-width: 400px) {
    body {
      padding-left: 0;
    }
    .menu {
      width: 230px;
      box-shadow: 0 0 0 100em rgba(0, 0, 0, 0);
      transform: translate3d(-230px, 0, 0);
      transition: all 0.3s ease-in-out;
    }
    .menu .smartphone-menu-trigger {
      width: 40px;
      height: 40px;
      position: absolute;
      left: 100%;
      background: #5bc995;
    }
    .menu .smartphone-menu-trigger:before,
    .menu .smartphone-menu-trigger:after {
      content: '';
      width: 50%;
      height: 2px;
      background: #fff;
      border-radius: 10px;
      position: absolute;
      top: 45%;
      left: 50%;
      transform: translate3d(-50%, -50%, 0);
    }
    .menu .smartphone-menu-trigger:after {
      top: 55%;
      transform: translate3d(-50%, -50%, 0);
    }
    .menu ul li {
      padding: 1em 1em 1em 3em;
      font-size: 1.2em;
    }
    .menu:focus {
      transform: translate3d(0, 0, 0);
      box-shadow: 0 0 0 100em rgba(0, 0, 0, 0.6);
    }
    .menu:focus .smartphone-menu-trigger {
      pointer-events: none;
    }
  }
</style>