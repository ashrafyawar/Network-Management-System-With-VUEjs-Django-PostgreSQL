<template>
  <div class="mainclass">    
    <admin-dashboard-base-view/>
    <admin-dashboard-card-view/>
    <br><br><br><br>

  </div>
</template>

<script>
  import AdminDashboardCardView from'../components/AdminDashboardCardsView.vue'
  import AdminDashboardBaseView from'../components/AdminDashboardBaseView.vue'
  import axios from 'axios'

 export default{
    name:'AdminDashboardSitesView',
    components:{
      AdminDashboardCardView,
      AdminDashboardBaseView
    },
    data:function(){
        return{
          userName:"ashraf",
          password:"pass",
          deviceInfo:[]
        }
    },
    methods:{
      getAdminList(){
        axios.get('/devicelist').then(response =>{
          this.deviceInfo = response.data
          console.log(this.deviceInfo);
        })
        .catch(error =>{
          console.log(error)
        })
      }
    },
    created: function(){
      this.getAdminList()
    }
  }

</script>

<style scoped>
  .panel{
    overflow-y: scroll;
    height: 300px;
  }
  .mainclass{
    overflow-x: hidden;
  }

  /* width */
::-webkit-scrollbar {
  width: 5px;
}

/* Track */
::-webkit-scrollbar-track {
  box-shadow: inset 0 0 5px grey; 
  border-radius: 10px;
}
 
/* Handle */
::-webkit-scrollbar-thumb {
  background: rgb(129, 125, 125); 
  border-radius: 10px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: rgb(129, 125, 125); 
}

.market-update-block {
    padding: 2em 2em;
    background: #999;
  }

  .market-update-block h3 {
    color: #fff;
    font-size: 2.5em;
    font-family: 'Carrois Gothic', sans-serif;
  }

  .market-update-block h4 {
    font-size: 1.2em;
    color: #fff;
    margin: 0.3em 0em;
    font-family: 'Carrois Gothic', sans-serif;
  }

  .market-update-block p {
    color: rgb(248, 248, 248);
    font-size: 0.8em;
    line-height: 1.8em;
  }

  .market-update-block.clr-block-1:hover {
    background: #3C3C3C;
    transition: 0.5s all;
    -webkit-transition: 0.5s all;
    -moz-transition: 0.5s all;
    -o-transition: 0.5s all;
  }

  .market-update-block.clr-block-2:hover {
    background: #3C3C3C;
    transition: 0.5s all;
    -webkit-transition: 0.5s all;
    -moz-transition: 0.5s all;
    -o-transition: 0.5s all;
  }

  .market-update-block.clr-block-3:hover {
    background: #3C3C3C;
    transition: 0.5s all;
    -webkit-transition: 0.5s all;
    -moz-transition: 0.5s all;
    -o-transition: 0.5s all;
  }

  .market-update-right i.fa.fa-user-o {
    font-size: 3em;
    color: #68AE00;
    width: 80px;
    height: 80px;
    background: #fff;
    text-align: center;
    border-radius: 49px;
    -webkit-border-radius: 49px;
    -moz-border-radius: 49px;
    -o-border-radius: 49px;
    line-height: 1.7em;
  }

  .market-update-right i.fa.fa-user-md {
    font-size: 3em;
    color: #FC8213;
    width: 80px;
    height: 80px;
    background: #fff;
    text-align: center;
    border-radius: 49px;
    -webkit-border-radius: 49px;
    -moz-border-radius: 49px;
    -o-border-radius: 49px;
    line-height: 1.7em;
  }

  .market-update-right i.fa.fa-calendar {
    font-size: 3em;
    color: #337AB7;
    width: 80px;
    height: 80px;
    background: #fff;
    text-align: center;
    border-radius: 49px;
    -webkit-border-radius: 49px;
    -moz-border-radius: 49px;
    -o-border-radius: 49px;
    line-height: 1.7em;
  }
  .market-update-left {
    padding: 0px;
  }
</style>